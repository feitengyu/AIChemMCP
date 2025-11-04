import sys
import json
# 动态导入当前设备对应的工具类（与主服务器文件同目录）
from tools.massSpectrometer_server_tools import ActionServerTools


# 创建全局工具管理器实例
tool_manager = ActionServerTools()


# --- 定义设备动作函数（自动生成，与工具类方法对应）---
def tool_from_liquid_chromatography_to_mass_spectrometry(**params):
    return tool_manager.tool_from_liquid_chromatography_to_mass_spectrometry(**params)


def tool_massSpectrometer(**params):
    return tool_manager.tool_massSpectrometer(**params)


def tool_from_liquid_chromatography_to_liquid_nitorgen(**params):
    return tool_manager.tool_from_liquid_chromatography_to_liquid_nitorgen(**params)



AVAILABLE_TOOLS_ACTION = {
    "from_liquid_chromatography_to_mass_spectrometry": tool_from_liquid_chromatography_to_mass_spectrometry,
    "massSpectrometer": tool_massSpectrometer,
    "from_liquid_chromatography_to_liquid_nitorgen": tool_from_liquid_chromatography_to_liquid_nitorgen
}


# --- MCP协议通信主逻辑（自动适配当前设备）---
def massSpectrometer_server_main_loop():
    """主循环：监听并响应Host的MCP协议请求"""
    for line in sys.stdin:
        try:
            request = json.loads(line)
            request_id = request.get("id")
            method_name = request.get("method")
            params = request.get("params", {})

            if method_name in AVAILABLE_TOOLS_ACTION:
                # 调用对应的工具函数（传递请求参数）
                tool_function = AVAILABLE_TOOLS_ACTION[method_name]
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

            # 响应结果（强制刷新缓冲区）
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
            print(f"--- [massSpectrometer_Server] Critical Error: {str(e)} ---", file=sys.stderr, flush=True)


def massSpectrometer_server_advertise_capabilities():
    """广播当前设备的MCP能力（设备信息、支持的动作）"""
    adv_message = {
        "jsonrpc": "2.0",
        "method": "protocol/advertise",
        "params": {
            "type": "server",
            "server": {
                "protocolVersion": "0.1.0",
                "displayName": "质谱工作站",
                "capabilities": {
                    "tools": [
        {
            "name": "from_liquid_chromatography_to_mass_spectrometry",
            "description": "从液相色谱仪纯化后的num个瓶子转移到质谱仪的西林瓶中",
            "parameters": {
                "type": "object",
                "properties": {
    "data": {
        "type": "string",
        "description": "data"
    },
    "num": {
        "type": "int",
        "description": "num"
    },
    "temp": {
        "type": "int",
        "description": "temp"
    }
},
                "required": ["data", "num", "temp"]
            }
        },
        {
            "name": "massSpectrometer",
            "description": "启动质谱仪",
            "parameters": {
                "type": "object",
                "properties": {
    "data": {
        "type": "string",
        "description": "data"
    },
    "temp": {
        "type": "int",
        "description": "temp"
    },
    "resultCode": {
        "type": "file",
        "description": "resultCode"
    }
},
                "required": ["data", "temp"]
            }
        },
        {
            "name": "from_liquid_chromatography_to_liquid_nitorgen",
            "description": "质谱仪运行出结果后，从液相色谱仪纯化后的第几号瓶子转移到液氮盆",
            "parameters": {
                "type": "object",
                "properties": {
    "data": {
        "type": "string",
        "description": "data"
    },
    "num": {
        "type": "int",
        "description": "num"
    },
    "temp": {
        "type": "int",
        "description": "temp"
    }
},
                "required": ["data", "num", "temp"]
            }
        }
                    ]
                }
            }
        }
    }
    print(json.dumps(adv_message, ensure_ascii=False), flush=True)
    print(f"--- [massSpectrometer_Server] 质谱工作站 is ready. ---", file=sys.stderr, flush=True)


if __name__ == "__main__":
    # 启动流程：先广播能力，再进入主循环
    massSpectrometer_server_advertise_capabilities()
    massSpectrometer_server_main_loop()
