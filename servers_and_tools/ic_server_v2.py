import sys
import json
# 动态导入当前设备对应的工具类
from ic_server_tools_v2 import UnifiedWorkstationTools


# 创建全局工具管理器实例
tool_manager = UnifiedWorkstationTools()


# --- 定义统一的工作站工具函数 ---
def tool_ic(task_description: str, **params):
    """
    执行离子色谱的任务
    
    参数:
        task_description: 任务描述，说明要执行的具体操作
        **params: 其他可选参数，根据具体任务需要传递
    """
    return tool_manager.tool_ic(task_description, **params)



AVAILABLE_TOOLS = {
    "离子色谱": tool_ic
}


# --- MCP协议通信主逻辑 ---
def ic_server_main_loop():
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
            print(f"--- [ic_Server] Error: {str(e)} ---", file=sys.stderr, flush=True)


def ic_server_advertise_capabilities():
    """广播当前设备的MCP能力"""
    adv_message = {
        "jsonrpc": "2.0",
        "method": "protocol/advertise",
        "params": {
            "type": "server",
            "server": {
                "protocolVersion": "0.1.0",
                "displayName": "离子色谱",
                "capabilities": {
                    "tools": [
        {
            "name": "离子色谱",
            "description": "离子色谱仪主要用于分离和检测溶液中的各种离子。它利用离子交换树脂对不同离子的亲和力差异，将混合溶液中的离子进行分离，然后通过检测器对分离后的离子进行定量分析。在环境监测等领域广泛应用。例如在环境水样检测中，可以检测水中的常见阴离子（如氯离子、硝酸根离子、硫酸根离子等）的含量，评估水质的污染程度；在食品检测中，可检测食品中的添加剂、营养成分等所含的离子。",
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
    print(f"--- [ic_Server] 离子色谱 已就绪 ---", file=sys.stderr, flush=True)


if __name__ == "__main__":
    # 启动流程：先广播能力，再进入主循环
    ic_server_advertise_capabilities()
    ic_server_main_loop()
