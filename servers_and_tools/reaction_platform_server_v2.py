import sys
import json
# 动态导入当前设备对应的工具类
from reaction_platform_server_tools_v2 import UnifiedWorkstationTools


# 创建全局工具管理器实例
tool_manager = UnifiedWorkstationTools()


# --- 定义统一的工作站工具函数 ---
def tool_reaction_platform(task_description: str, **params):
    """
    执行综合反应平台的任务
    
    参数:
        task_description: 任务描述，说明要执行的具体操作
        **params: 其他可选参数，根据具体任务需要传递
    """
    return tool_manager.tool_reaction_platform(task_description, **params)



AVAILABLE_TOOLS = {
    "综合反应平台": tool_reaction_platform
}


# --- MCP协议通信主逻辑 ---
def reaction_platform_server_main_loop():
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
            print(f"--- [reaction_platform_Server] Error: {str(e)} ---", file=sys.stderr, flush=True)


def reaction_platform_server_advertise_capabilities():
    """广播当前设备的MCP能力"""
    adv_message = {
        "jsonrpc": "2.0",
        "method": "protocol/advertise",
        "params": {
            "type": "server",
            "server": {
                "protocolVersion": "0.1.0",
                "displayName": "综合反应平台",
                "capabilities": {
                    "tools": [
        {
            "name": "综合反应平台",
            "description": "液体加样平台是专门用于准确添加液体试剂的设备。它可以精确控制加样的体积，从微量到大量的液体都能实现精准加样。在生物与化学实验中，该平台广泛应用于细胞培养、PCR反应、药物筛选以及化合物管理等场景，可确保每个样品添加的试剂体积一致，提高实验的重复性和可靠性。其自动化的加样过程减少了人工操作的误差，提高了实验效率，是生物、化学等实验室常用的液体处理设备。",
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
    print(f"--- [reaction_platform_Server] 综合反应平台 已就绪 ---", file=sys.stderr, flush=True)


if __name__ == "__main__":
    # 启动流程：先广播能力，再进入主循环
    reaction_platform_server_advertise_capabilities()
    reaction_platform_server_main_loop()
