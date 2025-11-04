import sys
import json
# 动态导入当前设备对应的工具类（与主服务器文件同目录）
from tools.spps_workstation_server_tools import ActionServerTools


# 创建全局工具管理器实例
tool_manager = ActionServerTools()


# --- 定义设备动作函数（自动生成，与工具类方法对应）---
def tool_start_synthesizer(**params):
    return tool_manager.tool_start_synthesizer(**params)


def tool_rotating_synthesizer(**params):
    return tool_manager.tool_rotating_synthesizer(**params)


def tool_get_synthesizer_rotating_ret(**params):
    return tool_manager.tool_get_synthesizer_rotating_ret(**params)


def tool_rotating_pyrolyzer(**params):
    return tool_manager.tool_rotating_pyrolyzer(**params)


def tool_get_pyrolyzer_rotating_ret(**params):
    return tool_manager.tool_get_pyrolyzer_rotating_ret(**params)


def tool_close_synthesizer(**params):
    return tool_manager.tool_close_synthesizer(**params)


def tool_close_pyrolyzer(**params):
    return tool_manager.tool_close_pyrolyzer(**params)


def tool_down_pyrolyzer_lock(**params):
    return tool_manager.tool_down_pyrolyzer_lock(**params)


def tool_get_upward_pyrolyzer_lock_ret(**params):
    return tool_manager.tool_get_upward_pyrolyzer_lock_ret(**params)


def tool_get_down_pyrolyzer_lock_ret(**params):
    return tool_manager.tool_get_down_pyrolyzer_lock_ret(**params)


def tool_upward_pyrolyzer_lock(**params):
    return tool_manager.tool_upward_pyrolyzer_lock(**params)


def tool_start_pyrolyzer(**params):
    return tool_manager.tool_start_pyrolyzer(**params)


def tool_pre_start_pyrolyzer(**params):
    return tool_manager.tool_pre_start_pyrolyzer(**params)


def tool_test_cmd(**params):
    return tool_manager.tool_test_cmd(**params)



AVAILABLE_TOOLS_ACTION = {
    "start_synthesizer": tool_start_synthesizer,
    "rotating_synthesizer": tool_rotating_synthesizer,
    "get_synthesizer_rotating_ret": tool_get_synthesizer_rotating_ret,
    "rotating_pyrolyzer": tool_rotating_pyrolyzer,
    "get_pyrolyzer_rotating_ret": tool_get_pyrolyzer_rotating_ret,
    "close_synthesizer": tool_close_synthesizer,
    "close_pyrolyzer": tool_close_pyrolyzer,
    "down_pyrolyzer_lock": tool_down_pyrolyzer_lock,
    "get_upward_pyrolyzer_lock_ret": tool_get_upward_pyrolyzer_lock_ret,
    "get_down_pyrolyzer_lock_ret": tool_get_down_pyrolyzer_lock_ret,
    "upward_pyrolyzer_lock": tool_upward_pyrolyzer_lock,
    "start_pyrolyzer": tool_start_pyrolyzer,
    "pre_start_pyrolyzer": tool_pre_start_pyrolyzer,
    "test_cmd": tool_test_cmd
}


# --- MCP协议通信主逻辑（自动适配当前设备）---
def spps_workstation_server_main_loop():
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
            print(f"--- [spps_workstation_Server] Critical Error: {str(e)} ---", file=sys.stderr, flush=True)


def spps_workstation_server_advertise_capabilities():
    """广播当前设备的MCP能力（设备信息、支持的动作）"""
    adv_message = {
        "jsonrpc": "2.0",
        "method": "protocol/advertise",
        "params": {
            "type": "server",
            "server": {
                "protocolVersion": "0.1.0",
                "displayName": "固相多肽工作站",
                "capabilities": {
                    "tools": [
        {
            "name": "start_synthesizer",
            "description": "开始合成",
            "parameters": {
                "type": "object",
                "properties": {
    "others": {
        "type": "array",
        "description": "开始合成",
        "properties": {
            "id": {
                "type": "int",
                "description": "主键"
            },
            "modelName": {
                "type": "string",
                "description": "模板名称"
            },
            "LoadAndStart": {
                "type": "int",
                "description": "启动类型",
                "enum": [
                    {
                        "label": "加载并启动",
                        "value": 1
                    },
                    {
                        "label": "只加载不启动",
                        "value": 0
                    }
                ]
            },
            "OperatingMode": {
                "type": "int",
                "description": "运行模式"
            },
            "UnfinishedContinue": {
                "type": "int",
                "description": "是否运行未完成的项目"
            },
            "channel": {
                "type": "int",
                "description": "通道"
            }
        },
        "required": [
            "LoadAndStart",
            "OperatingMode",
            "UnfinishedContinue",
            "channel"
        ]
    },
    "others.id": {
        "type": "int",
        "description": "主键"
    },
    "others.modelName": {
        "type": "string",
        "description": "模板名称"
    },
    "others.LoadAndStart": {
        "type": "int",
        "description": "启动类型",
        "enum": [
            {
                "label": "加载并启动",
                "value": 1
            },
            {
                "label": "只加载不启动",
                "value": 0
            }
        ]
    },
    "others.OperatingMode": {
        "type": "int",
        "description": "运行模式"
    },
    "others.UnfinishedContinue": {
        "type": "int",
        "description": "是否运行未完成的项目"
    },
    "others.channel": {
        "type": "int",
        "description": "通道"
    },
    "cmd": {
        "type": "string",
        "description": "操作指令"
    }
},
                "required": ["others.LoadAndStart", "others.OperatingMode", "others.UnfinishedContinue", "others.channel", "cmd"]
            }
        },
        {
            "name": "rotating_synthesizer",
            "description": "转动合成仪",
            "parameters": {
                "type": "object",
                "properties": {
    "cmd": {
        "type": "string",
        "description": "操作指令"
    },
    "others": {
        "type": "array",
        "description": "通道类别",
        "properties": {
            "channel": {
                "type": "int",
                "description": "通道"
            }
        },
        "required": [
            "channel"
        ]
    },
    "others.channel": {
        "type": "int",
        "description": "通道"
    }
},
                "required": ["cmd", "others", "others.channel"]
            }
        },
        {
            "name": "get_synthesizer_rotating_ret",
            "description": "合成仪取料结束",
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
            "channel": {
                "type": "int",
                "description": "通道"
            },
            "sleepTime": {
                "type": "int",
                "description": "等待取料完成时间（s）"
            }
        },
        "required": [
            "channel",
            "sleepTime"
        ]
    },
    "others.channel": {
        "type": "int",
        "description": "通道"
    },
    "others.sleepTime": {
        "type": "int",
        "description": "等待取料完成时间（s）"
    }
},
                "required": ["cmd", "others", "others.channel", "others.sleepTime"]
            }
        },
        {
            "name": "rotating_pyrolyzer",
            "description": "转动裂解仪",
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
            "channel": {
                "type": "int",
                "description": "通道"
            }
        },
        "required": [
            "channel"
        ]
    },
    "others.channel": {
        "type": "int",
        "description": "通道"
    }
},
                "required": ["cmd", "others.channel"]
            }
        },
        {
            "name": "get_pyrolyzer_rotating_ret",
            "description": "裂解仪取料结束",
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
            "channel": {
                "type": "int",
                "description": "通道"
            },
            "sleepTime": {
                "type": "int",
                "description": "等待取料完成时间（s）"
            }
        },
        "required": [
            "channel",
            "sleepTime"
        ]
    },
    "others.channel": {
        "type": "int",
        "description": "通道"
    },
    "others.sleepTime": {
        "type": "int",
        "description": "等待取料完成时间（s）"
    }
},
                "required": ["cmd", "others", "others.channel", "others.sleepTime"]
            }
        },
        {
            "name": "close_synthesizer",
            "description": "合成仪关门",
            "parameters": {
                "type": "object",
                "properties": {
    "operation": {
        "type": "string",
        "description": "操作指令"
    }
},
                "required": ["operation"]
            }
        },
        {
            "name": "close_pyrolyzer",
            "description": "裂解仪关门",
            "parameters": {
                "type": "object",
                "properties": {
    "operation": {
        "type": "string",
        "description": "操作指令"
    }
},
                "required": ["operation"]
            }
        },
        {
            "name": "down_pyrolyzer_lock",
            "description": "裂解仪离心管锁扣下移",
            "parameters": {
                "type": "object",
                "properties": {
    "operation": {
        "type": "string",
        "description": "操作指令"
    }
},
                "required": ["operation"]
            }
        },
        {
            "name": "get_upward_pyrolyzer_lock_ret",
            "description": "获取裂解仪离心管锁扣上移结果",
            "parameters": {
                "type": "object",
                "properties": {
    "operation": {
        "type": "string",
        "description": "操作指令"
    }
},
                "required": ["operation"]
            }
        },
        {
            "name": "get_down_pyrolyzer_lock_ret",
            "description": "获取裂解仪离心管锁扣下移结果",
            "parameters": {
                "type": "object",
                "properties": {
    "operation": {
        "type": "string",
        "description": "操作指令"
    }
},
                "required": ["operation"]
            }
        },
        {
            "name": "upward_pyrolyzer_lock",
            "description": "裂解仪离心管锁扣上移",
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
            "channel": {
                "type": "int",
                "description": "通道"
            }
        },
        "required": [
            "channel"
        ]
    },
    "others.channel": {
        "type": "int",
        "description": "通道"
    }
},
                "required": ["cmd", "others.channel"]
            }
        },
        {
            "name": "start_pyrolyzer",
            "description": "开始裂解",
            "parameters": {
                "type": "object",
                "properties": {
    "others": {
        "type": "array",
        "description": "开始裂解",
        "properties": {
            "LoadAndStart": {
                "type": "int",
                "description": "启动类型",
                "enum": [
                    {
                        "label": "加载并启动",
                        "value": 1
                    },
                    {
                        "label": "只加载不启动",
                        "value": 0
                    }
                ]
            },
            "OperatingMode": {
                "type": "int",
                "description": "运行模式"
            },
            "UnfinishedContinue": {
                "type": "int",
                "description": "是否运行未完成的项目"
            },
            "channel": {
                "type": "int",
                "description": "通道"
            }
        },
        "required": [
            "LoadAndStart",
            "OperatingMode",
            "UnfinishedContinue",
            "channel"
        ]
    },
    "others.LoadAndStart": {
        "type": "int",
        "description": "启动类型",
        "enum": [
            {
                "label": "加载并启动",
                "value": 1
            },
            {
                "label": "只加载不启动",
                "value": 0
            }
        ]
    },
    "others.OperatingMode": {
        "type": "int",
        "description": "运行模式"
    },
    "others.UnfinishedContinue": {
        "type": "int",
        "description": "是否运行未完成的项目"
    },
    "others.channel": {
        "type": "int",
        "description": "通道"
    },
    "cmd": {
        "type": "string",
        "description": "操作指令"
    }
},
                "required": ["others", "others.LoadAndStart", "others.OperatingMode", "others.UnfinishedContinue", "others.channel", "cmd"]
            }
        },
        {
            "name": "pre_start_pyrolyzer",
            "description": "开始裂解前处理",
            "parameters": {
                "type": "object",
                "properties": {
    "others": {
        "type": "array",
        "description": "开始裂解",
        "properties": {
            "id": {
                "type": "int",
                "description": "主键"
            },
            "modelName": {
                "type": "string",
                "description": "裂解模板名称"
            },
            "channel": {
                "type": "int",
                "description": "通道"
            }
        },
        "required": [
            "channel"
        ]
    },
    "others.id": {
        "type": "int",
        "description": "主键"
    },
    "others.modelName": {
        "type": "string",
        "description": "裂解模板名称"
    },
    "others.channel": {
        "type": "int",
        "description": "通道"
    },
    "cmd": {
        "type": "string",
        "description": "操作指令"
    }
},
                "required": ["others.channel", "cmd"]
            }
        },
        {
            "name": "test_cmd",
            "description": "测试指令",
            "parameters": {
                "type": "object",
                "properties": {
    "count": {
        "type": "int",
        "description": "count"
    }
},
                "required": ["count"]
            }
        }
                    ]
                }
            }
        }
    }
    print(json.dumps(adv_message, ensure_ascii=False), flush=True)
    print(f"--- [spps_workstation_Server] 固相多肽工作站 is ready. ---", file=sys.stderr, flush=True)


if __name__ == "__main__":
    # 启动流程：先广播能力，再进入主循环
    spps_workstation_server_advertise_capabilities()
    spps_workstation_server_main_loop()
