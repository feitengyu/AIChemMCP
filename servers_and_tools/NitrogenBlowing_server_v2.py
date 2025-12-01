import sys
import json
# 动态导入当前设备对应的工具类
from NitrogenBlowing_server_tools_v2 import UnifiedWorkstationTools


# 创建全局工具管理器实例
tool_manager = UnifiedWorkstationTools()


# --- 定义统一的工作站工具函数 ---
def tool_NitrogenBlowing(task_description: str, **params):
    """
    执行氮吹工作站的任务
    
    参数:
        task_description: 任务描述，说明要执行的具体操作
        **params: 其他可选参数，根据具体任务需要传递
    """
    return tool_manager.tool_NitrogenBlowing(task_description, **params)



AVAILABLE_TOOLS = {
    "氮吹工作站": tool_NitrogenBlowing
}


# --- MCP协议通信主逻辑 ---
def NitrogenBlowing_server_main_loop():
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
            print(f"--- [NitrogenBlowing_Server] Error: {str(e)} ---", file=sys.stderr, flush=True)


def NitrogenBlowing_server_advertise_capabilities():
    """广播当前设备的MCP能力"""
    adv_message = {
        "jsonrpc": "2.0",
        "method": "protocol/advertise",
        "params": {
            "type": "server",
            "server": {
                "protocolVersion": "0.1.0",
                "displayName": "氮吹工作站",
                "capabilities": {
                    "tools": [
        {
            "name": "氮吹工作站",
            "description": "氮吹处理工作站通过向样品表面吹入氮气，加速样品中溶剂的挥发，实现对样品的浓缩处理。它通常配备有多个样品位，可以同时处理多个样品，并且能够精确控制氮气的流量、温度等参数，以适应不同样品的处理需求。在药物分析、环境监测等领域，可用于将含有目标物质的溶液进行浓缩，提高后续分析检测的灵敏度和准确性。",
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
    print(f"--- [NitrogenBlowing_Server] 氮吹工作站 已就绪 ---", file=sys.stderr, flush=True)


if __name__ == "__main__":
    # 启动流程：先广播能力，再进入主循环
    NitrogenBlowing_server_advertise_capabilities()
    NitrogenBlowing_server_main_loop()
