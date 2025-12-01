import sys
import json
# 动态导入当前设备对应的工具类
from lithography_server_tools_v2 import UnifiedWorkstationTools


# 创建全局工具管理器实例
tool_manager = UnifiedWorkstationTools()


# --- 定义统一的工作站工具函数 ---
def tool_lithography(task_description: str, **params):
    """
    执行光刻工作站的任务
    
    参数:
        task_description: 任务描述，说明要执行的具体操作
        **params: 其他可选参数，根据具体任务需要传递
    """
    return tool_manager.tool_lithography(task_description, **params)



AVAILABLE_TOOLS = {
    "光刻工作站": tool_lithography
}


# --- MCP协议通信主逻辑 ---
def lithography_server_main_loop():
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
            print(f"--- [lithography_Server] Error: {str(e)} ---", file=sys.stderr, flush=True)


def lithography_server_advertise_capabilities():
    """广播当前设备的MCP能力"""
    adv_message = {
        "jsonrpc": "2.0",
        "method": "protocol/advertise",
        "params": {
            "type": "server",
            "server": {
                "protocolVersion": "0.1.0",
                "displayName": "光刻工作站",
                "capabilities": {
                    "tools": [
        {
            "name": "光刻工作站",
            "description": "纳米级三维激光直写 3D 打印设备（光刻胶专用）是一种高精度的微纳加工设备。它利用激光束对光刻胶进行逐点、逐层扫描曝光，通过控制激光的强度、扫描速度和曝光时间等参数，实现纳米级分辨率的三维结构制造。能够制造出复杂的微纳结构，如微纳光学器件、生物芯片、微机电系统等。该设备在微纳制造、生物医学工程、光学等领域具有重要应用，为这些领域的研究和产品开发提供了强大的微纳加工手段，推动了微纳技术的发展和应用。",
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
    print(f"--- [lithography_Server] 光刻工作站 已就绪 ---", file=sys.stderr, flush=True)


if __name__ == "__main__":
    # 启动流程：先广播能力，再进入主循环
    lithography_server_advertise_capabilities()
    lithography_server_main_loop()
