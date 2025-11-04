import sys
import json
# 动态导入当前设备对应的工具类（与主服务器文件同目录）
from tools.testf_server_tools import ActionServerTools


# 创建全局工具管理器实例
tool_manager = ActionServerTools()


# --- 定义设备动作函数（自动生成，与工具类方法对应）---
def tool_dispensing(**params):
    return tool_manager.tool_dispensing(**params)



AVAILABLE_TOOLS_ACTION = {
    "dispensing": tool_dispensing
}


# --- MCP协议通信主逻辑（自动适配当前设备）---
def testf_server_main_loop():
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
            print(f"--- [testf_Server] Critical Error: {str(e)} ---", file=sys.stderr, flush=True)


def testf_server_advertise_capabilities():
    """广播当前设备的MCP能力（设备信息、支持的动作）"""
    adv_message = {
        "jsonrpc": "2.0",
        "method": "protocol/advertise",
        "params": {
            "type": "server",
            "server": {
                "protocolVersion": "0.1.0",
                "displayName": "2-固体进样",
                "capabilities": {
                    "tools": [
        {
            "name": "dispensing",
            "description": "参数设置",
            "parameters": {
                "type": "object",
                "properties": {
    "material1": {
        "type": "array",
        "description": "酸碱液固体进样",
        "properties": {
            "scale": {
                "type": "string",
                "description": "物料名称",
                "enum": [
                    "酸1",
                    "酸2",
                    "酸3"
                ]
            },
            "number": {
                "type": "string",
                "description": "物料量"
            },
            "bottle": {
                "type": "string",
                "description": "瓶子编号"
            }
        },
        "required": [
            "scale",
            "number",
            "bottle"
        ]
    },
    "material1.scale": {
        "type": "string",
        "description": "物料名称",
        "enum": [
            "酸1",
            "酸2",
            "酸3"
        ]
    },
    "material1.number": {
        "type": "string",
        "description": "物料量"
    },
    "material1.bottle": {
        "type": "string",
        "description": "瓶子编号"
    },
    "material2": {
        "type": "array",
        "description": "浸渍液固体进样",
        "properties": {
            "bottle": {
                "type": "string",
                "description": "瓶子编号"
            },
            "material": {
                "type": "string",
                "description": "物料名称"
            },
            "number": {
                "type": "string",
                "description": "物料量"
            }
        },
        "required": [
            "bottle",
            "material",
            "number"
        ]
    },
    "material2.bottle": {
        "type": "string",
        "description": "瓶子编号"
    },
    "material2.material": {
        "type": "string",
        "description": "物料名称"
    },
    "material2.number": {
        "type": "string",
        "description": "物料量"
    }
},
                "required": ["material1", "material1.scale", "material1.number", "material1.bottle", "material2.bottle", "material2.material", "material2.number"]
            }
        }
                    ]
                }
            }
        }
    }
    print(json.dumps(adv_message, ensure_ascii=False), flush=True)
    print(f"--- [testf_Server] 2-固体进样 is ready. ---", file=sys.stderr, flush=True)


if __name__ == "__main__":
    # 启动流程：先广播能力，再进入主循环
    testf_server_advertise_capabilities()
    testf_server_main_loop()
