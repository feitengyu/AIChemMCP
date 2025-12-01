import sys
import json
# 动态导入当前设备对应的工具类
from confecting_workstation_server_tools_v2 import UnifiedWorkstationTools


# 创建全局工具管理器实例
tool_manager = UnifiedWorkstationTools()


# --- 定义统一的工作站工具函数 ---
def tool_confecting_workstation(task_description: str, **params):
    """
    执行电化学-配液仪的任务
    
    参数:
        task_description: 任务描述，说明要执行的具体操作
        **params: 其他可选参数，根据具体任务需要传递
    """
    return tool_manager.tool_confecting_workstation(task_description, **params)



AVAILABLE_TOOLS = {
    "电化学-配液仪": tool_confecting_workstation
}


# --- MCP协议通信主逻辑 ---
def confecting_workstation_server_main_loop():
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
            print(f"--- [confecting_workstation_Server] Error: {str(e)} ---", file=sys.stderr, flush=True)


def confecting_workstation_server_advertise_capabilities():
    """广播当前设备的MCP能力"""
    adv_message = {
        "jsonrpc": "2.0",
        "method": "protocol/advertise",
        "params": {
            "type": "server",
            "server": {
                "protocolVersion": "0.1.0",
                "displayName": "电化学-配液仪",
                "capabilities": {
                    "tools": [
        {
            "name": "电化学-配液仪",
            "description": "高通量自动配液仪能够快速、准确地配制不同浓度和体积的溶液。它可以按照预设的配方，自动吸取不同体积的试剂和溶剂，进行混合和稀释操作。在生物实验中，可用于配制细胞培养液、缓冲液等；在化学分析中，可用于配制标准溶液。相比于手动配液，自动配液仪具有更高的精度和重复性，能够同时处理多个样品，大大提高了配液的效率，适用于高通量的实验需求。",
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
    print(f"--- [confecting_workstation_Server] 电化学-配液仪 已就绪 ---", file=sys.stderr, flush=True)


if __name__ == "__main__":
    # 启动流程：先广播能力，再进入主循环
    confecting_workstation_server_advertise_capabilities()
    confecting_workstation_server_main_loop()
