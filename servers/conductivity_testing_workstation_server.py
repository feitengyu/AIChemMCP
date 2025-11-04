import sys
import json
# 动态导入当前设备对应的工具类（与主服务器文件同目录）
from tools.conductivity_testing_workstation_server_tools import ActionServerTools


# 创建全局工具管理器实例
tool_manager = ActionServerTools()


# --- 定义设备动作函数（自动生成，与工具类方法对应）---
def tool_init(**params):
    return tool_manager.tool_init(**params)


def tool_testing(**params):
    return tool_manager.tool_testing(**params)



AVAILABLE_TOOLS_ACTION = {
    "init": tool_init,
    "testing": tool_testing
}


# --- MCP协议通信主逻辑（自动适配当前设备）---
def conductivity_testing_workstation_server_main_loop():
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
            print(f"--- [conductivity_testing_workstation_Server] Critical Error: {str(e)} ---", file=sys.stderr, flush=True)


def conductivity_testing_workstation_server_advertise_capabilities():
    """广播当前设备的MCP能力（设备信息、支持的动作）"""
    adv_message = {
        "jsonrpc": "2.0",
        "method": "protocol/advertise",
        "params": {
            "type": "server",
            "server": {
                "protocolVersion": "0.1.0",
                "displayName": "电导率测试工作站",
                "capabilities": {
                    "tools": [
        {
            "name": "init",
            "description": "初始化",
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
            "name": "testing",
            "description": "电导率测试",
            "parameters": {
                "type": "object",
                "properties": {
    "operation": {
        "type": "string",
        "description": "操作指令"
    },
    "dry_time": {
        "type": "int",
        "description": "干燥时间（s）",
        "minimum": "0",
        "maximum": "86400"
    },
    "wash_time": {
        "type": "int",
        "description": "洗涤时间（s）",
        "minimum": "0",
        "maximum": "10"
    },
    "wash_speed": {
        "type": "int",
        "description": "清洗速度",
        "minimum": "10",
        "maximum": "100"
    }
},
                "required": ["operation", "dry_time", "wash_time", "wash_speed"]
            }
        }
                    ]
                }
            }
        }
    }
    print(json.dumps(adv_message, ensure_ascii=False), flush=True)
    print(f"--- [conductivity_testing_workstation_Server] 电导率测试工作站 is ready. ---", file=sys.stderr, flush=True)


if __name__ == "__main__":
    # 启动流程：先广播能力，再进入主循环
    conductivity_testing_workstation_server_advertise_capabilities()
    conductivity_testing_workstation_server_main_loop()
