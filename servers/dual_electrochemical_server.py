import sys
import json
# 动态导入当前设备对应的工具类（与主服务器文件同目录）
from tools.dual_electrochemical_server_tools import ActionServerTools


# 创建全局工具管理器实例
tool_manager = ActionServerTools()


# --- 定义设备动作函数（自动生成，与工具类方法对应）---
def tool_detection(**params):
    return tool_manager.tool_detection(**params)



AVAILABLE_TOOLS_ACTION = {
    "detection": tool_detection
}


# --- MCP协议通信主逻辑（自动适配当前设备）---
def dual_electrochemical_server_main_loop():
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
            print(f"--- [dual_electrochemical_Server] Critical Error: {str(e)} ---", file=sys.stderr, flush=True)


def dual_electrochemical_server_advertise_capabilities():
    """广播当前设备的MCP能力（设备信息、支持的动作）"""
    adv_message = {
        "jsonrpc": "2.0",
        "method": "protocol/advertise",
        "params": {
            "type": "server",
            "server": {
                "protocolVersion": "0.1.0",
                "displayName": "双工位电化学工作站",
                "capabilities": {
                    "tools": [
        {
            "name": "detection",
            "description": "电化学检测",
            "parameters": {
                "type": "object",
                "properties": {
    "pool": {
        "type": "int",
        "description": "电解池编号",
        "enum": [
            "1",
            "2"
        ]
    },
    "polish": {
        "type": "int",
        "description": "打磨时间（单位：分钟）",
        "minimum": "1",
        "maximum": "10"
    },
    "soakTime": {
        "type": "int",
        "description": "浸泡时间（单位：分钟）",
        "minimum": "1",
        "maximum": "10"
    },
    "electrolyteAdded": {
        "type": "int",
        "description": "电解液加入量（单位：毫升）",
        "minimum": "0",
        "maximum": "255"
    },
    "aerateTime": {
        "type": "int",
        "description": "通气时长（单位：分钟）",
        "minimum": "1",
        "maximum": "50"
    },
    "washingAdded": {
        "type": "int",
        "description": "清洗液加液量",
        "minimum": "0",
        "maximum": "255"
    },
    "speed": {
        "type": "int",
        "description": "磁力搅拌速度",
        "minimum": "500",
        "maximum": "2000"
    },
    "cleanTime": {
        "type": "int",
        "description": "清洗时间（单位：秒）",
        "minimum": "1",
        "maximum": "65535"
    },
    "cycles": {
        "type": "int",
        "description": "清洗次数",
        "minimum": "1",
        "maximum": "255"
    },
    "cyclicVoltammetry": {
        "type": "object",
        "description": "循环伏安法",
        "properties": {
            "isUse": {
                "type": "int",
                "description": "是否使用",
                "enum": [
                    {
                        "label": "是",
                        "value": "1"
                    },
                    {
                        "label": "否",
                        "value": "0"
                    }
                ]
            },
            "initE": {
                "type": "float",
                "description": "初始电位",
                "minimum": "-10",
                "maximum": "10"
            },
            "finalE": {
                "type": "float",
                "description": "终点电位",
                "minimum": "-10",
                "maximum": "10"
            },
            "highE": {
                "type": "float",
                "description": "上限电位",
                "minimum": "-10",
                "maximum": "10"
            },
            "lowE": {
                "type": "float",
                "description": "下限电位",
                "minimum": "-10",
                "maximum": "10"
            },
            "initialScanPolarity": {
                "type": "string",
                "description": "初始化扫码方向",
                "enum": [
                    {
                        "label": "正极",
                        "value": "p"
                    },
                    {
                        "label": "负极",
                        "value": "n"
                    }
                ]
            },
            "scanRate": {
                "type": "float",
                "description": "扫描速度",
                "minimum": "0.000001",
                "maximum": "10000"
            },
            "sweepSegments": {
                "type": "int",
                "description": "扫描段数",
                "minimum": "1",
                "maximum": "10000"
            },
            "sampleInterval": {
                "type": "float",
                "description": "采样间隔",
                "minimum": "0.001",
                "maximum": "0.064"
            },
            "quietTime": {
                "type": "int",
                "description": "静置时间",
                "minimum": "1",
                "maximum": "100000"
            },
            "sensitivity": {
                "type": "float",
                "description": "灵敏度",
                "minimum": "0.000000000001",
                "maximum": "0.1"
            }
        },
        "required": [
            "isUse"
        ]
    },
    "cyclicVoltammetry.isUse": {
        "type": "int",
        "description": "是否使用",
        "enum": [
            {
                "label": "是",
                "value": "1"
            },
            {
                "label": "否",
                "value": "0"
            }
        ]
    },
    "cyclicVoltammetry.initE": {
        "type": "float",
        "description": "初始电位",
        "minimum": "-10",
        "maximum": "10"
    },
    "cyclicVoltammetry.finalE": {
        "type": "float",
        "description": "终点电位",
        "minimum": "-10",
        "maximum": "10"
    },
    "cyclicVoltammetry.highE": {
        "type": "float",
        "description": "上限电位",
        "minimum": "-10",
        "maximum": "10"
    },
    "cyclicVoltammetry.lowE": {
        "type": "float",
        "description": "下限电位",
        "minimum": "-10",
        "maximum": "10"
    },
    "cyclicVoltammetry.initialScanPolarity": {
        "type": "string",
        "description": "初始化扫码方向",
        "enum": [
            {
                "label": "正极",
                "value": "p"
            },
            {
                "label": "负极",
                "value": "n"
            }
        ]
    },
    "cyclicVoltammetry.scanRate": {
        "type": "float",
        "description": "扫描速度",
        "minimum": "0.000001",
        "maximum": "10000"
    },
    "cyclicVoltammetry.sweepSegments": {
        "type": "int",
        "description": "扫描段数",
        "minimum": "1",
        "maximum": "10000"
    },
    "cyclicVoltammetry.sampleInterval": {
        "type": "float",
        "description": "采样间隔",
        "minimum": "0.001",
        "maximum": "0.064"
    },
    "cyclicVoltammetry.quietTime": {
        "type": "int",
        "description": "静置时间",
        "minimum": "1",
        "maximum": "100000"
    },
    "cyclicVoltammetry.sensitivity": {
        "type": "float",
        "description": "灵敏度",
        "minimum": "0.000000000001",
        "maximum": "0.1"
    },
    "linearSweepVoltammetry": {
        "type": "object",
        "description": "线性扫描伏安",
        "properties": {
            "isUse": {
                "type": "int",
                "description": "是否使用",
                "enum": [
                    {
                        "label": "是",
                        "value": "1"
                    },
                    {
                        "label": "否",
                        "value": "0"
                    }
                ]
            },
            "initE": {
                "type": "float",
                "description": "初始电位",
                "minimum": "-10",
                "maximum": "10"
            },
            "finalE": {
                "type": "float",
                "description": "终点电位",
                "minimum": "-10",
                "maximum": "10"
            },
            "scanRate": {
                "type": "float",
                "description": "扫描速度",
                "minimum": "0.000001",
                "maximum": "10000"
            },
            "sampleInterval": {
                "type": "float",
                "description": "采样间隔",
                "minimum": "0.001",
                "maximum": "0.064"
            },
            "quietTime": {
                "type": "int",
                "description": "静置时间",
                "minimum": "1",
                "maximum": "100000"
            },
            "sensitivity": {
                "type": "float",
                "description": "灵敏度",
                "minimum": "0.000000000001",
                "maximum": "0.1"
            }
        },
        "required": [
            "isUse"
        ]
    },
    "linearSweepVoltammetry.isUse": {
        "type": "int",
        "description": "是否使用",
        "enum": [
            {
                "label": "是",
                "value": "1"
            },
            {
                "label": "否",
                "value": "0"
            }
        ]
    },
    "linearSweepVoltammetry.initE": {
        "type": "float",
        "description": "初始电位",
        "minimum": "-10",
        "maximum": "10"
    },
    "linearSweepVoltammetry.finalE": {
        "type": "float",
        "description": "终点电位",
        "minimum": "-10",
        "maximum": "10"
    },
    "linearSweepVoltammetry.scanRate": {
        "type": "float",
        "description": "扫描速度",
        "minimum": "0.000001",
        "maximum": "10000"
    },
    "linearSweepVoltammetry.sampleInterval": {
        "type": "float",
        "description": "采样间隔",
        "minimum": "0.001",
        "maximum": "0.064"
    },
    "linearSweepVoltammetry.quietTime": {
        "type": "int",
        "description": "静置时间",
        "minimum": "1",
        "maximum": "100000"
    },
    "linearSweepVoltammetry.sensitivity": {
        "type": "float",
        "description": "灵敏度",
        "minimum": "0.000000000001",
        "maximum": "0.1"
    },
    "amperometricITCurve": {
        "type": "object",
        "description": "电流-时间曲线",
        "properties": {
            "isUse": {
                "type": "int",
                "description": "是否使用",
                "enum": [
                    {
                        "label": "是",
                        "value": "1"
                    },
                    {
                        "label": "否",
                        "value": "0"
                    }
                ]
            },
            "initE": {
                "type": "float",
                "description": "初始电位",
                "minimum": "-10",
                "maximum": "10"
            },
            "sampleInterval": {
                "type": "float",
                "description": "采样间隔",
                "minimum": "0.0000004",
                "maximum": "50"
            },
            "runTime": {
                "type": "int",
                "description": "运行时间",
                "minimum": "1",
                "maximum": "1000000"
            },
            "quietTime": {
                "type": "int",
                "description": "静置时间",
                "minimum": "1",
                "maximum": "100000"
            },
            "scalesDuringRun": {
                "type": "int",
                "description": "实验中电流量程档数",
                "enum": [
                    "1",
                    "2",
                    "3"
                ]
            },
            "sensitivity": {
                "type": "float",
                "description": "灵敏度",
                "minimum": "0.000000000001",
                "maximum": "0.1"
            }
        },
        "required": [
            "isUse"
        ]
    },
    "amperometricITCurve.isUse": {
        "type": "int",
        "description": "是否使用",
        "enum": [
            {
                "label": "是",
                "value": "1"
            },
            {
                "label": "否",
                "value": "0"
            }
        ]
    },
    "amperometricITCurve.initE": {
        "type": "float",
        "description": "初始电位",
        "minimum": "-10",
        "maximum": "10"
    },
    "amperometricITCurve.sampleInterval": {
        "type": "float",
        "description": "采样间隔",
        "minimum": "0.0000004",
        "maximum": "50"
    },
    "amperometricITCurve.runTime": {
        "type": "int",
        "description": "运行时间",
        "minimum": "1",
        "maximum": "1000000"
    },
    "amperometricITCurve.quietTime": {
        "type": "int",
        "description": "静置时间",
        "minimum": "1",
        "maximum": "100000"
    },
    "amperometricITCurve.scalesDuringRun": {
        "type": "int",
        "description": "实验中电流量程档数",
        "enum": [
            "1",
            "2",
            "3"
        ]
    },
    "amperometricITCurve.sensitivity": {
        "type": "float",
        "description": "灵敏度",
        "minimum": "0.000000000001",
        "maximum": "0.1"
    },
    "acImpedanceMeasurement": {
        "type": "object",
        "description": "交流阻抗测量",
        "properties": {
            "isUse": {
                "type": "int",
                "description": "是否使用",
                "enum": [
                    {
                        "label": "是",
                        "value": "1"
                    },
                    {
                        "label": "否",
                        "value": "0"
                    }
                ]
            },
            "initE": {
                "type": "float",
                "description": "初始电位",
                "minimum": "-10",
                "maximum": "10"
            },
            "amplitude": {
                "type": "float",
                "description": "振幅",
                "minimum": "0.001",
                "maximum": "0.7"
            },
            "highFrequency": {
                "type": "int",
                "description": "上限频率",
                "minimum": "0.0001",
                "maximum": "3000000"
            },
            "lowFrequency": {
                "type": "int",
                "description": "下限频率",
                "minimum": "0.00001",
                "maximum": "100000"
            },
            "quietTime": {
                "type": "int",
                "description": "静置时间",
                "minimum": "1",
                "maximum": "100000"
            }
        },
        "required": [
            "isUse"
        ]
    },
    "acImpedanceMeasurement.isUse": {
        "type": "int",
        "description": "是否使用",
        "enum": [
            {
                "label": "是",
                "value": "1"
            },
            {
                "label": "否",
                "value": "0"
            }
        ]
    },
    "acImpedanceMeasurement.initE": {
        "type": "float",
        "description": "初始电位",
        "minimum": "-10",
        "maximum": "10"
    },
    "acImpedanceMeasurement.amplitude": {
        "type": "float",
        "description": "振幅",
        "minimum": "0.001",
        "maximum": "0.7"
    },
    "acImpedanceMeasurement.highFrequency": {
        "type": "int",
        "description": "上限频率",
        "minimum": "0.0001",
        "maximum": "3000000"
    },
    "acImpedanceMeasurement.lowFrequency": {
        "type": "int",
        "description": "下限频率",
        "minimum": "0.00001",
        "maximum": "100000"
    },
    "acImpedanceMeasurement.quietTime": {
        "type": "int",
        "description": "静置时间",
        "minimum": "1",
        "maximum": "100000"
    },
    "electResult": {
        "type": "file",
        "description": "电化学结果"
    }
},
                "required": ["pool", "polish", "soakTime", "electrolyteAdded", "aerateTime", "washingAdded", "speed", "cleanTime", "cycles", "cyclicVoltammetry.isUse", "linearSweepVoltammetry.isUse", "amperometricITCurve.isUse", "acImpedanceMeasurement.isUse"]
            }
        }
                    ]
                }
            }
        }
    }
    print(json.dumps(adv_message, ensure_ascii=False), flush=True)
    print(f"--- [dual_electrochemical_Server] 双工位电化学工作站 is ready. ---", file=sys.stderr, flush=True)


if __name__ == "__main__":
    # 启动流程：先广播能力，再进入主循环
    dual_electrochemical_server_advertise_capabilities()
    dual_electrochemical_server_main_loop()
