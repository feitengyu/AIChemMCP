import sys
import json
# 动态导入当前设备对应的工具类（与主服务器文件同目录）
from tools.dryer_server_tools import ActionServerTools


# 创建全局工具管理器实例
tool_manager = ActionServerTools()


# --- 定义设备动作函数（自动生成，与工具类方法对应）---
def tool_open_door(**params):
    return tool_manager.tool_open_door(**params)


def tool_close_door(**params):
    return tool_manager.tool_close_door(**params)


def tool_dry(**params):
    return tool_manager.tool_dry(**params)


def tool_stop(**params):
    return tool_manager.tool_stop(**params)


def tool_wait(**params):
    return tool_manager.tool_wait(**params)


def tool_pure_dry(**params):
    return tool_manager.tool_pure_dry(**params)


def tool_start_heat(**params):
    return tool_manager.tool_start_heat(**params)



AVAILABLE_TOOLS_ACTION = {
    "open-door": tool_open_door,
    "close-door": tool_close_door,
    "dry": tool_dry,
    "stop": tool_stop,
    "wait": tool_wait,
    "pure_dry": tool_pure_dry,
    "start_heat": tool_start_heat
}


# --- MCP协议通信主逻辑（自动适配当前设备）---
def dryer_server_main_loop():
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
            print(f"--- [dryer_Server] Critical Error: {str(e)} ---", file=sys.stderr, flush=True)


def dryer_server_advertise_capabilities():
    """广播当前设备的MCP能力（设备信息、支持的动作）"""
    adv_message = {
        "jsonrpc": "2.0",
        "method": "protocol/advertise",
        "params": {
            "type": "server",
            "server": {
                "protocolVersion": "0.1.0",
                "displayName": "烘干机",
                "capabilities": {
                    "tools": [
        {
            "name": "open-door",
            "description": "开门",
            "parameters": {
                "type": "object",
                "properties": {
    "value": {
        "type": "string",
        "description": "门控制"
    }
},
                "required": ["value"]
            }
        },
        {
            "name": "close-door",
            "description": "关门",
            "parameters": {
                "type": "object",
                "properties": {
    "value": {
        "type": "string",
        "description": "门控制"
    },
    "temperature": {
        "type": "string",
        "description": "恒温温度[26,210]（℃）"
    }
},
                "required": ["value"]
            }
        },
        {
            "name": "dry",
            "description": "烘干",
            "parameters": {
                "type": "object",
                "properties": {
    "temperature": {
        "type": "float",
        "description": "温度（单位：摄氏度）",
        "minimum": "26",
        "maximum": "210"
    },
    "time": {
        "type": "int",
        "description": "时间（单位：分钟）",
        "minimum": "1",
        "maximum": "14400"
    }
},
                "required": ["temperature", "time"]
            }
        },
        {
            "name": "stop",
            "description": "停止烘干",
            "parameters": {
                "type": "object",
                "properties": {},
                "required": []
            }
        },
        {
            "name": "wait",
            "description": "等待降温",
            "parameters": {
                "type": "object",
                "properties": {
    "temperature": {
        "type": "int",
        "description": "温度"
    }
},
                "required": ["temperature"]
            }
        },
        {
            "name": "pure_dry",
            "description": "静置烘干",
            "parameters": {
                "type": "object",
                "properties": {
    "time": {
        "type": "int",
        "description": "烘干时间（单位：分钟）",
        "minimum": "1",
        "maximum": "14400"
    }
},
                "required": ["time"]
            }
        },
        {
            "name": "start_heat",
            "description": "设置温度并开启加热",
            "parameters": {
                "type": "object",
                "properties": {
    "temperature": {
        "type": "float",
        "description": "温度（单位：摄氏度）",
        "minimum": "26",
        "maximum": "210"
    }
},
                "required": ["temperature"]
            }
        }
                    ]
                }
            }
        }
    }
    print(json.dumps(adv_message, ensure_ascii=False), flush=True)
    print(f"--- [dryer_Server] 烘干机 is ready. ---", file=sys.stderr, flush=True)


if __name__ == "__main__":
    # 启动流程：先广播能力，再进入主循环
    dryer_server_advertise_capabilities()
    dryer_server_main_loop()
