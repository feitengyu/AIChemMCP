import sys
import json
# 动态导入当前设备对应的工具类（与主服务器文件同目录）
from tools.solid_dispensing_server_tools import ActionServerTools


# 创建全局工具管理器实例
tool_manager = ActionServerTools()


# --- 定义设备动作函数（自动生成，与工具类方法对应）---
def tool_door_open(**params):
    return tool_manager.tool_door_open(**params)


def tool_door_close(**params):
    return tool_manager.tool_door_close(**params)


def tool_set_balance(**params):
    return tool_manager.tool_set_balance(**params)


def tool_force_online(**params):
    return tool_manager.tool_force_online(**params)


def tool_force_offline(**params):
    return tool_manager.tool_force_offline(**params)



AVAILABLE_TOOLS_ACTION = {
    "door_open": tool_door_open,
    "door_close": tool_door_close,
    "set_balance": tool_set_balance,
    "force_online": tool_force_online,
    "force_offline": tool_force_offline
}


# --- MCP协议通信主逻辑（自动适配当前设备）---
def solid_dispensing_server_main_loop():
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
            print(f"--- [solid_dispensing_Server] Critical Error: {str(e)} ---", file=sys.stderr, flush=True)


def solid_dispensing_server_advertise_capabilities():
    """广播当前设备的MCP能力（设备信息、支持的动作）"""
    adv_message = {
        "jsonrpc": "2.0",
        "method": "protocol/advertise",
        "params": {
            "type": "server",
            "server": {
                "protocolVersion": "0.1.0",
                "displayName": "固体进样工作站",
                "capabilities": {
                    "tools": [
        {
            "name": "door_open",
            "description": "开门",
            "parameters": {
                "type": "object",
                "properties": {
    "operation": {
        "type": "string",
        "description": "参数 operation"
    },
    "door_position": {
        "type": "string",
        "description": "开门位置",
        "enum": [
            "right",
            "left",
            "all"
        ]
    }
},
                "required": ["operation"]
            }
        },
        {
            "name": "door_close",
            "description": "关门",
            "parameters": {
                "type": "object",
                "properties": {
    "operation": {
        "type": "string",
        "description": "参数 operation"
    },
    "door_position": {
        "type": "string",
        "description": "关门位置",
        "enum": [
            "right",
            "left",
            "all"
        ]
    }
},
                "required": ["operation"]
            }
        },
        {
            "name": "set_balance",
            "description": "进样",
            "parameters": {
                "type": "object",
                "properties": {
    "operation": {
        "type": "string",
        "description": "参数 operation"
    },
    "weight": {
        "type": "float",
        "description": "进样质量（克）",
        "minimum": "0",
        "maximum": "200"
    }
},
                "required": ["operation", "weight"]
            }
        },
        {
            "name": "force_online",
            "description": "强制上线",
            "parameters": {
                "type": "object",
                "properties": {
    "operation": {
        "type": "string",
        "description": "操作类型"
    }
},
                "required": ["operation"]
            }
        },
        {
            "name": "force_offline",
            "description": "强制下线",
            "parameters": {
                "type": "object",
                "properties": {
    "operation": {
        "type": "string",
        "description": "操作类型"
    }
},
                "required": ["operation"]
            }
        }
                    ]
                }
            }
        }
    }
    print(json.dumps(adv_message, ensure_ascii=False), flush=True)
    print(f"--- [solid_dispensing_Server] 固体进样工作站 is ready. ---", file=sys.stderr, flush=True)


if __name__ == "__main__":
    # 启动流程：先广播能力，再进入主循环
    solid_dispensing_server_advertise_capabilities()
    solid_dispensing_server_main_loop()
