import sys
import json
from tools.bo_serveer_tools import BOServerTools

# 创建一个全局的管理器实例。服务器的整个生命周期都将维持它的状态。
tool_manager = BOServerTools()


# --- 定义与MCP工具对应的函数 ---
def tool_initialize(search_space: dict):
    return tool_manager.tool_initialize()


def tool_observe(params: dict, yield_value: float):
    return tool_manager.tool_observe()


def tool_suggest():
    return tool_manager.tool_suggest()


AVAILABLE_TOOLS_BO = {
    "initialize": tool_initialize,
    "observe": tool_observe,
    "suggest": tool_suggest,
}


# --- MCP协议通信部分 ---
def bo_server_advertise_capabilities():
    adv_message = {
        "jsonrpc": "2.0",
        "method": "protocol/advertise",
        "params": {
            "type": "server",
            "server": {
                "protocolVersion": "0.1.0",
                "displayName": "Bayesian Optimization Server",
                "capabilities": {
                    "tools": [
                        {
                            "name": "initialize",
                            "description": "初始化一个新的BO会话，会清空所有历史数据。",
                            "parameters": {
                                "type": "object", "properties": {
                                    "search_space": {"type": "object",
                                                     "description": "定义参数的搜索范围, e.g., {'temperature': [60, 120]}"}
                                }, "required": ["search_space"]
                            }
                        },
                        {
                            "name": "observe",
                            "description": "向优化器提供一次实验的结果。",
                            "parameters": {
                                "type": "object", "properties": {
                                    "params": {"type": "object",
                                               "description": "本次实验的参数, e.g., {'temperature': 85.5}"},
                                    "yield_value": {"type": "number", "description": "本次实验的产率, e.g., 0.78"}
                                }, "required": ["params", "yield_value"]
                            }
                        },
                        {
                            "name": "suggest",
                            "description": "请求优化器给出下一个建议的实验参数。",
                            "parameters": {"type": "object", "properties": {}}
                        }
                    ]
                }
            }
        }
    }
    print(json.dumps(adv_message), flush=True)
    print("--- [MCP Server] BO Server is ready. ---", file=sys.stderr, flush=True)


def bo_server_main_loop():
    """主循环，监听和响应Host的请求"""
    for line in sys.stdin:
        try:
            request = json.loads(line)
            request_id = request.get("id")
            method_name = request.get("method")
            params = request.get("params", {})

            if method_name in AVAILABLE_TOOLS_BO:
                tool_function = AVAILABLE_TOOLS_BO[method_name]
                result = tool_function(**params)
                response = {"jsonrpc": "2.0", "result": result, "id": request_id}
            else:
                response = {"jsonrpc": "2.0", "error": {"code": -32601, "message": f"Method not found: {method_name}"},
                            "id": request_id}

            print(json.dumps(response), flush=True)

        except Exception as e:
            print(f"--- [MCP Server] Error: {e} ---", file=sys.stderr, flush=True)
            # 省略了详细的错误响应


if __name__ == "__main__":
    bo_server_advertise_capabilities()
    bo_server_main_loop()
