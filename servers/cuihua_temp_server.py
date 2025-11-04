import sys
import json
# 动态导入当前设备对应的工具类（与主服务器文件同目录）
from tools.cuihua_temp_server_tools import ActionServerTools


# 创建全局工具管理器实例
tool_manager = ActionServerTools()


# --- 定义设备动作函数（自动生成，与工具类方法对应）---
def tool_takePaper1(**params):
    return tool_manager.tool_takePaper1(**params)


def tool_startexperment(**params):
    return tool_manager.tool_startexperment(**params)


def tool_takePaper2(**params):
    return tool_manager.tool_takePaper2(**params)


def tool_robotActivation(**params):
    return tool_manager.tool_robotActivation(**params)


def tool_rawMaterialFinish(**params):
    return tool_manager.tool_rawMaterialFinish(**params)


def tool_takerPaperPosition(**params):
    return tool_manager.tool_takerPaperPosition(**params)


def tool_takeRawMaterials(**params):
    return tool_manager.tool_takeRawMaterials(**params)


def tool_prepareSample(**params):
    return tool_manager.tool_prepareSample(**params)


def tool_contactAngleTakeMaterial(**params):
    return tool_manager.tool_contactAngleTakeMaterial(**params)


def tool_movingSampleA(**params):
    return tool_manager.tool_movingSampleA(**params)


def tool_tensionerMaterialCollection(**params):
    return tool_manager.tool_tensionerMaterialCollection(**params)


def tool_putTurntable(**params):
    return tool_manager.tool_putTurntable(**params)


def tool_removePaperElectrolyticCell(**params):
    return tool_manager.tool_removePaperElectrolyticCell(**params)


def tool_putPaperElectrolyticCell(**params):
    return tool_manager.tool_putPaperElectrolyticCell(**params)


def tool_rotate(**params):
    return tool_manager.tool_rotate(**params)


def tool_peristalticPumpStarted(**params):
    return tool_manager.tool_peristalticPumpStarted(**params)


def tool_electrolyticCellElectricalRotation(**params):
    return tool_manager.tool_electrolyticCellElectricalRotation(**params)


def tool_resetElectrolyticMotorZero(**params):
    return tool_manager.tool_resetElectrolyticMotorZero(**params)


def tool_dischargePumpControlStop(**params):
    return tool_manager.tool_dischargePumpControlStop(**params)


def tool_peristalticPumpStopped(**params):
    return tool_manager.tool_peristalticPumpStopped(**params)


def tool_SwitchingValveControl(**params):
    return tool_manager.tool_SwitchingValveControl(**params)


def tool_dischargePumpControlStart(**params):
    return tool_manager.tool_dischargePumpControlStart(**params)


def tool_probePaperClamping(**params):
    return tool_manager.tool_probePaperClamping(**params)


def tool_releaseProbingPaper(**params):
    return tool_manager.tool_releaseProbingPaper(**params)


def tool_measuringFirstHalf(**params):
    return tool_manager.tool_measuringFirstHalf(**params)


def tool_contactAnglePlatformUp(**params):
    return tool_manager.tool_contactAnglePlatformUp(**params)


def tool_contactAnglePlatformDescent(**params):
    return tool_manager.tool_contactAnglePlatformDescent(**params)


def tool_measuringSecondHalf(**params):
    return tool_manager.tool_measuringSecondHalf(**params)


def tool_getTemplateList(**params):
    return tool_manager.tool_getTemplateList(**params)


def tool_measuringAdhesion2(**params):
    return tool_manager.tool_measuringAdhesion2(**params)



AVAILABLE_TOOLS_ACTION = {
    "takePaper1": tool_takePaper1,
    "startexperment": tool_startexperment,
    "takePaper2": tool_takePaper2,
    "robotActivation": tool_robotActivation,
    "rawMaterialFinish": tool_rawMaterialFinish,
    "takerPaperPosition": tool_takerPaperPosition,
    "takeRawMaterials": tool_takeRawMaterials,
    "prepareSample": tool_prepareSample,
    "contactAngleTakeMaterial": tool_contactAngleTakeMaterial,
    "movingSampleA": tool_movingSampleA,
    "tensionerMaterialCollection": tool_tensionerMaterialCollection,
    "putTurntable": tool_putTurntable,
    "removePaperElectrolyticCell": tool_removePaperElectrolyticCell,
    "putPaperElectrolyticCell": tool_putPaperElectrolyticCell,
    "rotate": tool_rotate,
    "peristalticPumpStarted": tool_peristalticPumpStarted,
    "electrolyticCellElectricalRotation": tool_electrolyticCellElectricalRotation,
    "resetElectrolyticMotorZero": tool_resetElectrolyticMotorZero,
    "dischargePumpControlStop": tool_dischargePumpControlStop,
    "peristalticPumpStopped": tool_peristalticPumpStopped,
    "SwitchingValveControl": tool_SwitchingValveControl,
    "dischargePumpControlStart": tool_dischargePumpControlStart,
    "probePaperClamping": tool_probePaperClamping,
    "releaseProbingPaper": tool_releaseProbingPaper,
    "measuringFirstHalf": tool_measuringFirstHalf,
    "contactAnglePlatformUp": tool_contactAnglePlatformUp,
    "contactAnglePlatformDescent": tool_contactAnglePlatformDescent,
    "measuringSecondHalf": tool_measuringSecondHalf,
    "getTemplateList": tool_getTemplateList,
    "measuringAdhesion2": tool_measuringAdhesion2
}


# --- MCP协议通信主逻辑（自动适配当前设备）---
def cuihua_temp_server_main_loop():
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
            print(f"--- [cuihua_temp_Server] Critical Error: {str(e)} ---", file=sys.stderr, flush=True)


def cuihua_temp_server_advertise_capabilities():
    """广播当前设备的MCP能力（设备信息、支持的动作）"""
    adv_message = {
        "jsonrpc": "2.0",
        "method": "protocol/advertise",
        "params": {
            "type": "server",
            "server": {
                "protocolVersion": "0.1.0",
                "displayName": "催化剂气液微环境工作站",
                "capabilities": {
                    "tools": [
        {
            "name": "takePaper1",
            "description": "从机器臂取碳纸放置",
            "parameters": {
                "type": "object",
                "properties": {
    "num": {
        "type": "int",
        "description": "碳纸编号（默认从1号开始取）"
    },
    "count": {
        "type": "int",
        "description": "一轮实验的总碳纸数量"
    }
},
                "required": ["num", "count"]
            }
        },
        {
            "name": "startexperment",
            "description": "开始实验",
            "parameters": {
                "type": "object",
                "properties": {
    "num": {
        "type": "int",
        "description": "碳纸编号（默认从1号开始取）"
    }
},
                "required": ["num"]
            }
        },
        {
            "name": "takePaper2",
            "description": "放置碳纸到转盘",
            "parameters": {
                "type": "object",
                "properties": {
    "num": {
        "type": "int",
        "description": "放置编号"
    }
},
                "required": ["num"]
            }
        },
        {
            "name": "robotActivation",
            "description": "机械臂启动",
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
    "type": {
        "type": "int",
        "description": "工作站编码类型"
    }
},
                "required": ["chainName", "ifAsynchronous", "sn", "method", "type"]
            }
        },
        {
            "name": "rawMaterialFinish",
            "description": "原料和碳纸夹准备完成",
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
    "type": {
        "type": "int",
        "description": "工作站编码类型"
    }
},
                "required": ["chainName", "ifAsynchronous", "sn", "method"]
            }
        },
        {
            "name": "takerPaperPosition",
            "description": "碳纸坐标",
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
    "index": {
        "type": "int",
        "description": "碳纸坐标"
    },
    "type": {
        "type": "int",
        "description": "工作站编码类型"
    }
},
                "required": ["chainName", "ifAsynchronous", "sn", "method", "index", "type"]
            }
        },
        {
            "name": "takeRawMaterials",
            "description": "取原料和碳纸夹",
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
    "type": {
        "type": "int",
        "description": "工作站编码类型"
    }
},
                "required": ["chainName", "ifAsynchronous", "sn", "method"]
            }
        },
        {
            "name": "prepareSample",
            "description": "准备样品 就是将样品移动到接触角仪",
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
    "type": {
        "type": "string",
        "description": "工作站编码类型"
    }
},
                "required": ["chainName", "ifAsynchronous", "sn", "method", "type"]
            }
        },
        {
            "name": "contactAngleTakeMaterial",
            "description": "接触角请求取料",
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
    "type": {
        "type": "int",
        "description": "工作站编码类型"
    }
},
                "required": ["chainName", "ifAsynchronous", "sn", "method"]
            }
        },
        {
            "name": "movingSampleA",
            "description": "移动样品到张力仪",
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
    "type": {
        "type": "string",
        "description": "工作站类型编码"
    }
},
                "required": ["chainName", "ifAsynchronous", "sn", "method", "type"]
            }
        },
        {
            "name": "tensionerMaterialCollection",
            "description": "机械臂去张力仪取料",
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
    "type": {
        "type": "int",
        "description": "工作站类型编码"
    }
},
                "required": ["chainName", "ifAsynchronous", "sn", "method", "type"]
            }
        },
        {
            "name": "putTurntable",
            "description": "机械臂请求到中转台碳纸放在碳纸转台上",
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
    "type": {
        "type": "int",
        "description": "工作站类型编码"
    }
},
                "required": ["chainName", "ifAsynchronous", "sn", "method", "type"]
            }
        },
        {
            "name": "removePaperElectrolyticCell",
            "description": "电解池碳纸取出",
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
    "type": {
        "type": "int",
        "description": "工作站类型编码"
    }
},
                "required": ["chainName", "ifAsynchronous", "sn", "method", "type"]
            }
        },
        {
            "name": "putPaperElectrolyticCell",
            "description": "机械臂去中转台拿碳纸放入到电解池中",
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
    "type": {
        "type": "int",
        "description": "工作站类型编码"
    }
},
                "required": ["chainName", "ifAsynchronous", "sn", "method", "type"]
            }
        },
        {
            "name": "rotate",
            "description": "中转台旋转根据编号",
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
    "number": {
        "type": "int",
        "description": "转台放置位置编号"
    },
    "type": {
        "type": "int",
        "description": "工作站类型编码"
    }
},
                "required": ["chainName", "ifAsynchronous", "sn", "method", "number", "type"]
            }
        },
        {
            "name": "peristalticPumpStarted",
            "description": "蠕动泵启动",
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
    "type": {
        "type": "int",
        "description": "工作站类型编码"
    }
},
                "required": ["chainName", "ifAsynchronous", "sn", "method", "type"]
            }
        },
        {
            "name": "electrolyticCellElectricalRotation",
            "description": "电解池电机旋转",
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
    "type": {
        "type": "int",
        "description": "工作站类型编码"
    }
},
                "required": ["chainName", "ifAsynchronous", "sn", "method"]
            }
        },
        {
            "name": "resetElectrolyticMotorZero",
            "description": "电解池电机归零",
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
    "type": {
        "type": "int",
        "description": "工作站类型编码"
    }
},
                "required": ["chainName", "ifAsynchronous", "sn", "method", "type"]
            }
        },
        {
            "name": "dischargePumpControlStop",
            "description": "排液泵 关闭",
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
    "type": {
        "type": "int",
        "description": "工作站类型编码"
    }
},
                "required": ["chainName", "ifAsynchronous", "sn", "method", "type"]
            }
        },
        {
            "name": "peristalticPumpStopped",
            "description": "蠕动泵关闭",
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
    "type": {
        "type": "int",
        "description": "工作站类型编码"
    }
},
                "required": ["chainName", "ifAsynchronous", "sn", "method"]
            }
        },
        {
            "name": "SwitchingValveControl",
            "description": "切换阀",
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
    "type": {
        "type": "int",
        "description": "工作站类型编码"
    }
},
                "required": ["chainName", "ifAsynchronous", "sn", "method", "type"]
            }
        },
        {
            "name": "dischargePumpControlStart",
            "description": "排液泵启动",
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
    "type": {
        "type": "int",
        "description": "工作站类型编码"
    }
},
                "required": ["chainName", "ifAsynchronous", "sn", "method"]
            }
        },
        {
            "name": "probePaperClamping",
            "description": "碳纸夹紧",
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
    "type": {
        "type": "int",
        "description": "工作站类型编码"
    }
},
                "required": ["chainName", "ifAsynchronous", "sn", "method", "type"]
            }
        },
        {
            "name": "releaseProbingPaper",
            "description": "碳纸松开",
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
    "type": {
        "type": "int",
        "description": "工作站类型编码"
    }
},
                "required": ["chainName", "ifAsynchronous", "sn", "method", "type"]
            }
        },
        {
            "name": "measuringFirstHalf",
            "description": "接触角仪参数设置",
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
    "metering": {
        "type": "int",
        "description": "液体体积"
    },
    "type": {
        "type": "int",
        "description": "工作站类型编码"
    }
},
                "required": ["chainName", "ifAsynchronous", "sn", "method", "metering", "type"]
            }
        },
        {
            "name": "contactAnglePlatformUp",
            "description": "接触角平台上升",
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
    "type": {
        "type": "int",
        "description": "工作站类型编码"
    }
},
                "required": ["chainName", "ifAsynchronous", "sn", "method", "type"]
            }
        },
        {
            "name": "contactAnglePlatformDescent",
            "description": "接触角平台下降",
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
    "type": {
        "type": "int",
        "description": "工作站类型编码"
    }
},
                "required": ["chainName", "ifAsynchronous", "sn", "method", "type"]
            }
        },
        {
            "name": "measuringSecondHalf",
            "description": "接触角仪拿取的碳纸编号",
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
    "firstName": {
        "type": "int",
        "description": "碳纸编号"
    },
    "type": {
        "type": "int",
        "description": "工作站类型编码"
    },
    "resultCode": {
        "type": "file",
        "description": "输出文件结果参数"
    }
},
                "required": ["chainName", "ifAsynchronous", "sn", "method", "firstName", "type"]
            }
        },
        {
            "name": "getTemplateList",
            "description": "获取模板列表",
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
            "name": "measuringAdhesion2",
            "description": "粘附力测试",
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
    "templateName": {
        "type": "string",
        "description": "模版名字"
    },
    "fileName": {
        "type": "int",
        "description": "碳纸文件编号"
    },
    "type": {
        "type": "int",
        "description": "工作站类型编码"
    },
    "resultCode": {
        "type": "file",
        "description": "输出文件参数"
    }
},
                "required": ["chainName", "ifAsynchronous", "sn", "method", "templateName", "fileName", "type"]
            }
        }
                    ]
                }
            }
        }
    }
    print(json.dumps(adv_message, ensure_ascii=False), flush=True)
    print(f"--- [cuihua_temp_Server] 催化剂气液微环境工作站 is ready. ---", file=sys.stderr, flush=True)


if __name__ == "__main__":
    # 启动流程：先广播能力，再进入主循环
    cuihua_temp_server_advertise_capabilities()
    cuihua_temp_server_main_loop()
