import sys
import json
# 动态导入当前设备对应的工具类
from gn_centrifugation_workstation_server_tools_v2 import UnifiedWorkstationTools


# 创建全局工具管理器实例
tool_manager = UnifiedWorkstationTools()


# --- 定义统一的工作站工具函数 ---
def tool_gn_centrifugation_workstation(task_description: str, **params):
    """
    执行离心工作站的任务
    
    参数:
        task_description: 任务描述，说明要执行的具体操作
        **params: 其他可选参数，根据具体任务需要传递
    """
    return tool_manager.tool_gn_centrifugation_workstation(task_description, **params)



AVAILABLE_TOOLS = {
    "离心工作站": tool_gn_centrifugation_workstation
}


# --- MCP协议通信主逻辑 ---
def gn_centrifugation_workstation_server_main_loop():
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
            print(f"--- [gn_centrifugation_workstation_Server] Error: {str(e)} ---", file=sys.stderr, flush=True)


def gn_centrifugation_workstation_server_advertise_capabilities():
    """广播当前设备的MCP能力"""
    adv_message = {
        "jsonrpc": "2.0",
        "method": "protocol/advertise",
        "params": {
            "type": "server",
            "server": {
                "protocolVersion": "0.1.0",
                "displayName": "离心工作站",
                "capabilities": {
                    "tools": [
        {
            "name": "离心工作站",
            "description": "离心处理工作站利用离心力的原理，对样品进行分离和处理。它配备有不同规格的转子，可以适应不同类型和体积的样品容器。通过调节离心速度、时间等参数，能够实现对不同密度、大小的物质的分离。在生物、化学等实验中广泛应用。例如在生物样品处理中，可用于分离细胞、细胞器等；在化学实验中，可用于沉淀的分离和溶液的澄清。",
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
    print(f"--- [gn_centrifugation_workstation_Server] 离心工作站 已就绪 ---", file=sys.stderr, flush=True)


if __name__ == "__main__":
    # 启动流程：先广播能力，再进入主循环
    gn_centrifugation_workstation_server_advertise_capabilities()
    gn_centrifugation_workstation_server_main_loop()
