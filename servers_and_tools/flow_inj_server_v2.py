import sys
import json
# 动态导入当前设备对应的工具类
from flow_inj_server_tools_v2 import UnifiedWorkstationTools


# 创建全局工具管理器实例
tool_manager = UnifiedWorkstationTools()


# --- 定义统一的工作站工具函数 ---
def tool_flow_inj(task_description: str, **params):
    """
    执行流动注射仪的任务
    
    参数:
        task_description: 任务描述，说明要执行的具体操作
        **params: 其他可选参数，根据具体任务需要传递
    """
    return tool_manager.tool_flow_inj(task_description, **params)



AVAILABLE_TOOLS = {
    "流动注射仪": tool_flow_inj
}


# --- MCP协议通信主逻辑 ---
def flow_inj_server_main_loop():
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
            print(f"--- [flow_inj_Server] Error: {str(e)} ---", file=sys.stderr, flush=True)


def flow_inj_server_advertise_capabilities():
    """广播当前设备的MCP能力"""
    adv_message = {
        "jsonrpc": "2.0",
        "method": "protocol/advertise",
        "params": {
            "type": "server",
            "server": {
                "protocolVersion": "0.1.0",
                "displayName": "流动注射仪",
                "capabilities": {
                    "tools": [
        {
            "name": "流动注射仪",
            "description": "SUPEC 5011流动注射分析系统主要适用于饮用水、地表水、地下水生活污水和工业废水中硫化物的分析。其中，使用亚甲基蓝分光光度法的测定范围为0.016mg/L~2.00mg/L，检出限为0.004mg/L(以S2-计)。
其工作原理为：在封闭的管路中，将一定体积的样品注射到一个流动的、无空气间隔的连续载流中，样品与试剂在分析模块中按选定的顺序和比例混合、反应，在非完全反应的条件下，进入流动检测池进行光度检测，定量测定样品中被测物质的含量。
其性能优势在于：便携性：体积小，重量轻，方便携带；灵动性：仪器可搭配不同型号的自动进样器，应用于常规实验室；同时配合便携箱，用于现场应急监测。实现批量自动、在线连续检测。",
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
    print(f"--- [flow_inj_Server] 流动注射仪 已就绪 ---", file=sys.stderr, flush=True)


if __name__ == "__main__":
    # 启动流程：先广播能力，再进入主循环
    flow_inj_server_advertise_capabilities()
    flow_inj_server_main_loop()
