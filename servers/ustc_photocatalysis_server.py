import sys
import json
# 动态导入当前设备对应的工具类（与主服务器文件同目录）
from ustc_photocatalysis_server_tools import ActionServerTools


# 创建全局工具管理器实例
tool_manager = ActionServerTools()


# --- 定义设备动作函数（自动生成，与工具类方法对应）---
def tool_open(**params):
    return tool_manager.tool_open(**params)


def tool_time(**params):
    return tool_manager.tool_time(**params)


def tool_closeall(**params):
    return tool_manager.tool_closeall(**params)



AVAILABLE_TOOLS_ACTION = {
    "open": tool_open,
    "time": tool_time,
    "closeall": tool_closeall
}


# --- MCP协议通信主逻辑（自动适配当前设备）---
def ustc_photocatalysis_server_main_loop():
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
            print(f"--- [ustc_photocatalysis_Server] Critical Error: {str(e)} ---", file=sys.stderr, flush=True)


def ustc_photocatalysis_server_advertise_capabilities():
    """广播当前设备的MCP能力（设备信息、支持的动作）"""
    adv_message = {
        "jsonrpc": "2.0",
        "method": "protocol/advertise",
        "params": {
            "type": "server",
            "server": {
                "protocolVersion": "0.1.0",
                "displayName": "光催化",
                "capabilities": {
                    "tools": [
        {
            "name": "open",
            "description": "开灯",
            "parameters": {
                "type": "object",
                "properties": {
    "operate": {
        "type": "string",
        "description": "开灯"
    },
    "value": {
        "type": "object",
        "description": "位置",
        "properties": {
            "light_1": {
                "type": "string",
                "description": "第一排灯",
                "enum": [
                    {
                        "label": "关灯",
                        "value": "0"
                    },
                    {
                        "label": "开灯",
                        "value": "1"
                    }
                ]
            },
            "light_2": {
                "type": "string",
                "description": "第二排灯",
                "enum": [
                    {
                        "label": "关灯",
                        "value": "0"
                    },
                    {
                        "label": "开灯",
                        "value": "1"
                    }
                ]
            },
            "light_3": {
                "type": "string",
                "description": "第三排灯",
                "enum": [
                    {
                        "label": "关灯",
                        "value": "0"
                    },
                    {
                        "label": "开灯",
                        "value": "1"
                    }
                ]
            },
            "light_4": {
                "type": "string",
                "description": "第四排灯",
                "enum": [
                    {
                        "label": "关灯",
                        "value": "0"
                    },
                    {
                        "label": "开灯",
                        "value": "1"
                    }
                ]
            }
        },
        "required": [
            "light_1",
            "light_2",
            "light_3",
            "light_4"
        ]
    },
    "value.light_1": {
        "type": "string",
        "description": "第一排灯",
        "enum": [
            {
                "label": "关灯",
                "value": "0"
            },
            {
                "label": "开灯",
                "value": "1"
            }
        ]
    },
    "value.light_2": {
        "type": "string",
        "description": "第二排灯",
        "enum": [
            {
                "label": "关灯",
                "value": "0"
            },
            {
                "label": "开灯",
                "value": "1"
            }
        ]
    },
    "value.light_3": {
        "type": "string",
        "description": "第三排灯",
        "enum": [
            {
                "label": "关灯",
                "value": "0"
            },
            {
                "label": "开灯",
                "value": "1"
            }
        ]
    },
    "value.light_4": {
        "type": "string",
        "description": "第四排灯",
        "enum": [
            {
                "label": "关灯",
                "value": "0"
            },
            {
                "label": "开灯",
                "value": "1"
            }
        ]
    }
},
                "required": ["operate", "value", "value.light_1", "value.light_2", "value.light_3", "value.light_4"]
            }
        },
        {
            "name": "time",
            "description": "照射时间",
            "parameters": {
                "type": "object",
                "properties": {
    "operate": {
        "type": "string",
        "description": "operate（单位：分钟）"
    },
    "value": {
        "type": "int",
        "description": "时间（单位：分钟）",
        "minimum": "1",
        "maximum": "2880"
    }
},
                "required": ["operate", "value"]
            }
        },
        {
            "name": "closeall",
            "description": "关闭所有灯",
            "parameters": {
                "type": "object",
                "properties": {
    "operate": {
        "type": "string",
        "description": "关闭所有灯"
    },
    "value": {
        "type": "object",
        "description": "位置",
        "properties": {
            "light_1": {
                "type": "string",
                "description": "第一排灯",
                "enum": [
                    {
                        "label": "关灯",
                        "value": "0"
                    },
                    {
                        "label": "开灯",
                        "value": "1"
                    }
                ]
            },
            "light_2": {
                "type": "string",
                "description": "第二排灯",
                "enum": [
                    {
                        "label": "关灯",
                        "value": "0"
                    },
                    {
                        "label": "开灯",
                        "value": "1"
                    }
                ]
            },
            "light_3": {
                "type": "string",
                "description": "第三排灯",
                "enum": [
                    {
                        "label": "关灯",
                        "value": "0"
                    },
                    {
                        "label": "开灯",
                        "value": "1"
                    }
                ]
            },
            "light_4": {
                "type": "string",
                "description": "第四排灯",
                "enum": [
                    {
                        "label": "关灯",
                        "value": "0"
                    },
                    {
                        "label": "开灯",
                        "value": "1"
                    }
                ]
            }
        },
        "required": [
            "light_1",
            "light_2",
            "light_3",
            "light_4"
        ]
    },
    "value.light_1": {
        "type": "string",
        "description": "第一排灯",
        "enum": [
            {
                "label": "关灯",
                "value": "0"
            },
            {
                "label": "开灯",
                "value": "1"
            }
        ]
    },
    "value.light_2": {
        "type": "string",
        "description": "第二排灯",
        "enum": [
            {
                "label": "关灯",
                "value": "0"
            },
            {
                "label": "开灯",
                "value": "1"
            }
        ]
    },
    "value.light_3": {
        "type": "string",
        "description": "第三排灯",
        "enum": [
            {
                "label": "关灯",
                "value": "0"
            },
            {
                "label": "开灯",
                "value": "1"
            }
        ]
    },
    "value.light_4": {
        "type": "string",
        "description": "第四排灯",
        "enum": [
            {
                "label": "关灯",
                "value": "0"
            },
            {
                "label": "开灯",
                "value": "1"
            }
        ]
    }
},
                "required": ["operate", "value", "value.light_1", "value.light_2", "value.light_3", "value.light_4"]
            }
        }
                    ]
                }
            }
        }
    }
    print(json.dumps(adv_message, ensure_ascii=False), flush=True)
    print(f"--- [ustc_photocatalysis_Server] 光催化 is ready. ---", file=sys.stderr, flush=True)


if __name__ == "__main__":
    # 启动流程：先广播能力，再进入主循环
    ustc_photocatalysis_server_advertise_capabilities()
    ustc_photocatalysis_server_main_loop()
