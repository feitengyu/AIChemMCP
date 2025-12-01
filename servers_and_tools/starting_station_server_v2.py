import sys
import json
# 动态导入当前设备对应的工具类
from starting_station_server_tools_v2 import UnifiedWorkstationTools


# 创建全局工具管理器实例
tool_manager = UnifiedWorkstationTools()


# --- 定义统一的工作站工具函数 ---
def tool_starting_station(task_description: str, **params):
    """
    执行物料站的任务
    
    参数:
        task_description: 任务描述，说明要执行的具体操作
        **params: 其他可选参数，根据具体任务需要传递
    """
    return tool_manager.tool_starting_station(task_description, **params)



AVAILABLE_TOOLS = {
    "物料站": tool_starting_station
}


# --- MCP协议通信主逻辑 ---
def starting_station_server_main_loop():
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
            print(f"--- [starting_station_Server] Error: {str(e)} ---", file=sys.stderr, flush=True)


def starting_station_server_advertise_capabilities():
    """广播当前设备的MCP能力"""
    adv_message = {
        "jsonrpc": "2.0",
        "method": "protocol/advertise",
        "params": {
            "type": "server",
            "server": {
                "protocolVersion": "0.1.0",
                "displayName": "物料站",
                "capabilities": {
                    "tools": [
        {
            "name": "物料站",
            "description": "实验室试剂储存柜主要用于安全、规范地储存各种化学试剂。它通常具有良好的通风、防火、防爆等功能，以确保试剂的储存安全。根据试剂的性质，如易燃、易爆、有毒、腐蚀性等，储存柜会进行分类存储，避免不同性质的试剂相互反应。同时，储存柜还配备有合理的标识和管理系统，方便试剂的查找和取用，有助于提高实验室的管理水平和安全性，保障实验工作的顺利进行。",
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
    print(f"--- [starting_station_Server] 物料站 已就绪 ---", file=sys.stderr, flush=True)


if __name__ == "__main__":
    # 启动流程：先广播能力，再进入主循环
    starting_station_server_advertise_capabilities()
    starting_station_server_main_loop()
