import sys
import json
# 动态导入当前设备对应的工具类（与主服务器文件同目录）
from tools.ALDWorkstation_server_tools import ActionServerTools


# 创建全局工具管理器实例
tool_manager = ActionServerTools()


# --- 定义设备动作函数（自动生成，与工具类方法对应）---
def tool_obtainSoftwareVersion(**params):
    return tool_manager.tool_obtainSoftwareVersion(**params)


def tool_getSystemStatus(**params):
    return tool_manager.tool_getSystemStatus(**params)


def tool_RecipeStart(**params):
    return tool_manager.tool_RecipeStart(**params)


def tool_heatingControlOfTubeFurnace(**params):
    return tool_manager.tool_heatingControlOfTubeFurnace(**params)


def tool_setTemperatureTubeFurnace(**params):
    return tool_manager.tool_setTemperatureTubeFurnace(**params)


def tool_getFurnaceTemperature(**params):
    return tool_manager.tool_getFurnaceTemperature(**params)


def tool_setChannelTemperature(**params):
    return tool_manager.tool_setChannelTemperature(**params)


def tool_getChannelTemperature(**params):
    return tool_manager.tool_getChannelTemperature(**params)


def tool_setChannelEnable(**params):
    return tool_manager.tool_setChannelEnable(**params)


def tool_getChannelPower(**params):
    return tool_manager.tool_getChannelPower(**params)


def tool_setValveEnable(**params):
    return tool_manager.tool_setValveEnable(**params)


def tool_setValvePulseTime(**params):
    return tool_manager.tool_setValvePulseTime(**params)


def tool_triggerValvePulse(**params):
    return tool_manager.tool_triggerValvePulse(**params)


def tool_setMfcFlow(**params):
    return tool_manager.tool_setMfcFlow(**params)


def tool_getMfcActualFlow(**params):
    return tool_manager.tool_getMfcActualFlow(**params)


def tool_setMfcFlowZeroPointCalibration(**params):
    return tool_manager.tool_setMfcFlowZeroPointCalibration(**params)


def tool_getVacuumPressure(**params):
    return tool_manager.tool_getVacuumPressure(**params)


def tool_getAlarmStatus(**params):
    return tool_manager.tool_getAlarmStatus(**params)


def tool_transmitterPower(**params):
    return tool_manager.tool_transmitterPower(**params)


def tool_ozoneGeneratorEnable(**params):
    return tool_manager.tool_ozoneGeneratorEnable(**params)


def tool_getList(**params):
    return tool_manager.tool_getList(**params)


def tool_loadRecipe(**params):
    return tool_manager.tool_loadRecipe(**params)


def tool_writeVent(**params):
    return tool_manager.tool_writeVent(**params)


def tool_writeEnableOzoneSwitch(**params):
    return tool_manager.tool_writeEnableOzoneSwitch(**params)


def tool_loadRecipeStart(**params):
    return tool_manager.tool_loadRecipeStart(**params)


def tool_closeDoorAld(**params):
    return tool_manager.tool_closeDoorAld(**params)


def tool_openDoorAld(**params):
    return tool_manager.tool_openDoorAld(**params)


def tool_downloadFile(**params):
    return tool_manager.tool_downloadFile(**params)



AVAILABLE_TOOLS_ACTION = {
    "obtainSoftwareVersion": tool_obtainSoftwareVersion,
    "getSystemStatus": tool_getSystemStatus,
    "RecipeStart": tool_RecipeStart,
    "heatingControlOfTubeFurnace": tool_heatingControlOfTubeFurnace,
    "setTemperatureTubeFurnace": tool_setTemperatureTubeFurnace,
    "getFurnaceTemperature": tool_getFurnaceTemperature,
    "setChannelTemperature": tool_setChannelTemperature,
    "getChannelTemperature": tool_getChannelTemperature,
    "setChannelEnable": tool_setChannelEnable,
    "getChannelPower": tool_getChannelPower,
    "setValveEnable": tool_setValveEnable,
    "setValvePulseTime": tool_setValvePulseTime,
    "triggerValvePulse": tool_triggerValvePulse,
    "setMfcFlow": tool_setMfcFlow,
    "getMfcActualFlow": tool_getMfcActualFlow,
    "setMfcFlowZeroPointCalibration": tool_setMfcFlowZeroPointCalibration,
    "getVacuumPressure": tool_getVacuumPressure,
    "getAlarmStatus": tool_getAlarmStatus,
    "transmitterPower": tool_transmitterPower,
    "ozoneGeneratorEnable": tool_ozoneGeneratorEnable,
    "getList": tool_getList,
    "loadRecipe": tool_loadRecipe,
    "writeVent": tool_writeVent,
    "writeEnableOzoneSwitch": tool_writeEnableOzoneSwitch,
    "loadRecipeStart": tool_loadRecipeStart,
    "closeDoorAld": tool_closeDoorAld,
    "openDoorAld": tool_openDoorAld,
    "downloadFile": tool_downloadFile
}


# --- MCP协议通信主逻辑（自动适配当前设备）---
def ALDWorkstation_server_main_loop():
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
            print(f"--- [ALDWorkstation_Server] Critical Error: {str(e)} ---", file=sys.stderr, flush=True)


def ALDWorkstation_server_advertise_capabilities():
    """广播当前设备的MCP能力（设备信息、支持的动作）"""
    adv_message = {
        "jsonrpc": "2.0",
        "method": "protocol/advertise",
        "params": {
            "type": "server",
            "server": {
                "protocolVersion": "0.1.0",
                "displayName": "ALD工作站",
                "capabilities": {
                    "tools": [
        {
            "name": "obtainSoftwareVersion",
            "description": "获取软件版本",
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
            "name": "getSystemStatus",
            "description": "获取ALD系统状态",
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
            "name": "RecipeStart",
            "description": "RecipeStart使能",
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
    "enable": {
        "type": "boolean",
        "description": "enable"
    }
},
                "required": ["chainName", "ifAsynchronous", "sn", "method", "enable"]
            }
        },
        {
            "name": "heatingControlOfTubeFurnace",
            "description": "管式炉加热控制",
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
    "status": {
        "type": "boolean",
        "description": "status"
    }
},
                "required": ["chainName", "ifAsynchronous", "sn", "method", "status"]
            }
        },
        {
            "name": "setTemperatureTubeFurnace",
            "description": "设置管式炉温度",
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
    "celsius": {
        "type": "float",
        "description": "celsius"
    }
},
                "required": ["chainName", "ifAsynchronous", "sn", "method", "celsius"]
            }
        },
        {
            "name": "getFurnaceTemperature",
            "description": "读取管式炉温度",
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
            "name": "setChannelTemperature",
            "description": "设置T1到T48的温度",
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
    "channel": {
        "type": "int",
        "description": "通道管式炉T1-T48"
    },
    "celsius": {
        "type": "float",
        "description": "温度"
    }
},
                "required": ["chainName", "ifAsynchronous", "sn", "method", "channel", "celsius"]
            }
        },
        {
            "name": "getChannelTemperature",
            "description": "读取T1到T48的温度设置",
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
            "name": "setChannelEnable",
            "description": "T1~T48使能",
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
    "channel": {
        "type": "int",
        "description": "通道T1-T48"
    },
    "enable": {
        "type": "boolean",
        "description": "使能"
    }
},
                "required": ["chainName", "ifAsynchronous", "sn", "method", "channel", "enable"]
            }
        },
        {
            "name": "getChannelPower",
            "description": "获取T1到T48的使能",
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
    "channel": {
        "type": "int",
        "description": "通道T1-T48"
    }
},
                "required": ["chainName", "ifAsynchronous", "sn", "method", "channel"]
            }
        },
        {
            "name": "setValveEnable",
            "description": "ALD阀1到阀24使能",
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
    "valve": {
        "type": "int",
        "description": "ALD阀几"
    },
    "enable": {
        "type": "boolean",
        "description": "开启或者是关闭"
    }
},
                "required": ["chainName", "ifAsynchronous", "sn", "method", "valve", "enable"]
            }
        },
        {
            "name": "setValvePulseTime",
            "description": "ALD阀1~阀24脉冲宽度(时间)",
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
    "valve": {
        "type": "int",
        "description": "ALD阀几"
    },
    "milliseconds": {
        "type": "int",
        "description": "设置的脉冲时间 毫秒"
    }
},
                "required": ["chainName", "ifAsynchronous", "sn", "method", "valve", "milliseconds"]
            }
        },
        {
            "name": "triggerValvePulse",
            "description": "ALD阀1~阀24脉冲使能",
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
    "valve": {
        "type": "int",
        "description": "ALD阀几"
    }
},
                "required": ["chainName", "ifAsynchronous", "sn", "method", "valve"]
            }
        },
        {
            "name": "setMfcFlow",
            "description": "设置流量计MFC1~MFC8的流量",
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
    "mfc": {
        "type": "int",
        "description": "MFC几"
    },
    "sccm": {
        "type": "int",
        "description": "设置的流量"
    }
},
                "required": ["chainName", "ifAsynchronous", "sn", "method", "mfc", "sccm"]
            }
        },
        {
            "name": "getMfcActualFlow",
            "description": "读取流量计MFC1~MFC8的实际流量",
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
    "mfc": {
        "type": "int",
        "description": "MFC几"
    }
},
                "required": ["chainName", "ifAsynchronous", "sn", "method", "mfc"]
            }
        },
        {
            "name": "setMfcFlowZeroPointCalibration",
            "description": "流量计MFC1~MFC8零点校准  enable false时设置流量无效,true时设置流量有效",
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
    "mfc": {
        "type": "int",
        "description": "mfc"
    },
    "enable": {
        "type": "boolean",
        "description": "设置流量是否有效"
    }
},
                "required": ["chainName", "ifAsynchronous", "sn", "method", "mfc", "enable"]
            }
        },
        {
            "name": "getVacuumPressure",
            "description": "获取真空压力",
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
            "name": "getAlarmStatus",
            "description": "获取告警状态",
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
            "name": "transmitterPower",
            "description": "设置臭氧发生器功率",
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
    "power": {
        "type": "int",
        "description": "power"
    }
},
                "required": ["chainName", "ifAsynchronous", "sn", "method", "power"]
            }
        },
        {
            "name": "ozoneGeneratorEnable",
            "description": "设置臭氧发生器使能",
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
    "enable": {
        "type": "boolean",
        "description": "enable"
    }
},
                "required": ["chainName", "ifAsynchronous", "sn", "method", "enable"]
            }
        },
        {
            "name": "getList",
            "description": "读取所有Recipe名称列表",
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
            "name": "loadRecipe",
            "description": "加载指定Recipe",
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
    "recipeName": {
        "type": "string",
        "description": "recipeName"
    }
},
                "required": ["chainName", "ifAsynchronous", "sn", "method"]
            }
        },
        {
            "name": "writeVent",
            "description": "Vent",
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
    "minute": {
        "type": "int",
        "description": "minute"
    }
},
                "required": ["chainName", "ifAsynchronous", "sn", "method", "minute"]
            }
        },
        {
            "name": "writeEnableOzoneSwitch",
            "description": "设置臭氧发生器电源通断",
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
    "enable": {
        "type": "boolean",
        "description": "enable"
    }
},
                "required": ["chainName", "ifAsynchronous", "sn", "method", "enable"]
            }
        },
        {
            "name": "loadRecipeStart",
            "description": "总体的加载recipe使能 并运行使能",
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
    "recipeName": {
        "type": "string",
        "description": "recipeName"
    },
    "minute": {
        "type": "int",
        "description": "minute"
    }
},
                "required": ["chainName", "ifAsynchronous", "sn", "method", "recipeName", "minute"]
            }
        },
        {
            "name": "closeDoorAld",
            "description": "ALD设备关闭舱门的recipe使能",
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
    "recipeName": {
        "type": "string",
        "description": "recipeName"
    }
},
                "required": ["chainName", "ifAsynchronous", "sn", "method", "recipeName"]
            }
        },
        {
            "name": "openDoorAld",
            "description": "ALD设备 调用开启舱门的recipe使能",
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
    "recipeName": {
        "type": "string",
        "description": "recipeName"
    }
},
                "required": ["chainName", "ifAsynchronous", "sn", "method", "recipeName"]
            }
        },
        {
            "name": "downloadFile",
            "description": "从平台接收脚本文件下载到本地",
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
    "fileUrl": {
        "type": "file",
        "description": "文件地址"
    },
    "fileType": {
        "type": "string",
        "description": "文件类型"
    },
    "savePath": {
        "type": "string",
        "description": "本地保存路径"
    }
},
                "required": ["chainName", "ifAsynchronous", "sn", "method", "fileUrl", "fileType", "savePath"]
            }
        }
                    ]
                }
            }
        }
    }
    print(json.dumps(adv_message, ensure_ascii=False), flush=True)
    print(f"--- [ALDWorkstation_Server] ALD工作站 is ready. ---", file=sys.stderr, flush=True)


if __name__ == "__main__":
    # 启动流程：先广播能力，再进入主循环
    ALDWorkstation_server_advertise_capabilities()
    ALDWorkstation_server_main_loop()
