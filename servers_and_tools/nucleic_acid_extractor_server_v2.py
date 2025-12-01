import sys
import json
# 动态导入当前设备对应的工具类
from nucleic_acid_extractor_server_tools_v2 import UnifiedWorkstationTools


# 创建全局工具管理器实例
tool_manager = UnifiedWorkstationTools()


# --- 定义统一的工作站工具函数 ---
def tool_nucleic_acid_extractor(task_description: str, **params):
    """
    执行核酸提取仪的任务
    
    参数:
        task_description: 任务描述，说明要执行的具体操作
        **params: 其他可选参数，根据具体任务需要传递
    """
    return tool_manager.tool_nucleic_acid_extractor(task_description, **params)



AVAILABLE_TOOLS = {
    "核酸提取仪": tool_nucleic_acid_extractor
}


# --- MCP协议通信主逻辑 ---
def nucleic_acid_extractor_server_main_loop():
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
            print(f"--- [nucleic_acid_extractor_Server] Error: {str(e)} ---", file=sys.stderr, flush=True)


def nucleic_acid_extractor_server_advertise_capabilities():
    """广播当前设备的MCP能力"""
    adv_message = {
        "jsonrpc": "2.0",
        "method": "protocol/advertise",
        "params": {
            "type": "server",
            "server": {
                "protocolVersion": "0.1.0",
                "displayName": "核酸提取仪",
                "capabilities": {
                    "tools": [
        {
            "name": "核酸提取仪",
            "description": "核酸提取仪是一种用于从生物样本中自动提取核酸（DNA 或 RNA）的设备。它利用磁珠法，通过自动化的操作流程，快速、高效地从样本中分离出纯净的核酸。在临床诊断、分子生物学研究等领域广泛应用。例如在新冠病毒检测中，核酸提取仪可以快速从咽拭子等样本中提取病毒核酸，为后续的核酸检测提供高质量的样本，提高检测效率和准确性。",
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
    print(f"--- [nucleic_acid_extractor_Server] 核酸提取仪 已就绪 ---", file=sys.stderr, flush=True)


if __name__ == "__main__":
    # 启动流程：先广播能力，再进入主循环
    nucleic_acid_extractor_server_advertise_capabilities()
    nucleic_acid_extractor_server_main_loop()
