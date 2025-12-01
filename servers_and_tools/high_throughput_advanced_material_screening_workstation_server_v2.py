import sys
import json
# 动态导入当前设备对应的工具类
from high_throughput_advanced_material_screening_workstation_server_tools_v2 import UnifiedWorkstationTools


# 创建全局工具管理器实例
tool_manager = UnifiedWorkstationTools()


# --- 定义统一的工作站工具函数 ---
def tool_high_throughput_advanced_material_screening_workstation(task_description: str, **params):
    """
    执行高通量电化学筛选工作站的任务
    
    参数:
        task_description: 任务描述，说明要执行的具体操作
        **params: 其他可选参数，根据具体任务需要传递
    """
    return tool_manager.tool_high_throughput_advanced_material_screening_workstation(task_description, **params)



AVAILABLE_TOOLS = {
    "高通量电化学筛选工作站": tool_high_throughput_advanced_material_screening_workstation
}


# --- MCP协议通信主逻辑 ---
def high_throughput_advanced_material_screening_workstation_server_main_loop():
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
            print(f"--- [high_throughput_advanced_material_screening_workstation_Server] Error: {str(e)} ---", file=sys.stderr, flush=True)


def high_throughput_advanced_material_screening_workstation_server_advertise_capabilities():
    """广播当前设备的MCP能力"""
    adv_message = {
        "jsonrpc": "2.0",
        "method": "protocol/advertise",
        "params": {
            "type": "server",
            "server": {
                "protocolVersion": "0.1.0",
                "displayName": "高通量电化学筛选工作站",
                "capabilities": {
                    "tools": [
        {
            "name": "高通量电化学筛选工作站",
            "description": "高通量先进材料筛选工作站能够快速、高效地对大量不同的材料样品进行性能筛选和评估。它集成了多种分析测试设备和自动化操作系统，可以对材料的物理性能（如强度、硬度、导电性等）、化学性能（如耐腐蚀性、催化活性等）进行同时测试。在材料研发中，可大大缩短材料筛选的周期，快速找到具有优良性能的材料，为新材料的开发和应用提供有力支持，例如在新能源材料、电子信息材料等领域的研发中具有重要应用。",
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
    print(f"--- [high_throughput_advanced_material_screening_workstation_Server] 高通量电化学筛选工作站 已就绪 ---", file=sys.stderr, flush=True)


if __name__ == "__main__":
    # 启动流程：先广播能力，再进入主循环
    high_throughput_advanced_material_screening_workstation_server_advertise_capabilities()
    high_throughput_advanced_material_screening_workstation_server_main_loop()
