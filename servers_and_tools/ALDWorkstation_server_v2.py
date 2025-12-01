import sys
import json
# 动态导入当前设备对应的工具类
from ALDWorkstation_server_tools_v2 import UnifiedWorkstationTools


# 创建全局工具管理器实例
tool_manager = UnifiedWorkstationTools()


# --- 定义统一的工作站工具函数 ---
def tool_ALDWorkstation(task_description: str, **params):
    """
    执行ALD工作站的任务
    
    参数:
        task_description: 任务描述，说明要执行的具体操作
        **params: 其他可选参数，根据具体任务需要传递
    """
    return tool_manager.tool_ALDWorkstation(task_description, **params)



AVAILABLE_TOOLS = {
    "ALD工作站": tool_ALDWorkstation
}


# --- MCP协议通信主逻辑 ---
def ALDWorkstation_server_main_loop():
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
            print(f"--- [ALDWorkstation_Server] Error: {str(e)} ---", file=sys.stderr, flush=True)


def ALDWorkstation_server_advertise_capabilities():
    """广播当前设备的MCP能力"""
    adv_message = {
        "jsonrpc": "2.0",
        "method": "protocol/advertise",
        "params": {
            "type": "server",
            "server": {
                "protocolVersion": "0.1.0",
                "displayName": "ALD工作站",
                "capabilities": {
                    "tools": [
        {
            "name": "ALD工作站",
            "description": "原子层沉积（ALD）催化剂合成系统是一种用于精确控制催化剂结构和组成的先进设备。它基于原子层沉积技术，通过交替脉冲式地将不同前驱体气体引入反应腔室，在基底表面进行自限制的化学反应，实现原子层厚度的薄膜或纳米结构的逐层生长。在催化剂合成方面，能够精确调控活性组分的负载量、分布和尺寸，制备出具有高度均匀性和重复性的催化剂。这有助于优化催化剂的性能，提高催化反应的活性、选择性和稳定性，广泛应用于能源催化、环境催化等领域，推动新型高效催化剂的研发和应用。",
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
    print(f"--- [ALDWorkstation_Server] ALD工作站 已就绪 ---", file=sys.stderr, flush=True)


if __name__ == "__main__":
    # 启动流程：先广播能力，再进入主循环
    ALDWorkstation_server_advertise_capabilities()
    ALDWorkstation_server_main_loop()
