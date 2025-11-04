import sys
import json
# 动态导入当前设备对应的工具类（与主服务器文件同目录）
from tools.mock_station_1_server_tools import ActionServerTools


# 创建全局工具管理器实例
tool_manager = ActionServerTools()


# --- 定义设备动作函数（自动生成，与工具类方法对应）---
def tool_指令1(**params):
    return tool_manager.tool_指令1(**params)



AVAILABLE_TOOLS_ACTION = {
    "指令1": tool_指令1
}


# --- MCP协议通信主逻辑（自动适配当前设备）---
def mock_station_1_server_main_loop():
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
            print(f"--- [mock_station_1_Server] Critical Error: {str(e)} ---", file=sys.stderr, flush=True)


def mock_station_1_server_advertise_capabilities():
    """广播当前设备的MCP能力（设备信息、支持的动作）"""
    adv_message = {
        "jsonrpc": "2.0",
        "method": "protocol/advertise",
        "params": {
            "type": "server",
            "server": {
                "protocolVersion": "0.1.0",
                "displayName": "模拟工作站1",
                "capabilities": {
                    "tools": [
        {
            "name": "指令1",
            "description": "command1",
            "parameters": {
                "type": "object",
                "properties": {
    "operation": {
        "type": "string",
        "description": "指令"
    },
    "name": {
        "type": "string",
        "description": "实验名称"
    },
    "speed": {
        "type": "int",
        "description": "速度（r/min）",
        "minimum": "0",
        "maximum": "800"
    },
    "is_quick": {
        "type": "string",
        "description": "快速模式"
    },
    "phone": {
        "type": "string",
        "description": "联系方式"
    },
    "paramfile": {
        "type": "file",
        "description": "参数文件"
    },
    "time": {
        "type": "int",
        "description": "时间（s）"
    },
    "object_param": {
        "type": "object",
        "description": "对象类型参数",
        "properties": {
            "child1": {
                "type": "string",
                "description": "子参数1"
            },
            "child2": {
                "type": "float",
                "description": "子参数2"
            }
        }
    },
    "object_param.child1": {
        "type": "string",
        "description": "子参数1"
    },
    "object_param.child2": {
        "type": "float",
        "description": "子参数2"
    },
    "obj_obj": {
        "type": "object",
        "description": "对象嵌套对象",
        "properties": {
            "obj": {
                "type": "object",
                "description": "对象类型",
                "properties": {
                    "obj.param1": {
                        "type": "string",
                        "description": "嵌套参数1"
                    }
                }
            },
            "obj.param1": {
                "type": "string",
                "description": "嵌套参数1"
            }
        }
    },
    "obj_obj.obj": {
        "type": "object",
        "description": "对象类型",
        "properties": {
            "obj.param1": {
                "type": "string",
                "description": "嵌套参数1"
            }
        }
    },
    "obj_obj.obj.param1": {
        "type": "string",
        "description": "嵌套参数1"
    },
    "obj_array": {
        "type": "object",
        "description": "对象嵌套数组",
        "properties": {
            "array": {
                "type": "array",
                "description": "嵌套数组",
                "properties": {
                    "array.param1": {
                        "type": "string",
                        "description": "参数1"
                    }
                }
            },
            "array.param1": {
                "type": "string",
                "description": "参数1"
            }
        }
    },
    "obj_array.array": {
        "type": "array",
        "description": "嵌套数组",
        "properties": {
            "array.param1": {
                "type": "string",
                "description": "参数1"
            }
        }
    },
    "obj_array.array.param1": {
        "type": "string",
        "description": "参数1"
    },
    "array_param": {
        "type": "array",
        "description": "数组类型参数",
        "properties": {
            "容器编号": {
                "type": "int",
                "description": "容器编号"
            },
            "volume": {
                "type": "float",
                "description": "容量（ml）"
            }
        }
    },
    "array_param.容器编号": {
        "type": "int",
        "description": "容器编号"
    },
    "array_param.volume": {
        "type": "float",
        "description": "容量（ml）"
    },
    "array_obj": {
        "type": "array",
        "description": "数组嵌套对象",
        "properties": {
            "obj": {
                "type": "object",
                "description": "对象类型",
                "properties": {
                    "obj.param1": {
                        "type": "string",
                        "description": "嵌套参数1"
                    }
                }
            },
            "obj.param1": {
                "type": "string",
                "description": "嵌套参数1"
            }
        }
    },
    "array_obj.obj": {
        "type": "object",
        "description": "对象类型",
        "properties": {
            "obj.param1": {
                "type": "string",
                "description": "嵌套参数1"
            }
        }
    },
    "array_obj.obj.param1": {
        "type": "string",
        "description": "嵌套参数1"
    },
    "array_array": {
        "type": "array",
        "description": "电化学测试",
        "properties": {
            "volt-ampere": {
                "type": "array",
                "description": "伏安法",
                "properties": {
                    "volt-ampere.voltage": {
                        "type": "float",
                        "description": "电压（v）"
                    },
                    "volt-ampere.electricity": {
                        "type": "float",
                        "description": "电流（A）"
                    }
                }
            },
            "volt-ampere.voltage": {
                "type": "float",
                "description": "电压（v）"
            },
            "volt-ampere.electricity": {
                "type": "float",
                "description": "电流（A）"
            },
            "cyclic_voltammetry": {
                "type": "array",
                "description": "循环伏安法",
                "properties": {
                    "cyclic_voltammetry.voltage": {
                        "type": "float",
                        "description": "电压（v）"
                    },
                    "cyclic_voltammetry.electricity": {
                        "type": "float",
                        "description": "电流（A）"
                    },
                    "cyclic_voltammetry.number": {
                        "type": "int",
                        "description": "循环次数"
                    }
                }
            },
            "cyclic_voltammetry.voltage": {
                "type": "float",
                "description": "电压（v）"
            },
            "cyclic_voltammetry.electricity": {
                "type": "float",
                "description": "电流（A）"
            },
            "cyclic_voltammetry.number": {
                "type": "int",
                "description": "循环次数"
            }
        }
    },
    "array_array.volt-ampere": {
        "type": "array",
        "description": "伏安法",
        "properties": {
            "volt-ampere.voltage": {
                "type": "float",
                "description": "电压（v）"
            },
            "volt-ampere.electricity": {
                "type": "float",
                "description": "电流（A）"
            }
        }
    },
    "array_array.volt-ampere.voltage": {
        "type": "float",
        "description": "电压（v）"
    },
    "array_array.volt-ampere.electricity": {
        "type": "float",
        "description": "电流（A）"
    },
    "array_array.cyclic_voltammetry": {
        "type": "array",
        "description": "循环伏安法",
        "properties": {
            "cyclic_voltammetry.voltage": {
                "type": "float",
                "description": "电压（v）"
            },
            "cyclic_voltammetry.electricity": {
                "type": "float",
                "description": "电流（A）"
            },
            "cyclic_voltammetry.number": {
                "type": "int",
                "description": "循环次数"
            }
        }
    },
    "array_array.cyclic_voltammetry.voltage": {
        "type": "float",
        "description": "电压（v）"
    },
    "array_array.cyclic_voltammetry.electricity": {
        "type": "float",
        "description": "电流（A）"
    },
    "array_array.cyclic_voltammetry.number": {
        "type": "int",
        "description": "循环次数"
    },
    "mock_template": {
        "type": "object",
        "description": "模拟模版",
        "properties": {
            "template": {
                "type": "string",
                "description": "化学模版"
            }
        },
        "required": [
            "template"
        ]
    },
    "mock_template.template": {
        "type": "string",
        "description": "化学模版"
    }
},
                "required": ["operation", "name", "is_quick", "phone", "object_param", "mock_template.template"]
            }
        }
                    ]
                }
            }
        }
    }
    print(json.dumps(adv_message, ensure_ascii=False), flush=True)
    print(f"--- [mock_station_1_Server] 模拟工作站1 is ready. ---", file=sys.stderr, flush=True)


if __name__ == "__main__":
    # 启动流程：先广播能力，再进入主循环
    mock_station_1_server_advertise_capabilities()
    mock_station_1_server_main_loop()
