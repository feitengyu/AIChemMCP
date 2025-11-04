import sys
import json
# 动态导入当前设备对应的工具类（与主服务器文件同目录）
from tools.DialysisWorkstation_server_tools import ActionServerTools


# 创建全局工具管理器实例
tool_manager = ActionServerTools()


# --- 定义设备动作函数（自动生成，与工具类方法对应）---
def tool_to_shaker_Dialysis_card(**params):
    return tool_manager.tool_to_shaker_Dialysis_card(**params)


def tool_Solution_to_shaker_Dialysis_card(**params):
    return tool_manager.tool_Solution_to_shaker_Dialysis_card(**params)



AVAILABLE_TOOLS_ACTION = {
    "to_shaker_Dialysis_card": tool_to_shaker_Dialysis_card,
    "Solution_to_shaker_Dialysis_card": tool_Solution_to_shaker_Dialysis_card
}


# --- MCP协议通信主逻辑（自动适配当前设备）---
def DialysisWorkstation_server_main_loop():
    """主循环：监听并响应Host的MCP协议请求"""
    for line in sys.stdin:
        try:
            request = json.loads(line)
            request_id = request.get("id")
            method_name = request.get("method")
            params = request.get("params", {})

            if method_name in AVAILABLE_TOOLS_ACTION:
                # 调用对应的工具函数（传递请求参数）
                tool_function = AVAILABLE_TOOLS_ACTION[method_name]
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

            # 响应结果（强制刷新缓冲区）
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
            print(f"--- [DialysisWorkstation_Server] Critical Error: {str(e)} ---", file=sys.stderr, flush=True)


def DialysisWorkstation_server_advertise_capabilities():
    """广播当前设备的MCP能力（设备信息、支持的动作）"""
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
            "name": "to_shaker_Dialysis_card",
            "description": "将num个透析卡转移至摇床",
            "parameters": {
                "type": "object",
                "properties": {
    "data": {
        "type": "string",
        "description": "data"
    },
    "num": {
        "type": "int",
        "description": "num"
    },
    "temp": {
        "type": "int",
        "description": "temp"
    }
},
                "required": ["num", "temp"]
            }
        },
        {
            "name": "Solution_to_shaker_Dialysis_card",
            "description": "将num个瓶子里的溶液转移至透析卡里并透析多少分钟",
            "parameters": {
                "type": "object",
                "properties": {
    "data": {
        "type": "string",
        "description": "data"
    },
    "num": {
        "type": "int",
        "description": "num"
    },
    "time": {
        "type": "int",
        "description": "time"
    },
    "temp": {
        "type": "int",
        "description": "temp"
    }
},
                "required": ["data", "num", "time", "temp"]
            }
        }
                    ]
                }
            }
        }
    }
    print(json.dumps(adv_message, ensure_ascii=False), flush=True)
    print(f"--- [DialysisWorkstation_Server] 透析工作站 is ready. ---", file=sys.stderr, flush=True)


if __name__ == "__main__":
    # 启动流程：先广播能力，再进入主循环
    DialysisWorkstation_server_advertise_capabilities()
    DialysisWorkstation_server_main_loop()
