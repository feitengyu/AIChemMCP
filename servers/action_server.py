import sys
import json
from tools.action_server_tools import ActionServerTools


# 创建一个全局的管理器实例。服务器的整个生命周期都将维持它的状态。
tool_manager = ActionServerTools()


# --- 定义与MCP工具对应的函数 -
def tool_robotic_reaction():
    return tool_manager.tool_robotic_reaction()


def tool_robotic_measurement():
    return tool_manager.tool_robotic_measurement()


def tool_robotic_characterization():
    return tool_manager.tool_robotic_characterization()


AVAILABLE_TOOLS_ACTION = {
    "robotic_reaction": tool_robotic_reaction,
    "robotic_measurement": tool_robotic_measurement,
    "robotic_characterization": tool_robotic_characterization,
}


# --- MCP协议通信部分 ---

def action_server_advertise_capabilities():
    """广播服务器提供的所有机器人动作"""
    adv_message = {
        "jsonrpc": "2.0",
        "method": "protocol/advertise",
        "params": {
            "type": "server",
            "server": {
                "protocolVersion": "0.1.0",
                "displayName": "Robotic Action Server",
                "capabilities": {
                    "tools": [
                        {
                            "name": "robotic_reaction",
                            "description": "指令机器人执行一个化学反应。这是一个耗时操作，成功后会返回一个新的样品ID。",
                            "parameters": {
                                "type": "object",
                                "properties": {
                                    "recipe": {"type": "object", "description": "描述反应物和条件的化学配方"},
                                    "vessel_id": {"type": "string", "description": "执行反应的容器ID, e.g., 'vessel_A'"}
                                },
                                "required": ["recipe", "vessel_id"]
                            }
                        },
                        {
                            "name": "robotic_measurement",
                            "description": "指令机器人对指定样品进行一次快速测量（如产率、pH值）。",
                            "parameters": {
                                "type": "object",
                                "properties": {
                                    "sample_id": {"type": "string", "description": "要测量的样品ID"},
                                    "measurement_type": {"type": "string",
                                                         "description": "要进行的测量类型, e.g., 'yield' or 'ph'"}
                                },
                                "required": ["sample_id", "measurement_type"]
                            }
                        },
                        {
                            "name": "robotic_characterization",
                            "description": "指令机器人对指定样品进行一次完整的表征分析（如光谱），返回数据文件的位置。",
                            "parameters": {
                                "type": "object",
                                "properties": {
                                    "sample_id": {"type": "string", "description": "要进行表征的样品ID"},
                                    "analysis_method": {"type": "string",
                                                        "description": "要使用的分析方法, e.g., 'HPLC', 'NMR'"}
                                },
                                "required": ["sample_id", "analysis_method"]
                            }
                        }
                    ]
                }
            }
        }
    }
    print(json.dumps(adv_message), flush=True)
    print("--- [MCP Server] Robotic Action Server is ready. ---", file=sys.stderr, flush=True)


def action_server_main_loop():
    """主循环，监听和响应Host的请求"""
    for line in sys.stdin:
        try:
            request = json.loads(line)
            request_id = request.get("id")
            method_name = request.get("method")
            params = request.get("params", {})

            if method_name in AVAILABLE_TOOLS_ACTION:
                tool_function = AVAILABLE_TOOLS_ACTION[method_name]
                result = tool_function(**params)
                response = {"jsonrpc": "2.0", "result": result, "id": request_id}
            else:
                response = {"jsonrpc": "2.0", "error": {"code": -32601, "message": f"Method not found: {method_name}"},
                            "id": request_id}

            print(json.dumps(response), flush=True)
        except Exception as e:
            error_msg = {"code": -32603, "message": f"Internal error: {e}"}
            response = {"jsonrpc": "2.0", "error": error_msg, "id": request.get("id")}
            print(json.dumps(response), flush=True)
            print(f"--- [MCP Server] Critical Error: {e} ---", file=sys.stderr, flush=True)


if __name__ == "__main__":
    action_server_advertise_capabilities()
    action_server_main_loop()
