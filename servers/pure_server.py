import sys
import json
# 动态导入当前设备对应的工具类（与主服务器文件同目录）
from pure_server_tools import ActionServerTools


# 创建全局工具管理器实例
tool_manager = ActionServerTools()


# --- 定义设备动作函数（自动生成，与工具类方法对应）---
def tool_open_door(**params):
    return tool_manager.tool_open_door(**params)


def tool_close_door(**params):
    return tool_manager.tool_close_door(**params)


def tool_start(**params):
    return tool_manager.tool_start(**params)



AVAILABLE_TOOLS_ACTION = {
    "open-door": tool_open_door,
    "close-door": tool_close_door,
    "start": tool_start
}


# --- MCP协议通信主逻辑（自动适配当前设备）---
def pure_server_main_loop():
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
            print(f"--- [pure_Server] Critical Error: {str(e)} ---", file=sys.stderr, flush=True)


def pure_server_advertise_capabilities():
    """广播当前设备的MCP能力（设备信息、支持的动作）"""
    adv_message = {
        "jsonrpc": "2.0",
        "method": "protocol/advertise",
        "params": {
            "type": "server",
            "server": {
                "protocolVersion": "0.1.0",
                "displayName": "纯化工作站",
                "capabilities": {
                    "tools": [
        {
            "name": "open-door",
            "description": "开门",
            "parameters": {
                "type": "object",
                "properties": {
    "operate": {
        "type": "string",
        "description": "操作"
    }
},
                "required": ["operate"]
            }
        },
        {
            "name": "close-door",
            "description": "关门",
            "parameters": {
                "type": "object",
                "properties": {
    "operate": {
        "type": "string",
        "description": "操作"
    }
},
                "required": ["operate"]
            }
        },
        {
            "name": "start",
            "description": "开始",
            "parameters": {
                "type": "object",
                "properties": {
    "operate": {
        "type": "string",
        "description": "操作"
    },
    "program": {
        "type": "int",
        "description": "方案",
        "enum": [
            {
                "label": "留液",
                "value": 1
            },
            {
                "label": "留固",
                "value": 2
            },
            {
                "label": "留固液",
                "value": 3
            }
        ]
    },
    "time": {
        "type": "int",
        "description": "时间（单位：分钟）",
        "minimum": "1",
        "maximum": "99"
    },
    "speed": {
        "type": "int",
        "description": "速度",
        "minimum": "0",
        "maximum": "12000"
    },
    "cleanNum": {
        "type": "int",
        "description": "清洗次数",
        "minimum": "1",
        "maximum": "10"
    },
    "washSolutions": {
        "type": "array",
        "description": "清洗液设置",
        "properties": {
            "washSolution": {
                "type": "int",
                "description": "清洗液",
                "enum": [
                    {
                        "label": "水",
                        "value": 1
                    },
                    {
                        "label": "酒精",
                        "value": 2
                    },
                    {
                        "label": "双氧水",
                        "value": 3
                    }
                ]
            }
        },
        "required": [
            "washSolution"
        ]
    },
    "washSolutions.washSolution": {
        "type": "int",
        "description": "清洗液",
        "enum": [
            {
                "label": "水",
                "value": 1
            },
            {
                "label": "酒精",
                "value": 2
            },
            {
                "label": "双氧水",
                "value": 3
            }
        ]
    },
    "autoStatus": {
        "type": "int",
        "description": "自动设置加液状态",
        "enum": [
            {
                "label": "是",
                "value": 0
            },
            {
                "label": "否",
                "value": 1
            }
        ]
    },
    "addLiquidNum": {
        "type": "int",
        "description": "手动设置加液量（单位：毫升）",
        "minimum": "1",
        "maximum": "50"
    },
    "isLeaveWashSolution": {
        "type": "int",
        "description": "是否保留清洗液",
        "enum": [
            {
                "label": "是",
                "value": 1
            },
            {
                "label": "否",
                "value": 0
            }
        ]
    },
    "leaveParam": {
        "type": "object",
        "description": "保留清洗液参数",
        "properties": {
            "leaveLiquidAmount": {
                "type": "int",
                "description": "保留清洗液数量（单位：毫升）",
                "minimum": "1",
                "maximum": "50"
            },
            "washSolution": {
                "type": "int",
                "description": "清洗液",
                "enum": [
                    {
                        "label": "水",
                        "value": 1
                    },
                    {
                        "label": "酒精",
                        "value": 2
                    },
                    {
                        "label": "双氧水",
                        "value": 3
                    }
                ]
            }
        }
    },
    "leaveParam.leaveLiquidAmount": {
        "type": "int",
        "description": "保留清洗液数量（单位：毫升）",
        "minimum": "1",
        "maximum": "50"
    },
    "leaveParam.washSolution": {
        "type": "int",
        "description": "清洗液",
        "enum": [
            {
                "label": "水",
                "value": 1
            },
            {
                "label": "酒精",
                "value": 2
            },
            {
                "label": "双氧水",
                "value": 3
            }
        ]
    }
},
                "required": ["operate", "program", "time", "speed", "cleanNum", "washSolutions", "washSolutions.washSolution", "autoStatus", "isLeaveWashSolution"]
            }
        }
                    ]
                }
            }
        }
    }
    print(json.dumps(adv_message, ensure_ascii=False), flush=True)
    print(f"--- [pure_Server] 纯化工作站 is ready. ---", file=sys.stderr, flush=True)


if __name__ == "__main__":
    # 启动流程：先广播能力，再进入主循环
    pure_server_advertise_capabilities()
    pure_server_main_loop()
