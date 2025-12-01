import sys
import json
# 动态导入当前设备对应的工具类
from Shaker_server_tools_v2 import UnifiedWorkstationTools


# 创建全局工具管理器实例
tool_manager = UnifiedWorkstationTools()


# --- 定义统一的工作站工具函数 ---
def tool_Shaker(task_description: str, **params):
    """
    执行摇床工作站的任务
    
    参数:
        task_description: 任务描述，说明要执行的具体操作
        **params: 其他可选参数，根据具体任务需要传递
    """
    return tool_manager.tool_Shaker(task_description, **params)



AVAILABLE_TOOLS = {
    "摇床工作站": tool_Shaker
}


# --- MCP协议通信主逻辑 ---
def Shaker_server_main_loop():
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
            print(f"--- [Shaker_Server] Error: {str(e)} ---", file=sys.stderr, flush=True)


def Shaker_server_advertise_capabilities():
    """广播当前设备的MCP能力"""
    adv_message = {
        "jsonrpc": "2.0",
        "method": "protocol/advertise",
        "params": {
            "type": "server",
            "server": {
                "protocolVersion": "0.1.0",
                "displayName": "摇床工作站",
                "capabilities": {
                    "tools": [
        {
            "name": "摇床工作站",
            "description": "实验用摇床是一种为实验室设计的样品制备和混合设备，其核心功能是通过可控的、温和的摇摆振荡，使放置在其平台上的试管、锥形瓶、培养皿等容器内的样品实现均匀混合、充分反应或高效溶解。它通过模拟人手摇晃的动作，但具有高度的一致性、重现性和稳定性，避免了人工操作带来的误差和疲劳，广泛应用于生物化学、分子生物学、医学检验等领域的细胞培养、染色、脱色、杂交反应等实验流程。",
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
    print(f"--- [Shaker_Server] 摇床工作站 已就绪 ---", file=sys.stderr, flush=True)


if __name__ == "__main__":
    # 启动流程：先广播能力，再进入主循环
    Shaker_server_advertise_capabilities()
    Shaker_server_main_loop()
