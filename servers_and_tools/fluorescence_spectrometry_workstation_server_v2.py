import sys
import json
# 动态导入当前设备对应的工具类
from fluorescence_spectrometry_workstation_server_tools_v2 import UnifiedWorkstationTools


# 创建全局工具管理器实例
tool_manager = UnifiedWorkstationTools()


# --- 定义统一的工作站工具函数 ---
def tool_fluorescence_spectrometry_workstation(task_description: str, **params):
    """
    执行荧光光谱工作站的任务
    
    参数:
        task_description: 任务描述，说明要执行的具体操作
        **params: 其他可选参数，根据具体任务需要传递
    """
    return tool_manager.tool_fluorescence_spectrometry_workstation(task_description, **params)



AVAILABLE_TOOLS = {
    "荧光光谱工作站": tool_fluorescence_spectrometry_workstation
}


# --- MCP协议通信主逻辑 ---
def fluorescence_spectrometry_workstation_server_main_loop():
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
            print(f"--- [fluorescence_spectrometry_workstation_Server] Error: {str(e)} ---", file=sys.stderr, flush=True)


def fluorescence_spectrometry_workstation_server_advertise_capabilities():
    """广播当前设备的MCP能力"""
    adv_message = {
        "jsonrpc": "2.0",
        "method": "protocol/advertise",
        "params": {
            "type": "server",
            "server": {
                "protocolVersion": "0.1.0",
                "displayName": "荧光光谱工作站",
                "capabilities": {
                    "tools": [
        {
            "name": "荧光光谱工作站",
            "description": "分子荧光光谱仪是一种用于分析物质分子结构和性质的仪器。它基于物质分子吸收光能后发射出荧光的原理工作。在大学实验室的化学分析中，可用于检测和定量分析具有荧光特性的化合物，如多环芳烃、某些生物分子等。通过测量荧光的发射波长、强度和寿命等参数，可以获取分子的电子结构、化学键信息以及分子间相互作用等情况，对于研究有机化合物的结构鉴定、药物分析等方面有着重要作用。",
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
    print(f"--- [fluorescence_spectrometry_workstation_Server] 荧光光谱工作站 已就绪 ---", file=sys.stderr, flush=True)


if __name__ == "__main__":
    # 启动流程：先广播能力，再进入主循环
    fluorescence_spectrometry_workstation_server_advertise_capabilities()
    fluorescence_spectrometry_workstation_server_main_loop()
