import sys
import json
# 动态导入当前设备对应的工具类
from spps_workstation_server_tools_v2 import UnifiedWorkstationTools


# 创建全局工具管理器实例
tool_manager = UnifiedWorkstationTools()


# --- 定义统一的工作站工具函数 ---
def tool_spps_workstation(task_description: str, **params):
    """
    执行固相多肽工作站的任务
    
    参数:
        task_description: 任务描述，说明要执行的具体操作
        **params: 其他可选参数，根据具体任务需要传递
    """
    return tool_manager.tool_spps_workstation(task_description, **params)



AVAILABLE_TOOLS = {
    "固相多肽工作站": tool_spps_workstation
}


# --- MCP协议通信主逻辑 ---
def spps_workstation_server_main_loop():
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
            print(f"--- [spps_workstation_Server] Error: {str(e)} ---", file=sys.stderr, flush=True)


def spps_workstation_server_advertise_capabilities():
    """广播当前设备的MCP能力"""
    adv_message = {
        "jsonrpc": "2.0",
        "method": "protocol/advertise",
        "params": {
            "type": "server",
            "server": {
                "protocolVersion": "0.1.0",
                "displayName": "固相多肽工作站",
                "capabilities": {
                    "tools": [
        {
            "name": "固相多肽工作站",
            "description": "固相多肽合成仪是用于人工合成多肽的设备。它基于固相合成的原理，将氨基酸逐个连接到固相载体上，通过不断重复脱保护、缩合等反应步骤，合成具有特定序列的多肽。在药物研发中，可合成具有生物活性的多肽药物；在蛋白质结构和功能研究中，可合成用于研究的多肽片段。其自动化的合成过程提高了合成效率和多肽的纯度，为多肽相关的研究和应用提供了有力的支持。",
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
    print(f"--- [spps_workstation_Server] 固相多肽工作站 已就绪 ---", file=sys.stderr, flush=True)


if __name__ == "__main__":
    # 启动流程：先广播能力，再进入主循环
    spps_workstation_server_advertise_capabilities()
    spps_workstation_server_main_loop()
