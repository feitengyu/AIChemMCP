import sys
import json
# 动态导入当前设备对应的工具类（与主服务器文件同目录）
from tools.nucleic_acid_extractor_server_tools import ActionServerTools


# 创建全局工具管理器实例
tool_manager = ActionServerTools()


# --- 定义设备动作函数（自动生成，与工具类方法对应）---
def tool_getProcedureList(**params):
    return tool_manager.tool_getProcedureList(**params)


def tool_getCurrentProcedure(**params):
    return tool_manager.tool_getCurrentProcedure(**params)


def tool_setCurrentProcedure(**params):
    return tool_manager.tool_setCurrentProcedure(**params)


def tool_startScanSample(**params):
    return tool_manager.tool_startScanSample(**params)


def tool_stopProcedure(**params):
    return tool_manager.tool_stopProcedure(**params)


def tool_getState(**params):
    return tool_manager.tool_getState(**params)



AVAILABLE_TOOLS_ACTION = {
    "getProcedureList": tool_getProcedureList,
    "getCurrentProcedure": tool_getCurrentProcedure,
    "setCurrentProcedure": tool_setCurrentProcedure,
    "startScanSample": tool_startScanSample,
    "stopProcedure": tool_stopProcedure,
    "getState": tool_getState
}


# --- MCP协议通信主逻辑（自动适配当前设备）---
def nucleic_acid_extractor_server_main_loop():
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
            print(f"--- [nucleic_acid_extractor_Server] Critical Error: {str(e)} ---", file=sys.stderr, flush=True)


def nucleic_acid_extractor_server_advertise_capabilities():
    """广播当前设备的MCP能力（设备信息、支持的动作）"""
    adv_message = {
        "jsonrpc": "2.0",
        "method": "protocol/advertise",
        "params": {
            "type": "server",
            "server": {
                "protocolVersion": "0.1.0",
                "displayName": "核酸提取仪",
                "capabilities": {
                    "tools": [
        {
            "name": "getProcedureList",
            "description": "获取方法列表",
            "parameters": {
                "type": "object",
                "properties": {
    "operate": {
        "type": "string",
        "description": "指令编码"
    }
},
                "required": ["operate"]
            }
        },
        {
            "name": "getCurrentProcedure",
            "description": "获取当前使用的方法",
            "parameters": {
                "type": "object",
                "properties": {
    "operate": {
        "type": "string",
        "description": "指令编码"
    }
},
                "required": ["operate"]
            }
        },
        {
            "name": "setCurrentProcedure",
            "description": "设置当前使用的方法",
            "parameters": {
                "type": "object",
                "properties": {
    "operate": {
        "type": "string",
        "description": "指令编码"
    },
    "Name": {
        "type": "string",
        "description": "方法名称",
        "enum": [
            {
                "label": "DP713",
                "value": "DP713"
            },
            {
                "label": "test",
                "value": "test"
            },
            {
                "label": "磁吸测试",
                "value": "磁吸测试"
            },
            {
                "label": "DP802",
                "value": "DP802"
            },
            {
                "label": "DP802 副本",
                "value": "DP802 副本"
            }
        ]
    }
},
                "required": ["operate", "Name"]
            }
        },
        {
            "name": "startScanSample",
            "description": "启动方法",
            "parameters": {
                "type": "object",
                "properties": {
    "operate": {
        "type": "string",
        "description": "指令编码"
    }
},
                "required": ["operate"]
            }
        },
        {
            "name": "stopProcedure",
            "description": "停止方法",
            "parameters": {
                "type": "object",
                "properties": {
    "operate": {
        "type": "string",
        "description": "指令编码"
    }
},
                "required": ["operate"]
            }
        },
        {
            "name": "getState",
            "description": "获取设备状态",
            "parameters": {
                "type": "object",
                "properties": {
    "operate": {
        "type": "string",
        "description": "指令编码"
    }
},
                "required": ["operate"]
            }
        }
                    ]
                }
            }
        }
    }
    print(json.dumps(adv_message, ensure_ascii=False), flush=True)
    print(f"--- [nucleic_acid_extractor_Server] 核酸提取仪 is ready. ---", file=sys.stderr, flush=True)


if __name__ == "__main__":
    # 启动流程：先广播能力，再进入主循环
    nucleic_acid_extractor_server_advertise_capabilities()
    nucleic_acid_extractor_server_main_loop()
