import sys
import json
# 动态导入当前设备对应的工具类
from furnace_workstation_server_tools_v2 import UnifiedWorkstationTools


# 创建全局工具管理器实例
tool_manager = UnifiedWorkstationTools()


# --- 定义统一的工作站工具函数 ---
def tool_furnace_workstation(task_description: str, **params):
    """
    执行电化学-高温炉的任务
    
    参数:
        task_description: 任务描述，说明要执行的具体操作
        **params: 其他可选参数，根据具体任务需要传递
    """
    return tool_manager.tool_furnace_workstation(task_description, **params)



AVAILABLE_TOOLS = {
    "电化学-高温炉": tool_furnace_workstation
}


# --- MCP协议通信主逻辑 ---
def furnace_workstation_server_main_loop():
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
            print(f"--- [furnace_workstation_Server] Error: {str(e)} ---", file=sys.stderr, flush=True)


def furnace_workstation_server_advertise_capabilities():
    """广播当前设备的MCP能力"""
    adv_message = {
        "jsonrpc": "2.0",
        "method": "protocol/advertise",
        "params": {
            "type": "server",
            "server": {
                "protocolVersion": "0.1.0",
                "displayName": "电化学-高温炉",
                "capabilities": {
                    "tools": [
        {
            "name": "电化学-高温炉",
            "description": "焦耳加热炉是利用电流通过电阻产生热量的原理来对样品进行加热的设备。它可以精确控制加热的温度、时间和升温速率等参数。在材料研究中，可用于对金属、陶瓷等材料进行热处理，改变材料的组织结构和性能，如提高金属的硬度、改善陶瓷的韧性等。在化学合成中，可用于提供特定的反应温度环境，促进化学反应的进行，对于一些需要高温条件的化学反应具有重要作用。",
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
    print(f"--- [furnace_workstation_Server] 电化学-高温炉 已就绪 ---", file=sys.stderr, flush=True)


if __name__ == "__main__":
    # 启动流程：先广播能力，再进入主循环
    furnace_workstation_server_advertise_capabilities()
    furnace_workstation_server_main_loop()
