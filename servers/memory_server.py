import sys
import json
from tools.memory_server_tools import MemoryServerTools

tool_manager = MemoryServerTools()


def tool_save_memory():
    return tool_manager.tool_save_memory()


def tool_load_raw_memory():
    return tool_manager.tool_load_raw_memory()


def tool_load_analyzed_memory():
    return tool_manager.tool_load_analyzed_memory()


AVAILABLE_TOOLS_MEMORY = {
    "save_memory": tool_save_memory,
    "load_raw_memory": tool_load_raw_memory,
    "load_analyzed_memory": tool_load_analyzed_memory
}


# --- MCP协议通信部分 ---
def memory_server_advertise_capabilities():
    """广播服务器提供的所有大语言分析动作"""
    adv_message = {
        "jsonrpc": "2.0",
        "method": "protocol/advertise",
        "params": {
            "type": "server",
            "server": {
                "protocolVersion": "0.1.0",
                "displayName": "Memory Server",
                "capabilities": {
                    "tools": [
                        {
                            "name": "save_memory",
                            "description": "将当前的实验结果储存进数据库。如果有与其相关的大语言模型分析，也一并存入数据库。",
                            "parameters": {
                                "type": "object",
                                "properties": {
                                    "hypothesis": {"type": "string", "description": "描述反应物和条件的化学配方"},
                                    "param_types": {"type": "array",
                                                    "description": "进行实验使用的二元胺的类别，共有两种",
                                                    "items": {"type": "string"}},
                                    "param_values": {"type": "array",
                                                     "description": "进行实验使用的二元胺的量，共有两个值，分别对应每一种胺",
                                                     "items": {"type": "number"}},
                                    "target": {"type": "float", "description": "二氧化碳吸收反应的目标值，"}
                                },
                                "required": ["param_types", "param_values", "target"]
                            }
                        },
                        {
                            "name": "load_raw_memory",
                            "description": "从数据库中取出所有储存的实验结果，仅包含使用二元胺的种类、数量和性能。",
                            "parameters": {
                                "type": "object",
                                "properties": {
                                }
                            }
                        },

                        {
                            "name": "load_analyzed_memory",
                            "description": "从数据库中仅仅取出所有包含大语言模型分析的实验结果，包含使用二元胺的种类、数量、性能和大语言模型分析。",
                            "parameters": {
                                "type": "object",
                                "properties": {
                                }
                            }
                        }
                    ]
                }
            }
        }
    }
    print(json.dumps(adv_message), flush=True)
    print("--- [MCP Server] Memory Server is ready. ---", file=sys.stderr, flush=True)


def memory_server_main_loop():
    """主循环，监听和响应Host的请求"""
    for line in sys.stdin:
        try:
            request = json.loads(line)
            request_id = request.get("id")
            method_name = request.get("method")
            params = request.get("params", {})

            if method_name in AVAILABLE_TOOLS_MEMORY:
                tool_function = AVAILABLE_TOOLS_MEMORY[method_name]
                result = tool_function(**params)
                response = {"jsonrpc": "2.0", "result": result, "id": request_id}
            else:
                response = {"jsonrpc": "2.0", "error": {"code": -32601, "message": f"Method not found: {method_name}"},
                            "id": request_id}

            print(json.dumps(response), flush=True)

        except Exception as e:
            print(f"--- [MCP Server] Error: {e} ---", file=sys.stderr, flush=True)
            # 省略了详细的错误响应


if __name__ == '__main__':
    memory_server_advertise_capabilities()
    memory_server_main_loop()
