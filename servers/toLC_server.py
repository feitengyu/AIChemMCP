import sys
import json
# 动态导入当前设备对应的工具类（与主服务器文件同目录）
from toLC_server_tools import ActionServerTools


# 创建全局工具管理器实例
tool_manager = ActionServerTools()


# --- 定义设备动作函数（自动生成，与工具类方法对应）---
def tool_start_pure(**params):
    return tool_manager.tool_start_pure(**params)



AVAILABLE_TOOLS_ACTION = {
    "start_pure": tool_start_pure
}


# --- MCP协议通信主逻辑（自动适配当前设备）---
def toLC_server_main_loop():
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
            print(f"--- [toLC_Server] Critical Error: {str(e)} ---", file=sys.stderr, flush=True)


def toLC_server_advertise_capabilities():
    """广播当前设备的MCP能力（设备信息、支持的动作）"""
    adv_message = {
        "jsonrpc": "2.0",
        "method": "protocol/advertise",
        "params": {
            "type": "server",
            "server": {
                "protocolVersion": "0.1.0",
                "displayName": "色谱工作站",
                "capabilities": {
                    "tools": [
        {
            "name": "start_pure",
            "description": "开始纯化",
            "parameters": {
                "type": "object",
                "properties": {
    "cmd": {
        "type": "string",
        "description": "操作指令"
    },
    "others": {
        "type": "array",
        "description": "参数",
        "properties": {
            "fileName": {
                "type": "string",
                "description": "fileName"
            },
            "sampleLocation": {
                "type": "string",
                "description": "sampleLocation"
            },
            "injVol": {
                "type": "float",
                "description": "injVol"
            },
            "inletFile": {
                "type": "string",
                "description": "inletFile"
            },
            "msFile": {
                "type": "string",
                "description": "msFile"
            },
            "fractionFile": {
                "type": "string",
                "description": "fractionFile"
            },
            "wavelengthA": {
                "type": "float",
                "description": "wavelengthA"
            },
            "massA": {
                "type": "string",
                "description": "massA"
            },
            "massB": {
                "type": "string",
                "description": "massB"
            },
            "fraction1": {
                "type": "string",
                "description": "fraction1"
            },
            "fraction2": {
                "type": "string",
                "description": "fraction2"
            },
            "index": {
                "type": "int",
                "description": "index"
            },
            "id": {
                "type": "string",
                "description": "id"
            }
        },
        "required": [
            "fileName",
            "sampleLocation",
            "injVol",
            "inletFile",
            "msFile",
            "index",
            "id"
        ]
    },
    "others.fileName": {
        "type": "string",
        "description": "fileName"
    },
    "others.sampleLocation": {
        "type": "string",
        "description": "sampleLocation"
    },
    "others.injVol": {
        "type": "float",
        "description": "injVol"
    },
    "others.inletFile": {
        "type": "string",
        "description": "inletFile"
    },
    "others.msFile": {
        "type": "string",
        "description": "msFile"
    },
    "others.fractionFile": {
        "type": "string",
        "description": "fractionFile"
    },
    "others.wavelengthA": {
        "type": "float",
        "description": "wavelengthA"
    },
    "others.massA": {
        "type": "string",
        "description": "massA"
    },
    "others.massB": {
        "type": "string",
        "description": "massB"
    },
    "others.fraction1": {
        "type": "string",
        "description": "fraction1"
    },
    "others.fraction2": {
        "type": "string",
        "description": "fraction2"
    },
    "others.index": {
        "type": "int",
        "description": "index"
    },
    "others.id": {
        "type": "string",
        "description": "id"
    }
},
                "required": ["cmd", "others", "others.fileName", "others.sampleLocation", "others.injVol", "others.inletFile", "others.msFile", "others.index", "others.id"]
            }
        }
                    ]
                }
            }
        }
    }
    print(json.dumps(adv_message, ensure_ascii=False), flush=True)
    print(f"--- [toLC_Server] 色谱工作站 is ready. ---", file=sys.stderr, flush=True)


if __name__ == "__main__":
    # 启动流程：先广播能力，再进入主循环
    toLC_server_advertise_capabilities()
    toLC_server_main_loop()
