import sys
import json
# 动态导入当前设备对应的工具类（与主服务器文件同目录）
from tools.battery_assemble_workstation_server_tools import ActionServerTools


# 创建全局工具管理器实例
tool_manager = ActionServerTools()


# --- 定义设备动作函数（自动生成，与工具类方法对应）---
def tool_dispensing(**params):
    return tool_manager.tool_dispensing(**params)


def tool_assemble(**params):
    return tool_manager.tool_assemble(**params)



AVAILABLE_TOOLS_ACTION = {
    "dispensing": tool_dispensing,
    "assemble": tool_assemble
}


# --- MCP协议通信主逻辑（自动适配当前设备）---
def battery_assemble_workstation_server_main_loop():
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
            print(f"--- [battery_assemble_workstation_Server] Critical Error: {str(e)} ---", file=sys.stderr, flush=True)


def battery_assemble_workstation_server_advertise_capabilities():
    """广播当前设备的MCP能力（设备信息、支持的动作）"""
    adv_message = {
        "jsonrpc": "2.0",
        "method": "protocol/advertise",
        "params": {
            "type": "server",
            "server": {
                "protocolVersion": "0.1.0",
                "displayName": "扣电工作站",
                "capabilities": {
                    "tools": [
        {
            "name": "dispensing",
            "description": "电池配液",
            "parameters": {
                "type": "object",
                "properties": {
    "recipes": {
        "type": "array",
        "description": "组装配方",
        "properties": {
            "startNo": {
                "type": "int",
                "description": "起始电池编号"
            },
            "endNo": {
                "type": "int",
                "description": "截止电池编号"
            },
            "recipeCode": {
                "type": "string",
                "description": "配方编号"
            },
            "recipeName": {
                "type": "string",
                "description": "配方名称"
            }
        },
        "required": [
            "startNo",
            "endNo",
            "recipeCode"
        ]
    },
    "recipes.startNo": {
        "type": "int",
        "description": "起始电池编号"
    },
    "recipes.endNo": {
        "type": "int",
        "description": "截止电池编号"
    },
    "recipes.recipeCode": {
        "type": "string",
        "description": "配方编号"
    },
    "recipes.recipeName": {
        "type": "string",
        "description": "配方名称"
    },
    "isConductionTest": {
        "type": "boolean",
        "description": "是否测试电导",
        "enum": [
            {
                "label": "是",
                "value": "true"
            },
            {
                "label": "否",
                "value": "false"
            }
        ]
    },
    "aluminiumFlakeCount": {
        "type": "int",
        "description": "铝片数量"
    },
    "resultCode": {
        "type": "file",
        "description": "resultCode"
    }
},
                "required": ["recipes", "recipes.startNo", "recipes.endNo", "recipes.recipeCode", "isConductionTest"]
            }
        },
        {
            "name": "assemble",
            "description": "电池组装",
            "parameters": {
                "type": "object",
                "properties": {
    "resultCode": {
        "type": "file",
        "description": "resultCode"
    }
},
                "required": []
            }
        }
                    ]
                }
            }
        }
    }
    print(json.dumps(adv_message, ensure_ascii=False), flush=True)
    print(f"--- [battery_assemble_workstation_Server] 扣电工作站 is ready. ---", file=sys.stderr, flush=True)


if __name__ == "__main__":
    # 启动流程：先广播能力，再进入主循环
    battery_assemble_workstation_server_advertise_capabilities()
    battery_assemble_workstation_server_main_loop()
