import sys
import json
# 动态导入当前设备对应的工具类
from single_atom_enzyme_mimicking_server_tools_v2 import UnifiedWorkstationTools


# 创建全局工具管理器实例
tool_manager = UnifiedWorkstationTools()


# --- 定义统一的工作站工具函数 ---
def tool_single_atom_enzyme_mimicking(task_description: str, **params):
    """
    执行单原子仿酶催化平台的任务
    
    参数:
        task_description: 任务描述，说明要执行的具体操作
        **params: 其他可选参数，根据具体任务需要传递
    """
    return tool_manager.tool_single_atom_enzyme_mimicking(task_description, **params)



AVAILABLE_TOOLS = {
    "单原子仿酶催化平台": tool_single_atom_enzyme_mimicking
}


# --- MCP协议通信主逻辑 ---
def single_atom_enzyme_mimicking_server_main_loop():
    """主循环：监听并响应Host的MCP协议请求"""
    for line in sys.stdin:
        try:
            request = json.loads(line)
            request_id = request.get("id")
            method_name = request.get("method")
            params = request.get("params", {})

            if method_name in AVAILABLE_TOOLS:
                # 调用对应的工具函数
                tool_function = AVAILABLE_TOOLS[method_name]
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

            # 响应结果
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
            print(f"--- [single_atom_enzyme_mimicking_Server] Error: {str(e)} ---", file=sys.stderr, flush=True)


def single_atom_enzyme_mimicking_server_advertise_capabilities():
    """广播当前设备的MCP能力"""
    adv_message = {
        "jsonrpc": "2.0",
        "method": "protocol/advertise",
        "params": {
            "type": "server",
            "server": {
                "protocolVersion": "0.1.0",
                "displayName": "单原子仿酶催化平台",
                "capabilities": {
                    "tools": [
        {
            "name": "单原子仿酶催化平台",
            "description": "单原子仿酶催化测试平台是专门用于研究单原子仿酶催化剂性能的实验平台。它可以模拟各种催化反应条件，精确控制反应温度、压力、反应物浓度等参数。通过先进的检测技术，如质谱、光谱等，实时监测反应过程中的物质变化和催化剂的活性。能够对单原子仿酶催化剂的催化活性、选择性、稳定性等性能进行全面评估。在能源催化、环境催化等领域，对于开发高效、低成本的单原子仿酶催化剂具有重要意义，有助于推动新型催化技术的发展和应用。",
            "parameters": {
                "type": "object",
                "properties": {
                    "task_description": {
                        "type": "string",
                        "description": "需要执行的具体任务描述"
                    }
                },
                "required": ["task_description"]
            }
        }
                    ]
                }
            }
        }
    }
    print(json.dumps(adv_message, ensure_ascii=False), flush=True)
    print(f"--- [single_atom_enzyme_mimicking_Server] 单原子仿酶催化平台 已就绪 ---", file=sys.stderr, flush=True)


if __name__ == "__main__":
    # 启动流程：先广播能力，再进入主循环
    single_atom_enzyme_mimicking_server_advertise_capabilities()
    single_atom_enzyme_mimicking_server_main_loop()
