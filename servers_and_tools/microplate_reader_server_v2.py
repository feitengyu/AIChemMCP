import sys
import json
# 动态导入当前设备对应的工具类
from microplate_reader_server_tools_v2 import UnifiedWorkstationTools


# 创建全局工具管理器实例
tool_manager = UnifiedWorkstationTools()


# --- 定义统一的工作站工具函数 ---
def tool_microplate_reader(task_description: str, **params):
    """
    执行酶标仪工作站的任务
    
    参数:
        task_description: 任务描述，说明要执行的具体操作
        **params: 其他可选参数，根据具体任务需要传递
    """
    return tool_manager.tool_microplate_reader(task_description, **params)



AVAILABLE_TOOLS = {
    "酶标仪工作站": tool_microplate_reader
}


# --- MCP协议通信主逻辑 ---
def microplate_reader_server_main_loop():
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
            print(f"--- [microplate_reader_Server] Error: {str(e)} ---", file=sys.stderr, flush=True)


def microplate_reader_server_advertise_capabilities():
    """广播当前设备的MCP能力"""
    adv_message = {
        "jsonrpc": "2.0",
        "method": "protocol/advertise",
        "params": {
            "type": "server",
            "server": {
                "protocolVersion": "0.1.0",
                "displayName": "酶标仪工作站",
                "capabilities": {
                    "tools": [
        {
            "name": "酶标仪工作站",
            "description": "多功能酶标仪可进行多种生物分子的定量分析。它能够检测多种信号，如吸光度、荧光强度、化学发光等。在免疫学实验中，可用于酶联免疫吸附测定（ELISA），检测血液中的抗体、抗原等物质的含量，辅助疾病的诊断和监测。在药物研发中，可用于筛选具有生物活性的化合物，评估药物的疗效。其多功能性和高灵敏度使得它在生命科学研究和临床诊断中得到广泛应用。",
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
    print(f"--- [microplate_reader_Server] 酶标仪工作站 已就绪 ---", file=sys.stderr, flush=True)


if __name__ == "__main__":
    # 启动流程：先广播能力，再进入主循环
    microplate_reader_server_advertise_capabilities()
    microplate_reader_server_main_loop()
