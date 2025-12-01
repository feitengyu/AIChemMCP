import sys
import json
# 动态导入当前设备对应的工具类
from UV_spectrophotometer_workstation_server_tools_v2 import UnifiedWorkstationTools


# 创建全局工具管理器实例
tool_manager = UnifiedWorkstationTools()


# --- 定义统一的工作站工具函数 ---
def tool_UV_spectrophotometer_workstation(task_description: str, **params):
    """
    执行紫外光谱工作站的任务
    
    参数:
        task_description: 任务描述，说明要执行的具体操作
        **params: 其他可选参数，根据具体任务需要传递
    """
    return tool_manager.tool_UV_spectrophotometer_workstation(task_description, **params)



AVAILABLE_TOOLS = {
    "紫外光谱工作站": tool_UV_spectrophotometer_workstation
}


# --- MCP协议通信主逻辑 ---
def UV_spectrophotometer_workstation_server_main_loop():
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
            print(f"--- [UV_spectrophotometer_workstation_Server] Error: {str(e)} ---", file=sys.stderr, flush=True)


def UV_spectrophotometer_workstation_server_advertise_capabilities():
    """广播当前设备的MCP能力"""
    adv_message = {
        "jsonrpc": "2.0",
        "method": "protocol/advertise",
        "params": {
            "type": "server",
            "server": {
                "protocolVersion": "0.1.0",
                "displayName": "紫外光谱工作站",
                "capabilities": {
                    "tools": [
        {
            "name": "紫外光谱工作站",
            "description": "紫外 - 可见分光光度计利用物质对紫外和可见光的吸收特性来进行分析。不同的物质对不同波长的光有特定的吸收峰，通过测量样品在不同波长下的吸光度，可以对物质进行定性和定量分析。在化学实验中，可用于测定溶液中物质的浓度，例如分析金属离子的含量。在生物领域，能检测核酸、蛋白质等生物大分子的浓度和纯度，为生物实验提供关键的数据支持。",
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
    print(f"--- [UV_spectrophotometer_workstation_Server] 紫外光谱工作站 已就绪 ---", file=sys.stderr, flush=True)


if __name__ == "__main__":
    # 启动流程：先广播能力，再进入主循环
    UV_spectrophotometer_workstation_server_advertise_capabilities()
    UV_spectrophotometer_workstation_server_main_loop()
