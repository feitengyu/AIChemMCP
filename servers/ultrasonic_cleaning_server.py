import sys
import json
# 动态导入当前设备对应的工具类（与主服务器文件同目录）
from ultrasonic_cleaning_server_tools import ActionServerTools


# 创建全局工具管理器实例
tool_manager = ActionServerTools()


# --- 定义设备动作函数（自动生成，与工具类方法对应）---
def tool_add_water(**params):
    return tool_manager.tool_add_water(**params)


def tool_drain_water(**params):
    return tool_manager.tool_drain_water(**params)


def tool_stop_clean(**params):
    return tool_manager.tool_stop_clean(**params)


def tool_open_heat(**params):
    return tool_manager.tool_open_heat(**params)


def tool_close_heat(**params):
    return tool_manager.tool_close_heat(**params)


def tool_start_clean(**params):
    return tool_manager.tool_start_clean(**params)



AVAILABLE_TOOLS_ACTION = {
    "add-water": tool_add_water,
    "drain-water": tool_drain_water,
    "stop_clean": tool_stop_clean,
    "open-heat": tool_open_heat,
    "close-heat": tool_close_heat,
    "start_clean": tool_start_clean
}


# --- MCP协议通信主逻辑（自动适配当前设备）---
def ultrasonic_cleaning_server_main_loop():
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
            print(f"--- [ultrasonic_cleaning_Server] Critical Error: {str(e)} ---", file=sys.stderr, flush=True)


def ultrasonic_cleaning_server_advertise_capabilities():
    """广播当前设备的MCP能力（设备信息、支持的动作）"""
    adv_message = {
        "jsonrpc": "2.0",
        "method": "protocol/advertise",
        "params": {
            "type": "server",
            "server": {
                "protocolVersion": "0.1.0",
                "displayName": "超声清洗",
                "capabilities": {
                    "tools": [
        {
            "name": "add-water",
            "description": "加水",
            "parameters": {
                "type": "object",
                "properties": {
    "operation": {
        "type": "string",
        "description": "操作符"
    },
    "value": {
        "type": "int",
        "description": "加水时间（单位：秒）"
    }
},
                "required": ["operation", "value"]
            }
        },
        {
            "name": "drain-water",
            "description": "排水",
            "parameters": {
                "type": "object",
                "properties": {
    "operation": {
        "type": "string",
        "description": "操作符"
    },
    "value": {
        "type": "int",
        "description": "排水时间（单位：秒）"
    }
},
                "required": ["operation", "value"]
            }
        },
        {
            "name": "stop_clean",
            "description": "停⽌超声清洗",
            "parameters": {
                "type": "object",
                "properties": {
    "operation": {
        "type": "string",
        "description": "操作符"
    },
    "value": {
        "type": "int",
        "description": "数值"
    }
},
                "required": ["operation", "value"]
            }
        },
        {
            "name": "open-heat",
            "description": "开启加热",
            "parameters": {
                "type": "object",
                "properties": {
    "operation": {
        "type": "string",
        "description": "操作符"
    },
    "value": {
        "type": "int",
        "description": "数值"
    }
},
                "required": ["operation", "value"]
            }
        },
        {
            "name": "close-heat",
            "description": "停⽌加热",
            "parameters": {
                "type": "object",
                "properties": {
    "operation": {
        "type": "string",
        "description": "操作符"
    },
    "value": {
        "type": "int",
        "description": "数值"
    }
},
                "required": ["operation", "value"]
            }
        },
        {
            "name": "start_clean",
            "description": "开启超声清洗",
            "parameters": {
                "type": "object",
                "properties": {
    "value": {
        "type": "int",
        "description": "清洗时间（单位：秒）"
    },
    "operation": {
        "type": "string",
        "description": "操作"
    }
},
                "required": ["value", "operation"]
            }
        }
                    ]
                }
            }
        }
    }
    print(json.dumps(adv_message, ensure_ascii=False), flush=True)
    print(f"--- [ultrasonic_cleaning_Server] 超声清洗 is ready. ---", file=sys.stderr, flush=True)


if __name__ == "__main__":
    # 启动流程：先广播能力，再进入主循环
    ultrasonic_cleaning_server_advertise_capabilities()
    ultrasonic_cleaning_server_main_loop()
