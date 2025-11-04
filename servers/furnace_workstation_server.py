import sys
import json
# 动态导入当前设备对应的工具类（与主服务器文件同目录）
from tools.furnace_workstation_server_tools import ActionServerTools


# 创建全局工具管理器实例
tool_manager = ActionServerTools()


# --- 定义设备动作函数（自动生成，与工具类方法对应）---
def tool_start(**params):
    return tool_manager.tool_start(**params)


def tool_start_new(**params):
    return tool_manager.tool_start_new(**params)



AVAILABLE_TOOLS_ACTION = {
    "start": tool_start,
    "start_new": tool_start_new
}


# --- MCP协议通信主逻辑（自动适配当前设备）---
def furnace_workstation_server_main_loop():
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
            print(f"--- [furnace_workstation_Server] Critical Error: {str(e)} ---", file=sys.stderr, flush=True)


def furnace_workstation_server_advertise_capabilities():
    """广播当前设备的MCP能力（设备信息、支持的动作）"""
    adv_message = {
        "jsonrpc": "2.0",
        "method": "protocol/advertise",
        "params": {
            "type": "server",
            "server": {
                "protocolVersion": "0.1.0",
                "displayName": "电化学-高温炉",
                "capabilities": {
                    "tools": [
        {
            "name": "start",
            "description": "流程开始",
            "parameters": {
                "type": "object",
                "properties": {
    "type": {
        "type": "string",
        "description": "仪器类型"
    },
    "cmd": {
        "type": "string",
        "description": "指令名称"
    },
    "Mode": {
        "type": "int",
        "description": "烧样模式",
        "enum": [
            {
                "label": "单点烧样",
                "value": "1"
            },
            {
                "label": "逐点烧样",
                "value": "0"
            }
        ]
    },
    "VPressure": {
        "type": "int",
        "description": "抽真空压力"
    },
    "Protected": {
        "type": "int",
        "description": "是否充保护气",
        "enum": [
            {
                "label": "是",
                "value": "1"
            },
            {
                "label": "否",
                "value": "0"
            }
        ]
    },
    "PPressure": {
        "type": "int",
        "description": "充保护气压力"
    },
    "PCount": {
        "type": "int",
        "description": "保护气循环次数"
    },
    "Row_0": {
        "type": "int",
        "description": "行号"
    },
    "Column_0": {
        "type": "int",
        "description": "列号"
    },
    "Temp_0": {
        "type": "int",
        "description": "加热温度(第1行第1列位置）"
    },
    "HeatingTime_0": {
        "type": "int",
        "description": "加热时间(第1行第1列位置）"
    },
    "CoolingTime_0": {
        "type": "int",
        "description": "冷却时间(第1行第1列位置）"
    },
    "Count_0": {
        "type": "int",
        "description": "循环次数(第1行第1列位置）"
    },
    "Row_1": {
        "type": "int",
        "description": "Row_1"
    },
    "Column_1": {
        "type": "int",
        "description": "列号"
    },
    "Temp_1": {
        "type": "int",
        "description": "加热温度(第2行第1列位置）"
    },
    "HeatingTime_1": {
        "type": "int",
        "description": "加热时间(第2行第1列位置）"
    },
    "CoolingTime_1": {
        "type": "int",
        "description": "冷却时间(第2行第1列位置）"
    },
    "Count_1": {
        "type": "int",
        "description": "循环次数(第2行第1列位置）"
    },
    "Row_2": {
        "type": "int",
        "description": "行号"
    },
    "Column_2": {
        "type": "int",
        "description": "列号"
    },
    "Temp_2": {
        "type": "int",
        "description": "加热温度(第3行第1列位置）"
    },
    "HeatingTime_2": {
        "type": "int",
        "description": "加热时间(第3行第1列位置）"
    },
    "CoolingTime_2": {
        "type": "int",
        "description": "冷却时间(第3行第1列位置）"
    },
    "Count_2": {
        "type": "int",
        "description": "循环次数(第3行第1列位置）"
    },
    "Row_3": {
        "type": "int",
        "description": "行号"
    },
    "Column_3": {
        "type": "int",
        "description": "列号"
    },
    "Temp_3": {
        "type": "int",
        "description": "加热温度(第4行第1列位置）"
    },
    "HeatingTime_3": {
        "type": "int",
        "description": "加热时间(第4行第1列位置）"
    },
    "CoolingTime_3": {
        "type": "int",
        "description": "冷却时间(第4行第1列位置）"
    },
    "Count_3": {
        "type": "int",
        "description": "循环次数(第4行第1列位置）"
    }
},
                "required": ["type", "cmd", "Mode", "VPressure", "Protected", "PPressure", "PCount", "Row_0", "Column_0", "Temp_0", "HeatingTime_0", "CoolingTime_0", "Count_0", "Row_1", "Column_1", "Temp_1", "HeatingTime_1", "CoolingTime_1", "Count_1", "Row_2", "Column_2", "Temp_2", "HeatingTime_2", "CoolingTime_2", "Count_2", "Row_3", "Column_3", "Temp_3", "HeatingTime_3", "CoolingTime_3", "Count_3"]
            }
        },
        {
            "name": "start_new",
            "description": "流程开始（只做3个位置）",
            "parameters": {
                "type": "object",
                "properties": {
    "type": {
        "type": "string",
        "description": "仪器类型"
    },
    "cmd": {
        "type": "string",
        "description": "指令名称"
    },
    "Mode": {
        "type": "int",
        "description": "烧样模式",
        "enum": [
            {
                "label": "单点烧样",
                "value": "1"
            },
            {
                "label": "逐点烧样",
                "value": "0"
            }
        ]
    },
    "VPressure": {
        "type": "int",
        "description": "抽真空压力"
    },
    "Protected": {
        "type": "int",
        "description": "是否充保护气",
        "enum": [
            {
                "label": "是",
                "value": "1"
            },
            {
                "label": "否",
                "value": "0"
            }
        ]
    },
    "PPressure": {
        "type": "int",
        "description": "充保护气压力"
    },
    "PCount": {
        "type": "int",
        "description": "保护气循环次数"
    },
    "Row_0": {
        "type": "int",
        "description": "行号"
    },
    "Column_0": {
        "type": "int",
        "description": "列号"
    },
    "Temp_0": {
        "type": "int",
        "description": "加热温度(第1行第1列位置）"
    },
    "HeatingTime_0": {
        "type": "int",
        "description": "加热时间(第1行第1列位置）"
    },
    "CoolingTime_0": {
        "type": "int",
        "description": "冷却时间(第1行第1列位置）"
    },
    "Count_0": {
        "type": "int",
        "description": "循环次数(第1行第1列位置）"
    },
    "Row_1": {
        "type": "int",
        "description": "Row_1"
    },
    "Column_1": {
        "type": "int",
        "description": "列号"
    },
    "Temp_1": {
        "type": "int",
        "description": "加热温度(第2行第1列位置）"
    },
    "HeatingTime_1": {
        "type": "int",
        "description": "加热时间(第2行第1列位置）"
    },
    "CoolingTime_1": {
        "type": "int",
        "description": "冷却时间(第2行第1列位置）"
    },
    "Count_1": {
        "type": "int",
        "description": "循环次数(第2行第1列位置）"
    },
    "Row_2": {
        "type": "int",
        "description": "行号"
    },
    "Column_2": {
        "type": "int",
        "description": "列号"
    },
    "Temp_2": {
        "type": "int",
        "description": "加热温度(第3行第1列位置）"
    },
    "HeatingTime_2": {
        "type": "int",
        "description": "加热时间(第3行第1列位置）"
    },
    "CoolingTime_2": {
        "type": "int",
        "description": "冷却时间(第3行第1列位置）"
    },
    "Count_2": {
        "type": "int",
        "description": "循环次数(第3行第1列位置）"
    }
},
                "required": ["type", "cmd", "Mode", "VPressure", "Protected", "PPressure", "PCount", "Row_0", "Column_0", "Temp_0", "HeatingTime_0", "CoolingTime_0", "Count_0", "Row_1", "Column_1", "Temp_1", "HeatingTime_1", "CoolingTime_1", "Count_1", "Row_2", "Column_2", "Temp_2", "HeatingTime_2", "CoolingTime_2", "Count_2"]
            }
        }
                    ]
                }
            }
        }
    }
    print(json.dumps(adv_message, ensure_ascii=False), flush=True)
    print(f"--- [furnace_workstation_Server] 电化学-高温炉 is ready. ---", file=sys.stderr, flush=True)


if __name__ == "__main__":
    # 启动流程：先广播能力，再进入主循环
    furnace_workstation_server_advertise_capabilities()
    furnace_workstation_server_main_loop()
