import sys
import json


class BOServerTools:

    def __init__(self):
        self.process_list = []

    def tool_initialize(self):
        self.process_list.append("tool_initialize")

    def tool_observe(self):
        self.process_list.append("tool_observe")

    def tool_suggest(self):
        self.process_list.append("tool_suggest")

    def tool_save_data(self):
        self.process_list.append("tool_save_data")

    def tool_load_data(self):
        self.process_list.append("tool_load_data")

    def tool_exit(self):
        self.process_list.append("tool_exit")


tool_manager = BOServerTools()


def tool_initialize():
    return tool_manager.tool_initialize()


def tool_observe():
    return tool_manager.tool_observe()


def tool_suggest():
    return tool_manager.tool_suggest()


def tool_save_data():
    return tool_manager.tool_save_data()


def tool_load_data():
    return tool_manager.tool_load_data()


def tool_exit():
    return tool_manager.tool_exit()


AVAILABLE_TOOLS_BO = {
    "initialize": tool_initialize,
    "observe": tool_observe,
    "suggest": tool_suggest,
    "save_data": tool_save_data,
    "load_data": tool_load_data,
    "exit": tool_exit
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
                                "type": "object", "properties": {}, "required": []
                            }
                        },
                        {
                            "name": "observe",
                            "description": "进行实验并观测，向优化器提供一次实验的结果。",
                            "parameters": {
                                "type": "object", "properties": {}, "required": []
                            }
                        },
                        {
                            "name": "suggest",
                            "description": "请求优化器给出下一个建议的实验参数。",
                            "parameters": {"type": "object", "properties": {}}
                        },
                        {
                            "name": "save_data",
                            "description": "保存优化器的历史数据。",
                            "parameters": {"type": "object", "properties": {}}
                        },
                        {
                            "name": "load_data",
                            "description": "加载优化器的历史数据。",
                            "parameters": {"type": "object", "properties": {}}
                        },
                        {
                            "name": "exit",
                            "description": "退出BO会话。",
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
