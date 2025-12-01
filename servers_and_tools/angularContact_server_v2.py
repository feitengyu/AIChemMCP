import sys
import json
# 动态导入当前设备对应的工具类
from angularContact_server_tools_v2 import UnifiedWorkstationTools


# 创建全局工具管理器实例
tool_manager = UnifiedWorkstationTools()


# --- 定义统一的工作站工具函数 ---
def tool_angularContact(task_description: str, **params):
    """
    执行角接触仪工作站的任务
    
    参数:
        task_description: 任务描述，说明要执行的具体操作
        **params: 其他可选参数，根据具体任务需要传递
    """
    return tool_manager.tool_angularContact(task_description, **params)



AVAILABLE_TOOLS = {
    "角接触仪工作站": tool_angularContact
}


# --- MCP协议通信主逻辑 ---
def angularContact_server_main_loop():
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
            print(f"--- [angularContact_Server] Error: {str(e)} ---", file=sys.stderr, flush=True)


def angularContact_server_advertise_capabilities():
    """广播当前设备的MCP能力"""
    adv_message = {
        "jsonrpc": "2.0",
        "method": "protocol/advertise",
        "params": {
            "type": "server",
            "server": {
                "protocolVersion": "0.1.0",
                "displayName": "角接触仪工作站",
                "capabilities": {
                    "tools": [
        {
            "name": "角接触仪工作站",
            "description": "接触角测量仪用于测量液体在固体表面的接触角，从而分析液体对固体表面的润湿性能。其原理是通过光学系统精确捕捉液体在固体表面形成的液滴形状，然后利用相应的算法计算出接触角的大小。在材料表面性能研究、涂料研发等领域有着重要应用。例如在研究防水涂层材料时，通过测量水滴在涂层表面的接触角，可以评估涂层的防水性能；在印刷行业中，测量油墨与纸张表面的接触角，有助于优化印刷工艺，提高印刷质量。",
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
    print(f"--- [angularContact_Server] 角接触仪工作站 已就绪 ---", file=sys.stderr, flush=True)


if __name__ == "__main__":
    # 启动流程：先广播能力，再进入主循环
    angularContact_server_advertise_capabilities()
    angularContact_server_main_loop()
