import sys
import json
# 动态导入当前设备对应的工具类（与主服务器文件同目录）
from tools.tensiometer_server_tools import ActionServerTools


# 创建全局工具管理器实例
tool_manager = ActionServerTools()


# --- 定义设备动作函数（自动生成，与工具类方法对应）---
def tool_movingSampleA(**params):
    return tool_manager.tool_movingSampleA(**params)


def tool_performAdhesionTest(**params):
    return tool_manager.tool_performAdhesionTest(**params)


def tool_tensionerMaterialCollection(**params):
    return tool_manager.tool_tensionerMaterialCollection(**params)


def tool_putTurntable(**params):
    return tool_manager.tool_putTurntable(**params)


def tool_rotate(**params):
    return tool_manager.tool_rotate(**params)


def tool_measuringAdhesion2(**params):
    return tool_manager.tool_measuringAdhesion2(**params)


def tool_getTemplateList(**params):
    return tool_manager.tool_getTemplateList(**params)



AVAILABLE_TOOLS_ACTION = {
    "movingSampleA": tool_movingSampleA,
    "performAdhesionTest": tool_performAdhesionTest,
    "tensionerMaterialCollection": tool_tensionerMaterialCollection,
    "putTurntable": tool_putTurntable,
    "rotate": tool_rotate,
    "measuringAdhesion2": tool_measuringAdhesion2,
    "getTemplateList": tool_getTemplateList
}


# --- MCP协议通信主逻辑（自动适配当前设备）---
def tensiometer_server_main_loop():
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
            print(f"--- [tensiometer_Server] Critical Error: {str(e)} ---", file=sys.stderr, flush=True)


def tensiometer_server_advertise_capabilities():
    """广播当前设备的MCP能力（设备信息、支持的动作）"""
    adv_message = {
        "jsonrpc": "2.0",
        "method": "protocol/advertise",
        "params": {
            "type": "server",
            "server": {
                "protocolVersion": "0.1.0",
                "displayName": "张力仪工作站",
                "capabilities": {
                    "tools": [
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
        "type": "int",
        "description": "工作站编号"
    }
},
                "required": ["chainName", "ifAsynchronous", "sn", "method", "type"]
            }
        },
        {
            "name": "performAdhesionTest",
            "description": "测量粘附力（废弃）",
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
    "startHeight": {
        "type": "float",
        "description": "起始高度(mm)"
    },
    "approachSpeed": {
        "type": "float",
        "description": "接触阶段速度(mm/s)"
    },
    "samplingInterval": {
        "type": "float",
        "description": "采样间隔(s)"
    },
    "triggerForce": {
        "type": "float",
        "description": "触发接触力阈值(N)"
    },
    "compressionDistance": {
        "type": "float",
        "description": "压缩距离(mm)"
    },
    "testSpeed": {
        "type": "float",
        "description": "测试阶段速度(mm/s)"
    },
    "maxSafetyForce": {
        "type": "float",
        "description": "安全力值阈值(N)"
    },
    "pullOffDistance": {
        "type": "float",
        "description": "判定完成的上拉距离(mm)"
    },
    "type": {
        "type": "int",
        "description": "工作站编号"
    }
},
                "required": ["chainName", "ifAsynchronous", "sn", "method", "startHeight", "approachSpeed", "samplingInterval", "triggerForce", "compressionDistance", "testSpeed", "maxSafetyForce", "pullOffDistance", "type"]
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
        "description": "工作站编号"
    }
},
                "required": ["chainName", "ifAsynchronous", "sn", "method", "type"]
            }
        },
        {
            "name": "putTurntable",
            "description": "机械臂请求到中转台碳纸放在电解池转台上",
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
            "name": "rotate",
            "description": "电解池转台旋转一格",
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
            "name": "measuringAdhesion2",
            "description": "测量粘附力",
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
        "description": "模版名字（请输入带后缀的全称文件名，比如Default.aut】）"
    },
    "type": {
        "type": "int",
        "description": "工作站编号"
    },
    "resultCode": {
        "type": "file",
        "description": "输出文件结果参数"
    }
},
                "required": ["chainName", "ifAsynchronous", "sn", "method", "templateName", "type"]
            }
        },
        {
            "name": "getTemplateList",
            "description": "获取模版列表",
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
    print(f"--- [tensiometer_Server] 张力仪工作站 is ready. ---", file=sys.stderr, flush=True)


if __name__ == "__main__":
    # 启动流程：先广播能力，再进入主循环
    tensiometer_server_advertise_capabilities()
    tensiometer_server_main_loop()
