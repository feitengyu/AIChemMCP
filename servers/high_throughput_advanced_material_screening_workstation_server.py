import sys
import json
# 动态导入当前设备对应的工具类（与主服务器文件同目录）
from high_throughput_advanced_material_screening_workstation_server_tools import ActionServerTools


# 创建全局工具管理器实例
tool_manager = ActionServerTools()


# --- 定义设备动作函数（自动生成，与工具类方法对应）---
def tool_DeviceReset(**params):
    return tool_manager.tool_DeviceReset(**params)


def tool_TakePhoto(**params):
    return tool_manager.tool_TakePhoto(**params)


def tool_Config(**params):
    return tool_manager.tool_Config(**params)


def tool_SlideLock(**params):
    return tool_manager.tool_SlideLock(**params)


def tool_SlideUnLock(**params):
    return tool_manager.tool_SlideUnLock(**params)


def tool_test(**params):
    return tool_manager.tool_test(**params)


def tool_test_all(**params):
    return tool_manager.tool_test_all(**params)



AVAILABLE_TOOLS_ACTION = {
    "DeviceReset": tool_DeviceReset,
    "TakePhoto": tool_TakePhoto,
    "Config": tool_Config,
    "SlideLock": tool_SlideLock,
    "SlideUnLock": tool_SlideUnLock,
    "test": tool_test,
    "test_all": tool_test_all
}


# --- MCP协议通信主逻辑（自动适配当前设备）---
def high_throughput_advanced_material_screening_workstation_server_main_loop():
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
            print(f"--- [high_throughput_advanced_material_screening_workstation_Server] Critical Error: {str(e)} ---", file=sys.stderr, flush=True)


def high_throughput_advanced_material_screening_workstation_server_advertise_capabilities():
    """广播当前设备的MCP能力（设备信息、支持的动作）"""
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
            "name": "DeviceReset",
            "description": "伸出样品台",
            "parameters": {
                "type": "object",
                "properties": {
    "type": {
        "type": "string",
        "description": "设备类型"
    },
    "cmd": {
        "type": "string",
        "description": "指令名称"
    },
    "Name": {
        "type": "string",
        "description": "脚本名称"
    }
},
                "required": ["type", "cmd", "Name"]
            }
        },
        {
            "name": "TakePhoto",
            "description": "到指定位置拍照",
            "parameters": {
                "type": "object",
                "properties": {
    "type": {
        "type": "string",
        "description": "设备类型"
    },
    "cmd": {
        "type": "string",
        "description": "指令名称"
    },
    "Name": {
        "type": "string",
        "description": "脚本名称"
    },
    "PhotoLocation": {
        "type": "int",
        "description": "拍照位置（1，2，3）",
        "enum": [
            {
                "label": "位置1",
                "value": "1"
            },
            {
                "label": "位置2",
                "value": "2"
            },
            {
                "label": "位置3",
                "value": "3"
            }
        ]
    },
    "result": {
        "type": "file",
        "description": "result"
    }
},
                "required": ["type", "cmd", "Name", "PhotoLocation"]
            }
        },
        {
            "name": "Config",
            "description": "配置样点映射关系",
            "parameters": {
                "type": "object",
                "properties": {
    "type": {
        "type": "string",
        "description": "设备类型"
    },
    "cmd": {
        "type": "string",
        "description": "指令名称"
    },
    "Name": {
        "type": "string",
        "description": "脚本名称"
    },
    "definitionParamUrl": {
        "type": "file",
        "description": "配置文件路径"
    }
},
                "required": ["type", "cmd", "Name", "definitionParamUrl"]
            }
        },
        {
            "name": "SlideLock",
            "description": "启动吸附底座",
            "parameters": {
                "type": "object",
                "properties": {
    "type": {
        "type": "string",
        "description": "设备类型"
    },
    "cmd": {
        "type": "string",
        "description": "指令名称"
    },
    "Name": {
        "type": "string",
        "description": "脚本名称"
    }
},
                "required": ["type", "cmd", "Name"]
            }
        },
        {
            "name": "SlideUnLock",
            "description": "关闭吸附底座",
            "parameters": {
                "type": "object",
                "properties": {
    "type": {
        "type": "string",
        "description": "设备类型"
    },
    "cmd": {
        "type": "string",
        "description": "指令名称"
    },
    "Name": {
        "type": "string",
        "description": "脚本名称"
    }
},
                "required": ["type", "cmd", "Name"]
            }
        },
        {
            "name": "test",
            "description": "嵌套单点实验",
            "parameters": {
                "type": "object",
                "properties": {
    "type": {
        "type": "string",
        "description": "设备类型"
    },
    "cmd": {
        "type": "string",
        "description": "指令名称"
    },
    "Name": {
        "type": "string",
        "description": "脚本名称"
    },
    "PhotoLocation": {
        "type": "int",
        "description": "实验玻碳片位置",
        "enum": [
            {
                "label": "位置1",
                "value": "1"
            },
            {
                "label": "位置2",
                "value": "2"
            },
            {
                "label": "位置3",
                "value": "3"
            }
        ]
    },
    "TestMethod": {
        "type": "int",
        "description": "实验模式"
    },
    "TestPoint": {
        "type": "int",
        "description": "测试点位"
    },
    "XAxis": {
        "type": "int",
        "description": "横坐标"
    },
    "YAxis": {
        "type": "int",
        "description": "纵坐标"
    },
    "TestParam": {
        "type": "array",
        "description": "多轮实验参数",
        "properties": {
            "CV": {
                "type": "array",
                "description": "CV实验",
                "properties": {
                    "CV.TestName": {
                        "type": "string",
                        "description": "实验名称"
                    },
                    "CV.InitElec": {
                        "type": "float",
                        "description": "CV初始电位（V）"
                    },
                    "CV.LowElec": {
                        "type": "float",
                        "description": "CV最低电位（V）"
                    },
                    "CV.HighElec": {
                        "type": "float",
                        "description": "CV最高电位（V）"
                    },
                    "CV.FinalElec": {
                        "type": "float",
                        "description": "CV终止电位（V）"
                    },
                    "CV.SampleInterval": {
                        "type": "float",
                        "description": "CV采样间隔（V）"
                    },
                    "CV.RestTime": {
                        "type": "int",
                        "description": "CV静止时间（s）"
                    },
                    "CV.ScanDirection": {
                        "type": "int",
                        "description": "CV扫描方向"
                    },
                    "CV.ScanCycles": {
                        "type": "int",
                        "description": "CV扫描圈数"
                    },
                    "CV.ScanSpeed": {
                        "type": "float",
                        "description": "CV扫描速度（V/s）"
                    },
                    "CV.Channel1Sensitivity": {
                        "type": "int",
                        "description": "CV通道灵敏度",
                        "enum": [
                            {
                                "label": "0~50pA(100G)",
                                "value": "1"
                            },
                            {
                                "label": "0~500pA(10G)",
                                "value": "2"
                            },
                            {
                                "label": "0~5nA(1G)",
                                "value": "3"
                            },
                            {
                                "label": "0~50nA(100M)",
                                "value": "4"
                            },
                            {
                                "label": "0~500nA(10M)",
                                "value": "5"
                            },
                            {
                                "label": "0~5uA(1M)",
                                "value": "6"
                            },
                            {
                                "label": "0~50uA(100K)",
                                "value": "7"
                            },
                            {
                                "label": "0~500uA(10K)",
                                "value": "8"
                            },
                            {
                                "label": "0~5mA(1K)",
                                "value": "9"
                            },
                            {
                                "label": "0~50mA(100)",
                                "value": "10"
                            },
                            {
                                "label": "0~200mA(10)",
                                "value": "11"
                            },
                            {
                                "label": "0~5pA(1T)",
                                "value": "13"
                            }
                        ]
                    }
                },
                "required": [
                    "CV.TestName",
                    "CV.InitElec",
                    "CV.LowElec",
                    "CV.HighElec",
                    "CV.FinalElec",
                    "CV.SampleInterval",
                    "CV.RestTime",
                    "CV.ScanDirection",
                    "CV.ScanCycles",
                    "CV.ScanSpeed",
                    "CV.Channel1Sensitivity"
                ]
            },
            "CV.TestName": {
                "type": "string",
                "description": "实验名称"
            },
            "CV.InitElec": {
                "type": "float",
                "description": "CV初始电位（V）"
            },
            "CV.LowElec": {
                "type": "float",
                "description": "CV最低电位（V）"
            },
            "CV.HighElec": {
                "type": "float",
                "description": "CV最高电位（V）"
            },
            "CV.FinalElec": {
                "type": "float",
                "description": "CV终止电位（V）"
            },
            "CV.SampleInterval": {
                "type": "float",
                "description": "CV采样间隔（V）"
            },
            "CV.RestTime": {
                "type": "int",
                "description": "CV静止时间（s）"
            },
            "CV.ScanDirection": {
                "type": "int",
                "description": "CV扫描方向"
            },
            "CV.ScanCycles": {
                "type": "int",
                "description": "CV扫描圈数"
            },
            "CV.ScanSpeed": {
                "type": "float",
                "description": "CV扫描速度（V/s）"
            },
            "CV.Channel1Sensitivity": {
                "type": "int",
                "description": "CV通道灵敏度",
                "enum": [
                    {
                        "label": "0~50pA(100G)",
                        "value": "1"
                    },
                    {
                        "label": "0~500pA(10G)",
                        "value": "2"
                    },
                    {
                        "label": "0~5nA(1G)",
                        "value": "3"
                    },
                    {
                        "label": "0~50nA(100M)",
                        "value": "4"
                    },
                    {
                        "label": "0~500nA(10M)",
                        "value": "5"
                    },
                    {
                        "label": "0~5uA(1M)",
                        "value": "6"
                    },
                    {
                        "label": "0~50uA(100K)",
                        "value": "7"
                    },
                    {
                        "label": "0~500uA(10K)",
                        "value": "8"
                    },
                    {
                        "label": "0~5mA(1K)",
                        "value": "9"
                    },
                    {
                        "label": "0~50mA(100)",
                        "value": "10"
                    },
                    {
                        "label": "0~200mA(10)",
                        "value": "11"
                    },
                    {
                        "label": "0~5pA(1T)",
                        "value": "13"
                    }
                ]
            },
            "LSV": {
                "type": "array",
                "description": "LSV实验",
                "properties": {
                    "LSV.TestName": {
                        "type": "string",
                        "description": "实验名称"
                    },
                    "LSV.SampleRate": {
                        "type": "float",
                        "description": "LSV采样频率（Hz）"
                    },
                    "LSV.ScanSpeed": {
                        "type": "float",
                        "description": "LSV扫描速度（V/s）"
                    },
                    "LSV.InitElec": {
                        "type": "float",
                        "description": "LSV初始电位（V）"
                    },
                    "LSV.RestTime": {
                        "type": "int",
                        "description": "LSV静止时间（s）"
                    },
                    "LSV.FinalElec": {
                        "type": "float",
                        "description": "LSV终止电位（V）"
                    },
                    "LSV.Channel1Sensitivity": {
                        "type": "int",
                        "description": "LSV通道灵敏度",
                        "enum": [
                            {
                                "label": "0~50pA(100G)",
                                "value": "1"
                            },
                            {
                                "label": "0~500pA(10G)",
                                "value": "2"
                            },
                            {
                                "label": "0~5nA(1G)",
                                "value": "3"
                            },
                            {
                                "label": "0~50nA(100M)",
                                "value": "4"
                            },
                            {
                                "label": "0~500nA(10M)",
                                "value": "5"
                            },
                            {
                                "label": "0~5uA(1M)",
                                "value": "6"
                            },
                            {
                                "label": "0~50uA(100K)",
                                "value": "7"
                            },
                            {
                                "label": "0~500uA(10K)",
                                "value": "8"
                            },
                            {
                                "label": "0~5mA(1K)",
                                "value": "9"
                            },
                            {
                                "label": "0~50mA(100)",
                                "value": "10"
                            },
                            {
                                "label": "0~200mA(10)",
                                "value": "11"
                            },
                            {
                                "label": "0~5pA(1T)",
                                "value": "13"
                            }
                        ]
                    }
                },
                "required": [
                    "LSV.TestName",
                    "LSV.SampleRate",
                    "LSV.ScanSpeed",
                    "LSV.InitElec",
                    "LSV.RestTime",
                    "LSV.FinalElec",
                    "LSV.Channel1Sensitivity"
                ]
            },
            "LSV.TestName": {
                "type": "string",
                "description": "实验名称"
            },
            "LSV.SampleRate": {
                "type": "float",
                "description": "LSV采样频率（Hz）"
            },
            "LSV.ScanSpeed": {
                "type": "float",
                "description": "LSV扫描速度（V/s）"
            },
            "LSV.InitElec": {
                "type": "float",
                "description": "LSV初始电位（V）"
            },
            "LSV.RestTime": {
                "type": "int",
                "description": "LSV静止时间（s）"
            },
            "LSV.FinalElec": {
                "type": "float",
                "description": "LSV终止电位（V）"
            },
            "LSV.Channel1Sensitivity": {
                "type": "int",
                "description": "LSV通道灵敏度",
                "enum": [
                    {
                        "label": "0~50pA(100G)",
                        "value": "1"
                    },
                    {
                        "label": "0~500pA(10G)",
                        "value": "2"
                    },
                    {
                        "label": "0~5nA(1G)",
                        "value": "3"
                    },
                    {
                        "label": "0~50nA(100M)",
                        "value": "4"
                    },
                    {
                        "label": "0~500nA(10M)",
                        "value": "5"
                    },
                    {
                        "label": "0~5uA(1M)",
                        "value": "6"
                    },
                    {
                        "label": "0~50uA(100K)",
                        "value": "7"
                    },
                    {
                        "label": "0~500uA(10K)",
                        "value": "8"
                    },
                    {
                        "label": "0~5mA(1K)",
                        "value": "9"
                    },
                    {
                        "label": "0~50mA(100)",
                        "value": "10"
                    },
                    {
                        "label": "0~200mA(10)",
                        "value": "11"
                    },
                    {
                        "label": "0~5pA(1T)",
                        "value": "13"
                    }
                ]
            },
            "IT": {
                "type": "array",
                "description": "IT实验",
                "properties": {
                    "IT.TestName": {
                        "type": "string",
                        "description": "实验名称"
                    },
                    "IT.InitElec": {
                        "type": "float",
                        "description": "IT初始电位"
                    },
                    "IT.SampleInterval": {
                        "type": "float",
                        "description": "IT采样间隔",
                        "enum": [
                            {
                                "label": "500ms",
                                "value": "0"
                            },
                            {
                                "label": "100ms",
                                "value": "1"
                            },
                            {
                                "label": "20ms",
                                "value": "2"
                            },
                            {
                                "label": "1ms",
                                "value": "3"
                            }
                        ]
                    },
                    "IT.RestTime": {
                        "type": "int",
                        "description": "IT静止时间（s）"
                    },
                    "IT.Channel1Sensitivity": {
                        "type": "int",
                        "description": "IT通道灵敏度",
                        "enum": [
                            {
                                "label": "0~50pA(100G)",
                                "value": "1"
                            },
                            {
                                "label": "0~500pA(10G)",
                                "value": "2"
                            },
                            {
                                "label": "0~5nA(1G)",
                                "value": "3"
                            },
                            {
                                "label": "0~50nA(100M)",
                                "value": "4"
                            },
                            {
                                "label": "0~500nA(10M)",
                                "value": "5"
                            },
                            {
                                "label": "0~5uA(1M)",
                                "value": "6"
                            },
                            {
                                "label": "0~50uA(100K)",
                                "value": "7"
                            },
                            {
                                "label": "0~500uA(10K)",
                                "value": "8"
                            },
                            {
                                "label": "0~5mA(1K)",
                                "value": "9"
                            },
                            {
                                "label": "0~50mA(100)",
                                "value": "10"
                            },
                            {
                                "label": "0~200mA(10)",
                                "value": "11"
                            },
                            {
                                "label": "0~5pA(1T)",
                                "value": "13"
                            }
                        ]
                    },
                    "IT.RunTime": {
                        "type": "float",
                        "description": "IT运行时间（s）"
                    }
                },
                "required": [
                    "IT.TestName",
                    "IT.InitElec",
                    "IT.SampleInterval",
                    "IT.RestTime",
                    "IT.Channel1Sensitivity",
                    "IT.RunTime"
                ]
            },
            "IT.TestName": {
                "type": "string",
                "description": "实验名称"
            },
            "IT.InitElec": {
                "type": "float",
                "description": "IT初始电位"
            },
            "IT.SampleInterval": {
                "type": "float",
                "description": "IT采样间隔",
                "enum": [
                    {
                        "label": "500ms",
                        "value": "0"
                    },
                    {
                        "label": "100ms",
                        "value": "1"
                    },
                    {
                        "label": "20ms",
                        "value": "2"
                    },
                    {
                        "label": "1ms",
                        "value": "3"
                    }
                ]
            },
            "IT.RestTime": {
                "type": "int",
                "description": "IT静止时间（s）"
            },
            "IT.Channel1Sensitivity": {
                "type": "int",
                "description": "IT通道灵敏度",
                "enum": [
                    {
                        "label": "0~50pA(100G)",
                        "value": "1"
                    },
                    {
                        "label": "0~500pA(10G)",
                        "value": "2"
                    },
                    {
                        "label": "0~5nA(1G)",
                        "value": "3"
                    },
                    {
                        "label": "0~50nA(100M)",
                        "value": "4"
                    },
                    {
                        "label": "0~500nA(10M)",
                        "value": "5"
                    },
                    {
                        "label": "0~5uA(1M)",
                        "value": "6"
                    },
                    {
                        "label": "0~50uA(100K)",
                        "value": "7"
                    },
                    {
                        "label": "0~500uA(10K)",
                        "value": "8"
                    },
                    {
                        "label": "0~5mA(1K)",
                        "value": "9"
                    },
                    {
                        "label": "0~50mA(100)",
                        "value": "10"
                    },
                    {
                        "label": "0~200mA(10)",
                        "value": "11"
                    },
                    {
                        "label": "0~5pA(1T)",
                        "value": "13"
                    }
                ]
            },
            "IT.RunTime": {
                "type": "float",
                "description": "IT运行时间（s）"
            },
            "OCPT": {
                "type": "array",
                "description": "OCPT实验",
                "properties": {
                    "OCPT.TestName": {
                        "type": "string",
                        "description": "实验名称"
                    },
                    "OCPT.SampleInterval": {
                        "type": "float",
                        "description": "OCPT采样间隔",
                        "enum": [
                            {
                                "label": "500ms",
                                "value": "0"
                            },
                            {
                                "label": "100ms",
                                "value": "1"
                            },
                            {
                                "label": "20ms",
                                "value": "2"
                            },
                            {
                                "label": "1ms",
                                "value": "3"
                            }
                        ]
                    },
                    "OCPT.HighElec": {
                        "type": "float",
                        "description": "OCPT高电位（V）"
                    },
                    "OCPT.RunTime": {
                        "type": "float",
                        "description": "OCPT运行时间（s）"
                    },
                    "OCPT.LowElec_OCPT": {
                        "type": "float",
                        "description": "OCPT低电位（V）"
                    }
                },
                "required": [
                    "OCPT.TestName",
                    "OCPT.SampleInterval",
                    "OCPT.HighElec",
                    "OCPT.RunTime",
                    "OCPT.LowElec_OCPT"
                ]
            },
            "OCPT.TestName": {
                "type": "string",
                "description": "实验名称"
            },
            "OCPT.SampleInterval": {
                "type": "float",
                "description": "OCPT采样间隔",
                "enum": [
                    {
                        "label": "500ms",
                        "value": "0"
                    },
                    {
                        "label": "100ms",
                        "value": "1"
                    },
                    {
                        "label": "20ms",
                        "value": "2"
                    },
                    {
                        "label": "1ms",
                        "value": "3"
                    }
                ]
            },
            "OCPT.HighElec": {
                "type": "float",
                "description": "OCPT高电位（V）"
            },
            "OCPT.RunTime": {
                "type": "float",
                "description": "OCPT运行时间（s）"
            },
            "OCPT.LowElec_OCPT": {
                "type": "float",
                "description": "OCPT低电位（V）"
            }
        },
        "required": [
            "CV.TestName",
            "CV.InitElec",
            "CV.LowElec",
            "CV.HighElec",
            "CV.FinalElec",
            "CV.SampleInterval",
            "CV.RestTime",
            "CV.ScanDirection",
            "CV.ScanCycles",
            "CV.ScanSpeed",
            "CV.Channel1Sensitivity",
            "LSV.TestName",
            "LSV.SampleRate",
            "LSV.ScanSpeed",
            "LSV.InitElec",
            "LSV.RestTime",
            "LSV.FinalElec",
            "LSV.Channel1Sensitivity",
            "IT.TestName",
            "IT.InitElec",
            "IT.SampleInterval",
            "IT.RestTime",
            "IT.Channel1Sensitivity",
            "IT.RunTime",
            "OCPT.TestName",
            "OCPT.SampleInterval",
            "OCPT.HighElec",
            "OCPT.RunTime",
            "OCPT.LowElec_OCPT"
        ]
    },
    "TestParam.CV": {
        "type": "array",
        "description": "CV实验",
        "properties": {
            "CV.TestName": {
                "type": "string",
                "description": "实验名称"
            },
            "CV.InitElec": {
                "type": "float",
                "description": "CV初始电位（V）"
            },
            "CV.LowElec": {
                "type": "float",
                "description": "CV最低电位（V）"
            },
            "CV.HighElec": {
                "type": "float",
                "description": "CV最高电位（V）"
            },
            "CV.FinalElec": {
                "type": "float",
                "description": "CV终止电位（V）"
            },
            "CV.SampleInterval": {
                "type": "float",
                "description": "CV采样间隔（V）"
            },
            "CV.RestTime": {
                "type": "int",
                "description": "CV静止时间（s）"
            },
            "CV.ScanDirection": {
                "type": "int",
                "description": "CV扫描方向"
            },
            "CV.ScanCycles": {
                "type": "int",
                "description": "CV扫描圈数"
            },
            "CV.ScanSpeed": {
                "type": "float",
                "description": "CV扫描速度（V/s）"
            },
            "CV.Channel1Sensitivity": {
                "type": "int",
                "description": "CV通道灵敏度",
                "enum": [
                    {
                        "label": "0~50pA(100G)",
                        "value": "1"
                    },
                    {
                        "label": "0~500pA(10G)",
                        "value": "2"
                    },
                    {
                        "label": "0~5nA(1G)",
                        "value": "3"
                    },
                    {
                        "label": "0~50nA(100M)",
                        "value": "4"
                    },
                    {
                        "label": "0~500nA(10M)",
                        "value": "5"
                    },
                    {
                        "label": "0~5uA(1M)",
                        "value": "6"
                    },
                    {
                        "label": "0~50uA(100K)",
                        "value": "7"
                    },
                    {
                        "label": "0~500uA(10K)",
                        "value": "8"
                    },
                    {
                        "label": "0~5mA(1K)",
                        "value": "9"
                    },
                    {
                        "label": "0~50mA(100)",
                        "value": "10"
                    },
                    {
                        "label": "0~200mA(10)",
                        "value": "11"
                    },
                    {
                        "label": "0~5pA(1T)",
                        "value": "13"
                    }
                ]
            }
        },
        "required": [
            "CV.TestName",
            "CV.InitElec",
            "CV.LowElec",
            "CV.HighElec",
            "CV.FinalElec",
            "CV.SampleInterval",
            "CV.RestTime",
            "CV.ScanDirection",
            "CV.ScanCycles",
            "CV.ScanSpeed",
            "CV.Channel1Sensitivity"
        ]
    },
    "TestParam.CV.TestName": {
        "type": "string",
        "description": "实验名称"
    },
    "TestParam.CV.InitElec": {
        "type": "float",
        "description": "CV初始电位（V）"
    },
    "TestParam.CV.LowElec": {
        "type": "float",
        "description": "CV最低电位（V）"
    },
    "TestParam.CV.HighElec": {
        "type": "float",
        "description": "CV最高电位（V）"
    },
    "TestParam.CV.FinalElec": {
        "type": "float",
        "description": "CV终止电位（V）"
    },
    "TestParam.CV.SampleInterval": {
        "type": "float",
        "description": "CV采样间隔（V）"
    },
    "TestParam.CV.RestTime": {
        "type": "int",
        "description": "CV静止时间（s）"
    },
    "TestParam.CV.ScanDirection": {
        "type": "int",
        "description": "CV扫描方向"
    },
    "TestParam.CV.ScanCycles": {
        "type": "int",
        "description": "CV扫描圈数"
    },
    "TestParam.CV.ScanSpeed": {
        "type": "float",
        "description": "CV扫描速度（V/s）"
    },
    "TestParam.CV.Channel1Sensitivity": {
        "type": "int",
        "description": "CV通道灵敏度",
        "enum": [
            {
                "label": "0~50pA(100G)",
                "value": "1"
            },
            {
                "label": "0~500pA(10G)",
                "value": "2"
            },
            {
                "label": "0~5nA(1G)",
                "value": "3"
            },
            {
                "label": "0~50nA(100M)",
                "value": "4"
            },
            {
                "label": "0~500nA(10M)",
                "value": "5"
            },
            {
                "label": "0~5uA(1M)",
                "value": "6"
            },
            {
                "label": "0~50uA(100K)",
                "value": "7"
            },
            {
                "label": "0~500uA(10K)",
                "value": "8"
            },
            {
                "label": "0~5mA(1K)",
                "value": "9"
            },
            {
                "label": "0~50mA(100)",
                "value": "10"
            },
            {
                "label": "0~200mA(10)",
                "value": "11"
            },
            {
                "label": "0~5pA(1T)",
                "value": "13"
            }
        ]
    },
    "TestParam.LSV": {
        "type": "array",
        "description": "LSV实验",
        "properties": {
            "LSV.TestName": {
                "type": "string",
                "description": "实验名称"
            },
            "LSV.SampleRate": {
                "type": "float",
                "description": "LSV采样频率（Hz）"
            },
            "LSV.ScanSpeed": {
                "type": "float",
                "description": "LSV扫描速度（V/s）"
            },
            "LSV.InitElec": {
                "type": "float",
                "description": "LSV初始电位（V）"
            },
            "LSV.RestTime": {
                "type": "int",
                "description": "LSV静止时间（s）"
            },
            "LSV.FinalElec": {
                "type": "float",
                "description": "LSV终止电位（V）"
            },
            "LSV.Channel1Sensitivity": {
                "type": "int",
                "description": "LSV通道灵敏度",
                "enum": [
                    {
                        "label": "0~50pA(100G)",
                        "value": "1"
                    },
                    {
                        "label": "0~500pA(10G)",
                        "value": "2"
                    },
                    {
                        "label": "0~5nA(1G)",
                        "value": "3"
                    },
                    {
                        "label": "0~50nA(100M)",
                        "value": "4"
                    },
                    {
                        "label": "0~500nA(10M)",
                        "value": "5"
                    },
                    {
                        "label": "0~5uA(1M)",
                        "value": "6"
                    },
                    {
                        "label": "0~50uA(100K)",
                        "value": "7"
                    },
                    {
                        "label": "0~500uA(10K)",
                        "value": "8"
                    },
                    {
                        "label": "0~5mA(1K)",
                        "value": "9"
                    },
                    {
                        "label": "0~50mA(100)",
                        "value": "10"
                    },
                    {
                        "label": "0~200mA(10)",
                        "value": "11"
                    },
                    {
                        "label": "0~5pA(1T)",
                        "value": "13"
                    }
                ]
            }
        },
        "required": [
            "LSV.TestName",
            "LSV.SampleRate",
            "LSV.ScanSpeed",
            "LSV.InitElec",
            "LSV.RestTime",
            "LSV.FinalElec",
            "LSV.Channel1Sensitivity"
        ]
    },
    "TestParam.LSV.TestName": {
        "type": "string",
        "description": "实验名称"
    },
    "TestParam.LSV.SampleRate": {
        "type": "float",
        "description": "LSV采样频率（Hz）"
    },
    "TestParam.LSV.ScanSpeed": {
        "type": "float",
        "description": "LSV扫描速度（V/s）"
    },
    "TestParam.LSV.InitElec": {
        "type": "float",
        "description": "LSV初始电位（V）"
    },
    "TestParam.LSV.RestTime": {
        "type": "int",
        "description": "LSV静止时间（s）"
    },
    "TestParam.LSV.FinalElec": {
        "type": "float",
        "description": "LSV终止电位（V）"
    },
    "TestParam.LSV.Channel1Sensitivity": {
        "type": "int",
        "description": "LSV通道灵敏度",
        "enum": [
            {
                "label": "0~50pA(100G)",
                "value": "1"
            },
            {
                "label": "0~500pA(10G)",
                "value": "2"
            },
            {
                "label": "0~5nA(1G)",
                "value": "3"
            },
            {
                "label": "0~50nA(100M)",
                "value": "4"
            },
            {
                "label": "0~500nA(10M)",
                "value": "5"
            },
            {
                "label": "0~5uA(1M)",
                "value": "6"
            },
            {
                "label": "0~50uA(100K)",
                "value": "7"
            },
            {
                "label": "0~500uA(10K)",
                "value": "8"
            },
            {
                "label": "0~5mA(1K)",
                "value": "9"
            },
            {
                "label": "0~50mA(100)",
                "value": "10"
            },
            {
                "label": "0~200mA(10)",
                "value": "11"
            },
            {
                "label": "0~5pA(1T)",
                "value": "13"
            }
        ]
    },
    "TestParam.IT": {
        "type": "array",
        "description": "IT实验",
        "properties": {
            "IT.TestName": {
                "type": "string",
                "description": "实验名称"
            },
            "IT.InitElec": {
                "type": "float",
                "description": "IT初始电位"
            },
            "IT.SampleInterval": {
                "type": "float",
                "description": "IT采样间隔",
                "enum": [
                    {
                        "label": "500ms",
                        "value": "0"
                    },
                    {
                        "label": "100ms",
                        "value": "1"
                    },
                    {
                        "label": "20ms",
                        "value": "2"
                    },
                    {
                        "label": "1ms",
                        "value": "3"
                    }
                ]
            },
            "IT.RestTime": {
                "type": "int",
                "description": "IT静止时间（s）"
            },
            "IT.Channel1Sensitivity": {
                "type": "int",
                "description": "IT通道灵敏度",
                "enum": [
                    {
                        "label": "0~50pA(100G)",
                        "value": "1"
                    },
                    {
                        "label": "0~500pA(10G)",
                        "value": "2"
                    },
                    {
                        "label": "0~5nA(1G)",
                        "value": "3"
                    },
                    {
                        "label": "0~50nA(100M)",
                        "value": "4"
                    },
                    {
                        "label": "0~500nA(10M)",
                        "value": "5"
                    },
                    {
                        "label": "0~5uA(1M)",
                        "value": "6"
                    },
                    {
                        "label": "0~50uA(100K)",
                        "value": "7"
                    },
                    {
                        "label": "0~500uA(10K)",
                        "value": "8"
                    },
                    {
                        "label": "0~5mA(1K)",
                        "value": "9"
                    },
                    {
                        "label": "0~50mA(100)",
                        "value": "10"
                    },
                    {
                        "label": "0~200mA(10)",
                        "value": "11"
                    },
                    {
                        "label": "0~5pA(1T)",
                        "value": "13"
                    }
                ]
            },
            "IT.RunTime": {
                "type": "float",
                "description": "IT运行时间（s）"
            }
        },
        "required": [
            "IT.TestName",
            "IT.InitElec",
            "IT.SampleInterval",
            "IT.RestTime",
            "IT.Channel1Sensitivity",
            "IT.RunTime"
        ]
    },
    "TestParam.IT.TestName": {
        "type": "string",
        "description": "实验名称"
    },
    "TestParam.IT.InitElec": {
        "type": "float",
        "description": "IT初始电位"
    },
    "TestParam.IT.SampleInterval": {
        "type": "float",
        "description": "IT采样间隔",
        "enum": [
            {
                "label": "500ms",
                "value": "0"
            },
            {
                "label": "100ms",
                "value": "1"
            },
            {
                "label": "20ms",
                "value": "2"
            },
            {
                "label": "1ms",
                "value": "3"
            }
        ]
    },
    "TestParam.IT.RestTime": {
        "type": "int",
        "description": "IT静止时间（s）"
    },
    "TestParam.IT.Channel1Sensitivity": {
        "type": "int",
        "description": "IT通道灵敏度",
        "enum": [
            {
                "label": "0~50pA(100G)",
                "value": "1"
            },
            {
                "label": "0~500pA(10G)",
                "value": "2"
            },
            {
                "label": "0~5nA(1G)",
                "value": "3"
            },
            {
                "label": "0~50nA(100M)",
                "value": "4"
            },
            {
                "label": "0~500nA(10M)",
                "value": "5"
            },
            {
                "label": "0~5uA(1M)",
                "value": "6"
            },
            {
                "label": "0~50uA(100K)",
                "value": "7"
            },
            {
                "label": "0~500uA(10K)",
                "value": "8"
            },
            {
                "label": "0~5mA(1K)",
                "value": "9"
            },
            {
                "label": "0~50mA(100)",
                "value": "10"
            },
            {
                "label": "0~200mA(10)",
                "value": "11"
            },
            {
                "label": "0~5pA(1T)",
                "value": "13"
            }
        ]
    },
    "TestParam.IT.RunTime": {
        "type": "float",
        "description": "IT运行时间（s）"
    },
    "TestParam.OCPT": {
        "type": "array",
        "description": "OCPT实验",
        "properties": {
            "OCPT.TestName": {
                "type": "string",
                "description": "实验名称"
            },
            "OCPT.SampleInterval": {
                "type": "float",
                "description": "OCPT采样间隔",
                "enum": [
                    {
                        "label": "500ms",
                        "value": "0"
                    },
                    {
                        "label": "100ms",
                        "value": "1"
                    },
                    {
                        "label": "20ms",
                        "value": "2"
                    },
                    {
                        "label": "1ms",
                        "value": "3"
                    }
                ]
            },
            "OCPT.HighElec": {
                "type": "float",
                "description": "OCPT高电位（V）"
            },
            "OCPT.RunTime": {
                "type": "float",
                "description": "OCPT运行时间（s）"
            },
            "OCPT.LowElec_OCPT": {
                "type": "float",
                "description": "OCPT低电位（V）"
            }
        },
        "required": [
            "OCPT.TestName",
            "OCPT.SampleInterval",
            "OCPT.HighElec",
            "OCPT.RunTime",
            "OCPT.LowElec_OCPT"
        ]
    },
    "TestParam.OCPT.TestName": {
        "type": "string",
        "description": "实验名称"
    },
    "TestParam.OCPT.SampleInterval": {
        "type": "float",
        "description": "OCPT采样间隔",
        "enum": [
            {
                "label": "500ms",
                "value": "0"
            },
            {
                "label": "100ms",
                "value": "1"
            },
            {
                "label": "20ms",
                "value": "2"
            },
            {
                "label": "1ms",
                "value": "3"
            }
        ]
    },
    "TestParam.OCPT.HighElec": {
        "type": "float",
        "description": "OCPT高电位（V）"
    },
    "TestParam.OCPT.RunTime": {
        "type": "float",
        "description": "OCPT运行时间（s）"
    },
    "TestParam.OCPT.LowElec_OCPT": {
        "type": "float",
        "description": "OCPT低电位（V）"
    },
    "result": {
        "type": "file",
        "description": "结果上传"
    }
},
                "required": ["type", "cmd", "Name", "PhotoLocation", "TestMethod", "TestPoint", "XAxis", "YAxis", "TestParam", "TestParam.CV.TestName", "TestParam.CV.InitElec", "TestParam.CV.LowElec", "TestParam.CV.HighElec", "TestParam.CV.FinalElec", "TestParam.CV.SampleInterval", "TestParam.CV.RestTime", "TestParam.CV.ScanDirection", "TestParam.CV.ScanCycles", "TestParam.CV.ScanSpeed", "TestParam.CV.Channel1Sensitivity", "TestParam.LSV.TestName", "TestParam.LSV.SampleRate", "TestParam.LSV.ScanSpeed", "TestParam.LSV.InitElec", "TestParam.LSV.RestTime", "TestParam.LSV.FinalElec", "TestParam.LSV.Channel1Sensitivity", "TestParam.IT.TestName", "TestParam.IT.InitElec", "TestParam.IT.SampleInterval", "TestParam.IT.RestTime", "TestParam.IT.Channel1Sensitivity", "TestParam.IT.RunTime", "TestParam.OCPT.TestName", "TestParam.OCPT.SampleInterval", "TestParam.OCPT.HighElec", "TestParam.OCPT.RunTime", "TestParam.OCPT.LowElec_OCPT"]
            }
        },
        {
            "name": "test_all",
            "description": "嵌套全点实验",
            "parameters": {
                "type": "object",
                "properties": {
    "type": {
        "type": "string",
        "description": "设备类型"
    },
    "cmd": {
        "type": "string",
        "description": "指令名称"
    },
    "Name": {
        "type": "string",
        "description": "脚本名称"
    },
    "PhotoLocation": {
        "type": "int",
        "description": "实验玻碳片位置",
        "enum": [
            {
                "label": "位置1",
                "value": "1"
            },
            {
                "label": "位置2",
                "value": "2"
            },
            {
                "label": "位置3",
                "value": "3"
            }
        ]
    },
    "TestMethod": {
        "type": "int",
        "description": "实验模式"
    },
    "TestPoint": {
        "type": "int",
        "description": "测试点位"
    },
    "XAxis": {
        "type": "int",
        "description": "横坐标"
    },
    "YAxis": {
        "type": "int",
        "description": "纵坐标"
    },
    "TestParam": {
        "type": "array",
        "description": "多轮实验参数",
        "properties": {
            "CV": {
                "type": "array",
                "description": "CV实验",
                "properties": {
                    "CV.TestName": {
                        "type": "string",
                        "description": "实验名称"
                    },
                    "CV.InitElec": {
                        "type": "float",
                        "description": "CV初始电位（V）"
                    },
                    "CV.LowElec": {
                        "type": "float",
                        "description": "CV最低电位（V）"
                    },
                    "CV.HighElec": {
                        "type": "float",
                        "description": "CV最高电位（V）"
                    },
                    "CV.FinalElec": {
                        "type": "float",
                        "description": "CV终止电位（V）"
                    },
                    "CV.SampleInterval": {
                        "type": "float",
                        "description": "CV采样间隔（V）"
                    },
                    "CV.RestTime": {
                        "type": "int",
                        "description": "CV静止时间（s）"
                    },
                    "CV.ScanDirection": {
                        "type": "int",
                        "description": "CV扫描方向"
                    },
                    "CV.ScanCycles": {
                        "type": "int",
                        "description": "CV扫描圈数"
                    },
                    "CV.ScanSpeed": {
                        "type": "float",
                        "description": "CV扫描速度（V/s）"
                    },
                    "CV.Channel1Sensitivity": {
                        "type": "int",
                        "description": "CV通道灵敏度",
                        "enum": [
                            {
                                "label": "0~50pA(100G)",
                                "value": "1"
                            },
                            {
                                "label": "0~500pA(10G)",
                                "value": "2"
                            },
                            {
                                "label": "0~5nA(1G)",
                                "value": "3"
                            },
                            {
                                "label": "0~50nA(100M)",
                                "value": "4"
                            },
                            {
                                "label": "0~500nA(10M)",
                                "value": "5"
                            },
                            {
                                "label": "0~5uA(1M)",
                                "value": "6"
                            },
                            {
                                "label": "0~50uA(100K)",
                                "value": "7"
                            },
                            {
                                "label": "0~500uA(10K)",
                                "value": "8"
                            },
                            {
                                "label": "0~5mA(1K)",
                                "value": "9"
                            },
                            {
                                "label": "0~50mA(100)",
                                "value": "10"
                            },
                            {
                                "label": "0~200mA(10)",
                                "value": "11"
                            },
                            {
                                "label": "0~5pA(1T)",
                                "value": "13"
                            }
                        ]
                    }
                },
                "required": [
                    "CV.TestName",
                    "CV.InitElec",
                    "CV.LowElec",
                    "CV.HighElec",
                    "CV.FinalElec",
                    "CV.SampleInterval",
                    "CV.RestTime",
                    "CV.ScanDirection",
                    "CV.ScanCycles",
                    "CV.ScanSpeed",
                    "CV.Channel1Sensitivity"
                ]
            },
            "CV.TestName": {
                "type": "string",
                "description": "实验名称"
            },
            "CV.InitElec": {
                "type": "float",
                "description": "CV初始电位（V）"
            },
            "CV.LowElec": {
                "type": "float",
                "description": "CV最低电位（V）"
            },
            "CV.HighElec": {
                "type": "float",
                "description": "CV最高电位（V）"
            },
            "CV.FinalElec": {
                "type": "float",
                "description": "CV终止电位（V）"
            },
            "CV.SampleInterval": {
                "type": "float",
                "description": "CV采样间隔（V）"
            },
            "CV.RestTime": {
                "type": "int",
                "description": "CV静止时间（s）"
            },
            "CV.ScanDirection": {
                "type": "int",
                "description": "CV扫描方向"
            },
            "CV.ScanCycles": {
                "type": "int",
                "description": "CV扫描圈数"
            },
            "CV.ScanSpeed": {
                "type": "float",
                "description": "CV扫描速度（V/s）"
            },
            "CV.Channel1Sensitivity": {
                "type": "int",
                "description": "CV通道灵敏度",
                "enum": [
                    {
                        "label": "0~50pA(100G)",
                        "value": "1"
                    },
                    {
                        "label": "0~500pA(10G)",
                        "value": "2"
                    },
                    {
                        "label": "0~5nA(1G)",
                        "value": "3"
                    },
                    {
                        "label": "0~50nA(100M)",
                        "value": "4"
                    },
                    {
                        "label": "0~500nA(10M)",
                        "value": "5"
                    },
                    {
                        "label": "0~5uA(1M)",
                        "value": "6"
                    },
                    {
                        "label": "0~50uA(100K)",
                        "value": "7"
                    },
                    {
                        "label": "0~500uA(10K)",
                        "value": "8"
                    },
                    {
                        "label": "0~5mA(1K)",
                        "value": "9"
                    },
                    {
                        "label": "0~50mA(100)",
                        "value": "10"
                    },
                    {
                        "label": "0~200mA(10)",
                        "value": "11"
                    },
                    {
                        "label": "0~5pA(1T)",
                        "value": "13"
                    }
                ]
            },
            "LSV": {
                "type": "array",
                "description": "LSV实验",
                "properties": {
                    "LSV.TestName": {
                        "type": "string",
                        "description": "实验名称"
                    },
                    "LSV.SampleRate": {
                        "type": "float",
                        "description": "LSV采样频率（Hz）"
                    },
                    "LSV.ScanSpeed": {
                        "type": "float",
                        "description": "LSV扫描速度（V/s）"
                    },
                    "LSV.InitElec": {
                        "type": "float",
                        "description": "LSV初始电位（V）"
                    },
                    "LSV.RestTime": {
                        "type": "int",
                        "description": "LSV静止时间（s）"
                    },
                    "LSV.FinalElec": {
                        "type": "float",
                        "description": "LSV终止电位（V）"
                    },
                    "LSV.Channel1Sensitivity": {
                        "type": "int",
                        "description": "LSV通道灵敏度",
                        "enum": [
                            {
                                "label": "0~50pA(100G)",
                                "value": "1"
                            },
                            {
                                "label": "0~500pA(10G)",
                                "value": "2"
                            },
                            {
                                "label": "0~5nA(1G)",
                                "value": "3"
                            },
                            {
                                "label": "0~50nA(100M)",
                                "value": "4"
                            },
                            {
                                "label": "0~500nA(10M)",
                                "value": "5"
                            },
                            {
                                "label": "0~5uA(1M)",
                                "value": "6"
                            },
                            {
                                "label": "0~50uA(100K)",
                                "value": "7"
                            },
                            {
                                "label": "0~500uA(10K)",
                                "value": "8"
                            },
                            {
                                "label": "0~5mA(1K)",
                                "value": "9"
                            },
                            {
                                "label": "0~50mA(100)",
                                "value": "10"
                            },
                            {
                                "label": "0~200mA(10)",
                                "value": "11"
                            },
                            {
                                "label": "0~5pA(1T)",
                                "value": "13"
                            }
                        ]
                    }
                },
                "required": [
                    "LSV.TestName",
                    "LSV.SampleRate",
                    "LSV.ScanSpeed",
                    "LSV.InitElec",
                    "LSV.RestTime",
                    "LSV.FinalElec",
                    "LSV.Channel1Sensitivity"
                ]
            },
            "LSV.TestName": {
                "type": "string",
                "description": "实验名称"
            },
            "LSV.SampleRate": {
                "type": "float",
                "description": "LSV采样频率（Hz）"
            },
            "LSV.ScanSpeed": {
                "type": "float",
                "description": "LSV扫描速度（V/s）"
            },
            "LSV.InitElec": {
                "type": "float",
                "description": "LSV初始电位（V）"
            },
            "LSV.RestTime": {
                "type": "int",
                "description": "LSV静止时间（s）"
            },
            "LSV.FinalElec": {
                "type": "float",
                "description": "LSV终止电位（V）"
            },
            "LSV.Channel1Sensitivity": {
                "type": "int",
                "description": "LSV通道灵敏度",
                "enum": [
                    {
                        "label": "0~50pA(100G)",
                        "value": "1"
                    },
                    {
                        "label": "0~500pA(10G)",
                        "value": "2"
                    },
                    {
                        "label": "0~5nA(1G)",
                        "value": "3"
                    },
                    {
                        "label": "0~50nA(100M)",
                        "value": "4"
                    },
                    {
                        "label": "0~500nA(10M)",
                        "value": "5"
                    },
                    {
                        "label": "0~5uA(1M)",
                        "value": "6"
                    },
                    {
                        "label": "0~50uA(100K)",
                        "value": "7"
                    },
                    {
                        "label": "0~500uA(10K)",
                        "value": "8"
                    },
                    {
                        "label": "0~5mA(1K)",
                        "value": "9"
                    },
                    {
                        "label": "0~50mA(100)",
                        "value": "10"
                    },
                    {
                        "label": "0~200mA(10)",
                        "value": "11"
                    },
                    {
                        "label": "0~5pA(1T)",
                        "value": "13"
                    }
                ]
            },
            "IT": {
                "type": "array",
                "description": "IT实验",
                "properties": {
                    "IT.TestName": {
                        "type": "string",
                        "description": "实验名称"
                    },
                    "IT.InitElec": {
                        "type": "float",
                        "description": "IT初始电位"
                    },
                    "IT.SampleInterval": {
                        "type": "float",
                        "description": "IT采样间隔",
                        "enum": [
                            {
                                "label": "500ms",
                                "value": "0"
                            },
                            {
                                "label": "100ms",
                                "value": "1"
                            },
                            {
                                "label": "20ms",
                                "value": "2"
                            },
                            {
                                "label": "1ms",
                                "value": "3"
                            }
                        ]
                    },
                    "IT.RestTime": {
                        "type": "int",
                        "description": "IT静止时间（s）"
                    },
                    "IT.Channel1Sensitivity": {
                        "type": "int",
                        "description": "IT通道灵敏度",
                        "enum": [
                            {
                                "label": "0~50pA(100G)",
                                "value": "1"
                            },
                            {
                                "label": "0~500pA(10G)",
                                "value": "2"
                            },
                            {
                                "label": "0~5nA(1G)",
                                "value": "3"
                            },
                            {
                                "label": "0~50nA(100M)",
                                "value": "4"
                            },
                            {
                                "label": "0~500nA(10M)",
                                "value": "5"
                            },
                            {
                                "label": "0~5uA(1M)",
                                "value": "6"
                            },
                            {
                                "label": "0~50uA(100K)",
                                "value": "7"
                            },
                            {
                                "label": "0~500uA(10K)",
                                "value": "8"
                            },
                            {
                                "label": "0~5mA(1K)",
                                "value": "9"
                            },
                            {
                                "label": "0~50mA(100)",
                                "value": "10"
                            },
                            {
                                "label": "0~200mA(10)",
                                "value": "11"
                            },
                            {
                                "label": "0~5pA(1T)",
                                "value": "13"
                            }
                        ]
                    },
                    "IT.RunTime": {
                        "type": "float",
                        "description": "IT运行时间（s）"
                    }
                },
                "required": [
                    "IT.TestName",
                    "IT.InitElec",
                    "IT.SampleInterval",
                    "IT.RestTime",
                    "IT.Channel1Sensitivity",
                    "IT.RunTime"
                ]
            },
            "IT.TestName": {
                "type": "string",
                "description": "实验名称"
            },
            "IT.InitElec": {
                "type": "float",
                "description": "IT初始电位"
            },
            "IT.SampleInterval": {
                "type": "float",
                "description": "IT采样间隔",
                "enum": [
                    {
                        "label": "500ms",
                        "value": "0"
                    },
                    {
                        "label": "100ms",
                        "value": "1"
                    },
                    {
                        "label": "20ms",
                        "value": "2"
                    },
                    {
                        "label": "1ms",
                        "value": "3"
                    }
                ]
            },
            "IT.RestTime": {
                "type": "int",
                "description": "IT静止时间（s）"
            },
            "IT.Channel1Sensitivity": {
                "type": "int",
                "description": "IT通道灵敏度",
                "enum": [
                    {
                        "label": "0~50pA(100G)",
                        "value": "1"
                    },
                    {
                        "label": "0~500pA(10G)",
                        "value": "2"
                    },
                    {
                        "label": "0~5nA(1G)",
                        "value": "3"
                    },
                    {
                        "label": "0~50nA(100M)",
                        "value": "4"
                    },
                    {
                        "label": "0~500nA(10M)",
                        "value": "5"
                    },
                    {
                        "label": "0~5uA(1M)",
                        "value": "6"
                    },
                    {
                        "label": "0~50uA(100K)",
                        "value": "7"
                    },
                    {
                        "label": "0~500uA(10K)",
                        "value": "8"
                    },
                    {
                        "label": "0~5mA(1K)",
                        "value": "9"
                    },
                    {
                        "label": "0~50mA(100)",
                        "value": "10"
                    },
                    {
                        "label": "0~200mA(10)",
                        "value": "11"
                    },
                    {
                        "label": "0~5pA(1T)",
                        "value": "13"
                    }
                ]
            },
            "IT.RunTime": {
                "type": "float",
                "description": "IT运行时间（s）"
            },
            "OCPT": {
                "type": "array",
                "description": "OCPT实验",
                "properties": {
                    "OCPT.TestName": {
                        "type": "string",
                        "description": "实验名称"
                    },
                    "OCPT.SampleInterval": {
                        "type": "float",
                        "description": "OCPT采样间隔",
                        "enum": [
                            {
                                "label": "500ms",
                                "value": "0"
                            },
                            {
                                "label": "100ms",
                                "value": "1"
                            },
                            {
                                "label": "20ms",
                                "value": "2"
                            },
                            {
                                "label": "1ms",
                                "value": "3"
                            }
                        ]
                    },
                    "OCPT.HighElec": {
                        "type": "float",
                        "description": "OCPT高电位（V）"
                    },
                    "OCPT.RunTime": {
                        "type": "float",
                        "description": "OCPT运行时间（s）"
                    },
                    "OCPT.LowElec_OCPT": {
                        "type": "float",
                        "description": "OCPT低电位（V）"
                    }
                },
                "required": [
                    "OCPT.TestName",
                    "OCPT.SampleInterval",
                    "OCPT.HighElec",
                    "OCPT.RunTime",
                    "OCPT.LowElec_OCPT"
                ]
            },
            "OCPT.TestName": {
                "type": "string",
                "description": "实验名称"
            },
            "OCPT.SampleInterval": {
                "type": "float",
                "description": "OCPT采样间隔",
                "enum": [
                    {
                        "label": "500ms",
                        "value": "0"
                    },
                    {
                        "label": "100ms",
                        "value": "1"
                    },
                    {
                        "label": "20ms",
                        "value": "2"
                    },
                    {
                        "label": "1ms",
                        "value": "3"
                    }
                ]
            },
            "OCPT.HighElec": {
                "type": "float",
                "description": "OCPT高电位（V）"
            },
            "OCPT.RunTime": {
                "type": "float",
                "description": "OCPT运行时间（s）"
            },
            "OCPT.LowElec_OCPT": {
                "type": "float",
                "description": "OCPT低电位（V）"
            }
        },
        "required": [
            "CV.TestName",
            "CV.InitElec",
            "CV.LowElec",
            "CV.HighElec",
            "CV.FinalElec",
            "CV.SampleInterval",
            "CV.RestTime",
            "CV.ScanDirection",
            "CV.ScanCycles",
            "CV.ScanSpeed",
            "CV.Channel1Sensitivity",
            "LSV.TestName",
            "LSV.SampleRate",
            "LSV.ScanSpeed",
            "LSV.InitElec",
            "LSV.RestTime",
            "LSV.FinalElec",
            "LSV.Channel1Sensitivity",
            "IT.TestName",
            "IT.InitElec",
            "IT.SampleInterval",
            "IT.RestTime",
            "IT.Channel1Sensitivity",
            "IT.RunTime",
            "OCPT.TestName",
            "OCPT.SampleInterval",
            "OCPT.HighElec",
            "OCPT.RunTime",
            "OCPT.LowElec_OCPT"
        ]
    },
    "TestParam.CV": {
        "type": "array",
        "description": "CV实验",
        "properties": {
            "CV.TestName": {
                "type": "string",
                "description": "实验名称"
            },
            "CV.InitElec": {
                "type": "float",
                "description": "CV初始电位（V）"
            },
            "CV.LowElec": {
                "type": "float",
                "description": "CV最低电位（V）"
            },
            "CV.HighElec": {
                "type": "float",
                "description": "CV最高电位（V）"
            },
            "CV.FinalElec": {
                "type": "float",
                "description": "CV终止电位（V）"
            },
            "CV.SampleInterval": {
                "type": "float",
                "description": "CV采样间隔（V）"
            },
            "CV.RestTime": {
                "type": "int",
                "description": "CV静止时间（s）"
            },
            "CV.ScanDirection": {
                "type": "int",
                "description": "CV扫描方向"
            },
            "CV.ScanCycles": {
                "type": "int",
                "description": "CV扫描圈数"
            },
            "CV.ScanSpeed": {
                "type": "float",
                "description": "CV扫描速度（V/s）"
            },
            "CV.Channel1Sensitivity": {
                "type": "int",
                "description": "CV通道灵敏度",
                "enum": [
                    {
                        "label": "0~50pA(100G)",
                        "value": "1"
                    },
                    {
                        "label": "0~500pA(10G)",
                        "value": "2"
                    },
                    {
                        "label": "0~5nA(1G)",
                        "value": "3"
                    },
                    {
                        "label": "0~50nA(100M)",
                        "value": "4"
                    },
                    {
                        "label": "0~500nA(10M)",
                        "value": "5"
                    },
                    {
                        "label": "0~5uA(1M)",
                        "value": "6"
                    },
                    {
                        "label": "0~50uA(100K)",
                        "value": "7"
                    },
                    {
                        "label": "0~500uA(10K)",
                        "value": "8"
                    },
                    {
                        "label": "0~5mA(1K)",
                        "value": "9"
                    },
                    {
                        "label": "0~50mA(100)",
                        "value": "10"
                    },
                    {
                        "label": "0~200mA(10)",
                        "value": "11"
                    },
                    {
                        "label": "0~5pA(1T)",
                        "value": "13"
                    }
                ]
            }
        },
        "required": [
            "CV.TestName",
            "CV.InitElec",
            "CV.LowElec",
            "CV.HighElec",
            "CV.FinalElec",
            "CV.SampleInterval",
            "CV.RestTime",
            "CV.ScanDirection",
            "CV.ScanCycles",
            "CV.ScanSpeed",
            "CV.Channel1Sensitivity"
        ]
    },
    "TestParam.CV.TestName": {
        "type": "string",
        "description": "实验名称"
    },
    "TestParam.CV.InitElec": {
        "type": "float",
        "description": "CV初始电位（V）"
    },
    "TestParam.CV.LowElec": {
        "type": "float",
        "description": "CV最低电位（V）"
    },
    "TestParam.CV.HighElec": {
        "type": "float",
        "description": "CV最高电位（V）"
    },
    "TestParam.CV.FinalElec": {
        "type": "float",
        "description": "CV终止电位（V）"
    },
    "TestParam.CV.SampleInterval": {
        "type": "float",
        "description": "CV采样间隔（V）"
    },
    "TestParam.CV.RestTime": {
        "type": "int",
        "description": "CV静止时间（s）"
    },
    "TestParam.CV.ScanDirection": {
        "type": "int",
        "description": "CV扫描方向"
    },
    "TestParam.CV.ScanCycles": {
        "type": "int",
        "description": "CV扫描圈数"
    },
    "TestParam.CV.ScanSpeed": {
        "type": "float",
        "description": "CV扫描速度（V/s）"
    },
    "TestParam.CV.Channel1Sensitivity": {
        "type": "int",
        "description": "CV通道灵敏度",
        "enum": [
            {
                "label": "0~50pA(100G)",
                "value": "1"
            },
            {
                "label": "0~500pA(10G)",
                "value": "2"
            },
            {
                "label": "0~5nA(1G)",
                "value": "3"
            },
            {
                "label": "0~50nA(100M)",
                "value": "4"
            },
            {
                "label": "0~500nA(10M)",
                "value": "5"
            },
            {
                "label": "0~5uA(1M)",
                "value": "6"
            },
            {
                "label": "0~50uA(100K)",
                "value": "7"
            },
            {
                "label": "0~500uA(10K)",
                "value": "8"
            },
            {
                "label": "0~5mA(1K)",
                "value": "9"
            },
            {
                "label": "0~50mA(100)",
                "value": "10"
            },
            {
                "label": "0~200mA(10)",
                "value": "11"
            },
            {
                "label": "0~5pA(1T)",
                "value": "13"
            }
        ]
    },
    "TestParam.LSV": {
        "type": "array",
        "description": "LSV实验",
        "properties": {
            "LSV.TestName": {
                "type": "string",
                "description": "实验名称"
            },
            "LSV.SampleRate": {
                "type": "float",
                "description": "LSV采样频率（Hz）"
            },
            "LSV.ScanSpeed": {
                "type": "float",
                "description": "LSV扫描速度（V/s）"
            },
            "LSV.InitElec": {
                "type": "float",
                "description": "LSV初始电位（V）"
            },
            "LSV.RestTime": {
                "type": "int",
                "description": "LSV静止时间（s）"
            },
            "LSV.FinalElec": {
                "type": "float",
                "description": "LSV终止电位（V）"
            },
            "LSV.Channel1Sensitivity": {
                "type": "int",
                "description": "LSV通道灵敏度",
                "enum": [
                    {
                        "label": "0~50pA(100G)",
                        "value": "1"
                    },
                    {
                        "label": "0~500pA(10G)",
                        "value": "2"
                    },
                    {
                        "label": "0~5nA(1G)",
                        "value": "3"
                    },
                    {
                        "label": "0~50nA(100M)",
                        "value": "4"
                    },
                    {
                        "label": "0~500nA(10M)",
                        "value": "5"
                    },
                    {
                        "label": "0~5uA(1M)",
                        "value": "6"
                    },
                    {
                        "label": "0~50uA(100K)",
                        "value": "7"
                    },
                    {
                        "label": "0~500uA(10K)",
                        "value": "8"
                    },
                    {
                        "label": "0~5mA(1K)",
                        "value": "9"
                    },
                    {
                        "label": "0~50mA(100)",
                        "value": "10"
                    },
                    {
                        "label": "0~200mA(10)",
                        "value": "11"
                    },
                    {
                        "label": "0~5pA(1T)",
                        "value": "13"
                    }
                ]
            }
        },
        "required": [
            "LSV.TestName",
            "LSV.SampleRate",
            "LSV.ScanSpeed",
            "LSV.InitElec",
            "LSV.RestTime",
            "LSV.FinalElec",
            "LSV.Channel1Sensitivity"
        ]
    },
    "TestParam.LSV.TestName": {
        "type": "string",
        "description": "实验名称"
    },
    "TestParam.LSV.SampleRate": {
        "type": "float",
        "description": "LSV采样频率（Hz）"
    },
    "TestParam.LSV.ScanSpeed": {
        "type": "float",
        "description": "LSV扫描速度（V/s）"
    },
    "TestParam.LSV.InitElec": {
        "type": "float",
        "description": "LSV初始电位（V）"
    },
    "TestParam.LSV.RestTime": {
        "type": "int",
        "description": "LSV静止时间（s）"
    },
    "TestParam.LSV.FinalElec": {
        "type": "float",
        "description": "LSV终止电位（V）"
    },
    "TestParam.LSV.Channel1Sensitivity": {
        "type": "int",
        "description": "LSV通道灵敏度",
        "enum": [
            {
                "label": "0~50pA(100G)",
                "value": "1"
            },
            {
                "label": "0~500pA(10G)",
                "value": "2"
            },
            {
                "label": "0~5nA(1G)",
                "value": "3"
            },
            {
                "label": "0~50nA(100M)",
                "value": "4"
            },
            {
                "label": "0~500nA(10M)",
                "value": "5"
            },
            {
                "label": "0~5uA(1M)",
                "value": "6"
            },
            {
                "label": "0~50uA(100K)",
                "value": "7"
            },
            {
                "label": "0~500uA(10K)",
                "value": "8"
            },
            {
                "label": "0~5mA(1K)",
                "value": "9"
            },
            {
                "label": "0~50mA(100)",
                "value": "10"
            },
            {
                "label": "0~200mA(10)",
                "value": "11"
            },
            {
                "label": "0~5pA(1T)",
                "value": "13"
            }
        ]
    },
    "TestParam.IT": {
        "type": "array",
        "description": "IT实验",
        "properties": {
            "IT.TestName": {
                "type": "string",
                "description": "实验名称"
            },
            "IT.InitElec": {
                "type": "float",
                "description": "IT初始电位"
            },
            "IT.SampleInterval": {
                "type": "float",
                "description": "IT采样间隔",
                "enum": [
                    {
                        "label": "500ms",
                        "value": "0"
                    },
                    {
                        "label": "100ms",
                        "value": "1"
                    },
                    {
                        "label": "20ms",
                        "value": "2"
                    },
                    {
                        "label": "1ms",
                        "value": "3"
                    }
                ]
            },
            "IT.RestTime": {
                "type": "int",
                "description": "IT静止时间（s）"
            },
            "IT.Channel1Sensitivity": {
                "type": "int",
                "description": "IT通道灵敏度",
                "enum": [
                    {
                        "label": "0~50pA(100G)",
                        "value": "1"
                    },
                    {
                        "label": "0~500pA(10G)",
                        "value": "2"
                    },
                    {
                        "label": "0~5nA(1G)",
                        "value": "3"
                    },
                    {
                        "label": "0~50nA(100M)",
                        "value": "4"
                    },
                    {
                        "label": "0~500nA(10M)",
                        "value": "5"
                    },
                    {
                        "label": "0~5uA(1M)",
                        "value": "6"
                    },
                    {
                        "label": "0~50uA(100K)",
                        "value": "7"
                    },
                    {
                        "label": "0~500uA(10K)",
                        "value": "8"
                    },
                    {
                        "label": "0~5mA(1K)",
                        "value": "9"
                    },
                    {
                        "label": "0~50mA(100)",
                        "value": "10"
                    },
                    {
                        "label": "0~200mA(10)",
                        "value": "11"
                    },
                    {
                        "label": "0~5pA(1T)",
                        "value": "13"
                    }
                ]
            },
            "IT.RunTime": {
                "type": "float",
                "description": "IT运行时间（s）"
            }
        },
        "required": [
            "IT.TestName",
            "IT.InitElec",
            "IT.SampleInterval",
            "IT.RestTime",
            "IT.Channel1Sensitivity",
            "IT.RunTime"
        ]
    },
    "TestParam.IT.TestName": {
        "type": "string",
        "description": "实验名称"
    },
    "TestParam.IT.InitElec": {
        "type": "float",
        "description": "IT初始电位"
    },
    "TestParam.IT.SampleInterval": {
        "type": "float",
        "description": "IT采样间隔",
        "enum": [
            {
                "label": "500ms",
                "value": "0"
            },
            {
                "label": "100ms",
                "value": "1"
            },
            {
                "label": "20ms",
                "value": "2"
            },
            {
                "label": "1ms",
                "value": "3"
            }
        ]
    },
    "TestParam.IT.RestTime": {
        "type": "int",
        "description": "IT静止时间（s）"
    },
    "TestParam.IT.Channel1Sensitivity": {
        "type": "int",
        "description": "IT通道灵敏度",
        "enum": [
            {
                "label": "0~50pA(100G)",
                "value": "1"
            },
            {
                "label": "0~500pA(10G)",
                "value": "2"
            },
            {
                "label": "0~5nA(1G)",
                "value": "3"
            },
            {
                "label": "0~50nA(100M)",
                "value": "4"
            },
            {
                "label": "0~500nA(10M)",
                "value": "5"
            },
            {
                "label": "0~5uA(1M)",
                "value": "6"
            },
            {
                "label": "0~50uA(100K)",
                "value": "7"
            },
            {
                "label": "0~500uA(10K)",
                "value": "8"
            },
            {
                "label": "0~5mA(1K)",
                "value": "9"
            },
            {
                "label": "0~50mA(100)",
                "value": "10"
            },
            {
                "label": "0~200mA(10)",
                "value": "11"
            },
            {
                "label": "0~5pA(1T)",
                "value": "13"
            }
        ]
    },
    "TestParam.IT.RunTime": {
        "type": "float",
        "description": "IT运行时间（s）"
    },
    "TestParam.OCPT": {
        "type": "array",
        "description": "OCPT实验",
        "properties": {
            "OCPT.TestName": {
                "type": "string",
                "description": "实验名称"
            },
            "OCPT.SampleInterval": {
                "type": "float",
                "description": "OCPT采样间隔",
                "enum": [
                    {
                        "label": "500ms",
                        "value": "0"
                    },
                    {
                        "label": "100ms",
                        "value": "1"
                    },
                    {
                        "label": "20ms",
                        "value": "2"
                    },
                    {
                        "label": "1ms",
                        "value": "3"
                    }
                ]
            },
            "OCPT.HighElec": {
                "type": "float",
                "description": "OCPT高电位（V）"
            },
            "OCPT.RunTime": {
                "type": "float",
                "description": "OCPT运行时间（s）"
            },
            "OCPT.LowElec_OCPT": {
                "type": "float",
                "description": "OCPT低电位（V）"
            }
        },
        "required": [
            "OCPT.TestName",
            "OCPT.SampleInterval",
            "OCPT.HighElec",
            "OCPT.RunTime",
            "OCPT.LowElec_OCPT"
        ]
    },
    "TestParam.OCPT.TestName": {
        "type": "string",
        "description": "实验名称"
    },
    "TestParam.OCPT.SampleInterval": {
        "type": "float",
        "description": "OCPT采样间隔",
        "enum": [
            {
                "label": "500ms",
                "value": "0"
            },
            {
                "label": "100ms",
                "value": "1"
            },
            {
                "label": "20ms",
                "value": "2"
            },
            {
                "label": "1ms",
                "value": "3"
            }
        ]
    },
    "TestParam.OCPT.HighElec": {
        "type": "float",
        "description": "OCPT高电位（V）"
    },
    "TestParam.OCPT.RunTime": {
        "type": "float",
        "description": "OCPT运行时间（s）"
    },
    "TestParam.OCPT.LowElec_OCPT": {
        "type": "float",
        "description": "OCPT低电位（V）"
    },
    "result": {
        "type": "file",
        "description": "结果上传"
    }
},
                "required": ["type", "cmd", "Name", "PhotoLocation", "TestMethod", "TestPoint", "XAxis", "YAxis", "TestParam", "TestParam.CV.TestName", "TestParam.CV.InitElec", "TestParam.CV.LowElec", "TestParam.CV.HighElec", "TestParam.CV.FinalElec", "TestParam.CV.SampleInterval", "TestParam.CV.RestTime", "TestParam.CV.ScanDirection", "TestParam.CV.ScanCycles", "TestParam.CV.ScanSpeed", "TestParam.CV.Channel1Sensitivity", "TestParam.LSV.TestName", "TestParam.LSV.SampleRate", "TestParam.LSV.ScanSpeed", "TestParam.LSV.InitElec", "TestParam.LSV.RestTime", "TestParam.LSV.FinalElec", "TestParam.LSV.Channel1Sensitivity", "TestParam.IT.TestName", "TestParam.IT.InitElec", "TestParam.IT.SampleInterval", "TestParam.IT.RestTime", "TestParam.IT.Channel1Sensitivity", "TestParam.IT.RunTime", "TestParam.OCPT.TestName", "TestParam.OCPT.SampleInterval", "TestParam.OCPT.HighElec", "TestParam.OCPT.RunTime", "TestParam.OCPT.LowElec_OCPT"]
            }
        }
                    ]
                }
            }
        }
    }
    print(json.dumps(adv_message, ensure_ascii=False), flush=True)
    print(f"--- [high_throughput_advanced_material_screening_workstation_Server] 高通量电化学筛选工作站 is ready. ---", file=sys.stderr, flush=True)


if __name__ == "__main__":
    # 启动流程：先广播能力，再进入主循环
    high_throughput_advanced_material_screening_workstation_server_advertise_capabilities()
    high_throughput_advanced_material_screening_workstation_server_main_loop()
