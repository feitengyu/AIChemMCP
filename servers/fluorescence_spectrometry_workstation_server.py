import sys
import json
# 动态导入当前设备对应的工具类（与主服务器文件同目录）
from tools.fluorescence_spectrometry_workstation_server_tools import ActionServerTools


# 创建全局工具管理器实例
tool_manager = ActionServerTools()


# --- 定义设备动作函数（自动生成，与工具类方法对应）---
def tool_setup(**params):
    return tool_manager.tool_setup(**params)


def tool_start(**params):
    return tool_manager.tool_start(**params)


def tool_light_on(**params):
    return tool_manager.tool_light_on(**params)


def tool_light_off(**params):
    return tool_manager.tool_light_off(**params)


def tool_drain(**params):
    return tool_manager.tool_drain(**params)


def tool_sample_injection_reset(**params):
    return tool_manager.tool_sample_injection_reset(**params)


def tool_sample_injection_start(**params):
    return tool_manager.tool_sample_injection_start(**params)


def tool_sample_injection_waste(**params):
    return tool_manager.tool_sample_injection_waste(**params)



AVAILABLE_TOOLS_ACTION = {
    "setup": tool_setup,
    "start": tool_start,
    "light_on": tool_light_on,
    "light_off": tool_light_off,
    "drain": tool_drain,
    "sample_injection_reset": tool_sample_injection_reset,
    "sample_injection_start": tool_sample_injection_start,
    "sample_injection_waste": tool_sample_injection_waste
}


# --- MCP协议通信主逻辑（自动适配当前设备）---
def fluorescence_spectrometry_workstation_server_main_loop():
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
            print(f"--- [fluorescence_spectrometry_workstation_Server] Critical Error: {str(e)} ---", file=sys.stderr, flush=True)


def fluorescence_spectrometry_workstation_server_advertise_capabilities():
    """广播当前设备的MCP能力（设备信息、支持的动作）"""
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
            "name": "setup",
            "description": "参数配置",
            "parameters": {
                "type": "object",
                "properties": {
    "operation": {
        "type": "string",
        "description": "操作符"
    },
    "spectrum_type": {
        "type": "string",
        "description": "光谱测定参数",
        "enum": [
            "fashe",
            "jifa",
            "tongbu"
        ]
    },
    "excitation_wavelength": {
        "type": "int",
        "description": "激发光波长(nm)",
        "minimum": "200",
        "maximum": "900"
    },
    "emission_start_wavelength": {
        "type": "int",
        "description": "发射波开始波长(nm)",
        "minimum": "200",
        "maximum": "900"
    },
    "emission_end_wavelength": {
        "type": "int",
        "description": "发射波结束波长(nm)",
        "minimum": "200",
        "maximum": "900"
    },
    "wavelength_interval": {
        "type": "string",
        "description": "数据间隔(nm)",
        "enum": [
            "0.1",
            "0.2",
            "0.5",
            "1.0",
            "2.0",
            "5.0",
            "10"
        ]
    },
    "scan_speed": {
        "type": "string",
        "description": "扫描速度(nm/min)",
        "enum": [
            "20",
            "60",
            "200",
            "600",
            "2000",
            "6000",
            "12000",
            "30000",
            "60000"
        ]
    }
},
                "required": ["operation", "spectrum_type", "excitation_wavelength", "emission_start_wavelength", "emission_end_wavelength", "wavelength_interval", "scan_speed"]
            }
        },
        {
            "name": "start",
            "description": "开始进样",
            "parameters": {
                "type": "object",
                "properties": {
    "operation": {
        "type": "string",
        "description": "操作符"
    },
    "resultCode": {
        "type": "file",
        "description": "resultCode"
    }
},
                "required": ["operation", "resultCode"]
            }
        },
        {
            "name": "light_on",
            "description": "开灯",
            "parameters": {
                "type": "object",
                "properties": {
    "operation": {
        "type": "string",
        "description": "操作符"
    }
},
                "required": ["operation"]
            }
        },
        {
            "name": "light_off",
            "description": "关灯",
            "parameters": {
                "type": "object",
                "properties": {
    "operation": {
        "type": "string",
        "description": "操作符"
    }
},
                "required": ["operation"]
            }
        },
        {
            "name": "drain",
            "description": "清洗",
            "parameters": {
                "type": "object",
                "properties": {
    "operation": {
        "type": "string",
        "description": "操作符"
    }
},
                "required": ["operation"]
            }
        },
        {
            "name": "sample_injection_reset",
            "description": "进样器复位",
            "parameters": {
                "type": "object",
                "properties": {
    "operation": {
        "type": "string",
        "description": "操作符"
    }
},
                "required": ["operation"]
            }
        },
        {
            "name": "sample_injection_start",
            "description": "进样器吸液",
            "parameters": {
                "type": "object",
                "properties": {
    "operation": {
        "type": "string",
        "description": "操作符"
    }
},
                "required": ["operation"]
            }
        },
        {
            "name": "sample_injection_waste",
            "description": "进样器清洗",
            "parameters": {
                "type": "object",
                "properties": {
    "operation": {
        "type": "string",
        "description": "操作符"
    }
},
                "required": ["operation"]
            }
        }
                    ]
                }
            }
        }
    }
    print(json.dumps(adv_message, ensure_ascii=False), flush=True)
    print(f"--- [fluorescence_spectrometry_workstation_Server] 荧光光谱工作站 is ready. ---", file=sys.stderr, flush=True)


if __name__ == "__main__":
    # 启动流程：先广播能力，再进入主循环
    fluorescence_spectrometry_workstation_server_advertise_capabilities()
    fluorescence_spectrometry_workstation_server_main_loop()
