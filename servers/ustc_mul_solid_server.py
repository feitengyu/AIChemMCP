import sys
import json
# 动态导入当前设备对应的工具类（与主服务器文件同目录）
from ustc_mul_solid_server_tools import ActionServerTools


# 创建全局工具管理器实例
tool_manager = ActionServerTools()


# --- 定义设备动作函数（自动生成，与工具类方法对应）---
def tool_project(**params):
    return tool_manager.tool_project(**params)


def tool_start_handle(**params):
    return tool_manager.tool_start_handle(**params)


def tool_put_over(**params):
    return tool_manager.tool_put_over(**params)


def tool_take_over(**params):
    return tool_manager.tool_take_over(**params)


def tool_start_auto(**params):
    return tool_manager.tool_start_auto(**params)


def tool_set_solid_inject_auto(**params):
    return tool_manager.tool_set_solid_inject_auto(**params)



AVAILABLE_TOOLS_ACTION = {
    "project": tool_project,
    "start_handle": tool_start_handle,
    "put_over": tool_put_over,
    "take_over": tool_take_over,
    "start_auto": tool_start_auto,
    "set_solid_inject_auto": tool_set_solid_inject_auto
}


# --- MCP协议通信主逻辑（自动适配当前设备）---
def ustc_mul_solid_server_main_loop():
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
            print(f"--- [ustc_mul_solid_Server] Critical Error: {str(e)} ---", file=sys.stderr, flush=True)


def ustc_mul_solid_server_advertise_capabilities():
    """广播当前设备的MCP能力（设备信息、支持的动作）"""
    adv_message = {
        "jsonrpc": "2.0",
        "method": "protocol/advertise",
        "params": {
            "type": "server",
            "server": {
                "protocolVersion": "0.1.0",
                "displayName": "多通道固体进样器",
                "capabilities": {
                    "tools": [
        {
            "name": "project",
            "description": "进料方案",
            "parameters": {
                "type": "object",
                "properties": {
    "operation": {
        "type": "string",
        "description": "指令"
    },
    "data": {
        "type": "array",
        "description": "方案",
        "properties": {
            "bottle_index": {
                "type": "int",
                "description": "进样瓶"
            },
            "material": {
                "type": "array",
                "description": "进料信息",
                "properties": {
                    "material.material_index": {
                        "type": "int",
                        "description": "物料编号",
                        "enum": [
                            {
                                "label": "物料1",
                                "value": "1"
                            },
                            {
                                "label": "物料2",
                                "value": "2"
                            },
                            {
                                "label": "物料3",
                                "value": "3"
                            },
                            {
                                "label": "物料4",
                                "value": "4"
                            },
                            {
                                "label": "物料5",
                                "value": "5"
                            },
                            {
                                "label": "物料6",
                                "value": "6"
                            },
                            {
                                "label": "物料7",
                                "value": "7"
                            },
                            {
                                "label": "物料8",
                                "value": "8"
                            },
                            {
                                "label": "物料9",
                                "value": "9"
                            },
                            {
                                "label": "物料10",
                                "value": "10"
                            },
                            {
                                "label": "物料11",
                                "value": "11"
                            },
                            {
                                "label": "物料12",
                                "value": "12"
                            },
                            {
                                "label": "物料13",
                                "value": "13"
                            },
                            {
                                "label": "物料14",
                                "value": "14"
                            },
                            {
                                "label": "物料15",
                                "value": "15"
                            },
                            {
                                "label": "物料16",
                                "value": "16"
                            },
                            {
                                "label": "物料17",
                                "value": "17"
                            },
                            {
                                "label": "物料18",
                                "value": "18"
                            },
                            {
                                "label": "物料19",
                                "value": "19"
                            },
                            {
                                "label": "物料20",
                                "value": "20"
                            },
                            {
                                "label": "物料21",
                                "value": "21"
                            },
                            {
                                "label": "物料22",
                                "value": "22"
                            },
                            {
                                "label": "物料23",
                                "value": "23"
                            },
                            {
                                "label": "物料24",
                                "value": "24"
                            },
                            {
                                "label": "物料25",
                                "value": "25"
                            },
                            {
                                "label": "物料26",
                                "value": "26"
                            },
                            {
                                "label": "物料27",
                                "value": "27"
                            },
                            {
                                "label": "物料28",
                                "value": "28"
                            },
                            {
                                "label": "物料29",
                                "value": "29"
                            },
                            {
                                "label": "物料30",
                                "value": "30"
                            }
                        ]
                    },
                    "material.weight": {
                        "type": "float",
                        "description": "加料量（单位：精度0.001g）",
                        "minimum": "0",
                        "maximum": "40"
                    }
                },
                "required": [
                    "material.material_index",
                    "material.weight"
                ]
            },
            "material.material_index": {
                "type": "int",
                "description": "物料编号",
                "enum": [
                    {
                        "label": "物料1",
                        "value": "1"
                    },
                    {
                        "label": "物料2",
                        "value": "2"
                    },
                    {
                        "label": "物料3",
                        "value": "3"
                    },
                    {
                        "label": "物料4",
                        "value": "4"
                    },
                    {
                        "label": "物料5",
                        "value": "5"
                    },
                    {
                        "label": "物料6",
                        "value": "6"
                    },
                    {
                        "label": "物料7",
                        "value": "7"
                    },
                    {
                        "label": "物料8",
                        "value": "8"
                    },
                    {
                        "label": "物料9",
                        "value": "9"
                    },
                    {
                        "label": "物料10",
                        "value": "10"
                    },
                    {
                        "label": "物料11",
                        "value": "11"
                    },
                    {
                        "label": "物料12",
                        "value": "12"
                    },
                    {
                        "label": "物料13",
                        "value": "13"
                    },
                    {
                        "label": "物料14",
                        "value": "14"
                    },
                    {
                        "label": "物料15",
                        "value": "15"
                    },
                    {
                        "label": "物料16",
                        "value": "16"
                    },
                    {
                        "label": "物料17",
                        "value": "17"
                    },
                    {
                        "label": "物料18",
                        "value": "18"
                    },
                    {
                        "label": "物料19",
                        "value": "19"
                    },
                    {
                        "label": "物料20",
                        "value": "20"
                    },
                    {
                        "label": "物料21",
                        "value": "21"
                    },
                    {
                        "label": "物料22",
                        "value": "22"
                    },
                    {
                        "label": "物料23",
                        "value": "23"
                    },
                    {
                        "label": "物料24",
                        "value": "24"
                    },
                    {
                        "label": "物料25",
                        "value": "25"
                    },
                    {
                        "label": "物料26",
                        "value": "26"
                    },
                    {
                        "label": "物料27",
                        "value": "27"
                    },
                    {
                        "label": "物料28",
                        "value": "28"
                    },
                    {
                        "label": "物料29",
                        "value": "29"
                    },
                    {
                        "label": "物料30",
                        "value": "30"
                    }
                ]
            },
            "material.weight": {
                "type": "float",
                "description": "加料量（单位：精度0.001g）",
                "minimum": "0",
                "maximum": "40"
            }
        },
        "required": [
            "bottle_index",
            "material",
            "material.material_index",
            "material.weight"
        ]
    },
    "data.bottle_index": {
        "type": "int",
        "description": "进样瓶"
    },
    "data.material": {
        "type": "array",
        "description": "进料信息",
        "properties": {
            "material.material_index": {
                "type": "int",
                "description": "物料编号",
                "enum": [
                    {
                        "label": "物料1",
                        "value": "1"
                    },
                    {
                        "label": "物料2",
                        "value": "2"
                    },
                    {
                        "label": "物料3",
                        "value": "3"
                    },
                    {
                        "label": "物料4",
                        "value": "4"
                    },
                    {
                        "label": "物料5",
                        "value": "5"
                    },
                    {
                        "label": "物料6",
                        "value": "6"
                    },
                    {
                        "label": "物料7",
                        "value": "7"
                    },
                    {
                        "label": "物料8",
                        "value": "8"
                    },
                    {
                        "label": "物料9",
                        "value": "9"
                    },
                    {
                        "label": "物料10",
                        "value": "10"
                    },
                    {
                        "label": "物料11",
                        "value": "11"
                    },
                    {
                        "label": "物料12",
                        "value": "12"
                    },
                    {
                        "label": "物料13",
                        "value": "13"
                    },
                    {
                        "label": "物料14",
                        "value": "14"
                    },
                    {
                        "label": "物料15",
                        "value": "15"
                    },
                    {
                        "label": "物料16",
                        "value": "16"
                    },
                    {
                        "label": "物料17",
                        "value": "17"
                    },
                    {
                        "label": "物料18",
                        "value": "18"
                    },
                    {
                        "label": "物料19",
                        "value": "19"
                    },
                    {
                        "label": "物料20",
                        "value": "20"
                    },
                    {
                        "label": "物料21",
                        "value": "21"
                    },
                    {
                        "label": "物料22",
                        "value": "22"
                    },
                    {
                        "label": "物料23",
                        "value": "23"
                    },
                    {
                        "label": "物料24",
                        "value": "24"
                    },
                    {
                        "label": "物料25",
                        "value": "25"
                    },
                    {
                        "label": "物料26",
                        "value": "26"
                    },
                    {
                        "label": "物料27",
                        "value": "27"
                    },
                    {
                        "label": "物料28",
                        "value": "28"
                    },
                    {
                        "label": "物料29",
                        "value": "29"
                    },
                    {
                        "label": "物料30",
                        "value": "30"
                    }
                ]
            },
            "material.weight": {
                "type": "float",
                "description": "加料量（单位：精度0.001g）",
                "minimum": "0",
                "maximum": "40"
            }
        },
        "required": [
            "material.material_index",
            "material.weight"
        ]
    },
    "data.material.material_index": {
        "type": "int",
        "description": "物料编号",
        "enum": [
            {
                "label": "物料1",
                "value": "1"
            },
            {
                "label": "物料2",
                "value": "2"
            },
            {
                "label": "物料3",
                "value": "3"
            },
            {
                "label": "物料4",
                "value": "4"
            },
            {
                "label": "物料5",
                "value": "5"
            },
            {
                "label": "物料6",
                "value": "6"
            },
            {
                "label": "物料7",
                "value": "7"
            },
            {
                "label": "物料8",
                "value": "8"
            },
            {
                "label": "物料9",
                "value": "9"
            },
            {
                "label": "物料10",
                "value": "10"
            },
            {
                "label": "物料11",
                "value": "11"
            },
            {
                "label": "物料12",
                "value": "12"
            },
            {
                "label": "物料13",
                "value": "13"
            },
            {
                "label": "物料14",
                "value": "14"
            },
            {
                "label": "物料15",
                "value": "15"
            },
            {
                "label": "物料16",
                "value": "16"
            },
            {
                "label": "物料17",
                "value": "17"
            },
            {
                "label": "物料18",
                "value": "18"
            },
            {
                "label": "物料19",
                "value": "19"
            },
            {
                "label": "物料20",
                "value": "20"
            },
            {
                "label": "物料21",
                "value": "21"
            },
            {
                "label": "物料22",
                "value": "22"
            },
            {
                "label": "物料23",
                "value": "23"
            },
            {
                "label": "物料24",
                "value": "24"
            },
            {
                "label": "物料25",
                "value": "25"
            },
            {
                "label": "物料26",
                "value": "26"
            },
            {
                "label": "物料27",
                "value": "27"
            },
            {
                "label": "物料28",
                "value": "28"
            },
            {
                "label": "物料29",
                "value": "29"
            },
            {
                "label": "物料30",
                "value": "30"
            }
        ]
    },
    "data.material.weight": {
        "type": "float",
        "description": "加料量（单位：精度0.001g）",
        "minimum": "0",
        "maximum": "40"
    }
},
                "required": ["data.bottle_index", "data.material", "data.material.material_index", "data.material.weight"]
            }
        },
        {
            "name": "start_handle",
            "description": "手动上样",
            "parameters": {
                "type": "object",
                "properties": {
    "operation": {
        "type": "string",
        "description": "指令"
    }
},
                "required": []
            }
        },
        {
            "name": "put_over",
            "description": "本轮放置结束",
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
            "name": "take_over",
            "description": "本轮拿取结束",
            "parameters": {
                "type": "object",
                "properties": {
    "operation": {
        "type": "string",
        "description": "指令"
    }
},
                "required": []
            }
        },
        {
            "name": "start_auto",
            "description": "自动开始",
            "parameters": {
                "type": "object",
                "properties": {
    "operation": {
        "type": "string",
        "description": "指令"
    }
},
                "required": []
            }
        },
        {
            "name": "set_solid_inject_auto",
            "description": "自动加样",
            "parameters": {
                "type": "object",
                "properties": {
    "operation": {
        "type": "string",
        "description": "指令"
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
    print(f"--- [ustc_mul_solid_Server] 多通道固体进样器 is ready. ---", file=sys.stderr, flush=True)


if __name__ == "__main__":
    # 启动流程：先广播能力，再进入主循环
    ustc_mul_solid_server_advertise_capabilities()
    ustc_mul_solid_server_main_loop()
