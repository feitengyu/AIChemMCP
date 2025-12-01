import sys
import json
# 动态导入当前设备对应的工具类
from liquid_dispensing_server_tools_v2 import UnifiedWorkstationTools


# 创建全局工具管理器实例
tool_manager = UnifiedWorkstationTools()


# --- 定义统一的工作站工具函数 ---
def tool_liquid_dispensing(task_description: str, **params):
    """
    执行液体进样站的任务
    
    参数:
        task_description: 任务描述，说明要执行的具体操作
        **params: 其他可选参数，根据具体任务需要传递
    """
    return tool_manager.tool_liquid_dispensing(task_description, **params)



AVAILABLE_TOOLS = {
    "液体进样站": tool_liquid_dispensing
}


# --- MCP协议通信主逻辑 ---
def liquid_dispensing_server_main_loop():
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
            print(f"--- [liquid_dispensing_Server] Error: {str(e)} ---", file=sys.stderr, flush=True)


def liquid_dispensing_server_advertise_capabilities():
    """广播当前设备的MCP能力"""
    adv_message = {
        "jsonrpc": "2.0",
        "method": "protocol/advertise",
        "params": {
            "type": "server",
            "server": {
                "protocolVersion": "0.1.0",
                "displayName": "液体进样站",
                "capabilities": {
                    "tools": [
        {
            "name": "液体进样站",
            "description": "自动液体处理工作站是一种多功能的液体处理设备。它可以进行精确的移液、分液、混合等操作，并且能够根据不同的实验需求进行灵活编程。其配备的高精度液体处理模块和智能控制系统，确保了液体处理的准确性和重复性。在药物研发、临床检验等领域，可用于高通量的样品处理，如药物筛选实验中的样品稀释、混合等操作，提高实验效率和质量。",
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
    print(f"--- [liquid_dispensing_Server] 液体进样站 已就绪 ---", file=sys.stderr, flush=True)


if __name__ == "__main__":
    # 启动流程：先广播能力，再进入主循环
    liquid_dispensing_server_advertise_capabilities()
    liquid_dispensing_server_main_loop()
