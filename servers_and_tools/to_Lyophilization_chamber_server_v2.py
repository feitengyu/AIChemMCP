import sys
import json
# 动态导入当前设备对应的工具类
from to_Lyophilization_chamber_server_tools_v2 import UnifiedWorkstationTools


# 创建全局工具管理器实例
tool_manager = UnifiedWorkstationTools()


# --- 定义统一的工作站工具函数 ---
def tool_to_Lyophilization_chamber(task_description: str, **params):
    """
    执行冷冻干燥工作站的任务
    
    参数:
        task_description: 任务描述，说明要执行的具体操作
        **params: 其他可选参数，根据具体任务需要传递
    """
    return tool_manager.tool_to_Lyophilization_chamber(task_description, **params)



AVAILABLE_TOOLS = {
    "冷冻干燥工作站": tool_to_Lyophilization_chamber
}


# --- MCP协议通信主逻辑 ---
def to_Lyophilization_chamber_server_main_loop():
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
            print(f"--- [to_Lyophilization_chamber_Server] Error: {str(e)} ---", file=sys.stderr, flush=True)


def to_Lyophilization_chamber_server_advertise_capabilities():
    """广播当前设备的MCP能力"""
    adv_message = {
        "jsonrpc": "2.0",
        "method": "protocol/advertise",
        "params": {
            "type": "server",
            "server": {
                "protocolVersion": "0.1.0",
                "displayName": "冷冻干燥工作站",
                "capabilities": {
                    "tools": [
        {
            "name": "冷冻干燥工作站",
            "description": "冷冻干燥机的工作原理是先将含水物质冻结成固态，然后在真空条件下使其中的水分直接升华成气态而除去。它可以最大程度地保持物质的原有结构和性质，避免在干燥过程中因高温或水分的存在而导致物质的变性、氧化等问题。常用于生物制品、药品、食品等的干燥保存，能够延长产品的保质期，同时保持其活性和营养成分。例如在保存疫苗、血清等生物制品时，冷冻干燥技术可以有效地保持其生物活性。",
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
    print(f"--- [to_Lyophilization_chamber_Server] 冷冻干燥工作站 已就绪 ---", file=sys.stderr, flush=True)


if __name__ == "__main__":
    # 启动流程：先广播能力，再进入主循环
    to_Lyophilization_chamber_server_advertise_capabilities()
    to_Lyophilization_chamber_server_main_loop()
