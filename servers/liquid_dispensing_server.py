import sys
import json
# 动态导入当前设备对应的工具类（与主服务器文件同目录）
from liquid_dispensing_server_tools import ActionServerTools


# 创建全局工具管理器实例
tool_manager = ActionServerTools()


# --- 定义设备动作函数（自动生成，与工具类方法对应）---
def tool_add_liquid(**params):
    return tool_manager.tool_add_liquid(**params)


def tool_tip_init(**params):
    return tool_manager.tool_tip_init(**params)


def tool_online(**params):
    return tool_manager.tool_online(**params)


def tool_offline(**params):
    return tool_manager.tool_offline(**params)


def tool_reset_init(**params):
    return tool_manager.tool_reset_init(**params)



AVAILABLE_TOOLS_ACTION = {
    "add_liquid": tool_add_liquid,
    "tip_init": tool_tip_init,
    "online": tool_online,
    "offline": tool_offline,
    "reset_init": tool_reset_init
}


# --- MCP协议通信主逻辑（自动适配当前设备）---
def liquid_dispensing_server_main_loop():
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
            print(f"--- [liquid_dispensing_Server] Critical Error: {str(e)} ---", file=sys.stderr, flush=True)


def liquid_dispensing_server_advertise_capabilities():
    """广播当前设备的MCP能力（设备信息、支持的动作）"""
    adv_message = {
        "jsonrpc": "2.0",
        "method": "protocol/advertise",
        "params": {
            "type": "server",
            "server": {
                "protocolVersion": "0.1.0",
                "displayName": "液体进样站",
                "capabilities": {
                    "tools": [
        {
            "name": "add_liquid",
            "description": "加样",
            "parameters": {
                "type": "object",
                "properties": {
    "project": {
        "type": "array",
        "description": "加样方案",
        "properties": {
            "tube_num": {
                "type": "string",
                "description": "加样瓶号"
            },
            "bottle0": {
                "type": "float",
                "description": "1号原液瓶(ml)"
            },
            "bottle1": {
                "type": "float",
                "description": "2号原液瓶(ml)"
            },
            "bottle2": {
                "type": "float",
                "description": "3号原液瓶(ml)"
            },
            "bottle3": {
                "type": "float",
                "description": "4号原液瓶(ml)"
            },
            "bottle4": {
                "type": "float",
                "description": "5号原液瓶(ml)"
            },
            "bottle5": {
                "type": "float",
                "description": "6号原液瓶(ml)"
            }
        },
        "required": [
            "tube_num"
        ]
    },
    "project.tube_num": {
        "type": "string",
        "description": "加样瓶号"
    },
    "project.bottle0": {
        "type": "float",
        "description": "1号原液瓶(ml)"
    },
    "project.bottle1": {
        "type": "float",
        "description": "2号原液瓶(ml)"
    },
    "project.bottle2": {
        "type": "float",
        "description": "3号原液瓶(ml)"
    },
    "project.bottle3": {
        "type": "float",
        "description": "4号原液瓶(ml)"
    },
    "project.bottle4": {
        "type": "float",
        "description": "5号原液瓶(ml)"
    },
    "project.bottle5": {
        "type": "float",
        "description": "6号原液瓶(ml)"
    },
    "operation": {
        "type": "string",
        "description": "操作"
    }
},
                "required": ["project", "project.tube_num"]
            }
        },
        {
            "name": "tip_init",
            "description": "tip头复位",
            "parameters": {
                "type": "object",
                "properties": {
    "operation": {
        "type": "string",
        "description": "指令"
    }
},
                "required": ["operation"]
            }
        },
        {
            "name": "online",
            "description": "强制上线",
            "parameters": {
                "type": "object",
                "properties": {
    "operation": {
        "type": "string",
        "description": "指令"
    }
},
                "required": ["operation"]
            }
        },
        {
            "name": "offline",
            "description": "强制下线",
            "parameters": {
                "type": "object",
                "properties": {
    "operation": {
        "type": "string",
        "description": "指令"
    }
},
                "required": ["operation"]
            }
        },
        {
            "name": "reset_init",
            "description": "枪头夹抓复位",
            "parameters": {
                "type": "object",
                "properties": {
    "operation": {
        "type": "string",
        "description": "命令"
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
    print(f"--- [liquid_dispensing_Server] 液体进样站 is ready. ---", file=sys.stderr, flush=True)


if __name__ == "__main__":
    # 启动流程：先广播能力，再进入主循环
    liquid_dispensing_server_advertise_capabilities()
    liquid_dispensing_server_main_loop()
