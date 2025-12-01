import sys
import json
# 动态导入当前设备对应的工具类
from cod_server_tools_v2 import UnifiedWorkstationTools


# 创建全局工具管理器实例
tool_manager = UnifiedWorkstationTools()


# --- 定义统一的工作站工具函数 ---
def tool_cod(task_description: str, **params):
    """
    执行COD分析仪的任务
    
    参数:
        task_description: 任务描述，说明要执行的具体操作
        **params: 其他可选参数，根据具体任务需要传递
    """
    return tool_manager.tool_cod(task_description, **params)



AVAILABLE_TOOLS = {
    "COD分析仪": tool_cod
}


# --- MCP协议通信主逻辑 ---
def cod_server_main_loop():
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
            print(f"--- [cod_Server] Error: {str(e)} ---", file=sys.stderr, flush=True)


def cod_server_advertise_capabilities():
    """广播当前设备的MCP能力"""
    adv_message = {
        "jsonrpc": "2.0",
        "method": "protocol/advertise",
        "params": {
            "type": "server",
            "server": {
                "protocolVersion": "0.1.0",
                "displayName": "COD分析仪",
                "capabilities": {
                    "tools": [
        {
            "name": "COD分析仪",
            "description": "化学需氧量测定仪主要用于测定水样中有机物等还原性物质的含量。其原理是在强酸性条件下，用一定量的重铬酸钾氧化水样中的还原性物质，通过测量氧化剂的消耗量来计算化学需氧量（COD）的值。COD 是衡量水体受有机物污染程度的重要指标之一。在环境监测中，通过 COD 测定仪可以快速、准确地检测地表水、工业废水等的污染状况，为水质评价和污染治理提供依据。",
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
    print(f"--- [cod_Server] COD分析仪 已就绪 ---", file=sys.stderr, flush=True)


if __name__ == "__main__":
    # 启动流程：先广播能力，再进入主循环
    cod_server_advertise_capabilities()
    cod_server_main_loop()
