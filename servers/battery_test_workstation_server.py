import sys
import json
# 动态导入当前设备对应的工具类（与主服务器文件同目录）
from tools.battery_test_workstation_server_tools import ActionServerTools


# 创建全局工具管理器实例
tool_manager = ActionServerTools()


# --- 定义设备动作函数（自动生成，与工具类方法对应）---
def tool_open_door(**params):
    return tool_manager.tool_open_door(**params)


def tool_close_door(**params):
    return tool_manager.tool_close_door(**params)


def tool_start_with_file(**params):
    return tool_manager.tool_start_with_file(**params)



AVAILABLE_TOOLS_ACTION = {
    "open-door": tool_open_door,
    "close-door": tool_close_door,
    "start_with_file": tool_start_with_file
}


# --- MCP协议通信主逻辑（自动适配当前设备）---
def battery_test_workstation_server_main_loop():
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
            print(f"--- [battery_test_workstation_Server] Critical Error: {str(e)} ---", file=sys.stderr, flush=True)


def battery_test_workstation_server_advertise_capabilities():
    """广播当前设备的MCP能力（设备信息、支持的动作）"""
    adv_message = {
        "jsonrpc": "2.0",
        "method": "protocol/advertise",
        "params": {
            "type": "server",
            "server": {
                "protocolVersion": "0.1.0",
                "displayName": "BTS测试工作站",
                "capabilities": {
                    "tools": [
        {
            "name": "open-door",
            "description": "开门",
            "parameters": {
                "type": "object",
                "properties": {
    "operation": {
        "type": "int",
        "description": "参数 operation"
    }
},
                "required": ["operation"]
            }
        },
        {
            "name": "close-door",
            "description": "关门",
            "parameters": {
                "type": "object",
                "properties": {
    "operation": {
        "type": "int",
        "description": "参数 operation"
    }
},
                "required": ["operation"]
            }
        },
        {
            "name": "start_with_file",
            "description": "通道控制-工步下拉选",
            "parameters": {
                "type": "object",
                "properties": {
    "battery_test_info": {
        "type": "array",
        "description": "电池测试工步",
        "properties": {
            "startNo": {
                "type": "int",
                "description": "起始电池编号"
            },
            "endNo": {
                "type": "int",
                "description": "截止电池编号"
            },
            "path": {
                "type": "string",
                "description": "工步路径"
            },
            "name": {
                "type": "string",
                "description": "工步名称"
            }
        },
        "required": [
            "startNo",
            "endNo"
        ]
    },
    "battery_test_info.startNo": {
        "type": "int",
        "description": "起始电池编号"
    },
    "battery_test_info.endNo": {
        "type": "int",
        "description": "截止电池编号"
    },
    "battery_test_info.path": {
        "type": "string",
        "description": "工步路径"
    },
    "battery_test_info.name": {
        "type": "string",
        "description": "工步名称"
    },
    "resultCode": {
        "type": "file",
        "description": "resultCode"
    }
},
                "required": ["battery_test_info", "battery_test_info.startNo", "battery_test_info.endNo"]
            }
        }
                    ]
                }
            }
        }
    }
    print(json.dumps(adv_message, ensure_ascii=False), flush=True)
    print(f"--- [battery_test_workstation_Server] BTS测试工作站 is ready. ---", file=sys.stderr, flush=True)


if __name__ == "__main__":
    # 启动流程：先广播能力，再进入主循环
    battery_test_workstation_server_advertise_capabilities()
    battery_test_workstation_server_main_loop()
