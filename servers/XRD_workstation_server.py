import sys
import json
# 动态导入当前设备对应的工具类（与主服务器文件同目录）
from XRD_workstation_server_tools import ActionServerTools


# 创建全局工具管理器实例
tool_manager = ActionServerTools()


# --- 定义设备动作函数（自动生成，与工具类方法对应）---
def tool_setMod(**params):
    return tool_manager.tool_setMod(**params)


def tool_setSampleName(**params):
    return tool_manager.tool_setSampleName(**params)


def tool_setSampleId(**params):
    return tool_manager.tool_setSampleId(**params)


def tool_setStartAngleAndEndAngle(**params):
    return tool_manager.tool_setStartAngleAndEndAngle(**params)


def tool_setHighPressure(**params):
    return tool_manager.tool_setHighPressure(**params)


def tool_setMeasureSpeedAndStepWidth(**params):
    return tool_manager.tool_setMeasureSpeedAndStepWidth(**params)


def tool_startMeasurement(**params):
    return tool_manager.tool_startMeasurement(**params)


def tool_stopMeasurement(**params):
    return tool_manager.tool_stopMeasurement(**params)


def tool_closeDooropenDoor(**params):
    return tool_manager.tool_closeDooropenDoor(**params)


def tool_openDoor(**params):
    return tool_manager.tool_openDoor(**params)


def tool_getFileInputStream(**params):
    return tool_manager.tool_getFileInputStream(**params)



AVAILABLE_TOOLS_ACTION = {
    "setMod": tool_setMod,
    "setSampleName": tool_setSampleName,
    "setSampleId": tool_setSampleId,
    "setStartAngleAndEndAngle": tool_setStartAngleAndEndAngle,
    "setHighPressure": tool_setHighPressure,
    "setMeasureSpeedAndStepWidth": tool_setMeasureSpeedAndStepWidth,
    "startMeasurement": tool_startMeasurement,
    "stopMeasurement": tool_stopMeasurement,
    "closeDooropenDoor": tool_closeDooropenDoor,
    "openDoor": tool_openDoor,
    "getFileInputStream": tool_getFileInputStream
}


# --- MCP协议通信主逻辑（自动适配当前设备）---
def XRD_workstation_server_main_loop():
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
            print(f"--- [XRD_workstation_Server] Critical Error: {str(e)} ---", file=sys.stderr, flush=True)


def XRD_workstation_server_advertise_capabilities():
    """广播当前设备的MCP能力（设备信息、支持的动作）"""
    adv_message = {
        "jsonrpc": "2.0",
        "method": "protocol/advertise",
        "params": {
            "type": "server",
            "server": {
                "protocolVersion": "0.1.0",
                "displayName": "XRD工作站(ALD平台)",
                "capabilities": {
                    "tools": [
        {
            "name": "setMod",
            "description": "切换控制模式",
            "parameters": {
                "type": "object",
                "properties": {
    "chainName": {
        "type": "string",
        "description": "chainName"
    },
    "ifAsynchronous": {
        "type": "boolean",
        "description": "ifAsynchronous"
    },
    "sn": {
        "type": "string",
        "description": "sn"
    },
    "method": {
        "type": "string",
        "description": "method"
    },
    "mod": {
        "type": "string",
        "description": "mod"
    }
},
                "required": ["chainName", "ifAsynchronous", "sn", "method", "mod"]
            }
        },
        {
            "name": "setSampleName",
            "description": "设置样品名称",
            "parameters": {
                "type": "object",
                "properties": {
    "chainName": {
        "type": "string",
        "description": "chainName"
    },
    "ifAsynchronous": {
        "type": "boolean",
        "description": "ifAsynchronous"
    },
    "sn": {
        "type": "string",
        "description": "sn"
    },
    "method": {
        "type": "string",
        "description": "method"
    },
    "name": {
        "type": "string",
        "description": "name"
    }
},
                "required": ["chainName", "ifAsynchronous", "sn", "method", "name"]
            }
        },
        {
            "name": "setSampleId",
            "description": "设置样品编号",
            "parameters": {
                "type": "object",
                "properties": {
    "chainName": {
        "type": "string",
        "description": "chainName"
    },
    "ifAsynchronous": {
        "type": "boolean",
        "description": "ifAsynchronous"
    },
    "sn": {
        "type": "string",
        "description": "sn"
    },
    "method": {
        "type": "string",
        "description": "method"
    },
    "id": {
        "type": "string",
        "description": "id"
    }
},
                "required": ["chainName", "ifAsynchronous", "sn", "method", "id"]
            }
        },
        {
            "name": "setStartAngleAndEndAngle",
            "description": "设置起始角和终止角",
            "parameters": {
                "type": "object",
                "properties": {
    "chainName": {
        "type": "string",
        "description": "chainName"
    },
    "ifAsynchronous": {
        "type": "boolean",
        "description": "ifAsynchronous"
    },
    "sn": {
        "type": "string",
        "description": "sn"
    },
    "method": {
        "type": "string",
        "description": "method"
    },
    "startAngle": {
        "type": "float",
        "description": "startAngle"
    },
    "endAngle": {
        "type": "float",
        "description": "endAngle"
    }
},
                "required": ["chainName", "ifAsynchronous", "sn", "method", "startAngle", "endAngle"]
            }
        },
        {
            "name": "setHighPressure",
            "description": "设置管电压和管电流值",
            "parameters": {
                "type": "object",
                "properties": {
    "chainName": {
        "type": "string",
        "description": "chainName"
    },
    "ifAsynchronous": {
        "type": "boolean",
        "description": "ifAsynchronous"
    },
    "sn": {
        "type": "string",
        "description": "sn"
    },
    "method": {
        "type": "string",
        "description": "method"
    },
    "voltage": {
        "type": "int",
        "description": "voltage"
    },
    "electricity": {
        "type": "int",
        "description": "electricity"
    }
},
                "required": ["chainName", "ifAsynchronous", "sn", "method", "voltage", "electricity"]
            }
        },
        {
            "name": "setMeasureSpeedAndStepWidth",
            "description": "设置  测量速度和步宽角度",
            "parameters": {
                "type": "object",
                "properties": {
    "chainName": {
        "type": "string",
        "description": "chainName"
    },
    "ifAsynchronous": {
        "type": "boolean",
        "description": "ifAsynchronous"
    },
    "sn": {
        "type": "string",
        "description": "sn"
    },
    "method": {
        "type": "string",
        "description": "method"
    },
    "measureSpeed": {
        "type": "float",
        "description": "measureSpeed"
    },
    "stepWidth": {
        "type": "float",
        "description": "stepWidth"
    }
},
                "required": ["chainName", "ifAsynchronous", "sn", "method", "measureSpeed", "stepWidth"]
            }
        },
        {
            "name": "startMeasurement",
            "description": "控制开始测量",
            "parameters": {
                "type": "object",
                "properties": {
    "chainName": {
        "type": "string",
        "description": "chainName"
    },
    "ifAsynchronous": {
        "type": "boolean",
        "description": "ifAsynchronous"
    },
    "sn": {
        "type": "string",
        "description": "sn"
    },
    "method": {
        "type": "string",
        "description": "method"
    }
},
                "required": ["chainName", "ifAsynchronous", "sn", "method"]
            }
        },
        {
            "name": "stopMeasurement",
            "description": "控制停止测量",
            "parameters": {
                "type": "object",
                "properties": {
    "chainName": {
        "type": "string",
        "description": "chainName"
    },
    "ifAsynchronous": {
        "type": "boolean",
        "description": "ifAsynchronous"
    },
    "sn": {
        "type": "string",
        "description": "sn"
    },
    "method": {
        "type": "string",
        "description": "method"
    }
},
                "required": ["chainName", "ifAsynchronous", "sn", "method"]
            }
        },
        {
            "name": "closeDooropenDoor",
            "description": "控制关门",
            "parameters": {
                "type": "object",
                "properties": {
    "chainName": {
        "type": "string",
        "description": "chainName"
    },
    "ifAsynchronous": {
        "type": "boolean",
        "description": "ifAsynchronous"
    },
    "sn": {
        "type": "string",
        "description": "sn"
    },
    "method": {
        "type": "string",
        "description": "method"
    }
},
                "required": ["chainName", "ifAsynchronous", "sn", "method"]
            }
        },
        {
            "name": "openDoor",
            "description": "控制门移动位置  开门",
            "parameters": {
                "type": "object",
                "properties": {
    "chainName": {
        "type": "string",
        "description": "chainName"
    },
    "ifAsynchronous": {
        "type": "boolean",
        "description": "ifAsynchronous"
    },
    "sn": {
        "type": "string",
        "description": "sn"
    },
    "method": {
        "type": "string",
        "description": "method"
    },
    "distance": {
        "type": "float",
        "description": "distance"
    }
},
                "required": ["chainName", "ifAsynchronous", "sn", "method", "distance"]
            }
        },
        {
            "name": "getFileInputStream",
            "description": "文件上传",
            "parameters": {
                "type": "object",
                "properties": {
    "chainName": {
        "type": "string",
        "description": "chainName"
    },
    "ifAsynchronous": {
        "type": "boolean",
        "description": "ifAsynchronous"
    },
    "sn": {
        "type": "string",
        "description": "sn"
    },
    "method": {
        "type": "string",
        "description": "method"
    },
    "paramCode": {
        "type": "string",
        "description": "paramCode"
    },
    "resultCode": {
        "type": "file",
        "description": "输出文件参数"
    }
},
                "required": ["chainName", "ifAsynchronous", "sn", "method", "paramCode"]
            }
        }
                    ]
                }
            }
        }
    }
    print(json.dumps(adv_message, ensure_ascii=False), flush=True)
    print(f"--- [XRD_workstation_Server] XRD工作站(ALD平台) is ready. ---", file=sys.stderr, flush=True)


if __name__ == "__main__":
    # 启动流程：先广播能力，再进入主循环
    XRD_workstation_server_advertise_capabilities()
    XRD_workstation_server_main_loop()
