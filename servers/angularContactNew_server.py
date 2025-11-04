import sys
import json
# 动态导入当前设备对应的工具类（与主服务器文件同目录）
from tools.angularContactNew_server_tools import ActionServerTools


# 创建全局工具管理器实例
tool_manager = ActionServerTools()


# --- 定义设备动作函数（自动生成，与工具类方法对应）---
def tool_startupWorkstation(**params):
    return tool_manager.tool_startupWorkstation(**params)


def tool_robotActivation(**params):
    return tool_manager.tool_robotActivation(**params)


def tool_rawMaterialFinish(**params):
    return tool_manager.tool_rawMaterialFinish(**params)


def tool_takeRawMaterials(**params):
    return tool_manager.tool_takeRawMaterials(**params)


def tool_contactAnglePlatformUp(**params):
    return tool_manager.tool_contactAnglePlatformUp(**params)


def tool_prepareSample(**params):
    return tool_manager.tool_prepareSample(**params)


def tool_measuringContactAngle(**params):
    return tool_manager.tool_measuringContactAngle(**params)


def tool_contactAngleTakeMaterial(**params):
    return tool_manager.tool_contactAngleTakeMaterial(**params)



AVAILABLE_TOOLS_ACTION = {
    "startupWorkstation": tool_startupWorkstation,
    "robotActivation": tool_robotActivation,
    "rawMaterialFinish": tool_rawMaterialFinish,
    "takeRawMaterials": tool_takeRawMaterials,
    "contactAnglePlatformUp": tool_contactAnglePlatformUp,
    "prepareSample": tool_prepareSample,
    "measuringContactAngle": tool_measuringContactAngle,
    "contactAngleTakeMaterial": tool_contactAngleTakeMaterial
}


# --- MCP协议通信主逻辑（自动适配当前设备）---
def angularContactNew_server_main_loop():
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
            print(f"--- [angularContactNew_Server] Critical Error: {str(e)} ---", file=sys.stderr, flush=True)


def angularContactNew_server_advertise_capabilities():
    """广播当前设备的MCP能力（设备信息、支持的动作）"""
    adv_message = {
        "jsonrpc": "2.0",
        "method": "protocol/advertise",
        "params": {
            "type": "server",
            "server": {
                "protocolVersion": "0.1.0",
                "displayName": "接触角测量仪工作站（含电压施加装置）",
                "capabilities": {
                    "tools": [
        {
            "name": "startupWorkstation",
            "description": "启动机器臂",
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
        "description": "工作站编号"
    }
},
                "required": ["chainName", "ifAsynchronous", "sn", "method", "type"]
            }
        },
        {
            "name": "robotActivation",
            "description": "激活机器臂",
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
        "description": "工作站编号"
    }
},
                "required": ["chainName", "ifAsynchronous", "sn", "method", "type"]
            }
        },
        {
            "name": "rawMaterialFinish",
            "description": "完成碳纸准备",
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
        "description": "工作站编号"
    }
},
                "required": ["chainName", "ifAsynchronous", "sn", "method", "type"]
            }
        },
        {
            "name": "takeRawMaterials",
            "description": "取原料和探纸夹",
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
        "description": "工作站编号"
    }
},
                "required": ["chainName", "ifAsynchronous", "sn", "method", "type"]
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
        "description": "工作站编号"
    }
},
                "required": ["chainName", "ifAsynchronous", "sn", "method", "type"]
            }
        },
        {
            "name": "prepareSample",
            "description": "移动样品到接触角仪",
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
        "description": "工作站编号"
    }
},
                "required": ["chainName", "ifAsynchronous", "sn", "method", "type"]
            }
        },
        {
            "name": "measuringContactAngle",
            "description": "开始滴液测量接触角",
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
        "type": "float",
        "description": "滴液量"
    },
    "name": {
        "type": "string",
        "description": "设置保存的本地文件名称"
    },
    "type": {
        "type": "int",
        "description": "工作站编号"
    },
    "resultCode": {
        "type": "file",
        "description": "输出结果文件参数"
    }
},
                "required": ["chainName", "ifAsynchronous", "sn", "method", "metering", "name", "type"]
            }
        },
        {
            "name": "contactAngleTakeMaterial",
            "description": "接触角测量完成请求取料",
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
        "description": "工作站编号"
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
    print(f"--- [angularContactNew_Server] 接触角测量仪工作站（含电压施加装置） is ready. ---", file=sys.stderr, flush=True)


if __name__ == "__main__":
    # 启动流程：先广播能力，再进入主循环
    angularContactNew_server_advertise_capabilities()
    angularContactNew_server_main_loop()
