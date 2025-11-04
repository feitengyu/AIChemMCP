import sys
import json
from tools.prediction_server_tools import PredictionServerTools

tool_manager = PredictionServerTools()


def tool_evaluate_suggestions():
    return tool_manager.tool_evaluate_suggestions()


def tool_active_learning_loop():
    return tool_manager.tool_active_learning_loop()


AVAILABLE_TOOLS_PREDICTION = {
    "evaluate_suggestions": tool_evaluate_suggestions,
    "active_learning_loop": tool_active_learning_loop
}


# --- MCP协议通信部分 ---
def prediction_server_advertise_capabilities():
    """广播服务器提供的所有预测小模型动作"""
    adv_message = {
        "jsonrpc": "2.0",
        "method": "protocol/advertise",
        "params": {
            "type": "server",
            "server": {
                "protocolVersion": "0.1.0",
                "displayName": "Prediction Server",
                "capabilities": {
                    "tools": [
                        {
                            "name": "evaluate_suggestions",
                            "description": "通过预测小模型对当前推荐进行初步验证。",
                            "parameters": {
                                "type": "object",
                                "properties": {
                                    "param_types": {"type": "array",
                                                    "description": "推荐使用的二元胺的类别，共有两种",
                                                    "items": {"type": "string"}},
                                    "param_values": {"type": "array",
                                                     "description": "推荐使用的二元胺的量，共有两个值，分别对应每一种胺",
                                                     "items": {"type": "number"}}
                                },
                                "required": ["param_types", "param_values"]
                            }
                        },
                        {
                            "name": "active_learning_loop",
                            "description": "通过历史数据对预测小模型进行迭代式的训练，以提高模型的准确性。",
                            "parameters": {
                                "type": "object",
                                "properties": {
                                    "params_types": {"type": "array",
                                                     "description": "历史数据中所有二元胺的类别的信息，每个元素是一个二元数组",
                                                     "items": {"type": "array",
                                                               "description": "使用的二元胺的类别，共有两种",
                                                               "items": {"type": "string"}}},
                                    "params_values": {"type": "array",
                                                      "description": "历史数据中所有二元胺的量的信息，每个元素是一个二元数组",
                                                      "items": {"type": "array",
                                                                "description": "使用的二元胺的量，共有两个值，分别对应每一种胺",
                                                                "items": {"type": "number"}}},
                                    "targets": {"type": "array",
                                                "description": "历史数据中所有二元胺的产物信息，每个元素是一个数字",
                                                "items": {"type": "number"}}
                                },
                                "required": ["params_types", "params_values", "targets"]
                            }
                        }
                    ]
                }
            }
        }
    }
    print(json.dumps(adv_message), flush=True)
    print("--- [MCP Server] Memory Server is ready. ---", file=sys.stderr, flush=True)


def prediction_server_main_loop():
    """主循环，监听和响应Host的请求"""
    for line in sys.stdin:
        try:
            request = json.loads(line)
            request_id = request.get("id")
            method_name = request.get("method")
            params = request.get("params", {})

            if method_name in AVAILABLE_TOOLS_PREDICTION:
                tool_function = AVAILABLE_TOOLS_PREDICTION[method_name]
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
    prediction_server_advertise_capabilities()
    prediction_server_main_loop()
