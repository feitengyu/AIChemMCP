import sys
import json
# 动态导入当前设备对应的工具类（与主服务器文件同目录）
from tools.PlantSeedlingEquipmentWorkstation_server_tools import ActionServerTools


# 创建全局工具管理器实例
tool_manager = ActionServerTools()


# --- 定义设备动作函数（自动生成，与工具类方法对应）---
def tool_initialize(**params):
    return tool_manager.tool_initialize(**params)


def tool_opendoor(**params):
    return tool_manager.tool_opendoor(**params)


def tool_rotate(**params):
    return tool_manager.tool_rotate(**params)


def tool_closedoor(**params):
    return tool_manager.tool_closedoor(**params)


def tool_light(**params):
    return tool_manager.tool_light(**params)


def tool_setincubator(**params):
    return tool_manager.tool_setincubator(**params)


def tool_starttask(**params):
    return tool_manager.tool_starttask(**params)


def tool_stoptask(**params):
    return tool_manager.tool_stoptask(**params)



AVAILABLE_TOOLS_ACTION = {
    "initialize": tool_initialize,
    "opendoor": tool_opendoor,
    "rotate": tool_rotate,
    "closedoor": tool_closedoor,
    "light": tool_light,
    "setincubator": tool_setincubator,
    "starttask": tool_starttask,
    "stoptask": tool_stoptask
}


# --- MCP协议通信主逻辑（自动适配当前设备）---
def PlantSeedlingEquipmentWorkstation_server_main_loop():
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
            print(f"--- [PlantSeedlingEquipmentWorkstation_Server] Critical Error: {str(e)} ---", file=sys.stderr, flush=True)


def PlantSeedlingEquipmentWorkstation_server_advertise_capabilities():
    """广播当前设备的MCP能力（设备信息、支持的动作）"""
    adv_message = {
        "jsonrpc": "2.0",
        "method": "protocol/advertise",
        "params": {
            "type": "server",
            "server": {
                "protocolVersion": "0.1.0",
                "displayName": "植物幼苗设备工作站",
                "capabilities": {
                    "tools": [
        {
            "name": "initialize",
            "description": "初始化",
            "parameters": {
                "type": "object",
                "properties": {
    "command": {
        "type": "string",
        "description": "命令"
    },
    "Template": {
        "type": "string",
        "description": "模版名称"
    }
},
                "required": ["command", "Template"]
            }
        },
        {
            "name": "opendoor",
            "description": "开门",
            "parameters": {
                "type": "object",
                "properties": {
    "command": {
        "type": "string",
        "description": "命令"
    }
},
                "required": ["command"]
            }
        },
        {
            "name": "rotate",
            "description": "旋转到指定位置",
            "parameters": {
                "type": "object",
                "properties": {
    "command": {
        "type": "string",
        "description": "命令"
    },
    "Position": {
        "type": "int",
        "description": "位置"
    }
},
                "required": ["command", "Position"]
            }
        },
        {
            "name": "closedoor",
            "description": "关门",
            "parameters": {
                "type": "object",
                "properties": {
    "command": {
        "type": "string",
        "description": "命令"
    }
},
                "required": ["command"]
            }
        },
        {
            "name": "light",
            "description": "是否开启培养光源",
            "parameters": {
                "type": "object",
                "properties": {
    "command": {
        "type": "string",
        "description": "命令"
    },
    "status": {
        "type": "int",
        "description": "是否开启",
        "enum": [
            {
                "label": "是",
                "value": "1"
            },
            {
                "label": "否",
                "value": "0"
            }
        ]
    },
    "Intensity": {
        "type": "int",
        "description": "光源强度"
    }
},
                "required": ["command", "status", "Intensity"]
            }
        },
        {
            "name": "setincubator",
            "description": "设置温湿度",
            "parameters": {
                "type": "object",
                "properties": {
    "command": {
        "type": "string",
        "description": "命令"
    },
    "Temperature": {
        "type": "float",
        "description": "温度"
    },
    "Humidity": {
        "type": "float",
        "description": "湿度"
    }
},
                "required": ["command", "Temperature", "Humidity"]
            }
        },
        {
            "name": "starttask",
            "description": "开始拍摄",
            "parameters": {
                "type": "object",
                "properties": {
    "command": {
        "type": "string",
        "description": "命令"
    },
    "resultCode": {
        "type": "file",
        "description": "输出结果参数"
    }
},
                "required": ["command"]
            }
        },
        {
            "name": "stoptask",
            "description": "停止拍摄",
            "parameters": {
                "type": "object",
                "properties": {
    "command": {
        "type": "string",
        "description": "命令"
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
    print(f"--- [PlantSeedlingEquipmentWorkstation_Server] 植物幼苗设备工作站 is ready. ---", file=sys.stderr, flush=True)


if __name__ == "__main__":
    # 启动流程：先广播能力，再进入主循环
    PlantSeedlingEquipmentWorkstation_server_advertise_capabilities()
    PlantSeedlingEquipmentWorkstation_server_main_loop()
