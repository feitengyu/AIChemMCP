import sys
import json
# 动态导入当前设备对应的工具类
from massSpectrometer_server_tools_v2 import UnifiedWorkstationTools


# 创建全局工具管理器实例
tool_manager = UnifiedWorkstationTools()


# --- 定义统一的工作站工具函数 ---
def tool_massSpectrometer(task_description: str, **params):
    """
    执行质谱工作站的任务
    
    参数:
        task_description: 任务描述，说明要执行的具体操作
        **params: 其他可选参数，根据具体任务需要传递
    """
    return tool_manager.tool_massSpectrometer(task_description, **params)



AVAILABLE_TOOLS = {
    "质谱工作站": tool_massSpectrometer
}


# --- MCP协议通信主逻辑 ---
def massSpectrometer_server_main_loop():
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
            print(f"--- [massSpectrometer_Server] Error: {str(e)} ---", file=sys.stderr, flush=True)


def massSpectrometer_server_advertise_capabilities():
    """广播当前设备的MCP能力"""
    adv_message = {
        "jsonrpc": "2.0",
        "method": "protocol/advertise",
        "params": {
            "type": "server",
            "server": {
                "protocolVersion": "0.1.0",
                "displayName": "质谱工作站",
                "capabilities": {
                    "tools": [
        {
            "name": "质谱工作站",
            "description": "液相色谱 - 质谱联用仪是将液相色谱的高分离能力与质谱的高灵敏度和高鉴别能力相结合的分析仪器。液相色谱先将复杂混合物中的各组分进行分离，然后质谱对分离后的各组分进行离子化和质量分析。质谱能够提供各组分的分子量，从而对化合物进行准确的定性分析。在药物研发、代谢组学、食品安全等领域，可用于分析复杂样品中的微量成分，鉴定未知化合物，以及研究药物的代谢途径等。",
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
    print(f"--- [massSpectrometer_Server] 质谱工作站 已就绪 ---", file=sys.stderr, flush=True)


if __name__ == "__main__":
    # 启动流程：先广播能力，再进入主循环
    massSpectrometer_server_advertise_capabilities()
    massSpectrometer_server_main_loop()
