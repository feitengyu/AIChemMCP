import sys
import json
# 动态导入当前设备对应的工具类（与主服务器文件同目录）
from tools.NitrogenBlowing_server_tools import ActionServerTools


# 创建全局工具管理器实例
tool_manager = ActionServerTools()


# --- 定义设备动作函数（自动生成，与工具类方法对应）---
def tool_Move_toN(**params):
    return tool_manager.tool_Move_toN(**params)


def tool_N_blow(**params):
    return tool_manager.tool_N_blow(**params)


def tool_ethyl_ether_to_N(**params):
    return tool_manager.tool_ethyl_ether_to_N(**params)



AVAILABLE_TOOLS_ACTION = {
    "Move_toN": tool_Move_toN,
    "N_blow": tool_N_blow,
    "ethyl_ether_to_N": tool_ethyl_ether_to_N
}


# --- MCP协议通信主逻辑（自动适配当前设备）---
def NitrogenBlowing_server_main_loop():
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
            print(f"--- [NitrogenBlowing_Server] Critical Error: {str(e)} ---", file=sys.stderr, flush=True)


def NitrogenBlowing_server_advertise_capabilities():
    """广播当前设备的MCP能力（设备信息、支持的动作）"""
    adv_message = {
        "jsonrpc": "2.0",
        "method": "protocol/advertise",
        "params": {
            "type": "server",
            "server": {
                "protocolVersion": "0.1.0",
                "displayName": "氮吹工作站",
                "capabilities": {
                    "tools": [
        {
            "name": "Move_toN",
            "description": "将接收的多肽溶液转移至氮吹工位",
            "parameters": {
                "type": "object",
                "properties": {
    "data": {
        "type": "string",
        "description": "data"
    },
    "temp": {
        "type": "int",
        "description": "temp"
    }
},
                "required": ["data", "temp"]
            }
        },
        {
            "name": "N_blow",
            "description": "启动氮吹",
            "parameters": {
                "type": "object",
                "properties": {
    "data": {
        "type": "string",
        "description": "data"
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
                "required": ["data", "time", "temp"]
            }
        },
        {
            "name": "ethyl_ether_to_N",
            "description": "将瓶子从乙醚工位转移至氮吹工位",
            "parameters": {
                "type": "object",
                "properties": {
    "data": {
        "type": "string",
        "description": "data"
    },
    "temp": {
        "type": "int",
        "description": "temp"
    }
},
                "required": ["data", "temp"]
            }
        }
                    ]
                }
            }
        }
    }
    print(json.dumps(adv_message, ensure_ascii=False), flush=True)
    print(f"--- [NitrogenBlowing_Server] 氮吹工作站 is ready. ---", file=sys.stderr, flush=True)


if __name__ == "__main__":
    # 启动流程：先广播能力，再进入主循环
    NitrogenBlowing_server_advertise_capabilities()
    NitrogenBlowing_server_main_loop()
