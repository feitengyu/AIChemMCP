import sys
import json
# 动态导入当前设备对应的工具类（与主服务器文件同目录）
from tools.spotting_workstation_server_tools import ActionServerTools


# 创建全局工具管理器实例
tool_manager = ActionServerTools()


# --- 定义设备动作函数（自动生成，与工具类方法对应）---
def tool_opendoor(**params):
    return tool_manager.tool_opendoor(**params)


def tool_closedoor(**params):
    return tool_manager.tool_closedoor(**params)


def tool_start(**params):
    return tool_manager.tool_start(**params)


def tool_SlideLock(**params):
    return tool_manager.tool_SlideLock(**params)


def tool_SlideUnLock(**params):
    return tool_manager.tool_SlideUnLock(**params)



AVAILABLE_TOOLS_ACTION = {
    "opendoor": tool_opendoor,
    "closedoor": tool_closedoor,
    "start": tool_start,
    "SlideLock": tool_SlideLock,
    "SlideUnLock": tool_SlideUnLock
}


# --- MCP协议通信主逻辑（自动适配当前设备）---
def spotting_workstation_server_main_loop():
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
            print(f"--- [spotting_workstation_Server] Critical Error: {str(e)} ---", file=sys.stderr, flush=True)


def spotting_workstation_server_advertise_capabilities():
    """广播当前设备的MCP能力（设备信息、支持的动作）"""
    adv_message = {
        "jsonrpc": "2.0",
        "method": "protocol/advertise",
        "params": {
            "type": "server",
            "server": {
                "protocolVersion": "0.1.0",
                "displayName": "电化学-点样仪",
                "capabilities": {
                    "tools": [
        {
            "name": "opendoor",
            "description": "开门",
            "parameters": {
                "type": "object",
                "properties": {
    "type": {
        "type": "string",
        "description": "仪器类型"
    },
    "cmd": {
        "type": "string",
        "description": "指令名称"
    },
    "Name": {
        "type": "string",
        "description": "脚本名称"
    }
},
                "required": ["type", "cmd", "Name"]
            }
        },
        {
            "name": "closedoor",
            "description": "关门",
            "parameters": {
                "type": "object",
                "properties": {
    "type": {
        "type": "string",
        "description": "仪器类型"
    },
    "cmd": {
        "type": "string",
        "description": "指令名称"
    },
    "Name": {
        "type": "string",
        "description": "脚本名称"
    }
},
                "required": ["type", "cmd", "Name"]
            }
        },
        {
            "name": "start",
            "description": "点样实验",
            "parameters": {
                "type": "object",
                "properties": {
    "type": {
        "type": "string",
        "description": "仪器类型"
    },
    "cmd": {
        "type": "string",
        "description": "指令名称"
    },
    "Name": {
        "type": "string",
        "description": "脚本名称"
    },
    "definitionParamUrl": {
        "type": "file",
        "description": "配置文件路径"
    }
},
                "required": ["type", "cmd", "Name", "definitionParamUrl"]
            }
        },
        {
            "name": "SlideLock",
            "description": "启动真空泵",
            "parameters": {
                "type": "object",
                "properties": {
    "type": {
        "type": "string",
        "description": "仪器类型"
    },
    "cmd": {
        "type": "string",
        "description": "指令名称"
    },
    "Name": {
        "type": "string",
        "description": "脚本名称"
    }
},
                "required": ["type", "cmd", "Name"]
            }
        },
        {
            "name": "SlideUnLock",
            "description": "关闭真空泵",
            "parameters": {
                "type": "object",
                "properties": {
    "type": {
        "type": "string",
        "description": "仪器类型"
    },
    "cmd": {
        "type": "string",
        "description": "指令名称"
    },
    "Name": {
        "type": "string",
        "description": "脚本名称"
    }
},
                "required": ["type", "cmd", "Name"]
            }
        }
                    ]
                }
            }
        }
    }
    print(json.dumps(adv_message, ensure_ascii=False), flush=True)
    print(f"--- [spotting_workstation_Server] 电化学-点样仪 is ready. ---", file=sys.stderr, flush=True)


if __name__ == "__main__":
    # 启动流程：先广播能力，再进入主循环
    spotting_workstation_server_advertise_capabilities()
    spotting_workstation_server_main_loop()
