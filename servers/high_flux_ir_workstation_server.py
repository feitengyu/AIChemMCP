import sys
import json
# 动态导入当前设备对应的工具类（与主服务器文件同目录）
from tools.high_flux_ir_workstation_server_tools import ActionServerTools


# 创建全局工具管理器实例
tool_manager = ActionServerTools()


# --- 定义设备动作函数（自动生成，与工具类方法对应）---
def tool_start_check(**params):
    return tool_manager.tool_start_check(**params)


def tool_prefix_operate(**params):
    return tool_manager.tool_prefix_operate(**params)


def tool_collect_sample_back(**params):
    return tool_manager.tool_collect_sample_back(**params)


def tool_sleep(**params):
    return tool_manager.tool_sleep(**params)


def tool_confirm_tip_position(**params):
    return tool_manager.tool_confirm_tip_position(**params)



AVAILABLE_TOOLS_ACTION = {
    "start_check": tool_start_check,
    "prefix_operate": tool_prefix_operate,
    "collect_sample_back": tool_collect_sample_back,
    "sleep": tool_sleep,
    "confirm_tip_position": tool_confirm_tip_position
}


# --- MCP协议通信主逻辑（自动适配当前设备）---
def high_flux_ir_workstation_server_main_loop():
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
            print(f"--- [high_flux_ir_workstation_Server] Critical Error: {str(e)} ---", file=sys.stderr, flush=True)


def high_flux_ir_workstation_server_advertise_capabilities():
    """广播当前设备的MCP能力（设备信息、支持的动作）"""
    adv_message = {
        "jsonrpc": "2.0",
        "method": "protocol/advertise",
        "params": {
            "type": "server",
            "server": {
                "protocolVersion": "0.1.0",
                "displayName": "高通量平台-红外光谱工作站",
                "capabilities": {
                    "tools": [
        {
            "name": "start_check",
            "description": "开始检测",
            "parameters": {
                "type": "object",
                "properties": {
    "operation": {
        "type": "string",
        "description": "操作指令"
    },
    "resultCode": {
        "type": "string",
        "description": "resultCode"
    }
},
                "required": ["operation", "resultCode"]
            }
        },
        {
            "name": "prefix_operate",
            "description": "检测前处理",
            "parameters": {
                "type": "object",
                "properties": {
    "operation": {
        "type": "string",
        "description": "操作指令"
    }
},
                "required": ["operation"]
            }
        },
        {
            "name": "collect_sample_back",
            "description": "采集样本背景",
            "parameters": {
                "type": "object",
                "properties": {
    "operation": {
        "type": "string",
        "description": "操作指令"
    }
},
                "required": ["operation"]
            }
        },
        {
            "name": "sleep",
            "description": "静置晾干",
            "parameters": {
                "type": "object",
                "properties": {
    "operation": {
        "type": "string",
        "description": "操作指令"
    },
    "time": {
        "type": "int",
        "description": "静置晾干时间（s）"
    }
},
                "required": ["operation", "time"]
            }
        },
        {
            "name": "confirm_tip_position",
            "description": "确认tip头位置",
            "parameters": {
                "type": "object",
                "properties": {
    "operation": {
        "type": "string",
        "description": "操作指令"
    },
    "position": {
        "type": "int",
        "description": "当前使用的tip头位置（1-48）",
        "minimum": "1",
        "maximum": "48"
    }
},
                "required": ["operation", "position"]
            }
        }
                    ]
                }
            }
        }
    }
    print(json.dumps(adv_message, ensure_ascii=False), flush=True)
    print(f"--- [high_flux_ir_workstation_Server] 高通量平台-红外光谱工作站 is ready. ---", file=sys.stderr, flush=True)


if __name__ == "__main__":
    # 启动流程：先广播能力，再进入主循环
    high_flux_ir_workstation_server_advertise_capabilities()
    high_flux_ir_workstation_server_main_loop()
