import sys
import json
# 动态导入当前设备对应的工具类
from DialysisWorkstation_server_tools_v2 import UnifiedWorkstationTools


# 创建全局工具管理器实例
tool_manager = UnifiedWorkstationTools()


# --- 定义统一的工作站工具函数 ---
def tool_DialysisWorkstation(task_description: str, **params):
    """
    执行透析工作站的任务
    
    参数:
        task_description: 任务描述，说明要执行的具体操作
        **params: 其他可选参数，根据具体任务需要传递
    """
    return tool_manager.tool_DialysisWorkstation(task_description, **params)



AVAILABLE_TOOLS = {
    "透析工作站": tool_DialysisWorkstation
}


# --- MCP协议通信主逻辑 ---
def DialysisWorkstation_server_main_loop():
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
            print(f"--- [DialysisWorkstation_Server] Error: {str(e)} ---", file=sys.stderr, flush=True)


def DialysisWorkstation_server_advertise_capabilities():
    """广播当前设备的MCP能力"""
    adv_message = {
        "jsonrpc": "2.0",
        "method": "protocol/advertise",
        "params": {
            "type": "server",
            "server": {
                "protocolVersion": "0.1.0",
                "displayName": "透析工作站",
                "capabilities": {
                    "tools": [
        {
            "name": "透析工作站",
            "description": "样品透析装置主要用于分离和纯化生物分子。它利用半透膜的特性，允许小分子物质自由通过，而大分子物质则被截留在半透膜内。在实验中，可以将含有不同大小分子的样品放入透析袋或透析池中，通过不断更换透析液，使小分子杂质逐渐扩散到透析液中，从而达到分离和纯化大分子物质的目的。常用于蛋白质、核酸等生物大分子的提纯，去除样品中的盐离子、小分子杂质等。",
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
    print(f"--- [DialysisWorkstation_Server] 透析工作站 已就绪 ---", file=sys.stderr, flush=True)


if __name__ == "__main__":
    # 启动流程：先广播能力，再进入主循环
    DialysisWorkstation_server_advertise_capabilities()
    DialysisWorkstation_server_main_loop()
