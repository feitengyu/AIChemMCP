import sys
import json
# 动态导入当前设备对应的工具类（与主服务器文件同目录）
from tools.MassSpectrometer_ALD_platform_server_tools import ActionServerTools


# 创建全局工具管理器实例
tool_manager = ActionServerTools()


# --- 定义设备动作函数（自动生成，与工具类方法对应）---
def tool_powerOnVacSys(**params):
    return tool_manager.tool_powerOnVacSys(**params)


def tool_powerOffVacSys(**params):
    return tool_manager.tool_powerOffVacSys(**params)


def tool_queryVacSysStatus(**params):
    return tool_manager.tool_queryVacSysStatus(**params)


def tool_powerOnElecSys(**params):
    return tool_manager.tool_powerOnElecSys(**params)


def tool_powerOffElecSys(**params):
    return tool_manager.tool_powerOffElecSys(**params)


def tool_sendTraceRangeData(**params):
    return tool_manager.tool_sendTraceRangeData(**params)


def tool_startACQ(**params):
    return tool_manager.tool_startACQ(**params)


def tool_stopACQ(**params):
    return tool_manager.tool_stopACQ(**params)


def tool_getFileInputStream(**params):
    return tool_manager.tool_getFileInputStream(**params)


def tool_automaticOperation(**params):
    return tool_manager.tool_automaticOperation(**params)


def tool_sampleInstallationCompleted(**params):
    return tool_manager.tool_sampleInstallationCompleted(**params)



AVAILABLE_TOOLS_ACTION = {
    "powerOnVacSys": tool_powerOnVacSys,
    "powerOffVacSys": tool_powerOffVacSys,
    "queryVacSysStatus": tool_queryVacSysStatus,
    "powerOnElecSys": tool_powerOnElecSys,
    "powerOffElecSys": tool_powerOffElecSys,
    "sendTraceRangeData": tool_sendTraceRangeData,
    "startACQ": tool_startACQ,
    "stopACQ": tool_stopACQ,
    "getFileInputStream": tool_getFileInputStream,
    "automaticOperation": tool_automaticOperation,
    "sampleInstallationCompleted": tool_sampleInstallationCompleted
}


# --- MCP协议通信主逻辑（自动适配当前设备）---
def MassSpectrometer_ALD_platform_server_main_loop():
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
            print(f"--- [MassSpectrometer_(ALD_platform)_Server] Critical Error: {str(e)} ---", file=sys.stderr, flush=True)


def MassSpectrometer_ALD_platform_server_advertise_capabilities():
    """广播当前设备的MCP能力（设备信息、支持的动作）"""
    adv_message = {
        "jsonrpc": "2.0",
        "method": "protocol/advertise",
        "params": {
            "type": "server",
            "server": {
                "protocolVersion": "0.1.0",
                "displayName": "质谱工作站（ALD平台）",
                "capabilities": {
                    "tools": [
        {
            "name": "powerOnVacSys",
            "description": "真空系统打开",
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
            "name": "powerOffVacSys",
            "description": "真空系统关闭",
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
            "name": "queryVacSysStatus",
            "description": "查询真空状态",
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
            "name": "powerOnElecSys",
            "description": "电控系统打开",
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
            "name": "powerOffElecSys",
            "description": "电控系统关闭",
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
            "name": "sendTraceRangeData",
            "description": "质荷比参数设定",
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
        "type": "array",
        "description": "method"
    },
    "dataCount": {
        "type": "int",
        "description": "dataCount"
    }
},
                "required": ["chainName", "ifAsynchronous", "sn", "method", "dataCount"]
            }
        },
        {
            "name": "startACQ",
            "description": "开始采集",
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
            "name": "stopACQ",
            "description": "停止采集",
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
    "resultCode": {
        "type": "file",
        "description": "输出文件参数"
    },
    "paramCode": {
        "type": "string",
        "description": "参数 paramCode"
    }
},
                "required": ["chainName", "ifAsynchronous", "sn", "method", "resultCode"]
            }
        },
        {
            "name": "automaticOperation",
            "description": "管式炉自动运行   1",
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
            "name": "sampleInstallationCompleted",
            "description": "判断真空系统是否满足   2炉后续工作",
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
        }
                    ]
                }
            }
        }
    }
    print(json.dumps(adv_message, ensure_ascii=False), flush=True)
    print(f"--- [MassSpectrometer_(ALD_platform)_Server] 质谱工作站（ALD平台） is ready. ---", file=sys.stderr, flush=True)


if __name__ == "__main__":
    # 启动流程：先广播能力，再进入主循环
    MassSpectrometer_ALD_platform_server_advertise_capabilities()
    MassSpectrometer_ALD_platform_server_main_loop()
