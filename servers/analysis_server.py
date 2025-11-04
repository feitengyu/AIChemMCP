import sys
import json
from tools.analysis_server_tools import AnalysisServerTools


tool_manager = AnalysisServerTools()


def tool_analyse_results():
    return tool_manager.tool_analyse_results()


def tool_analysis_suggestion():
    return tool_manager.tool_analysis_suggestion()


AVAILABLE_TOOLS_ANALYSIS = {
    "analyse_results": tool_analyse_results,
    "analysis_suggestion": tool_analysis_suggestion
}


# --- MCP协议通信部分 ---
def analysis_server_advertise_capabilities():
    """广播服务器提供的所有大语言分析动作"""
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
                            "name": "analyse_results",
                            "description": "使用大语言模型分析历史数据，根据分析结果提出五个化学假设。对于每个假设，必须要给出其逻辑，以及哪些历史数据支持这个假设。",
                            "parameters": {
                                "type": "object",
                                "properties": {
                                    "hypotheses": {"type": "string", "description": "描述反应物和条件的化学配方"},
                                    "logics": {"type": "string", "description": "执行反应的容器ID, e.g., 'vessel_A'"},
                                    "supporting_data": {"type": "array", "description": ""}
                                },
                                "required": ["recipe", "vessel_id"]
                            }
                        },
                        {
                            "name": "analysis_suggestion",
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
                        }
                    ]
                }
            }
        }
    }
    print(json.dumps(adv_message), flush=True)
    print("--- [MCP Server] LLM Analysis Server is ready. ---", file=sys.stderr, flush=True)


def analysis_server_main_loop():
    """主循环，监听和响应Host的请求"""
    for line in sys.stdin:
        try:
            request = json.loads(line)
            request_id = request.get("id")
            method_name = request.get("method")
            params = request.get("params", {})

            if method_name in AVAILABLE_TOOLS_ANALYSIS:
                tool_function = AVAILABLE_TOOLS_ANALYSIS[method_name]
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
    analysis_server_advertise_capabilities()
    analysis_server_main_loop()
