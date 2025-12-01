import sys
import json
# 动态导入当前设备对应的工具类
from nh3n_server_tools_v2 import UnifiedWorkstationTools


# 创建全局工具管理器实例
tool_manager = UnifiedWorkstationTools()


# --- 定义统一的工作站工具函数 ---
def tool_nh3n(task_description: str, **params):
    """
    执行氨氮工作站的任务
    
    参数:
        task_description: 任务描述，说明要执行的具体操作
        **params: 其他可选参数，根据具体任务需要传递
    """
    return tool_manager.tool_nh3n(task_description, **params)



AVAILABLE_TOOLS = {
    "氨氮工作站": tool_nh3n
}


# --- MCP协议通信主逻辑 ---
def nh3n_server_main_loop():
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
            print(f"--- [nh3n_Server] Error: {str(e)} ---", file=sys.stderr, flush=True)


def nh3n_server_advertise_capabilities():
    """广播当前设备的MCP能力"""
    adv_message = {
        "jsonrpc": "2.0",
        "method": "protocol/advertise",
        "params": {
            "type": "server",
            "server": {
                "protocolVersion": "0.1.0",
                "displayName": "氨氮工作站",
                "capabilities": {
                    "tools": [
        {
            "name": "氨氮工作站",
            "description": "氨氮测定仪专门用于测定水样中氨氮的含量。氨氮是指水中以游离氨（NH₃）和铵离子（NH₄⁺）形式存在的氮。该仪器通常采用比色法等检测方法，通过与特定试剂反应，生成具有特定颜色的产物，然后根据颜色的深浅来定量测定氨氮的含量。在水质监测中，氨氮含量是评估水体污染程度的重要指标之一，过高的氨氮含量会对水生生物造成危害，氨氮测定仪对于及时掌握水质状况和采取相应治理措施具有重要意义。",
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
    print(f"--- [nh3n_Server] 氨氮工作站 已就绪 ---", file=sys.stderr, flush=True)


if __name__ == "__main__":
    # 启动流程：先广播能力，再进入主循环
    nh3n_server_advertise_capabilities()
    nh3n_server_main_loop()
