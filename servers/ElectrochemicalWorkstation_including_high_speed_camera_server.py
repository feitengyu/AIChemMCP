import sys
import json
# 动态导入当前设备对应的工具类（与主服务器文件同目录）
from tools.ElectrochemicalWorkstation_including_high_speed_camera_server_tools import ActionServerTools


# 创建全局工具管理器实例
tool_manager = ActionServerTools()


# --- 定义设备动作函数（自动生成，与工具类方法对应）---
def tool_connectCamera(**params):
    return tool_manager.tool_connectCamera(**params)


def tool_setCameraSettings(**params):
    return tool_manager.tool_setCameraSettings(**params)


def tool_startRecording(**params):
    return tool_manager.tool_startRecording(**params)


def tool_setExperimentProgram1(**params):
    return tool_manager.tool_setExperimentProgram1(**params)


def tool_startExperiment(**params):
    return tool_manager.tool_startExperiment(**params)


def tool_getResultFileTelephony(**params):
    return tool_manager.tool_getResultFileTelephony(**params)


def tool_getPhotoFileBase64(**params):
    return tool_manager.tool_getPhotoFileBase64(**params)


def tool_setExperimentProgram2(**params):
    return tool_manager.tool_setExperimentProgram2(**params)


def tool_takePaper(**params):
    return tool_manager.tool_takePaper(**params)


def tool_num(**params):
    return tool_manager.tool_num(**params)


def tool_startActivationSteps(**params):
    return tool_manager.tool_startActivationSteps(**params)


def tool_conversion1(**params):
    return tool_manager.tool_conversion1(**params)


def tool_conversion2(**params):
    return tool_manager.tool_conversion2(**params)


def tool_rotate(**params):
    return tool_manager.tool_rotate(**params)


def tool_peristalticPumpStarted(**params):
    return tool_manager.tool_peristalticPumpStarted(**params)


def tool_peristalticPumpStopped(**params):
    return tool_manager.tool_peristalticPumpStopped(**params)


def tool_putPaperElectrolyticCell(**params):
    return tool_manager.tool_putPaperElectrolyticCell(**params)


def tool_probePaperClamping(**params):
    return tool_manager.tool_probePaperClamping(**params)


def tool_removePaperElectrolyticCell(**params):
    return tool_manager.tool_removePaperElectrolyticCell(**params)


def tool_releaseProbingPaper(**params):
    return tool_manager.tool_releaseProbingPaper(**params)


def tool_dischargePumpControlStart(**params):
    return tool_manager.tool_dischargePumpControlStart(**params)


def tool_dischargePumpControlStop(**params):
    return tool_manager.tool_dischargePumpControlStop(**params)


def tool_SwitchingValveControl(**params):
    return tool_manager.tool_SwitchingValveControl(**params)


def tool_putterForward(**params):
    return tool_manager.tool_putterForward(**params)


def tool_putterBack(**params):
    return tool_manager.tool_putterBack(**params)


def tool_putCarbonPaperProcess(**params):
    return tool_manager.tool_putCarbonPaperProcess(**params)


def tool_removeCarbonPaperProcess(**params):
    return tool_manager.tool_removeCarbonPaperProcess(**params)


def tool_SwitchingValveControlOn(**params):
    return tool_manager.tool_SwitchingValveControlOn(**params)


def tool_SwitchingValveControlOff(**params):
    return tool_manager.tool_SwitchingValveControlOff(**params)



AVAILABLE_TOOLS_ACTION = {
    "connectCamera": tool_connectCamera,
    "setCameraSettings": tool_setCameraSettings,
    "startRecording": tool_startRecording,
    "setExperimentProgram1": tool_setExperimentProgram1,
    "startExperiment": tool_startExperiment,
    "getResultFileTelephony": tool_getResultFileTelephony,
    "getPhotoFileBase64": tool_getPhotoFileBase64,
    "setExperimentProgram2": tool_setExperimentProgram2,
    "takePaper": tool_takePaper,
    "num": tool_num,
    "startActivationSteps": tool_startActivationSteps,
    "conversion1": tool_conversion1,
    "conversion2": tool_conversion2,
    "rotate": tool_rotate,
    "peristalticPumpStarted": tool_peristalticPumpStarted,
    "peristalticPumpStopped": tool_peristalticPumpStopped,
    "putPaperElectrolyticCell": tool_putPaperElectrolyticCell,
    "probePaperClamping": tool_probePaperClamping,
    "removePaperElectrolyticCell": tool_removePaperElectrolyticCell,
    "releaseProbingPaper": tool_releaseProbingPaper,
    "dischargePumpControlStart": tool_dischargePumpControlStart,
    "dischargePumpControlStop": tool_dischargePumpControlStop,
    "SwitchingValveControl": tool_SwitchingValveControl,
    "putterForward": tool_putterForward,
    "putterBack": tool_putterBack,
    "putCarbonPaperProcess": tool_putCarbonPaperProcess,
    "removeCarbonPaperProcess": tool_removeCarbonPaperProcess,
    "SwitchingValveControlOn": tool_SwitchingValveControlOn,
    "SwitchingValveControlOff": tool_SwitchingValveControlOff
}


# --- MCP协议通信主逻辑（自动适配当前设备）---
def ElectrochemicalWorkstation_including_high_speed_camera_server_main_loop():
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
            print(f"--- [ElectrochemicalWorkstation_(including_high_speed_camera)_Server] Critical Error: {str(e)} ---", file=sys.stderr, flush=True)


def ElectrochemicalWorkstation_including_high_speed_camera_server_advertise_capabilities():
    """广播当前设备的MCP能力（设备信息、支持的动作）"""
    adv_message = {
        "jsonrpc": "2.0",
        "method": "protocol/advertise",
        "params": {
            "type": "server",
            "server": {
                "protocolVersion": "0.1.0",
                "displayName": "电化学工作站（含高速摄像机）",
                "capabilities": {
                    "tools": [
        {
            "name": "connectCamera",
            "description": "连接高速摄像头",
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
            "name": "setCameraSettings",
            "description": "设置相机参数",
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
    "exposure": {
        "type": "int",
        "description": "曝光时间"
    },
    "frameRate": {
        "type": "int",
        "description": "帧率（FPS）"
    },
    "captureTime": {
        "type": "int",
        "description": "拍照时间"
    },
    "delay": {
        "type": "float",
        "description": "相机延迟时间"
    },
    "selfframes": {
        "type": "array",
        "description": "自定义指定获取的帧数",
        "properties": {
            "test": {
                "type": "int",
                "description": "参数 test"
            }
        },
        "required": [
            "test"
        ]
    },
    "selfframes.test": {
        "type": "int",
        "description": "参数 test"
    },
    "frame": {
        "type": "int",
        "description": "前后多少帧"
    },
    "experimentNumber": {
        "type": "int",
        "description": "拿取实验碳纸编号"
    },
    "type": {
        "type": "int",
        "description": "工作站类型编码"
    }
},
                "required": ["chainName", "ifAsynchronous", "sn", "method", "exposure", "frameRate", "captureTime", "delay", "selfframes", "selfframes.test", "frame", "experimentNumber", "type"]
            }
        },
        {
            "name": "startRecording",
            "description": "开始录像",
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
            "name": "setExperimentProgram1",
            "description": "设置活化程序文件",
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
    "program": {
        "type": "string",
        "description": "实验程序"
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
            "name": "startExperiment",
            "description": "开始实验",
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
    "triggerStart": {
        "type": "boolean",
        "description": "是否触发",
        "enum": [
            "true",
            "false"
        ]
    },
    "resultCode": {
        "type": "file",
        "description": "输出结果参数"
    },
    "type": {
        "type": "int",
        "description": "工作站类型"
    }
},
                "required": ["chainName", "ifAsynchronous", "sn", "method", "triggerStart", "resultCode", "type"]
            }
        },
        {
            "name": "getResultFileTelephony",
            "description": "电化学工作站结果返回",
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
        "description": "工作站类型"
    }
},
                "required": ["chainName", "ifAsynchronous", "sn", "method", "type"]
            }
        },
        {
            "name": "getPhotoFileBase64",
            "description": "高速摄像头结果返回",
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
        "description": "工作站类型"
    }
},
                "required": ["chainName", "ifAsynchronous", "sn", "method", "type"]
            }
        },
        {
            "name": "setExperimentProgram2",
            "description": "设置测试程序文件",
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
    "program": {
        "type": "string",
        "description": "实验程序"
    },
    "type": {
        "type": "int",
        "description": "工作站类型"
    }
},
                "required": ["chainName", "ifAsynchronous", "sn", "method", "program", "type"]
            }
        },
        {
            "name": "takePaper",
            "description": "从转盘取碳纸",
            "parameters": {
                "type": "object",
                "properties": {
    "num": {
        "type": "int",
        "description": "转盘上的碳纸编号"
    }
},
                "required": ["num"]
            }
        },
        {
            "name": "num",
            "description": "获取迭代次数",
            "parameters": {
                "type": "object",
                "properties": {
    "data": {
        "type": "array",
        "description": "迭代数据",
        "properties": {
            "num": {
                "type": "int",
                "description": "编号"
            },
            "time": {
                "type": "string",
                "description": "时间"
            }
        },
        "required": [
            "num",
            "time"
        ]
    },
    "data.num": {
        "type": "int",
        "description": "编号"
    },
    "data.time": {
        "type": "string",
        "description": "时间"
    }
},
                "required": ["data", "data.num", "data.time"]
            }
        },
        {
            "name": "startActivationSteps",
            "description": "活化开启",
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
    "triggerStart": {
        "type": "boolean",
        "description": "是否触发",
        "enum": [
            "true",
            "false"
        ]
    },
    "resultCode": {
        "type": "file",
        "description": "输出结果参数"
    },
    "type": {
        "type": "int",
        "description": "工作站类型"
    }
},
                "required": ["chainName", "ifAsynchronous", "sn", "method", "triggerStart", "resultCode", "type"]
            }
        },
        {
            "name": "conversion1",
            "description": "传入base64的活化程序文件",
            "parameters": {
                "type": "object",
                "properties": {
    "file_url": {
        "type": "file",
        "description": "活化程序上传地址"
    },
    "file_type": {
        "type": "string",
        "description": "活化程序文件类型（.nox）"
    },
    "num": {
        "type": "int",
        "description": "程序文件标识号（活化-1 测试-2）"
    },
    "type": {
        "type": "int",
        "description": "指令所属的工作站编号"
    }
},
                "required": ["file_url", "file_type", "num", "type"]
            }
        },
        {
            "name": "conversion2",
            "description": "传入base64的测试程序文件",
            "parameters": {
                "type": "object",
                "properties": {
    "file_url": {
        "type": "file",
        "description": "测试程序上传地址"
    },
    "file_type": {
        "type": "string",
        "description": "活化程序文件类型（.nox）"
    },
    "num": {
        "type": "int",
        "description": "程序文件类型（1-活化  2-测试）"
    },
    "type": {
        "type": "int",
        "description": "指令所属的工作站编码"
    }
},
                "required": ["file_url", "file_type", "num", "type"]
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
        "description": "中转台碳纸编号"
    },
    "type": {
        "type": "int",
        "description": "工作站类型"
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
        "description": "工作站类型"
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
        "description": "工作站类型"
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
        "description": "工作站类型"
    }
},
                "required": ["chainName", "ifAsynchronous", "sn", "method", "type"]
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
        "description": "工作站类型"
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
        "description": "工作站类型"
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
        "description": "工作站类型"
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
        "description": "工作站类型"
    }
},
                "required": ["chainName", "ifAsynchronous", "sn", "method", "type"]
            }
        },
        {
            "name": "dischargePumpControlStop",
            "description": "排液泵关闭",
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
        "description": "工作站类型"
    }
},
                "required": ["chainName", "ifAsynchronous", "sn", "method", "type"]
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
        "description": "工作站类型"
    }
},
                "required": ["chainName", "ifAsynchronous", "sn", "method", "type"]
            }
        },
        {
            "name": "putterForward",
            "description": "电解池推杆前进进行拿取",
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
        "description": "工作站类型"
    }
},
                "required": ["chainName", "ifAsynchronous", "sn", "method", "type"]
            }
        },
        {
            "name": "putterBack",
            "description": "电解池推杆后退进行拿取",
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
        "description": "工作站类型"
    }
},
                "required": ["chainName", "ifAsynchronous", "sn", "method", "type"]
            }
        },
        {
            "name": "putCarbonPaperProcess",
            "description": "碳纸放入电解池",
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
        "description": "工作站类型"
    }
},
                "required": ["chainName", "ifAsynchronous", "sn", "method", "type"]
            }
        },
        {
            "name": "removeCarbonPaperProcess",
            "description": "碳纸取出电解池",
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
        "description": "工作站类型"
    }
},
                "required": ["chainName", "ifAsynchronous", "sn", "method", "type"]
            }
        },
        {
            "name": "SwitchingValveControlOn",
            "description": "切换阀打开",
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
        "description": "工作站类型"
    }
},
                "required": ["chainName", "ifAsynchronous", "sn", "method", "type"]
            }
        },
        {
            "name": "SwitchingValveControlOff",
            "description": "切换阀关闭",
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
        "description": "工作站类型"
    }
},
                "required": ["chainName", "ifAsynchronous", "sn", "method", "type"]
            }
        }
                    ]
                }
            }
        }
    }
    print(json.dumps(adv_message, ensure_ascii=False), flush=True)
    print(f"--- [ElectrochemicalWorkstation_(including_high_speed_camera)_Server] 电化学工作站（含高速摄像机） is ready. ---", file=sys.stderr, flush=True)


if __name__ == "__main__":
    # 启动流程：先广播能力，再进入主循环
    ElectrochemicalWorkstation_including_high_speed_camera_server_advertise_capabilities()
    ElectrochemicalWorkstation_including_high_speed_camera_server_main_loop()
