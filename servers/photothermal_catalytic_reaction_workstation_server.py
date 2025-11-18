import sys
import json
# 动态导入当前设备对应的工具类（与主服务器文件同目录）
from photothermal_catalytic_reaction_workstation_server_tools import ActionServerTools


# 创建全局工具管理器实例
tool_manager = ActionServerTools()


# --- 定义设备动作函数（自动生成，与工具类方法对应）---
def tool_R_axis_rotation(**params):
    return tool_manager.tool_R_axis_rotation(**params)


def tool_start(**params):
    return tool_manager.tool_start(**params)


def tool_stop(**params):
    return tool_manager.tool_stop(**params)


def tool_R_axis_init(**params):
    return tool_manager.tool_R_axis_init(**params)


def tool_start_gas_monitoring(**params):
    return tool_manager.tool_start_gas_monitoring(**params)


def tool_start_three_channel_gas(**params):
    return tool_manager.tool_start_three_channel_gas(**params)


def tool_start_xenon_lamp(**params):
    return tool_manager.tool_start_xenon_lamp(**params)


def tool_start_temp_controller(**params):
    return tool_manager.tool_start_temp_controller(**params)


def tool_param_test(**params):
    return tool_manager.tool_param_test(**params)


def tool_no_param(**params):
    return tool_manager.tool_no_param(**params)



AVAILABLE_TOOLS_ACTION = {
    "R_axis_rotation": tool_R_axis_rotation,
    "start": tool_start,
    "stop": tool_stop,
    "R_axis_init": tool_R_axis_init,
    "start_gas_monitoring": tool_start_gas_monitoring,
    "start_three_channel_gas": tool_start_three_channel_gas,
    "start_xenon_lamp": tool_start_xenon_lamp,
    "start_temp_controller": tool_start_temp_controller,
    "param_test": tool_param_test,
    "no_param": tool_no_param
}


# --- MCP协议通信主逻辑（自动适配当前设备）---
def photothermal_catalytic_reaction_workstation_server_main_loop():
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
            print(f"--- [photothermal_catalytic_reaction_workstation_Server] Critical Error: {str(e)} ---", file=sys.stderr, flush=True)


def photothermal_catalytic_reaction_workstation_server_advertise_capabilities():
    """广播当前设备的MCP能力（设备信息、支持的动作）"""
    adv_message = {
        "jsonrpc": "2.0",
        "method": "protocol/advertise",
        "params": {
            "type": "server",
            "server": {
                "protocolVersion": "0.1.0",
                "displayName": "光热催化反应工作站",
                "capabilities": {
                    "tools": [
        {
            "name": "R_axis_rotation",
            "description": "R轴转动",
            "parameters": {
                "type": "object",
                "properties": {
    "operation": {
        "type": "string",
        "description": "操作符"
    },
    "value": {
        "type": "int",
        "description": "旋转角度（单位：度）",
        "minimum": "0",
        "maximum": "180"
    }
},
                "required": ["operation", "value"]
            }
        },
        {
            "name": "start",
            "description": "开始光热催化",
            "parameters": {
                "type": "object",
                "properties": {
    "operation": {
        "type": "string",
        "description": "操作符"
    },
    "init_temp": {
        "type": "int",
        "description": "起始温度（单位：摄氏度）"
    },
    "time": {
        "type": "int",
        "description": "升温时间（单位：秒）"
    },
    "final_temp": {
        "type": "int",
        "description": "终止温度（单位：摄氏度）"
    },
    "set_ac": {
        "type": "int",
        "description": "设置电流（单位：安培）"
    },
    "set_channel_1": {
        "type": "int",
        "description": "设置气体通道1流量（单位：毫升每分钟）",
        "minimum": "2",
        "maximum": "200"
    },
    "set_channel_2": {
        "type": "int",
        "description": "设置气体通道2流量（单位：毫升每分钟）",
        "minimum": "2",
        "maximum": "200"
    },
    "set_channel_3": {
        "type": "int",
        "description": "设置气体通道3流量（单位：毫升每分钟）",
        "minimum": "2",
        "maximum": "200"
    },
    "set_light_distance": {
        "type": "int",
        "description": "设置光源高度"
    }
},
                "required": ["operation", "init_temp", "time", "final_temp", "set_ac"]
            }
        },
        {
            "name": "stop",
            "description": "关闭所有仪器",
            "parameters": {
                "type": "object",
                "properties": {
    "operation": {
        "type": "string",
        "description": "操作符"
    },
    "resultCode": {
        "type": "file",
        "description": "resultCode"
    }
},
                "required": ["operation", "resultCode"]
            }
        },
        {
            "name": "R_axis_init",
            "description": "R轴回零",
            "parameters": {
                "type": "object",
                "properties": {
    "operation": {
        "type": "string",
        "description": "操作符"
    },
    "value": {
        "type": "int",
        "description": "旋转角度（单位：度）"
    }
},
                "required": ["operation", "value"]
            }
        },
        {
            "name": "start_gas_monitoring",
            "description": "开启气体检测",
            "parameters": {
                "type": "object",
                "properties": {
    "operation": {
        "type": "string",
        "description": "操作符"
    },
    "value": {
        "type": "int",
        "description": "漏气流量值"
    }
},
                "required": ["operation", "value"]
            }
        },
        {
            "name": "start_three_channel_gas",
            "description": "开始通气",
            "parameters": {
                "type": "object",
                "properties": {
    "operation": {
        "type": "string",
        "description": "操作符"
    },
    "set_channel_1": {
        "type": "int",
        "description": "设置气体通道1流量",
        "minimum": "2",
        "maximum": "200"
    },
    "set_channel_2": {
        "type": "int",
        "description": "设置气体通道2流量",
        "minimum": "2",
        "maximum": "200"
    },
    "set_channel_3": {
        "type": "int",
        "description": "设置气体通道3流量",
        "minimum": "2",
        "maximum": "200"
    }
},
                "required": ["operation", "set_channel_1", "set_channel_2", "set_channel_3"]
            }
        },
        {
            "name": "start_xenon_lamp",
            "description": "开启氙灯",
            "parameters": {
                "type": "object",
                "properties": {
    "operation": {
        "type": "string",
        "description": "操作符"
    },
    "current": {
        "type": "int",
        "description": "电流（单位：安培）"
    }
},
                "required": ["operation", "current"]
            }
        },
        {
            "name": "start_temp_controller",
            "description": "开启温控仪",
            "parameters": {
                "type": "object",
                "properties": {
    "operation": {
        "type": "string",
        "description": "操作符"
    },
    "init_temp": {
        "type": "int",
        "description": "起始温度（单位：摄氏度）"
    },
    "time": {
        "type": "int",
        "description": "升温时间（单位：分钟）"
    },
    "target_temp": {
        "type": "int",
        "description": "目标温度（单位：摄氏度）"
    }
},
                "required": ["operation", "init_temp", "time", "target_temp"]
            }
        },
        {
            "name": "param_test",
            "description": "测试参数设置",
            "parameters": {
                "type": "object",
                "properties": {
    "others": {
        "type": "array",
        "description": "指令",
        "properties": {
            "initTemp": {
                "type": "float",
                "description": "初始温度"
            },
            "itemList": {
                "type": "array",
                "description": "温度参数",
                "properties": {
                    "itemList.temp": {
                        "type": "float",
                        "description": "目标温度"
                    },
                    "itemList.time": {
                        "type": "float",
                        "description": "升温时间"
                    }
                },
                "required": [
                    "itemList.temp",
                    "itemList.time"
                ]
            },
            "itemList.temp": {
                "type": "float",
                "description": "目标温度"
            },
            "itemList.time": {
                "type": "float",
                "description": "升温时间"
            }
        },
        "required": [
            "initTemp",
            "itemList",
            "itemList.temp",
            "itemList.time"
        ]
    },
    "others.initTemp": {
        "type": "float",
        "description": "初始温度"
    },
    "others.itemList": {
        "type": "array",
        "description": "温度参数",
        "properties": {
            "itemList.temp": {
                "type": "float",
                "description": "目标温度"
            },
            "itemList.time": {
                "type": "float",
                "description": "升温时间"
            }
        },
        "required": [
            "itemList.temp",
            "itemList.time"
        ]
    },
    "others.itemList.temp": {
        "type": "float",
        "description": "目标温度"
    },
    "others.itemList.time": {
        "type": "float",
        "description": "升温时间"
    }
},
                "required": ["others.initTemp", "others.itemList", "others.itemList.temp", "others.itemList.time"]
            }
        },
        {
            "name": "no_param",
            "description": "无参数测试",
            "parameters": {
                "type": "object",
                "properties": {
    "MicExpParam": {
        "type": "object",
        "description": "MicExpParam",
        "properties": {
            "ReactantOptions": {
                "type": "object",
                "description": "ReactantOptions",
                "properties": {
                    "ReactantOptions.Polarity": {
                        "type": "int",
                        "description": "Polarity",
                        "enum": [
                            {
                                "label": "极性强",
                                "value": 0
                            },
                            {
                                "label": "极性中",
                                "value": 1
                            },
                            {
                                "label": "极性弱",
                                "value": 2
                            }
                        ]
                    },
                    "ReactantOptions.Capacity": {
                        "type": "int",
                        "description": "Capacity",
                        "enum": [
                            {
                                "label": "容量小于10ml",
                                "value": 0
                            },
                            {
                                "label": "容量 10-30ml",
                                "value": 1
                            },
                            {
                                "label": "容量大于 30ml",
                                "value": 2
                            }
                        ]
                    }
                },
                "required": [
                    "ReactantOptions.Polarity",
                    "ReactantOptions.Capacity"
                ]
            },
            "ReactantOptions.Polarity": {
                "type": "int",
                "description": "Polarity",
                "enum": [
                    {
                        "label": "极性强",
                        "value": 0
                    },
                    {
                        "label": "极性中",
                        "value": 1
                    },
                    {
                        "label": "极性弱",
                        "value": 2
                    }
                ]
            },
            "ReactantOptions.Capacity": {
                "type": "int",
                "description": "Capacity",
                "enum": [
                    {
                        "label": "容量小于10ml",
                        "value": 0
                    },
                    {
                        "label": "容量 10-30ml",
                        "value": 1
                    },
                    {
                        "label": "容量大于 30ml",
                        "value": 2
                    }
                ]
            },
            "Stages": {
                "type": "array",
                "description": "Stages",
                "properties": {
                    "Stages.TargetTemperature": {
                        "type": "int",
                        "description": "TargetTemperature"
                    },
                    "Stages.MaxPressure": {
                        "type": "int",
                        "description": "MaxPressure"
                    }
                },
                "required": [
                    "Stages.TargetTemperature",
                    "Stages.MaxPressure"
                ]
            },
            "Stages.TargetTemperature": {
                "type": "int",
                "description": "TargetTemperature"
            },
            "Stages.MaxPressure": {
                "type": "int",
                "description": "MaxPressure"
            }
        },
        "required": [
            "ReactantOptions",
            "ReactantOptions.Polarity",
            "ReactantOptions.Capacity",
            "Stages",
            "Stages.TargetTemperature",
            "Stages.MaxPressure"
        ]
    },
    "MicExpParam.ReactantOptions": {
        "type": "object",
        "description": "ReactantOptions",
        "properties": {
            "ReactantOptions.Polarity": {
                "type": "int",
                "description": "Polarity",
                "enum": [
                    {
                        "label": "极性强",
                        "value": 0
                    },
                    {
                        "label": "极性中",
                        "value": 1
                    },
                    {
                        "label": "极性弱",
                        "value": 2
                    }
                ]
            },
            "ReactantOptions.Capacity": {
                "type": "int",
                "description": "Capacity",
                "enum": [
                    {
                        "label": "容量小于10ml",
                        "value": 0
                    },
                    {
                        "label": "容量 10-30ml",
                        "value": 1
                    },
                    {
                        "label": "容量大于 30ml",
                        "value": 2
                    }
                ]
            }
        },
        "required": [
            "ReactantOptions.Polarity",
            "ReactantOptions.Capacity"
        ]
    },
    "MicExpParam.ReactantOptions.Polarity": {
        "type": "int",
        "description": "Polarity",
        "enum": [
            {
                "label": "极性强",
                "value": 0
            },
            {
                "label": "极性中",
                "value": 1
            },
            {
                "label": "极性弱",
                "value": 2
            }
        ]
    },
    "MicExpParam.ReactantOptions.Capacity": {
        "type": "int",
        "description": "Capacity",
        "enum": [
            {
                "label": "容量小于10ml",
                "value": 0
            },
            {
                "label": "容量 10-30ml",
                "value": 1
            },
            {
                "label": "容量大于 30ml",
                "value": 2
            }
        ]
    },
    "MicExpParam.Stages": {
        "type": "array",
        "description": "Stages",
        "properties": {
            "Stages.TargetTemperature": {
                "type": "int",
                "description": "TargetTemperature"
            },
            "Stages.MaxPressure": {
                "type": "int",
                "description": "MaxPressure"
            }
        },
        "required": [
            "Stages.TargetTemperature",
            "Stages.MaxPressure"
        ]
    },
    "MicExpParam.Stages.TargetTemperature": {
        "type": "int",
        "description": "TargetTemperature"
    },
    "MicExpParam.Stages.MaxPressure": {
        "type": "int",
        "description": "MaxPressure"
    }
},
                "required": ["MicExpParam", "MicExpParam.ReactantOptions", "MicExpParam.ReactantOptions.Polarity", "MicExpParam.ReactantOptions.Capacity", "MicExpParam.Stages", "MicExpParam.Stages.TargetTemperature", "MicExpParam.Stages.MaxPressure"]
            }
        }
                    ]
                }
            }
        }
    }
    print(json.dumps(adv_message, ensure_ascii=False), flush=True)
    print(f"--- [photothermal_catalytic_reaction_workstation_Server] 光热催化反应工作站 is ready. ---", file=sys.stderr, flush=True)


if __name__ == "__main__":
    # 启动流程：先广播能力，再进入主循环
    photothermal_catalytic_reaction_workstation_server_advertise_capabilities()
    photothermal_catalytic_reaction_workstation_server_main_loop()
