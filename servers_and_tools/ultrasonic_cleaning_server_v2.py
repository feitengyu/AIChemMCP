import sys
import json
# 动态导入当前设备对应的工具类
from ultrasonic_cleaning_server_tools_v2 import UnifiedWorkstationTools


# 创建全局工具管理器实例
tool_manager = UnifiedWorkstationTools()


# --- 定义统一的工作站工具函数 ---
def tool_ultrasonic_cleaning(task_description: str, **params):
    """
    执行超声清洗的任务
    
    参数:
        task_description: 任务描述，说明要执行的具体操作
        **params: 其他可选参数，根据具体任务需要传递
    """
    return tool_manager.tool_ultrasonic_cleaning(task_description, **params)



AVAILABLE_TOOLS = {
    "超声清洗": tool_ultrasonic_cleaning
}


# --- MCP协议通信主逻辑 ---
def ultrasonic_cleaning_server_main_loop():
    """主循环：监听并响应Host的MCP协议请求"""
    for line in sys.stdin:
        try:
            request = json.loads(line)
            request_id = request.get("id")
            method_name = request.get("method")
            params = request.get("params", {})

            if method_name in AVAILABLE_TOOLS:
                # 调用对应的工具函数
                tool_function = AVAILABLE_TOOLS[method_name]
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

            # 响应结果
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
            print(f"--- [ultrasonic_cleaning_Server] Error: {str(e)} ---", file=sys.stderr, flush=True)


def ultrasonic_cleaning_server_advertise_capabilities():
    """广播当前设备的MCP能力"""
    adv_message = {
        "jsonrpc": "2.0",
        "method": "protocol/advertise",
        "params": {
            "type": "server",
            "server": {
                "protocolVersion": "0.1.0",
                "displayName": "超声清洗",
                "capabilities": {
                    "tools": [
        {
            "name": "超声清洗",
            "description": "超声波处理工作站利用超声波的空化效应、机械效应等对样品进行处理。超声波在液体中传播时产生的微小气泡的形成和破裂，能够产生强大的冲击力和剪切力，可用于细胞破碎、样品分散、加速化学反应等。在生物、化学等实验中有着广泛应用。例如在生物样品处理中，可用于提取细胞内的蛋白质、核酸等生物大分子；在化学合成中，能够加速反应速率，提高反应产率。",
            "parameters": {
                "type": "object",
                "properties": {
                    "task_description": {
                        "type": "string",
                        "description": "需要执行的具体任务描述"
                    }
                },
                "required": ["task_description"]
            }
        }
                    ]
                }
            }
        }
    }
    print(json.dumps(adv_message, ensure_ascii=False), flush=True)
    print(f"--- [ultrasonic_cleaning_Server] 超声清洗 已就绪 ---", file=sys.stderr, flush=True)


if __name__ == "__main__":
    # 启动流程：先广播能力，再进入主循环
    ultrasonic_cleaning_server_advertise_capabilities()
    ultrasonic_cleaning_server_main_loop()
