import sys
import json
# 动态导入当前设备对应的工具类
from tptn_server_tools_v2 import UnifiedWorkstationTools


# 创建全局工具管理器实例
tool_manager = UnifiedWorkstationTools()


# --- 定义统一的工作站工具函数 ---
def tool_tptn(task_description: str, **params):
    """
    执行总磷总氮工作站的任务
    
    参数:
        task_description: 任务描述，说明要执行的具体操作
        **params: 其他可选参数，根据具体任务需要传递
    """
    return tool_manager.tool_tptn(task_description, **params)



AVAILABLE_TOOLS = {
    "总磷总氮工作站": tool_tptn
}


# --- MCP协议通信主逻辑 ---
def tptn_server_main_loop():
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
            print(f"--- [tptn_Server] Error: {str(e)} ---", file=sys.stderr, flush=True)


def tptn_server_advertise_capabilities():
    """广播当前设备的MCP能力"""
    adv_message = {
        "jsonrpc": "2.0",
        "method": "protocol/advertise",
        "params": {
            "type": "server",
            "server": {
                "protocolVersion": "0.1.0",
                "displayName": "总磷总氮工作站",
                "capabilities": {
                    "tools": [
        {
            "name": "总磷总氮工作站",
            "description": "总磷总氮测定仪用于同时测定水样中的总磷和总氮含量。对于总磷的测定，通常先将水样中的各种含磷化合物氧化为正磷酸盐，然后通过比色法等方法进行定量分析；对于总氮的测定，一般将水样中的含氮化合物氧化为硝酸盐，再进行检测。总磷和总氮是水体富营养化的重要指标，通过总磷总氮测定仪可以及时了解水体的营养状况，为水资源保护和治理提供数据支持。",
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
    print(f"--- [tptn_Server] 总磷总氮工作站 已就绪 ---", file=sys.stderr, flush=True)


if __name__ == "__main__":
    # 启动流程：先广播能力，再进入主循环
    tptn_server_advertise_capabilities()
    tptn_server_main_loop()
