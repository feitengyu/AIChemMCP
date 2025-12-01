import sys
import json
# 动态导入当前设备对应的工具类
from toLC_server_tools_v2 import UnifiedWorkstationTools


# 创建全局工具管理器实例
tool_manager = UnifiedWorkstationTools()


# --- 定义统一的工作站工具函数 ---
def tool_toLC(task_description: str, **params):
    """
    执行色谱工作站的任务
    
    参数:
        task_description: 任务描述，说明要执行的具体操作
        **params: 其他可选参数，根据具体任务需要传递
    """
    return tool_manager.tool_toLC(task_description, **params)



AVAILABLE_TOOLS = {
    "色谱工作站": tool_toLC
}


# --- MCP协议通信主逻辑 ---
def toLC_server_main_loop():
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
            print(f"--- [toLC_Server] Error: {str(e)} ---", file=sys.stderr, flush=True)


def toLC_server_advertise_capabilities():
    """广播当前设备的MCP能力"""
    adv_message = {
        "jsonrpc": "2.0",
        "method": "protocol/advertise",
        "params": {
            "type": "server",
            "server": {
                "protocolVersion": "0.1.0",
                "displayName": "色谱工作站",
                "capabilities": {
                    "tools": [
        {
            "name": "色谱工作站",
            "description": "制备型液相色谱仪主要用于从复杂混合物中分离和制备大量的目标化合物。它具有较大的分离柱和较高的样品负载能力。在天然产物研究中，可从植物提取物等复杂样品中分离出具有生物活性的化合物，为药物研发提供足够量的纯品进行进一步的研究和开发。通过优化色谱条件，可以实现高纯度和高产量的目标化合物制备，满足科研和生产对大量纯化合物的需求。",
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
    print(f"--- [toLC_Server] 色谱工作站 已就绪 ---", file=sys.stderr, flush=True)


if __name__ == "__main__":
    # 启动流程：先广播能力，再进入主循环
    toLC_server_advertise_capabilities()
    toLC_server_main_loop()
