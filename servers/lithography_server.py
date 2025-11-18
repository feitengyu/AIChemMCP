import sys
import json
# 动态导入当前设备对应的工具类（与主服务器文件同目录）
from lithography_server_tools import ActionServerTools


# 创建全局工具管理器实例
tool_manager = ActionServerTools()


# --- 定义设备动作函数（自动生成，与工具类方法对应）---
def tool_init_communication(**params):
    return tool_manager.tool_init_communication(**params)


def tool_laser_on(**params):
    return tool_manager.tool_laser_on(**params)


def tool_take_samples(**params):
    return tool_manager.tool_take_samples(**params)


def tool_open_vacuum_cupule(**params):
    return tool_manager.tool_open_vacuum_cupule(**params)


def tool_close_vacuum_cupule(**params):
    return tool_manager.tool_close_vacuum_cupule(**params)


def tool_open_camera(**params):
    return tool_manager.tool_open_camera(**params)


def tool_pos_light(**params):
    return tool_manager.tool_pos_light(**params)


def tool_raise_stage(**params):
    return tool_manager.tool_raise_stage(**params)


def tool_interface_detect(**params):
    return tool_manager.tool_interface_detect(**params)


def tool_load_samples(**params):
    return tool_manager.tool_load_samples(**params)


def tool_start_lithography(**params):
    return tool_manager.tool_start_lithography(**params)


def tool_down_stage(**params):
    return tool_manager.tool_down_stage(**params)


def tool_neg_light(**params):
    return tool_manager.tool_neg_light(**params)


def tool_close_camera(**params):
    return tool_manager.tool_close_camera(**params)


def tool_close_door(**params):
    return tool_manager.tool_close_door(**params)


def tool_open_door(**params):
    return tool_manager.tool_open_door(**params)



AVAILABLE_TOOLS_ACTION = {
    "init_communication": tool_init_communication,
    "laser_on": tool_laser_on,
    "take_samples": tool_take_samples,
    "open_vacuum_cupule": tool_open_vacuum_cupule,
    "close_vacuum_cupule": tool_close_vacuum_cupule,
    "open_camera": tool_open_camera,
    "pos_light": tool_pos_light,
    "raise_stage": tool_raise_stage,
    "interface_detect": tool_interface_detect,
    "load_samples": tool_load_samples,
    "start_lithography": tool_start_lithography,
    "down_stage": tool_down_stage,
    "neg_light": tool_neg_light,
    "close_camera": tool_close_camera,
    "close_door": tool_close_door,
    "open_door": tool_open_door
}


# --- MCP协议通信主逻辑（自动适配当前设备）---
def lithography_server_main_loop():
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
            print(f"--- [lithography_Server] Critical Error: {str(e)} ---", file=sys.stderr, flush=True)


def lithography_server_advertise_capabilities():
    """广播当前设备的MCP能力（设备信息、支持的动作）"""
    adv_message = {
        "jsonrpc": "2.0",
        "method": "protocol/advertise",
        "params": {
            "type": "server",
            "server": {
                "protocolVersion": "0.1.0",
                "displayName": "光刻工作站",
                "capabilities": {
                    "tools": [
        {
            "name": "init_communication",
            "description": "选择通信串口",
            "parameters": {
                "type": "object",
                "properties": {
    "operation": {
        "type": "string",
        "description": "操作指令"
    },
    "serial": {
        "type": "string",
        "description": "通信串口"
    }
},
                "required": ["operation", "serial"]
            }
        },
        {
            "name": "laser_on",
            "description": "出光",
            "parameters": {
                "type": "object",
                "properties": {
    "operation": {
        "type": "string",
        "description": "操作指令"
    },
    "laser_power": {
        "type": "float",
        "description": "出光功率",
        "minimum": "0",
        "maximum": "100"
    }
},
                "required": ["operation", "laser_power"]
            }
        },
        {
            "name": "take_samples",
            "description": "取出样品",
            "parameters": {
                "type": "object",
                "properties": {
    "operation": {
        "type": "string",
        "description": "操作指令"
    },
    "x_to": {
        "type": "float",
        "description": "x取值（mm）",
        "minimum": "-100",
        "maximum": "100"
    },
    "y_to": {
        "type": "float",
        "description": "y取值（mm）",
        "minimum": "-100",
        "maximum": "100"
    },
    "z_move": {
        "type": "float",
        "description": "z取值（mm）",
        "minimum": "-4.9",
        "maximum": "4.9"
    }
},
                "required": ["operation", "x_to", "y_to", "z_move"]
            }
        },
        {
            "name": "open_vacuum_cupule",
            "description": "打开真空吸盘",
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
            "name": "close_vacuum_cupule",
            "description": "关闭真空吸盘",
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
            "name": "open_camera",
            "description": "开启相机",
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
            "name": "pos_light",
            "description": "设置投射照明值",
            "parameters": {
                "type": "object",
                "properties": {
    "operation": {
        "type": "string",
        "description": "操作指令"
    },
    "pos_value": {
        "type": "int",
        "description": "照明值",
        "minimum": "0",
        "maximum": "99"
    }
},
                "required": ["operation", "pos_value"]
            }
        },
        {
            "name": "raise_stage",
            "description": "抬升样品",
            "parameters": {
                "type": "object",
                "properties": {
    "operation": {
        "type": "string",
        "description": "操作指令"
    },
    "distance": {
        "type": "int",
        "description": "抬升距离（um）",
        "minimum": "0",
        "maximum": "3000"
    }
},
                "required": ["operation", "distance"]
            }
        },
        {
            "name": "interface_detect",
            "description": "界面探测",
            "parameters": {
                "type": "object",
                "properties": {
    "operation": {
        "type": "string",
        "description": "操作指令"
    },
    "method_name": {
        "type": "string",
        "description": "方法名称"
    },
    "start_position": {
        "type": "float",
        "description": "起始位置（um）",
        "minimum": "1",
        "maximum": "1000"
    },
    "z_range": {
        "type": "float",
        "description": "z轴范围（um）",
        "minimum": "2",
        "maximum": "1000"
    },
    "z_step": {
        "type": "float",
        "description": "步进（um）",
        "minimum": "-1",
        "maximum": "5"
    },
    "wait_time": {
        "type": "int",
        "description": "等待时间（ms）",
        "minimum": "2",
        "maximum": "500"
    },
    "device_type": {
        "type": "int",
        "description": "探测设备",
        "enum": [
            {
                "label": "PZ",
                "value": 0
            },
            {
                "label": "Z",
                "value": 1
            }
        ]
    },
    "auto_light": {
        "type": "int",
        "description": "是否自动开启灯光",
        "enum": [
            {
                "label": "否",
                "value": 0
            },
            {
                "label": "是",
                "value": 1
            }
        ]
    },
    "detect_shape": {
        "type": "int",
        "description": "探测形状",
        "enum": [
            {
                "label": "cross",
                "value": 0
            },
            {
                "label": "circle",
                "value": 1
            },
            {
                "label": "square",
                "value": 2
            }
        ]
    },
    "radius": {
        "type": "float",
        "description": "范围（um）",
        "minimum": "1",
        "maximum": "90000"
    },
    "fit_core": {
        "type": "int",
        "description": "计算核心",
        "enum": [
            {
                "label": "Gaussion",
                "value": 0
            },
            {
                "label": "Sigmoid",
                "value": 1
            }
        ]
    },
    "detect_points_num": {
        "type": "int",
        "description": "探测点个数",
        "enum": [
            {
                "label": "3",
                "value": 3
            },
            {
                "label": "5",
                "value": 5
            },
            {
                "label": "7",
                "value": 7
            },
            {
                "label": "9",
                "value": 9
            }
        ]
    },
    "kx": {
        "type": "float",
        "description": "调平参数x",
        "minimum": "-10",
        "maximum": "10"
    },
    "ky": {
        "type": "float",
        "description": "调平参数y",
        "minimum": "-10",
        "maximum": "10"
    },
    "win_size": {
        "type": "int",
        "description": "采样范围（pixel）",
        "minimum": "2",
        "maximum": "10"
    },
    "camera_type": {
        "type": "int",
        "description": "相机类型",
        "enum": [
            {
                "label": "主相机",
                "value": 0
            },
            {
                "label": "探测相机",
                "value": 1
            },
            {
                "label": "共聚焦相机",
                "value": 2
            }
        ]
    }
},
                "required": ["operation", "method_name", "start_position", "z_range", "z_step", "wait_time", "device_type", "auto_light", "detect_shape", "radius", "fit_core", "detect_points_num", "kx", "ky", "win_size", "camera_type"]
            }
        },
        {
            "name": "load_samples",
            "description": "载入样品",
            "parameters": {
                "type": "object",
                "properties": {
    "operation": {
        "type": "string",
        "description": "操作指令"
    },
    "x_to": {
        "type": "float",
        "description": "x取值（mm）",
        "minimum": "-100",
        "maximum": "100"
    },
    "y_to": {
        "type": "float",
        "description": "y取值（mm）",
        "minimum": "-100",
        "maximum": "100"
    },
    "z_move": {
        "type": "float",
        "description": "z取值（mm）",
        "minimum": "-4.9",
        "maximum": "4.9"
    }
},
                "required": ["operation", "x_to", "y_to", "z_move"]
            }
        },
        {
            "name": "start_lithography",
            "description": "开始光刻",
            "parameters": {
                "type": "object",
                "properties": {
    "operation": {
        "type": "string",
        "description": "操作指令"
    },
    "process_script": {
        "type": "object",
        "description": "运行脚本",
        "properties": {
            "id": {
                "type": "string",
                "description": "脚本"
            }
        },
        "required": [
            "id"
        ]
    },
    "process_script.id": {
        "type": "string",
        "description": "脚本"
    },
    "matrix": {
        "type": "string",
        "description": "预设加工矩阵"
    },
    "base_speed": {
        "type": "float",
        "description": "基础加工速度"
    },
    "speed_step": {
        "type": "float",
        "description": "加工速度步进"
    },
    "base_laser_power": {
        "type": "float",
        "description": "基础激光功率"
    },
    "power_step": {
        "type": "float",
        "description": "基础激光功率步进"
    },
    "resultCode": {
        "type": "string",
        "description": "resultCode"
    }
},
                "required": ["operation", "process_script", "process_script.id", "matrix", "base_speed", "speed_step", "base_laser_power", "power_step", "resultCode"]
            }
        },
        {
            "name": "down_stage",
            "description": "下降样品台",
            "parameters": {
                "type": "object",
                "properties": {
    "operation": {
        "type": "string",
        "description": "操作指令"
    },
    "distance": {
        "type": "int",
        "description": "下降距离（um）",
        "minimum": "0",
        "maximum": "3000"
    }
},
                "required": ["operation", "distance"]
            }
        },
        {
            "name": "neg_light",
            "description": "设置反射照明值",
            "parameters": {
                "type": "object",
                "properties": {
    "operation": {
        "type": "string",
        "description": "操作指令"
    },
    "neg_value": {
        "type": "int",
        "description": "照明值",
        "minimum": "0",
        "maximum": "99"
    }
},
                "required": ["operation", "neg_value"]
            }
        },
        {
            "name": "close_camera",
            "description": "关闭相机",
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
            "name": "close_door",
            "description": "关门",
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
            "name": "open_door",
            "description": "开门",
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
        }
                    ]
                }
            }
        }
    }
    print(json.dumps(adv_message, ensure_ascii=False), flush=True)
    print(f"--- [lithography_Server] 光刻工作站 is ready. ---", file=sys.stderr, flush=True)


if __name__ == "__main__":
    # 启动流程：先广播能力，再进入主循环
    lithography_server_advertise_capabilities()
    lithography_server_main_loop()
