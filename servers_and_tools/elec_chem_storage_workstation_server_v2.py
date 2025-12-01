import sys
import json
# 动态导入当前设备对应的工具类
from elec_chem_storage_workstation_server_tools_v2 import UnifiedWorkstationTools


# 创建全局工具管理器实例
tool_manager = UnifiedWorkstationTools()


# --- 定义统一的工作站工具函数 ---
def tool_elec_chem_storage_workstation(task_description: str, **params):
    """
    执行置物工作站的任务
    
    参数:
        task_description: 任务描述，说明要执行的具体操作
        **params: 其他可选参数，根据具体任务需要传递
    """
    return tool_manager.tool_elec_chem_storage_workstation(task_description, **params)



AVAILABLE_TOOLS = {
    "置物工作站": tool_elec_chem_storage_workstation
}


# --- MCP协议通信主逻辑 ---
def elec_chem_storage_workstation_server_main_loop():
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
            print(f"--- [elec_chem_storage_workstation_Server] Error: {str(e)} ---", file=sys.stderr, flush=True)


def elec_chem_storage_workstation_server_advertise_capabilities():
    """广播当前设备的MCP能力"""
    adv_message = {
        "jsonrpc": "2.0",
        "method": "protocol/advertise",
        "params": {
            "type": "server",
            "server": {
                "protocolVersion": "0.1.0",
                "displayName": "置物工作站",
                "capabilities": {
                    "tools": [
        {
            "name": "置物工作站",
            "description": "样品静置工作站为样品提供一个稳定、安静的环境，用于样品的静置和平衡。在一些实验中，样品在处理后需要一定的时间进行静置，以达到稳定的状态或使某些反应充分进行。该工作站可以精确控制环境的温度、湿度等条件，确保样品在静置过程中不受外界干扰。例如在一些化学分析实验中，样品在混合或反应后需要静置一段时间以达到均匀的状态，样品静置工作站能够提供适宜的条件，保证实验结果的准确性。",
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
    print(f"--- [elec_chem_storage_workstation_Server] 置物工作站 已就绪 ---", file=sys.stderr, flush=True)


if __name__ == "__main__":
    # 启动流程：先广播能力，再进入主循环
    elec_chem_storage_workstation_server_advertise_capabilities()
    elec_chem_storage_workstation_server_main_loop()
