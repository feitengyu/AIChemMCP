import sys
import json
# 动态导入当前设备对应的工具类
from icpms_workstation_server_tools_v2 import UnifiedWorkstationTools


# 创建全局工具管理器实例
tool_manager = UnifiedWorkstationTools()


# --- 定义统一的工作站工具函数 ---
def tool_icpms_workstation(task_description: str, **params):
    """
    执行等离子体质谱仪的任务
    
    参数:
        task_description: 任务描述，说明要执行的具体操作
        **params: 其他可选参数，根据具体任务需要传递
    """
    return tool_manager.tool_icpms_workstation(task_description, **params)



AVAILABLE_TOOLS = {
    "等离子体质谱仪": tool_icpms_workstation
}


# --- MCP协议通信主逻辑 ---
def icpms_workstation_server_main_loop():
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
            print(f"--- [icpms_workstation_Server] Error: {str(e)} ---", file=sys.stderr, flush=True)


def icpms_workstation_server_advertise_capabilities():
    """广播当前设备的MCP能力"""
    adv_message = {
        "jsonrpc": "2.0",
        "method": "protocol/advertise",
        "params": {
            "type": "server",
            "server": {
                "protocolVersion": "0.1.0",
                "displayName": "等离子体质谱仪",
                "capabilities": {
                    "tools": [
        {
            "name": "等离子体质谱仪",
            "description": "电感耦合等离子体质谱仪是一种用于元素分析的高灵敏度仪器。它将样品引入高温等离子体中，使样品中的元素原子化并离子化，然后通过质谱仪对离子进行分离和检测。该仪器能够同时检测多种元素，并且具有极低的检测限，可检测到痕量甚至超痕量的元素。在环境监测、地质分析、生物医学等领域广泛应用。例如在环境样品中，可以检测重金属元素的含量；在生物医学研究中，可用于微量元素的代谢研究等。",
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
    print(f"--- [icpms_workstation_Server] 等离子体质谱仪 已就绪 ---", file=sys.stderr, flush=True)


if __name__ == "__main__":
    # 启动流程：先广播能力，再进入主循环
    icpms_workstation_server_advertise_capabilities()
    icpms_workstation_server_main_loop()
