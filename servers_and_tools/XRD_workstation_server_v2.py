import sys
import json
# 动态导入当前设备对应的工具类
from XRD_workstation_server_tools_v2 import UnifiedWorkstationTools


# 创建全局工具管理器实例
tool_manager = UnifiedWorkstationTools()


# --- 定义统一的工作站工具函数 ---
def tool_XRD_workstation(task_description: str, **params):
    """
    执行XRD工作站(ALD平台)的任务
    
    参数:
        task_description: 任务描述，说明要执行的具体操作
        **params: 其他可选参数，根据具体任务需要传递
    """
    return tool_manager.tool_XRD_workstation(task_description, **params)



AVAILABLE_TOOLS = {
    "XRD工作站(ALD平台)": tool_XRD_workstation
}


# --- MCP协议通信主逻辑 ---
def XRD_workstation_server_main_loop():
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
            print(f"--- [XRD_workstation_Server] Error: {str(e)} ---", file=sys.stderr, flush=True)


def XRD_workstation_server_advertise_capabilities():
    """广播当前设备的MCP能力"""
    adv_message = {
        "jsonrpc": "2.0",
        "method": "protocol/advertise",
        "params": {
            "type": "server",
            "server": {
                "protocolVersion": "0.1.0",
                "displayName": "XRD工作站(ALD平台)",
                "capabilities": {
                    "tools": [
        {
            "name": "XRD工作站(ALD平台)",
            "description": "X 射线衍射仪（XRD）主要用于分析物质的晶体结构、物相组成和晶体缺陷等。其工作原理是基于 X 射线与晶体中原子的相互作用产生衍射现象。当 X 射线照射到晶体样品上时，不同晶面会产生衍射，通过测量衍射峰的位置、强度和形状等信息，可以确定晶体的晶格常数、晶胞类型、原子坐标等晶体结构参数。同时，还能对多相混合物中的各相进行定性和定量分析。广泛应用于材料科学、地质学、化学、物理学等领域，是研究晶体材料性质和结构的重要工具。",
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
    print(f"--- [XRD_workstation_Server] XRD工作站(ALD平台) 已就绪 ---", file=sys.stderr, flush=True)


if __name__ == "__main__":
    # 启动流程：先广播能力，再进入主循环
    XRD_workstation_server_advertise_capabilities()
    XRD_workstation_server_main_loop()
