import sys
import json
# 动态导入当前设备对应的工具类（与主服务器文件同目录）
from tools.Chlorophyll_Fluorescence_Workstation_server_tools import ActionServerTools


# 创建全局工具管理器实例
tool_manager = ActionServerTools()


# --- 定义设备动作函数（自动生成，与工具类方法对应）---
def tool_init(**params):
    return tool_manager.tool_init(**params)


def tool_door_open(**params):
    return tool_manager.tool_door_open(**params)


def tool_platform_down(**params):
    return tool_manager.tool_platform_down(**params)


def tool_door_close(**params):
    return tool_manager.tool_door_close(**params)


def tool_quick_light_curve(**params):
    return tool_manager.tool_quick_light_curve(**params)


def tool_slow_kinetics(**params):
    return tool_manager.tool_slow_kinetics(**params)


def tool_check_status(**params):
    return tool_manager.tool_check_status(**params)


def tool_platform_up(**params):
    return tool_manager.tool_platform_up(**params)



AVAILABLE_TOOLS_ACTION = {
    "init": tool_init,
    "door_open": tool_door_open,
    "platform_down": tool_platform_down,
    "door_close": tool_door_close,
    "quick_light_curve": tool_quick_light_curve,
    "slow_kinetics": tool_slow_kinetics,
    "check_status": tool_check_status,
    "platform_up": tool_platform_up
}


# --- MCP协议通信主逻辑（自动适配当前设备）---
def Chlorophyll_Fluorescence_Workstation_server_main_loop():
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
            print(f"--- [Chlorophyll_Fluorescence_Workstation_Server] Critical Error: {str(e)} ---", file=sys.stderr, flush=True)


def Chlorophyll_Fluorescence_Workstation_server_advertise_capabilities():
    """广播当前设备的MCP能力（设备信息、支持的动作）"""
    adv_message = {
        "jsonrpc": "2.0",
        "method": "protocol/advertise",
        "params": {
            "type": "server",
            "server": {
                "protocolVersion": "0.1.0",
                "displayName": "叶绿素荧光成像工作站",
                "capabilities": {
                    "tools": [
        {
            "name": "init",
            "description": "初始化设备",
            "parameters": {
                "type": "object",
                "properties": {
    "command": {
        "type": "string",
        "description": "指令"
    }
},
                "required": ["command"]
            }
        },
        {
            "name": "door_open",
            "description": "打开测量门",
            "parameters": {
                "type": "object",
                "properties": {
    "command": {
        "type": "string",
        "description": "指令"
    }
},
                "required": ["command"]
            }
        },
        {
            "name": "platform_down",
            "description": "降低检测台",
            "parameters": {
                "type": "object",
                "properties": {
    "command": {
        "type": "string",
        "description": "指令"
    }
},
                "required": ["command"]
            }
        },
        {
            "name": "door_close",
            "description": "关闭测量门",
            "parameters": {
                "type": "object",
                "properties": {
    "command": {
        "type": "string",
        "description": "指令"
    }
},
                "required": ["command"]
            }
        },
        {
            "name": "quick_light_curve",
            "description": "快速光曲线",
            "parameters": {
                "type": "object",
                "properties": {
    "command": {
        "type": "string",
        "description": "指令"
    },
    "time": {
        "type": "int",
        "description": "光照持续时间（秒）"
    },
    "intensities": {
        "type": "array",
        "description": "光强档位",
        "properties": {
            "level": {
                "type": "string",
                "description": "光强档位"
            }
        },
        "required": [
            "level"
        ]
    },
    "intensities.level": {
        "type": "string",
        "description": "光强档位"
    },
    "resultCode": {
        "type": "file",
        "description": "输出参数编码"
    }
},
                "required": ["command", "time", "intensities", "intensities.level"]
            }
        },
        {
            "name": "slow_kinetics",
            "description": "慢动力学曲线",
            "parameters": {
                "type": "object",
                "properties": {
    "command": {
        "type": "string",
        "description": "指令"
    },
    "under_light": {
        "type": "array",
        "description": "光照下的时间（秒）",
        "properties": {
            "light": {
                "type": "int",
                "description": "光照下的时间（秒）"
            }
        },
        "required": [
            "light"
        ]
    },
    "under_light.light": {
        "type": "int",
        "description": "光照下的时间（秒）"
    },
    "under_dark": {
        "type": "array",
        "description": "暗环境下的时间（秒）",
        "properties": {
            "dark": {
                "type": "int",
                "description": "暗环境下的时间（秒）"
            }
        },
        "required": [
            "dark"
        ]
    },
    "under_dark.dark": {
        "type": "int",
        "description": "暗环境下的时间（秒）"
    },
    "intensities": {
        "type": "array",
        "description": "光强档位",
        "properties": {
            "level": {
                "type": "string",
                "description": "光强档位"
            }
        },
        "required": [
            "level"
        ]
    },
    "intensities.level": {
        "type": "string",
        "description": "光强档位"
    },
    "resultCode": {
        "type": "file",
        "description": "输出参数编码"
    }
},
                "required": ["command", "under_light", "under_light.light", "under_dark", "under_dark.dark", "intensities.level"]
            }
        },
        {
            "name": "check_status",
            "description": "指令状态查询",
            "parameters": {
                "type": "object",
                "properties": {
    "command": {
        "type": "string",
        "description": "指令"
    },
    "operation": {
        "type": "string",
        "description": "操作指令的名字",
        "properties": {
            "light": {
                "type": "int",
                "description": "光照下的时间（秒）"
            }
        },
        "required": [
            "light"
        ]
    },
    "operation.light": {
        "type": "int",
        "description": "光照下的时间（秒）"
    }
},
                "required": ["command", "operation", "operation.light"]
            }
        },
        {
            "name": "platform_up",
            "description": "上升检测台",
            "parameters": {
                "type": "object",
                "properties": {
    "command": {
        "type": "string",
        "description": "指令"
    }
},
                "required": ["command"]
            }
        }
                    ]
                }
            }
        }
    }
    print(json.dumps(adv_message, ensure_ascii=False), flush=True)
    print(f"--- [Chlorophyll_Fluorescence_Workstation_Server] 叶绿素荧光成像工作站 is ready. ---", file=sys.stderr, flush=True)


if __name__ == "__main__":
    # 启动流程：先广播能力，再进入主循环
    Chlorophyll_Fluorescence_Workstation_server_advertise_capabilities()
    Chlorophyll_Fluorescence_Workstation_server_main_loop()
