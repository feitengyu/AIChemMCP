import sys
import json
# 动态导入当前设备对应的工具类
from microplate_reader_303_server_tools_v2 import UnifiedWorkstationTools


# 创建全局工具管理器实例
tool_manager = UnifiedWorkstationTools()


# --- 定义统一的工作站工具函数 ---
def tool_microplate_reader_303(task_description: str, **params):
    """
    执行酶标仪303谱学的任务
    
    参数:
        task_description: 任务描述，说明要执行的具体操作
        **params: 其他可选参数，根据具体任务需要传递
    """
    return tool_manager.tool_microplate_reader_303(task_description, **params)



AVAILABLE_TOOLS = {
    "酶标仪303谱学": tool_microplate_reader_303
}


# --- MCP协议通信主逻辑 ---
def microplate_reader_303_server_main_loop():
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
            print(f"--- [microplate_reader_303_Server] Error: {str(e)} ---", file=sys.stderr, flush=True)


def microplate_reader_303_server_advertise_capabilities():
    """广播当前设备的MCP能力"""
    adv_message = {
        "jsonrpc": "2.0",
        "method": "protocol/advertise",
        "params": {
            "type": "server",
            "server": {
                "protocolVersion": "0.1.0",
                "displayName": "酶标仪303谱学",
                "capabilities": {
                    "tools": [
        {
            "name": "酶标仪303谱学",
            "description": "酶标仪是一种用于酶联免疫吸附测定（ELISA）等实验的仪器。它通过检测酶标记物与底物反应后产生的颜色变化来定量分析样品中的目标物质。在生物医学研究中，可用于检测血液中的抗体、抗原含量，进行疾病的诊断和监测。在生命科学实验中，也可用于分析细胞因子、蛋白质等生物分子的浓度，为科研人员提供准确的实验数据，推动相关领域的研究进展。",
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
    print(f"--- [microplate_reader_303_Server] 酶标仪303谱学 已就绪 ---", file=sys.stderr, flush=True)


if __name__ == "__main__":
    # 启动流程：先广播能力，再进入主循环
    microplate_reader_303_server_advertise_capabilities()
    microplate_reader_303_server_main_loop()
