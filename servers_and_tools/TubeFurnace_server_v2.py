import sys
import json
# 动态导入当前设备对应的工具类
from TubeFurnace_server_tools_v2 import UnifiedWorkstationTools


# 创建全局工具管理器实例
tool_manager = UnifiedWorkstationTools()


# --- 定义统一的工作站工具函数 ---
def tool_TubeFurnace(task_description: str, **params):
    """
    执行管式炉处理工作站的任务
    
    参数:
        task_description: 任务描述，说明要执行的具体操作
        **params: 其他可选参数，根据具体任务需要传递
    """
    return tool_manager.tool_TubeFurnace(task_description, **params)



AVAILABLE_TOOLS = {
    "管式炉处理工作站": tool_TubeFurnace
}


# --- MCP协议通信主逻辑 ---
def TubeFurnace_server_main_loop():
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
            print(f"--- [TubeFurnace_Server] Error: {str(e)} ---", file=sys.stderr, flush=True)


def TubeFurnace_server_advertise_capabilities():
    """广播当前设备的MCP能力"""
    adv_message = {
        "jsonrpc": "2.0",
        "method": "protocol/advertise",
        "params": {
            "type": "server",
            "server": {
                "protocolVersion": "0.1.0",
                "displayName": "管式炉处理工作站",
                "capabilities": {
                    "tools": [
        {
            "name": "管式炉处理工作站",
            "description": "自动化处理管式炉是一种具有自动化控制功能的高温热处理设备。它采用管状炉膛结构，通常用于对样品进行高温烧结、退火、焙烧等热处理工艺。通过先进的自动化控制系统，可以精确控制炉内的温度、升温速率、保温时间和降温速率等参数。样品放置在炉管内，可在不同气氛（如空气、氮气、氢气等）下进行处理。广泛应用于材料科学、陶瓷制造、粉末冶金等领域，用于制备和处理各种高性能材料，如陶瓷材料、金属基复合材料等，提高材料的性能和质量。",
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
    print(f"--- [TubeFurnace_Server] 管式炉处理工作站 已就绪 ---", file=sys.stderr, flush=True)


if __name__ == "__main__":
    # 启动流程：先广播能力，再进入主循环
    TubeFurnace_server_advertise_capabilities()
    TubeFurnace_server_main_loop()
