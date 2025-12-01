import sys
import json
# 动态导入当前设备对应的工具类
from peptideSynthesizer_server_tools_v2 import UnifiedWorkstationTools


# 创建全局工具管理器实例
tool_manager = UnifiedWorkstationTools()


# --- 定义统一的工作站工具函数 ---
def tool_peptideSynthesizer(task_description: str, **params):
    """
    执行多肽合成仪的任务
    
    参数:
        task_description: 任务描述，说明要执行的具体操作
        **params: 其他可选参数，根据具体任务需要传递
    """
    return tool_manager.tool_peptideSynthesizer(task_description, **params)



AVAILABLE_TOOLS = {
    "多肽合成仪": tool_peptideSynthesizer
}


# --- MCP协议通信主逻辑 ---
def peptideSynthesizer_server_main_loop():
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
            print(f"--- [peptideSynthesizer_Server] Error: {str(e)} ---", file=sys.stderr, flush=True)


def peptideSynthesizer_server_advertise_capabilities():
    """广播当前设备的MCP能力"""
    adv_message = {
        "jsonrpc": "2.0",
        "method": "protocol/advertise",
        "params": {
            "type": "server",
            "server": {
                "protocolVersion": "0.1.0",
                "displayName": "多肽合成仪",
                "capabilities": {
                    "tools": [
        {
            "name": "多肽合成仪",
            "description": "全自动多肽合成仪是一种用于自动合成多肽的设备。它按照预先设定的氨基酸序列，通过化学反应逐步将氨基酸连接起来，形成多肽链。该仪器具有高度自动化的特点，能够精确控制反应条件，如温度、试剂比例等，确保多肽合成的准确性和效率。在生物制药、蛋白质研究等领域有着重要应用。例如在药物研发中，可以利用它合成具有特定功能的多肽药物，为新药的开发提供支持。",
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
    print(f"--- [peptideSynthesizer_Server] 多肽合成仪 已就绪 ---", file=sys.stderr, flush=True)


if __name__ == "__main__":
    # 启动流程：先广播能力，再进入主循环
    peptideSynthesizer_server_advertise_capabilities()
    peptideSynthesizer_server_main_loop()
