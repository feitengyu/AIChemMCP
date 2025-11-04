import sys
import json
# 动态导入当前设备对应的工具类（与主服务器文件同目录）
from tools.SolutionAspirationWorkstation_A_server_tools import ActionServerTools


# 创建全局工具管理器实例
tool_manager = ActionServerTools()


# --- 定义设备动作函数（自动生成，与工具类方法对应）---
def tool_group1(**params):
    return tool_manager.tool_group1(**params)



AVAILABLE_TOOLS_ACTION = {
    "group1": tool_group1
}


# --- MCP协议通信主逻辑（自动适配当前设备）---
def SolutionAspirationWorkstation_A_server_main_loop():
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
            print(f"--- [SolutionAspirationWorkstation_A_Server] Critical Error: {str(e)} ---", file=sys.stderr, flush=True)


def SolutionAspirationWorkstation_A_server_advertise_capabilities():
    """广播当前设备的MCP能力（设备信息、支持的动作）"""
    adv_message = {
        "jsonrpc": "2.0",
        "method": "protocol/advertise",
        "params": {
            "type": "server",
            "server": {
                "protocolVersion": "0.1.0",
                "displayName": "溶液A吸取工作站",
                "capabilities": {
                    "tools": [
        {
            "name": "group1",
            "description": "吸取溶液A",
            "parameters": {
                "type": "object",
                "properties": {
    "type": {
        "type": "int",
        "description": "对应的group分组"
    },
    "ml_A": {
        "type": "int",
        "description": "吸取A溶液50ul"
    },
    "ml_B": {
        "type": "int",
        "description": "吸取B溶液50ul"
    },
    "time1": {
        "type": "int",
        "description": "振荡 2 min"
    },
    "ml": {
        "type": "int",
        "description": "吸取混匀后的液体 50 uL"
    },
    "add": {
        "type": "int",
        "description": "旋涂加速度 2000 rpm"
    },
    "speed": {
        "type": "int",
        "description": "旋涂转速rpm"
    },
    "time2": {
        "type": "int",
        "description": "旋涂时间"
    },
    "temperature": {
        "type": "int",
        "description": "退火温度-摄氏度"
    },
    "time3": {
        "type": "int",
        "description": "退火时间min"
    },
    "length": {
        "type": "int",
        "description": "荧光光谱检测波长"
    },
    "up": {
        "type": "int",
        "description": "荧光光谱检测波长测量上限"
    },
    "down": {
        "type": "int",
        "description": "荧光光谱检测波长测量下限"
    }
},
                "required": ["type", "ml_A", "ml_B", "time1", "ml", "add", "speed", "time2", "temperature", "time3", "length", "up", "down"]
            }
        }
                    ]
                }
            }
        }
    }
    print(json.dumps(adv_message, ensure_ascii=False), flush=True)
    print(f"--- [SolutionAspirationWorkstation_A_Server] 溶液A吸取工作站 is ready. ---", file=sys.stderr, flush=True)


if __name__ == "__main__":
    # 启动流程：先广播能力，再进入主循环
    SolutionAspirationWorkstation_A_server_advertise_capabilities()
    SolutionAspirationWorkstation_A_server_main_loop()
