import sys
import json
# 动态导入当前设备对应的工具类
from photothermal_catalytic_reaction_workstation_server_tools_v2 import UnifiedWorkstationTools


# 创建全局工具管理器实例
tool_manager = UnifiedWorkstationTools()


# --- 定义统一的工作站工具函数 ---
def tool_photothermal_catalytic_reaction_workstation(task_description: str, **params):
    """
    执行光热催化反应工作站的任务
    
    参数:
        task_description: 任务描述，说明要执行的具体操作
        **params: 其他可选参数，根据具体任务需要传递
    """
    return tool_manager.tool_photothermal_catalytic_reaction_workstation(task_description, **params)



AVAILABLE_TOOLS = {
    "光热催化反应工作站": tool_photothermal_catalytic_reaction_workstation
}


# --- MCP协议通信主逻辑 ---
def photothermal_catalytic_reaction_workstation_server_main_loop():
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
            print(f"--- [photothermal_catalytic_reaction_workstation_Server] Error: {str(e)} ---", file=sys.stderr, flush=True)


def photothermal_catalytic_reaction_workstation_server_advertise_capabilities():
    """广播当前设备的MCP能力"""
    adv_message = {
        "jsonrpc": "2.0",
        "method": "protocol/advertise",
        "params": {
            "type": "server",
            "server": {
                "protocolVersion": "0.1.0",
                "displayName": "光热催化反应工作站",
                "capabilities": {
                    "tools": [
        {
            "name": "光热催化反应工作站",
            "description": "温度控制器是一种用于精确控制温度的设备。在实验室中，许多实验需要在特定的温度条件下进行，温度控制器能够实时监测环境或样品的温度，并根据设定的温度值自动调节加热或制冷设备的工作状态，使温度保持在设定的范围内。它具有高精度的温度控制功能，可以将温度波动控制在极小的范围内，确保实验在稳定的温度条件下进行。温度控制器可应用于各种需要温度控制的实验场景，如材料热处理、生物培养、化学反应等，为实验结果的准确性和可靠性提供重要保障。",
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
    print(f"--- [photothermal_catalytic_reaction_workstation_Server] 光热催化反应工作站 已就绪 ---", file=sys.stderr, flush=True)


if __name__ == "__main__":
    # 启动流程：先广播能力，再进入主循环
    photothermal_catalytic_reaction_workstation_server_advertise_capabilities()
    photothermal_catalytic_reaction_workstation_server_main_loop()
