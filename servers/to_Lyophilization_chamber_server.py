import sys
import json
# 动态导入当前设备对应的工具类（与主服务器文件同目录）
from tools.to_Lyophilization_chamber_server_tools import ActionServerTools


# 创建全局工具管理器实例
tool_manager = ActionServerTools()


# --- 定义设备动作函数（自动生成，与工具类方法对应）---
def tool_to_Lyophilization_chamber(**params):
    return tool_manager.tool_to_Lyophilization_chamber(**params)


def tool_from_liquid_chromatography_to_liquid_nitorgen(**params):
    return tool_manager.tool_from_liquid_chromatography_to_liquid_nitorgen(**params)


def tool_start_Liquid_N(**params):
    return tool_manager.tool_start_Liquid_N(**params)


def tool_stop_Lyophilization_chamber(**params):
    return tool_manager.tool_stop_Lyophilization_chamber(**params)



AVAILABLE_TOOLS_ACTION = {
    "to_Lyophilization_chamber": tool_to_Lyophilization_chamber,
    "from_liquid_chromatography_to_liquid_nitorgen": tool_from_liquid_chromatography_to_liquid_nitorgen,
    "start_Liquid_N": tool_start_Liquid_N,
    "stop_Lyophilization_chamber": tool_stop_Lyophilization_chamber
}


# --- MCP协议通信主逻辑（自动适配当前设备）---
def to_Lyophilization_chamber_server_main_loop():
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
            print(f"--- [to_Lyophilization_chamber_Server] Critical Error: {str(e)} ---", file=sys.stderr, flush=True)


def to_Lyophilization_chamber_server_advertise_capabilities():
    """广播当前设备的MCP能力（设备信息、支持的动作）"""
    adv_message = {
        "jsonrpc": "2.0",
        "method": "protocol/advertise",
        "params": {
            "type": "server",
            "server": {
                "protocolVersion": "0.1.0",
                "displayName": "冷冻干燥工作站",
                "capabilities": {
                    "tools": [
        {
            "name": "to_Lyophilization_chamber",
            "description": "将num个瓶子转移至冻干仓并启动冻干",
            "parameters": {
                "type": "object",
                "properties": {
    "data": {
        "type": "string",
        "description": "data"
    },
    "num": {
        "type": "int",
        "description": "num"
    },
    "temp": {
        "type": "int",
        "description": "temp"
    }
},
                "required": ["data", "num", "temp"]
            }
        },
        {
            "name": "from_liquid_chromatography_to_liquid_nitorgen",
            "description": "质谱仪运行出结果后，从液相色谱仪纯化后的第几号瓶子转移到液氮盆",
            "parameters": {
                "type": "object",
                "properties": {
    "data": {
        "type": "string",
        "description": "data"
    },
    "num_Lc": {
        "type": "int",
        "description": "num_Lc"
    },
    "temp": {
        "type": "int",
        "description": "temp"
    },
    "num_Liquid_N": {
        "type": "int",
        "description": "num_Liquid_N"
    }
},
                "required": ["data", "temp"]
            }
        },
        {
            "name": "start_Liquid_N",
            "description": "启动液氮冷冻并冷冻5分钟",
            "parameters": {
                "type": "object",
                "properties": {
    "data": {
        "type": "string",
        "description": "data"
    },
    "time": {
        "type": "int",
        "description": "time"
    },
    "temp": {
        "type": "int",
        "description": "temp"
    }
},
                "required": ["data", "time", "temp"]
            }
        },
        {
            "name": "stop_Lyophilization_chamber",
            "description": "停止冻干并将num个瓶子从冷冻仓转移至存储试管架",
            "parameters": {
                "type": "object",
                "properties": {
    "data": {
        "type": "string",
        "description": "data"
    },
    "num": {
        "type": "int",
        "description": "num"
    },
    "temp": {
        "type": "int",
        "description": "temp"
    },
    "ml": {
        "type": "int",
        "description": "ml"
    },
    "time": {
        "type": "int",
        "description": "time"
    }
},
                "required": ["data", "num", "temp", "ml", "time"]
            }
        }
                    ]
                }
            }
        }
    }
    print(json.dumps(adv_message, ensure_ascii=False), flush=True)
    print(f"--- [to_Lyophilization_chamber_Server] 冷冻干燥工作站 is ready. ---", file=sys.stderr, flush=True)


if __name__ == "__main__":
    # 启动流程：先广播能力，再进入主循环
    to_Lyophilization_chamber_server_advertise_capabilities()
    to_Lyophilization_chamber_server_main_loop()
