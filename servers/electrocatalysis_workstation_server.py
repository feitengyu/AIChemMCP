import sys
import json
# 动态导入当前设备对应的工具类（与主服务器文件同目录）
from tools.electrocatalysis_workstation_server_tools import ActionServerTools


# 创建全局工具管理器实例
tool_manager = ActionServerTools()


# --- 定义设备动作函数（自动生成，与工具类方法对应）---
def tool_open_door(**params):
    return tool_manager.tool_open_door(**params)


def tool_close_door(**params):
    return tool_manager.tool_close_door(**params)


def tool_dissolve(**params):
    return tool_manager.tool_dissolve(**params)


def tool_evaporate(**params):
    return tool_manager.tool_evaporate(**params)



AVAILABLE_TOOLS_ACTION = {
    "open-door": tool_open_door,
    "close-door": tool_close_door,
    "dissolve": tool_dissolve,
    "evaporate": tool_evaporate
}


# --- MCP协议通信主逻辑（自动适配当前设备）---
def electrocatalysis_workstation_server_main_loop():
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
            print(f"--- [electrocatalysis_workstation_Server] Critical Error: {str(e)} ---", file=sys.stderr, flush=True)


def electrocatalysis_workstation_server_advertise_capabilities():
    """广播当前设备的MCP能力（设备信息、支持的动作）"""
    adv_message = {
        "jsonrpc": "2.0",
        "method": "protocol/advertise",
        "params": {
            "type": "server",
            "server": {
                "protocolVersion": "0.1.0",
                "displayName": "滴液工作站与电催化工作站",
                "capabilities": {
                    "tools": [
        {
            "name": "open-door",
            "description": "开门",
            "parameters": {
                "type": "object",
                "properties": {
    "kind": {
        "type": "string",
        "description": "参数 kind"
    }
},
                "required": []
            }
        },
        {
            "name": "close-door",
            "description": "关门",
            "parameters": {
                "type": "object",
                "properties": {
    "kind": {
        "type": "string",
        "description": "参数 kind"
    }
},
                "required": []
            }
        },
        {
            "name": "dissolve",
            "description": "溶解",
            "parameters": {
                "type": "object",
                "properties": {
    "kind": {
        "type": "string",
        "description": "参数 kind"
    }
},
                "required": []
            }
        },
        {
            "name": "evaporate",
            "description": "蒸发",
            "parameters": {
                "type": "object",
                "properties": {
    "material": {
        "type": "array",
        "description": "物料",
        "properties": {
            "kind": {
                "type": "string",
                "description": "通道号",
                "enum": [
                    "A",
                    "B",
                    "C"
                ]
            },
            "value": {
                "type": "float",
                "description": "物质质量（单位：克）",
                "minimum": "1",
                "maximum": "2"
            }
        },
        "required": [
            "kind",
            "value"
        ]
    },
    "material.kind": {
        "type": "string",
        "description": "通道号",
        "enum": [
            "A",
            "B",
            "C"
        ]
    },
    "material.value": {
        "type": "float",
        "description": "物质质量（单位：克）",
        "minimum": "1",
        "maximum": "2"
    },
    "channel": {
        "type": "array",
        "description": "通道号测试用",
        "enum": [
            {
                "value": "A",
                "label": "通道A"
            },
            {
                "value": "B",
                "label": "通道B"
            },
            {
                "value": "C",
                "label": "通道C"
            }
        ]
    },
    "code3": {
        "type": "object",
        "description": "参数3",
        "properties": {
            "aa": {
                "type": "int",
                "description": "aaa",
                "minimum": "1",
                "maximum": "5"
            },
            "bb": {
                "type": "float",
                "description": "bbb",
                "minimum": "1",
                "maximum": "8"
            }
        },
        "required": [
            "aa",
            "bb"
        ]
    },
    "code3.aa": {
        "type": "int",
        "description": "aaa",
        "minimum": "1",
        "maximum": "5"
    },
    "code3.bb": {
        "type": "float",
        "description": "bbb",
        "minimum": "1",
        "maximum": "8"
    },
    "param4": {
        "type": "string",
        "description": "参数4",
        "enum": [
            {
                "value": "A",
                "label": "通道A"
            },
            {
                "value": "B",
                "label": "通道B"
            },
            {
                "value": "C",
                "label": "通道C"
            }
        ]
    }
},
                "required": ["material.kind", "material.value", "code3", "code3.aa", "code3.bb", "param4"]
            }
        }
                    ]
                }
            }
        }
    }
    print(json.dumps(adv_message, ensure_ascii=False), flush=True)
    print(f"--- [electrocatalysis_workstation_Server] 滴液工作站与电催化工作站 is ready. ---", file=sys.stderr, flush=True)


if __name__ == "__main__":
    # 启动流程：先广播能力，再进入主循环
    electrocatalysis_workstation_server_advertise_capabilities()
    electrocatalysis_workstation_server_main_loop()
