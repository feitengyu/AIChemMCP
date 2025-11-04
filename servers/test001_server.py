import sys
import json
# 动态导入当前设备对应的工具类（与主服务器文件同目录）
from tools.test001_server_tools import ActionServerTools


# 创建全局工具管理器实例
tool_manager = ActionServerTools()


# --- 定义设备动作函数（自动生成，与工具类方法对应）---
def tool_start(**params):
    return tool_manager.tool_start(**params)


def tool_getResult(**params):
    return tool_manager.tool_getResult(**params)


def tool_ces(**params):
    return tool_manager.tool_ces(**params)



AVAILABLE_TOOLS_ACTION = {
    "start": tool_start,
    "getResult": tool_getResult,
    "ces": tool_ces
}


# --- MCP协议通信主逻辑（自动适配当前设备）---
def test001_server_main_loop():
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
            print(f"--- [test001_Server] Critical Error: {str(e)} ---", file=sys.stderr, flush=True)


def test001_server_advertise_capabilities():
    """广播当前设备的MCP能力（设备信息、支持的动作）"""
    adv_message = {
        "jsonrpc": "2.0",
        "method": "protocol/advertise",
        "params": {
            "type": "server",
            "server": {
                "protocolVersion": "0.1.0",
                "displayName": "测试指令操作",
                "capabilities": {
                    "tools": [
        {
            "name": "start",
            "description": "start",
            "parameters": {
                "type": "object",
                "properties": {
    "number": {
        "type": "int",
        "description": "产品数量",
        "minimum": "0",
        "maximum": "10"
    },
    "trayNumber": {
        "type": "int",
        "description": "盘子数量",
        "minimum": "0",
        "maximum": "1"
    },
    "width": {
        "type": "int",
        "description": "产品宽度（需大于22）",
        "minimum": "22",
        "maximum": "50"
    },
    "angle": {
        "type": "int",
        "description": "拍照间隔角度",
        "minimum": "0",
        "maximum": "360"
    },
    "operation": {
        "type": "string",
        "description": "operation"
    },
    "frequency": {
        "type": "string",
        "description": "膜拉升次数",
        "minimum": "0",
        "maximum": "40"
    },
    "deviceConfigs": {
        "type": "array",
        "description": "膜拉升测试设置",
        "properties": {
            "deformation": {
                "type": "float",
                "description": "形变值",
                "minimum": "50",
                "maximum": "80"
            },
            "pullingForce": {
                "type": "float",
                "description": "拉力",
                "minimum": "50",
                "maximum": "200"
            },
            "pullingSpeed": {
                "type": "float",
                "description": "拉升速度",
                "minimum": "1",
                "maximum": "20"
            },
            "windTimes": {
                "type": "float",
                "description": "风枪加热时间",
                "minimum": "0",
                "maximum": "300"
            }
        },
        "required": [
            "deformation",
            "pullingForce",
            "pullingSpeed",
            "windTimes"
        ]
    },
    "deviceConfigs.deformation": {
        "type": "float",
        "description": "形变值",
        "minimum": "50",
        "maximum": "80"
    },
    "deviceConfigs.pullingForce": {
        "type": "float",
        "description": "拉力",
        "minimum": "50",
        "maximum": "200"
    },
    "deviceConfigs.pullingSpeed": {
        "type": "float",
        "description": "拉升速度",
        "minimum": "1",
        "maximum": "20"
    },
    "deviceConfigs.windTimes": {
        "type": "float",
        "description": "风枪加热时间",
        "minimum": "0",
        "maximum": "300"
    },
    "ttttt": {
        "type": "object",
        "description": "ttttt",
        "properties": {
            "yyy": {
                "type": "string",
                "description": "id"
            }
        }
    },
    "ttttt.yyy": {
        "type": "string",
        "description": "id"
    },
    "molecularWeight": {
        "type": "object",
        "description": "createTime",
        "properties": {
            "createTime": {
                "type": "string",
                "description": "createTime"
            }
        },
        "required": [
            "createTime"
        ]
    },
    "molecularWeight.createTime": {
        "type": "string",
        "description": "createTime"
    }
},
                "required": ["number", "trayNumber", "width", "angle", "operation", "frequency", "deviceConfigs.deformation", "deviceConfigs.pullingForce", "deviceConfigs.pullingSpeed", "deviceConfigs.windTimes", "molecularWeight.createTime"]
            }
        },
        {
            "name": "getResult",
            "description": "getResult",
            "parameters": {
                "type": "object",
                "properties": {
    "getResult": {
        "type": "file",
        "description": "getResult"
    },
    "operation": {
        "type": "string",
        "description": "operation"
    }
},
                "required": []
            }
        },
        {
            "name": "ces",
            "description": "paramstest",
            "parameters": {
                "type": "object",
                "properties": {
    "getResult": {
        "type": "file",
        "description": "getResult"
    },
    "operation": {
        "type": "string",
        "description": "operation"
    },
    "paramstest1": {
        "type": "int",
        "description": "int"
    },
    "paramstest": {
        "type": "float",
        "description": "float"
    }
},
                "required": ["paramstest1"]
            }
        }
                    ]
                }
            }
        }
    }
    print(json.dumps(adv_message, ensure_ascii=False), flush=True)
    print(f"--- [test001_Server] 测试指令操作 is ready. ---", file=sys.stderr, flush=True)


if __name__ == "__main__":
    # 启动流程：先广播能力，再进入主循环
    test001_server_advertise_capabilities()
    test001_server_main_loop()
