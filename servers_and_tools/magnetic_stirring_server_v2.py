import sys
import json
# 动态导入当前设备对应的工具类
from magnetic_stirring_server_tools_v2 import UnifiedWorkstationTools


# 创建全局工具管理器实例
tool_manager = UnifiedWorkstationTools()


# --- 定义统一的工作站工具函数 ---
def tool_magnetic_stirring(task_description: str, **params):
    """
    执行磁力搅拌工作站的任务
    
    参数:
        task_description: 任务描述，说明要执行的具体操作
        **params: 其他可选参数，根据具体任务需要传递
    """
    return tool_manager.tool_magnetic_stirring(task_description, **params)



AVAILABLE_TOOLS = {
    "磁力搅拌工作站": tool_magnetic_stirring
}


# --- MCP协议通信主逻辑 ---
def magnetic_stirring_server_main_loop():
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
            print(f"--- [magnetic_stirring_Server] Error: {str(e)} ---", file=sys.stderr, flush=True)


def magnetic_stirring_server_advertise_capabilities():
    """广播当前设备的MCP能力"""
    adv_message = {
        "jsonrpc": "2.0",
        "method": "protocol/advertise",
        "params": {
            "type": "server",
            "server": {
                "protocolVersion": "0.1.0",
                "displayName": "磁力搅拌工作站",
                "capabilities": {
                    "tools": [
        {
            "name": "磁力搅拌工作站",
            "description": "磁力搅拌工作站通过旋转的磁盘产生的离心力和剪切力，对放置在磁盘上的容器内的液体进行搅拌。它可以实现快速、高效的搅拌效果，使溶液充分混合。该工作站通常具有可调节的搅拌速度和时间设置，能够满足不同实验的需求。在化学合成、材料制备等实验中，可用于加速化学反应、促进物质的溶解和混合等，提高实验效率和产品质量。",
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
    print(f"--- [magnetic_stirring_Server] 磁力搅拌工作站 已就绪 ---", file=sys.stderr, flush=True)


if __name__ == "__main__":
    # 启动流程：先广播能力，再进入主循环
    magnetic_stirring_server_advertise_capabilities()
    magnetic_stirring_server_main_loop()
