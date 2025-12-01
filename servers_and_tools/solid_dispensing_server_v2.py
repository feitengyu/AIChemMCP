import sys
import json
# 动态导入当前设备对应的工具类
from solid_dispensing_server_tools_v2 import UnifiedWorkstationTools


# 创建全局工具管理器实例
tool_manager = UnifiedWorkstationTools()


# --- 定义统一的工作站工具函数 ---
def tool_solid_dispensing(task_description: str, **params):
    """
    执行固体进样工作站的任务
    
    参数:
        task_description: 任务描述，说明要执行的具体操作
        **params: 其他可选参数，根据具体任务需要传递
    """
    return tool_manager.tool_solid_dispensing(task_description, **params)



AVAILABLE_TOOLS = {
    "固体进样工作站": tool_solid_dispensing
}


# --- MCP协议通信主逻辑 ---
def solid_dispensing_server_main_loop():
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
            print(f"--- [solid_dispensing_Server] Error: {str(e)} ---", file=sys.stderr, flush=True)


def solid_dispensing_server_advertise_capabilities():
    """广播当前设备的MCP能力"""
    adv_message = {
        "jsonrpc": "2.0",
        "method": "protocol/advertise",
        "params": {
            "type": "server",
            "server": {
                "protocolVersion": "0.1.0",
                "displayName": "固体进样工作站",
                "capabilities": {
                    "tools": [
        {
            "name": "固体进样工作站",
            "description": "固体自动进样工作站用于自动向容器中加入固体样品。它能够准确地称量和加入一定量的固体样品，避免了人工操作可能带来的误差和污染。该工作站通常配备有高精度的称量装置和加样系统，可以按照预设的程序将固体样品准确地加入目标容器，可提高固体样品称量的效率和准确性。",
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
    print(f"--- [solid_dispensing_Server] 固体进样工作站 已就绪 ---", file=sys.stderr, flush=True)


if __name__ == "__main__":
    # 启动流程：先广播能力，再进入主循环
    solid_dispensing_server_advertise_capabilities()
    solid_dispensing_server_main_loop()
