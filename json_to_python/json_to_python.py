import json
import os
import sys
from string import Template

# 需要跳过的无效ID列表
INVALID_IDS = [
    1384653908411392,
    1161336116904960,
    518965240202240,
    501678392181760,
    484961779909632
]

def sanitize_name(name):
    """将名称中的连字符/特殊字符替换为下划线，确保符合Python命名规范"""
    return name.replace("-", "_").replace(".", "_").replace(" ", "_")

def parse_param_iterative(param, parent_key=""):
    """迭代方式处理参数，避免递归导致的栈溢出"""
    stack = [(param, parent_key)]
    properties = {}
    required = []
    
    while stack:
        current_param, current_parent = stack.pop()
        param_code = current_param["paramCode"]
        full_key = f"{current_parent}.{param_code}" if current_parent else param_code
        
        # 参数基本信息
        prop = {
            "type": current_param["dataType"],
            "description": current_param["paramName"] or f"参数 {param_code}"
        }
        
        # 处理单位
        if current_param.get("unitTypeName"):
            prop["description"] += f"（单位：{current_param['unitTypeName']}）"
        
        # 处理约束（枚举/范围，兼容constraintValue为JSON字符串的情况）
        constraint_type = current_param.get("constraintType")
        constraint_value = current_param.get("constraintValue")
        if constraint_type == "ENUM" and constraint_value:
            try:
                prop["enum"] = json.loads(constraint_value)
            except (json.JSONDecodeError, TypeError):
                prop["enum"] = [v.strip() for v in constraint_value.split(",")] if "," in constraint_value else constraint_value
        elif constraint_type == "RANGE" and constraint_value:
            range_parts = constraint_value.strip("[]()").split(",")
            if len(range_parts) == 2:
                prop["minimum"] = range_parts[0].strip()
                prop["maximum"] = range_parts[1].strip()
        
        # 处理必填项（兼容required为null的情况）
        if current_param.get("required") == 1:
            required.append(full_key)
        
        # 处理子参数（嵌套对象）
        if current_param.get("childParams"):
            child_props = {}
            child_required = []
            
            # 将子参数添加到栈中处理
            for child in reversed(current_param["childParams"]):
                stack.append((child, full_key))
            
            # 暂时存储当前参数，等待子参数处理完成
            prop["properties"] = {}  # 占位符，稍后填充
            properties[full_key] = ("pending", prop, child_props, child_required)
        else:
            properties[full_key] = ("complete", prop)
    
    # 第二遍处理：填充嵌套属性
    final_properties = {}
    for key, value in properties.items():
        status, data = value[0], value[1]
        if status == "complete":
            final_properties[key] = data
        else:  # pending
            _, prop, child_props, child_required = value
            # 收集所有子属性
            for child_key, child_value in properties.items():
                if child_key.startswith(key + "."):
                    child_props[child_key.split(".", 1)[1]] = child_value[1] if child_value[0] == "complete" else child_value[1]
                    if child_key in required:
                        child_required.append(child_key.split(".", 1)[1])
            
            prop["properties"] = child_props
            if child_required:
                prop["required"] = child_required
            final_properties[key] = prop
    
    return final_properties, required

def generate_server_code(json_data, sanitize_device_code):
    """
    根据输入的JSON数据生成MCP服务器代码
    :param json_data: 源JSON数据
    :param sanitize_device_code: 处理后的设备标识（用于文件名/导入路径）
    :return: 生成的主服务器代码
    """
    # 解析JSON核心数据
    device_name = json_data["data"]["name"]
    actions = json_data["data"]["actions"]

    # 1. 生成工具函数（如tool_open_door，处理连字符）
    tool_functions = []
    for action in actions:
        action_code_sanitized = sanitize_name(action["code"])
        func_name = f"tool_{action_code_sanitized}"
        # 函数接收**params参数（适配带参数的动作）
        tool_functions.append(f"""def {func_name}(**params):
    return tool_manager.{func_name}(**params)
""")
    tool_functions_str = "\n\n".join(tool_functions)

    # 2. 生成工具映射字典（修复原代码连字符导致的语法错误）
    tool_mappings = []
    for action in actions:
        action_code_raw = action["code"]  # 原始动作名（用于协议匹配）
        action_code_sanitized = sanitize_name(action["code"])  # 处理后的函数名
        tool_mappings.append(f'    "{action_code_raw}": tool_{action_code_sanitized}')
    tool_mappings_str = ",\n".join(tool_mappings)

    # 3. 生成广播消息中的工具能力描述（处理param.required为null的情况）
    capabilities_tools = []
    for action in actions:
        action_code_raw = action["code"]
        action_name = action["name"]
        params = action["params"]
        
        # 使用迭代方式处理参数，避免递归
        properties, required = {}, []
        for param in params:
            param_props, param_required = parse_param_iterative(param)
            properties.update(param_props)
            required.extend(param_required)

        # 组装单个工具的能力描述
        capabilities_tools.append(f"""        {{
            "name": "{action_code_raw}",
            "description": "{action_name}",
            "parameters": {{
                "type": "object",
                "properties": {json.dumps(properties, ensure_ascii=False, indent=4)},
                "required": {json.dumps(required, ensure_ascii=False)}
            }}
        }}""")
    capabilities_tools_str = ",\n".join(capabilities_tools)

    # 4. 代码模板（动态导入工具类，基于设备标识）
    code_template = Template("""import sys
import json
# 动态导入当前设备对应的工具类（与主服务器文件同目录）
from ${sanitize_device_code}_server_tools import ActionServerTools


# 创建全局工具管理器实例
tool_manager = ActionServerTools()


# --- 定义设备动作函数（自动生成，与工具类方法对应）---
$tool_functions


AVAILABLE_TOOLS_ACTION = {
$tool_mappings
}


# --- MCP协议通信主逻辑（自动适配当前设备）---
def ${sanitize_device_code}_server_main_loop():
    \"\"\"主循环：监听并响应Host的MCP协议请求\"\"\"
    for line in sys.stdin:
        try:
            request = json.loads(line)
            request_id = request.get("id")
            method_name = request.get("method")
            params = request.get("params", {})

            if method_name in AVAILABLE_TOOLS_ACTION:
                # 调用对应的工具函数（传递请求参数）
                tool_function = AVAILABLE_TOOLS_ACTION[method_name]
                result = tool_function(**params)
                response = {
                    "jsonrpc": "2.0",
                    "result": result,
                    "id": request_id
                }
            else:
                # 方法不存在错误
                response = {
                    "jsonrpc": "2.0",
                    "error": {
                        "code": -32601,
                        "message": f"Method not found: {method_name}"
                    },
                    "id": request_id
                }

            # 响应结果（强制刷新缓冲区）
            print(json.dumps(response, ensure_ascii=False), flush=True)
        except Exception as e:
            # 内部错误处理
            error_msg = {
                "code": -32603,
                "message": f"Internal error: {str(e)}"
            }
            response = {
                "jsonrpc": "2.0",
                "error": error_msg,
                "id": request.get("id")
            }
            print(json.dumps(response, ensure_ascii=False), flush=True)
            print(f"--- [${sanitize_device_code}_Server] Critical Error: {str(e)} ---", file=sys.stderr, flush=True)


def ${sanitize_device_code}_server_advertise_capabilities():
    \"\"\"广播当前设备的MCP能力（设备信息、支持的动作）\"\"\"
    adv_message = {
        "jsonrpc": "2.0",
        "method": "protocol/advertise",
        "params": {
            "type": "server",
            "server": {
                "protocolVersion": "0.1.0",
                "displayName": "${device_name}",
                "capabilities": {
                    "tools": [
$capabilities_tools
                    ]
                }
            }
        }
    }
    print(json.dumps(adv_message, ensure_ascii=False), flush=True)
    print(f"--- [${sanitize_device_code}_Server] ${device_name} is ready. ---", file=sys.stderr, flush=True)


if __name__ == "__main__":
    # 启动流程：先广播能力，再进入主循环
    ${sanitize_device_code}_server_advertise_capabilities()
    ${sanitize_device_code}_server_main_loop()
""")

    # 填充模板并返回代码
    return code_template.substitute(
        sanitize_device_code=sanitize_device_code,
        device_name=device_name,
        tool_functions=tool_functions_str,
        tool_mappings=tool_mappings_str,
        capabilities_tools=capabilities_tools_str
    )


def generate_server_tools_code(json_data, sanitize_device_code):
    """
    生成设备对应的工具类文件（_server_tools.py）
    :param json_data: 源JSON数据
    :param sanitize_device_code: 处理后的设备标识（用于类名注释）
    :return: 生成的工具类代码
    """
    actions = json_data["data"]["actions"]
    # 生成ActionServerTools类的方法（与JSON中的动作一一对应）
    tool_methods = []
    for action in actions:
        action_code_raw = action["code"]
        action_code_sanitized = sanitize_name(action["code"])
        method_name = f"tool_{action_code_sanitized}"
        # 方法接收**params（适配带参数的动作），抛未实现异常
        tool_methods.append(f"""    def {method_name}(self, **params):
        \"\"\"{action["name"]}（动作标识：{action_code_raw}）- 需实现具体逻辑\"\"\"
        raise NotImplementedError(f"未实现 {action["name"]}({action_code_raw}) 的工具逻辑")""")

    # 组装工具类代码（类名固定为ActionServerTools，方法动态生成）
    tools_code = f"""\"\"\"
{sanitize_device_code} 设备工具类
功能：定义设备所有动作的工具方法接口，需手动实现具体逻辑
生成时间：{json_data["data"]["updateTime"] or "未知"}
\"\"\"

class ActionServerTools:
    \"\"\"设备动作工具管理器：每个方法对应一个设备动作\"\"\"
{chr(10).join(tool_methods)}
"""
    return tools_code

def process_single_json(file_path):
    """处理单个JSON文件的核心逻辑"""
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            json_data = json.load(f)

        # 顶层 data 必须存在
        if not json_data.get("data"):
            print(f"跳过无效JSON文件: {os.path.basename(file_path)}")
            return False

        # 获取唯一标识
        device_code_raw = json_data["data"].get("code")
        device_id = json_data["data"].get("id")

        if not device_code_raw or not device_id:
            print(f"跳过缺少 code/id 的文件: {os.path.basename(file_path)}")
            return False

        # 生成唯一设备标识（避免多个 starting_station 冲突）
        unique_device_code = f"{device_code_raw}_{device_id}"
        sanitize_device_code = sanitize_name(unique_device_code)

        # 生成 server 文件
        server_filename = f"{sanitize_device_code}_server.py"
        server_code = generate_server_code(json_data, sanitize_device_code)
        with open(server_filename, "w", encoding="utf-8") as f:
            f.write(server_code)

        # 生成 tools 文件
        tools_filename = f"{sanitize_device_code}_server_tools.py"
        tools_code = generate_server_tools_code(json_data, sanitize_device_code)
        with open(tools_filename, "w", encoding="utf-8") as f:
            f.write(tools_code)

        print(f"✅ 已生成：{server_filename} 和 {tools_filename}")
        return True

    except Exception as e:
        print(f"❌ 处理文件 {file_path} 失败：{e}")
        return False

    """处理单个JSON文件的核心逻辑"""
    try:
        # 2. 读取并解析JSON数据 - 使用更高效的方式
        with open(file_path, "r", encoding="utf-8") as f:
            # 先读取一小部分来检查基本信息
            preview_data = f.read(1024)
            f.seek(0)
            
            # 检查是否包含必要字段
            if '"code":200' not in preview_data and '"code": 200' not in preview_data:
                print(f"跳过非200响应的文件: {os.path.basename(file_path)}")
                return False
                
            json_data = json.load(f)

        # 校验JSON结构（确保包含必要字段）
        if json_data.get("code") != 200 or not json_data.get("data"):
            print(f"跳过无效JSON文件: {os.path.basename(file_path)}")
            return False
            
        # 检查是否需要跳过此ID
        device_id = json_data["data"].get("id")
        if device_id in INVALID_IDS:
            print(f"跳过无效ID的工作站: {device_id} (文件名: {os.path.basename(file_path)})")
            return False

        device_code_raw = json_data["data"].get("code")
        if not device_code_raw:
            print(f"跳过无code字段的文件: {os.path.basename(file_path)}")
            return False

        # 3. 生成标准化的设备标识（用于文件名、函数名）
        sanitize_device_code = sanitize_name(device_code_raw)

        # 4. 生成主服务器文件（{设备标识}_server.py）
        server_filename = f"{sanitize_device_code}_server.py"
        server_code = generate_server_code(json_data, sanitize_device_code)
        with open(server_filename, "w", encoding="utf-8") as f:
            f.write(server_code)
        print(f"✅ 主服务器文件生成完成：{server_filename}（来源：{os.path.basename(file_path)}）")

        # 5. 生成工具类文件（{设备标识}_server_tools.py）
        tools_filename = f"{sanitize_device_code}_server_tools.py"
        tools_code = generate_server_tools_code(json_data, sanitize_device_code)
        with open(tools_filename, "w", encoding="utf-8") as f:
            f.write(tools_code)
        print(f"✅ 工具类文件生成完成：{tools_filename}（来源：{os.path.basename(file_path)}）")

        print(f"🎉 单个JSON处理完成！设备标识：{device_code_raw}（标准化后：{sanitize_device_code}）\n")
        return True

    except Exception as e:
        print(f"❌ 处理文件 {os.path.basename(file_path)} 失败：{str(e)}", file=sys.stderr)
        print("-" * 50 + "\n")
        return False


if __name__ == "__main__":
    # 1. 配置待遍历的JSON文件夹路径（用户可修改）
    JSON_FOLDER_PATH = r"src/AIChemMCP/workstation_data"

    # 检查文件夹是否存在
    if not os.path.exists(JSON_FOLDER_PATH):
        print(f"错误：文件夹 {JSON_FOLDER_PATH} 不存在！", file=sys.stderr)
        sys.exit(1)

    # 检查文件夹是否可访问
    if not os.path.isdir(JSON_FOLDER_PATH):
        print(f"错误：{JSON_FOLDER_PATH} 不是有效的文件夹！", file=sys.stderr)
        sys.exit(1)

    # 遍历文件夹中的所有JSON文件
    json_files = [
        entry.path for entry in os.scandir(JSON_FOLDER_PATH)
        if entry.is_file() and entry.name.lower().endswith(".json")
    ]

    if not json_files:
        print(f"提示：在 {JSON_FOLDER_PATH} 中未找到任何JSON文件", file=sys.stderr)
        sys.exit(0)

    print(f"📁 找到 {len(json_files)} 个JSON文件，开始批量处理...")
    print("=" * 60 + "\n")

    # 批量处理每个JSON文件 - 添加进度显示和内存优化
    success_count = 0
    processed_count = 0
    
    for i, json_file in enumerate(json_files):
        processed_count += 1
        print(f"处理进度: {processed_count}/{len(json_files)}")
        
        if process_single_json(json_file):
            success_count += 1
            
        # 每处理10个文件，尝试释放一些内存
        if processed_count % 10 == 0:
            import gc
            gc.collect()

    # 输出批量处理结果汇总
    print("=" * 60)
    print(f"📊 批量处理完成！")
    print(f"总文件数：{len(json_files)}")
    print(f"成功数：{success_count}")
    print(f"失败数：{len(json_files) - success_count}")