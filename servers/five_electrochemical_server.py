import sys
import json
# 动态导入当前设备对应的工具类（与主服务器文件同目录）
from tools.five_electrochemical_server_tools import ActionServerTools


# 创建全局工具管理器实例
tool_manager = ActionServerTools()


# --- 定义设备动作函数（自动生成，与工具类方法对应）---
def tool_detection(**params):
    return tool_manager.tool_detection(**params)



AVAILABLE_TOOLS_ACTION = {
    "detection": tool_detection
}


# --- MCP协议通信主逻辑（自动适配当前设备）---
def five_electrochemical_server_main_loop():
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
            print(f"--- [five_electrochemical_Server] Critical Error: {str(e)} ---", file=sys.stderr, flush=True)


def five_electrochemical_server_advertise_capabilities():
    """广播当前设备的MCP能力（设备信息、支持的动作）"""
    adv_message = {
        "jsonrpc": "2.0",
        "method": "protocol/advertise",
        "params": {
            "type": "server",
            "server": {
                "protocolVersion": "0.1.0",
                "displayName": "五工位电化学工作站",
                "capabilities": {
                    "tools": [
        {
            "name": "detection",
            "description": "电化学检测",
            "parameters": {
                "type": "object",
                "properties": {
    "poolOne": {
        "type": "object",
        "description": "电解池1号",
        "properties": {
            "joinStatus": {
                "type": "string",
                "description": "是否参与实验",
                "enum": [
                    {
                        "label": "否",
                        "value": "0"
                    },
                    {
                        "label": "是",
                        "value": "1"
                    }
                ]
            },
            "bottleType": {
                "type": "string",
                "description": "西林瓶类型",
                "enum": [
                    {
                        "label": "关盖螺口瓶",
                        "value": "closedCapScrewBottle"
                    },
                    {
                        "label": "无盖螺口瓶",
                        "value": "uncapScrewBottle"
                    },
                    {
                        "label": "无盖平口瓶",
                        "value": "uncapFlatMouthedBottle"
                    }
                ]
            },
            "bottleCathode": {
                "type": "string",
                "description": "阴极西林瓶",
                "enum": 1
            },
            "bottleAnode": {
                "type": "string",
                "description": "阳极西林瓶",
                "enum": 1
            },
            "bottleCatalyst": {
                "type": "string",
                "description": "催化剂瓶",
                "enum": 1
            },
            "catalystCapacity": {
                "type": "string",
                "description": "催化剂容量（单位：微升）",
                "minimum": "10",
                "maximum": "15000"
            },
            "catalystDropletVolume": {
                "type": "string",
                "description": "催化剂滴液量（单位：微升）",
                "minimum": "10",
                "maximum": "300"
            },
            "carbonPaperType": {
                "type": "string",
                "description": "碳纸类型",
                "enum": [
                    {
                        "label": "亲水性碳纸",
                        "value": "hydrophilicity"
                    },
                    {
                        "label": "疏水性碳纸",
                        "value": "hydrophobicity"
                    }
                ]
            },
            "dryerType": {
                "type": "string",
                "description": "碳纸晾干方式",
                "enum": [
                    {
                        "label": "加热晾干",
                        "value": "heat"
                    },
                    {
                        "label": "自然晾干",
                        "value": "naturalDry"
                    }
                ]
            },
            "dryerTime": {
                "type": "string",
                "description": "碳纸晾干时间（单位：分钟）",
                "minimum": "1",
                "maximum": "90"
            },
            "dryerPower": {
                "type": "string",
                "description": "碳纸晾干温度（单位：摄氏度）",
                "minimum": "0",
                "maximum": "70"
            },
            "electrolyteCycleSpeed": {
                "type": "string",
                "description": "电解池循环速度（单位：毫升/分钟）",
                "minimum": "5",
                "maximum": "35"
            },
            "ventilationTime": {
                "type": "string",
                "description": "通气时长（单位：秒）",
                "minimum": "1",
                "maximum": "60"
            },
            "cleaningFrequency": {
                "type": "string",
                "description": "电解液清洗次数",
                "minimum": "1",
                "maximum": "5"
            },
            "cvStatus": {
                "type": "string",
                "description": "循环伏安法-是否检测",
                "enum": [
                    {
                        "label": "不检测",
                        "value": "0"
                    },
                    {
                        "label": "检测",
                        "value": "1"
                    }
                ]
            },
            "cvInitE": {
                "type": "string",
                "description": "循环伏安法-初始电位（单位：伏特）",
                "minimum": "-10",
                "maximum": "10"
            },
            "cvHighE": {
                "type": "string",
                "description": "循环伏安法-上限电位（单位：伏特）",
                "minimum": "-10",
                "maximum": "10"
            },
            "cvLowE": {
                "type": "string",
                "description": "循环伏安法-下限电位（单位：伏特）",
                "minimum": "-10",
                "maximum": "10"
            },
            "cvFinalE": {
                "type": "string",
                "description": "循环伏安法-终点电位（单位：伏特）",
                "minimum": "-10",
                "maximum": "10"
            },
            "cvInitialScanPolarity": {
                "type": "string",
                "description": "循环伏安法-初始化扫码方向",
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
            "cvScanRate": {
                "type": "string",
                "description": "循环伏安法-扫描速度",
                "minimum": "1e-6",
                "maximum": "10000"
            },
            "cvSweepSegments": {
                "type": "string",
                "description": "循环伏安法-扫描段数",
                "minimum": "1",
                "maximum": "1000000"
            },
            "cvSampleInterval": {
                "type": "string",
                "description": "循环伏安法-采样间隔",
                "minimum": "0.001",
                "maximum": "0.064"
            },
            "cvQuietTime": {
                "type": "string",
                "description": "循环伏安法-静置时间",
                "minimum": "1",
                "maximum": "1000000"
            },
            "cvSensitivity": {
                "type": "string",
                "description": "循环伏安法-灵敏度",
                "enum": [
                    "1e-001",
                    "1e-002",
                    "1e-003",
                    "1e-004",
                    "1e-005",
                    "1e-006",
                    "1e-007",
                    "1e-008",
                    "1e-009",
                    "1e-010",
                    "1e-011",
                    "1e-012"
                ]
            },
            "lsvStatus": {
                "type": "string",
                "description": "线性扫描伏安法-是否检测",
                "enum": [
                    {
                        "label": "不检测",
                        "value": "0"
                    },
                    {
                        "label": "检测",
                        "value": "1"
                    }
                ]
            },
            "lsvInitE": {
                "type": "string",
                "description": "线性扫描伏安法-初始电位（单位：伏特）",
                "minimum": "-10",
                "maximum": "10"
            },
            "lsvFinalE": {
                "type": "string",
                "description": "线性扫描伏安法-终点电位（单位：伏特）",
                "minimum": "-10",
                "maximum": "10"
            },
            "lsvScanRate": {
                "type": "string",
                "description": "线性扫描伏安法-扫描速度",
                "minimum": "1e-6",
                "maximum": "20000"
            },
            "lsvSampleInterval": {
                "type": "string",
                "description": "线性扫描伏安法-采样间隔",
                "minimum": "0.001",
                "maximum": "0.064"
            },
            "lsvQuietTime": {
                "type": "string",
                "description": "线性扫描伏安法-静置时间",
                "minimum": "1",
                "maximum": "1000000"
            },
            "lsvSensitivity": {
                "type": "string",
                "description": "线性扫描伏安法-灵敏度",
                "enum": [
                    "1e-001",
                    "1e-002",
                    "1e-003",
                    "1e-004",
                    "1e-005",
                    "1e-006",
                    "1e-007",
                    "1e-008",
                    "1e-009",
                    "1e-010",
                    "1e-011",
                    "1e-012"
                ]
            },
            "etcStatus": {
                "type": "string",
                "description": "电流/时间曲线-是否检测",
                "enum": [
                    {
                        "label": "不检测",
                        "value": "0"
                    },
                    {
                        "label": "检测",
                        "value": "1"
                    }
                ]
            },
            "etcInitE": {
                "type": "string",
                "description": "电流/时间曲线-初始电位（单位：伏特）",
                "minimum": "-10",
                "maximum": "10"
            },
            "etcSampleInterval": {
                "type": "string",
                "description": "电流/时间曲线-采样间隔",
                "minimum": "1e-6",
                "maximum": "50"
            },
            "etcRunTime": {
                "type": "string",
                "description": "电流/时间曲线-运行时间",
                "minimum": "0.001",
                "maximum": "500000"
            },
            "etcQuietTime": {
                "type": "string",
                "description": "电流/时间曲线-静置时间",
                "minimum": "1",
                "maximum": "1000000"
            },
            "etcScalesDuringRun": {
                "type": "string",
                "description": "电流/时间曲线-电流量程档数",
                "enum": 1
            },
            "etcSensitivity": {
                "type": "string",
                "description": "电流/时间曲线-灵敏度",
                "enum": [
                    "1e-001",
                    "1e-002",
                    "1e-003",
                    "1e-004",
                    "1e-005",
                    "1e-006",
                    "1e-007",
                    "1e-008",
                    "1e-009",
                    "1e-010",
                    "1e-011",
                    "1e-012"
                ]
            },
            "acimStatus": {
                "type": "string",
                "description": "交流阻抗测量-是否检测",
                "enum": [
                    {
                        "label": "不检测",
                        "value": "0"
                    },
                    {
                        "label": "检测",
                        "value": "1"
                    }
                ]
            },
            "acimInitE": {
                "type": "string",
                "description": "交流阻抗测量-初始电位（单位：伏特）",
                "minimum": "-10",
                "maximum": "10"
            },
            "acimHighFrequency": {
                "type": "string",
                "description": "交流阻抗测量-上限频率（单位：赫兹）",
                "minimum": "1e-4",
                "maximum": "2e6"
            },
            "acimLowFrequency": {
                "type": "string",
                "description": "交流阻抗测量-下限频率（单位：赫兹）",
                "minimum": "1e-5",
                "maximum": "1e5"
            },
            "acimAmplitude": {
                "type": "string",
                "description": "交流阻抗测量-振幅",
                "minimum": "1e-5",
                "maximum": "0.7"
            },
            "acimQuietTime": {
                "type": "string",
                "description": "交流阻抗测量-静置时间",
                "minimum": "1",
                "maximum": "1000000"
            }
        },
        "required": [
            "joinStatus",
            "bottleType",
            "bottleCathode",
            "bottleAnode",
            "bottleCatalyst",
            "catalystCapacity",
            "catalystDropletVolume",
            "carbonPaperType",
            "dryerType",
            "dryerTime",
            "dryerPower",
            "electrolyteCycleSpeed",
            "ventilationTime",
            "cleaningFrequency",
            "cvStatus",
            "lsvStatus",
            "etcStatus",
            "acimStatus"
        ]
    },
    "poolOne.joinStatus": {
        "type": "string",
        "description": "是否参与实验",
        "enum": [
            {
                "label": "否",
                "value": "0"
            },
            {
                "label": "是",
                "value": "1"
            }
        ]
    },
    "poolOne.bottleType": {
        "type": "string",
        "description": "西林瓶类型",
        "enum": [
            {
                "label": "关盖螺口瓶",
                "value": "closedCapScrewBottle"
            },
            {
                "label": "无盖螺口瓶",
                "value": "uncapScrewBottle"
            },
            {
                "label": "无盖平口瓶",
                "value": "uncapFlatMouthedBottle"
            }
        ]
    },
    "poolOne.bottleCathode": {
        "type": "string",
        "description": "阴极西林瓶",
        "enum": 1
    },
    "poolOne.bottleAnode": {
        "type": "string",
        "description": "阳极西林瓶",
        "enum": 1
    },
    "poolOne.bottleCatalyst": {
        "type": "string",
        "description": "催化剂瓶",
        "enum": 1
    },
    "poolOne.catalystCapacity": {
        "type": "string",
        "description": "催化剂容量（单位：微升）",
        "minimum": "10",
        "maximum": "15000"
    },
    "poolOne.catalystDropletVolume": {
        "type": "string",
        "description": "催化剂滴液量（单位：微升）",
        "minimum": "10",
        "maximum": "300"
    },
    "poolOne.carbonPaperType": {
        "type": "string",
        "description": "碳纸类型",
        "enum": [
            {
                "label": "亲水性碳纸",
                "value": "hydrophilicity"
            },
            {
                "label": "疏水性碳纸",
                "value": "hydrophobicity"
            }
        ]
    },
    "poolOne.dryerType": {
        "type": "string",
        "description": "碳纸晾干方式",
        "enum": [
            {
                "label": "加热晾干",
                "value": "heat"
            },
            {
                "label": "自然晾干",
                "value": "naturalDry"
            }
        ]
    },
    "poolOne.dryerTime": {
        "type": "string",
        "description": "碳纸晾干时间（单位：分钟）",
        "minimum": "1",
        "maximum": "90"
    },
    "poolOne.dryerPower": {
        "type": "string",
        "description": "碳纸晾干温度（单位：摄氏度）",
        "minimum": "0",
        "maximum": "70"
    },
    "poolOne.electrolyteCycleSpeed": {
        "type": "string",
        "description": "电解池循环速度（单位：毫升/分钟）",
        "minimum": "5",
        "maximum": "35"
    },
    "poolOne.ventilationTime": {
        "type": "string",
        "description": "通气时长（单位：秒）",
        "minimum": "1",
        "maximum": "60"
    },
    "poolOne.cleaningFrequency": {
        "type": "string",
        "description": "电解液清洗次数",
        "minimum": "1",
        "maximum": "5"
    },
    "poolOne.cvStatus": {
        "type": "string",
        "description": "循环伏安法-是否检测",
        "enum": [
            {
                "label": "不检测",
                "value": "0"
            },
            {
                "label": "检测",
                "value": "1"
            }
        ]
    },
    "poolOne.cvInitE": {
        "type": "string",
        "description": "循环伏安法-初始电位（单位：伏特）",
        "minimum": "-10",
        "maximum": "10"
    },
    "poolOne.cvHighE": {
        "type": "string",
        "description": "循环伏安法-上限电位（单位：伏特）",
        "minimum": "-10",
        "maximum": "10"
    },
    "poolOne.cvLowE": {
        "type": "string",
        "description": "循环伏安法-下限电位（单位：伏特）",
        "minimum": "-10",
        "maximum": "10"
    },
    "poolOne.cvFinalE": {
        "type": "string",
        "description": "循环伏安法-终点电位（单位：伏特）",
        "minimum": "-10",
        "maximum": "10"
    },
    "poolOne.cvInitialScanPolarity": {
        "type": "string",
        "description": "循环伏安法-初始化扫码方向",
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
    "poolOne.cvScanRate": {
        "type": "string",
        "description": "循环伏安法-扫描速度",
        "minimum": "1e-6",
        "maximum": "10000"
    },
    "poolOne.cvSweepSegments": {
        "type": "string",
        "description": "循环伏安法-扫描段数",
        "minimum": "1",
        "maximum": "1000000"
    },
    "poolOne.cvSampleInterval": {
        "type": "string",
        "description": "循环伏安法-采样间隔",
        "minimum": "0.001",
        "maximum": "0.064"
    },
    "poolOne.cvQuietTime": {
        "type": "string",
        "description": "循环伏安法-静置时间",
        "minimum": "1",
        "maximum": "1000000"
    },
    "poolOne.cvSensitivity": {
        "type": "string",
        "description": "循环伏安法-灵敏度",
        "enum": [
            "1e-001",
            "1e-002",
            "1e-003",
            "1e-004",
            "1e-005",
            "1e-006",
            "1e-007",
            "1e-008",
            "1e-009",
            "1e-010",
            "1e-011",
            "1e-012"
        ]
    },
    "poolOne.lsvStatus": {
        "type": "string",
        "description": "线性扫描伏安法-是否检测",
        "enum": [
            {
                "label": "不检测",
                "value": "0"
            },
            {
                "label": "检测",
                "value": "1"
            }
        ]
    },
    "poolOne.lsvInitE": {
        "type": "string",
        "description": "线性扫描伏安法-初始电位（单位：伏特）",
        "minimum": "-10",
        "maximum": "10"
    },
    "poolOne.lsvFinalE": {
        "type": "string",
        "description": "线性扫描伏安法-终点电位（单位：伏特）",
        "minimum": "-10",
        "maximum": "10"
    },
    "poolOne.lsvScanRate": {
        "type": "string",
        "description": "线性扫描伏安法-扫描速度",
        "minimum": "1e-6",
        "maximum": "20000"
    },
    "poolOne.lsvSampleInterval": {
        "type": "string",
        "description": "线性扫描伏安法-采样间隔",
        "minimum": "0.001",
        "maximum": "0.064"
    },
    "poolOne.lsvQuietTime": {
        "type": "string",
        "description": "线性扫描伏安法-静置时间",
        "minimum": "1",
        "maximum": "1000000"
    },
    "poolOne.lsvSensitivity": {
        "type": "string",
        "description": "线性扫描伏安法-灵敏度",
        "enum": [
            "1e-001",
            "1e-002",
            "1e-003",
            "1e-004",
            "1e-005",
            "1e-006",
            "1e-007",
            "1e-008",
            "1e-009",
            "1e-010",
            "1e-011",
            "1e-012"
        ]
    },
    "poolOne.etcStatus": {
        "type": "string",
        "description": "电流/时间曲线-是否检测",
        "enum": [
            {
                "label": "不检测",
                "value": "0"
            },
            {
                "label": "检测",
                "value": "1"
            }
        ]
    },
    "poolOne.etcInitE": {
        "type": "string",
        "description": "电流/时间曲线-初始电位（单位：伏特）",
        "minimum": "-10",
        "maximum": "10"
    },
    "poolOne.etcSampleInterval": {
        "type": "string",
        "description": "电流/时间曲线-采样间隔",
        "minimum": "1e-6",
        "maximum": "50"
    },
    "poolOne.etcRunTime": {
        "type": "string",
        "description": "电流/时间曲线-运行时间",
        "minimum": "0.001",
        "maximum": "500000"
    },
    "poolOne.etcQuietTime": {
        "type": "string",
        "description": "电流/时间曲线-静置时间",
        "minimum": "1",
        "maximum": "1000000"
    },
    "poolOne.etcScalesDuringRun": {
        "type": "string",
        "description": "电流/时间曲线-电流量程档数",
        "enum": 1
    },
    "poolOne.etcSensitivity": {
        "type": "string",
        "description": "电流/时间曲线-灵敏度",
        "enum": [
            "1e-001",
            "1e-002",
            "1e-003",
            "1e-004",
            "1e-005",
            "1e-006",
            "1e-007",
            "1e-008",
            "1e-009",
            "1e-010",
            "1e-011",
            "1e-012"
        ]
    },
    "poolOne.acimStatus": {
        "type": "string",
        "description": "交流阻抗测量-是否检测",
        "enum": [
            {
                "label": "不检测",
                "value": "0"
            },
            {
                "label": "检测",
                "value": "1"
            }
        ]
    },
    "poolOne.acimInitE": {
        "type": "string",
        "description": "交流阻抗测量-初始电位（单位：伏特）",
        "minimum": "-10",
        "maximum": "10"
    },
    "poolOne.acimHighFrequency": {
        "type": "string",
        "description": "交流阻抗测量-上限频率（单位：赫兹）",
        "minimum": "1e-4",
        "maximum": "2e6"
    },
    "poolOne.acimLowFrequency": {
        "type": "string",
        "description": "交流阻抗测量-下限频率（单位：赫兹）",
        "minimum": "1e-5",
        "maximum": "1e5"
    },
    "poolOne.acimAmplitude": {
        "type": "string",
        "description": "交流阻抗测量-振幅",
        "minimum": "1e-5",
        "maximum": "0.7"
    },
    "poolOne.acimQuietTime": {
        "type": "string",
        "description": "交流阻抗测量-静置时间",
        "minimum": "1",
        "maximum": "1000000"
    },
    "poolTwo": {
        "type": "object",
        "description": "电解池2号",
        "properties": {
            "joinStatus": {
                "type": "string",
                "description": "是否参与实验",
                "enum": [
                    {
                        "label": "否",
                        "value": "0"
                    },
                    {
                        "label": "是",
                        "value": "1"
                    }
                ]
            },
            "bottleType": {
                "type": "string",
                "description": "西林瓶类型",
                "enum": [
                    {
                        "label": "关盖螺口瓶",
                        "value": "closedCapScrewBottle"
                    },
                    {
                        "label": "无盖螺口瓶",
                        "value": "uncapScrewBottle"
                    },
                    {
                        "label": "无盖平口瓶",
                        "value": "uncapFlatMouthedBottle"
                    }
                ]
            },
            "bottleCathode": {
                "type": "string",
                "description": "阴极西林瓶",
                "enum": 2
            },
            "bottleAnode": {
                "type": "string",
                "description": "阳极西林瓶",
                "enum": 2
            },
            "bottleCatalyst": {
                "type": "string",
                "description": "催化剂瓶",
                "enum": 2
            },
            "catalystCapacity": {
                "type": "string",
                "description": "催化剂容量（单位：微升）",
                "minimum": "10",
                "maximum": "15000"
            },
            "catalystDropletVolume": {
                "type": "string",
                "description": "催化剂滴液量（单位：微升）",
                "minimum": "10",
                "maximum": "300"
            },
            "carbonPaperType": {
                "type": "string",
                "description": "碳纸类型",
                "enum": [
                    {
                        "label": "亲水性碳纸",
                        "value": "hydrophilicity"
                    },
                    {
                        "label": "疏水性碳纸",
                        "value": "hydrophobicity"
                    }
                ]
            },
            "dryerType": {
                "type": "string",
                "description": "碳纸晾干方式",
                "enum": [
                    {
                        "label": "加热晾干",
                        "value": "heat"
                    },
                    {
                        "label": "自然晾干",
                        "value": "naturalDry"
                    }
                ]
            },
            "dryerTime": {
                "type": "string",
                "description": "碳纸晾干时间（单位：分钟）",
                "minimum": "1",
                "maximum": "90"
            },
            "dryerPower": {
                "type": "string",
                "description": "碳纸晾干温度（单位：摄氏度）",
                "minimum": "0",
                "maximum": "70"
            },
            "electrolyteCycleSpeed": {
                "type": "string",
                "description": "电解池循环速度（单位：毫升/分钟）",
                "minimum": "5",
                "maximum": "35"
            },
            "ventilationTime": {
                "type": "string",
                "description": "通气时长（单位：秒）",
                "minimum": "1",
                "maximum": "60"
            },
            "cleaningFrequency": {
                "type": "string",
                "description": "电解液清洗次数",
                "minimum": "1",
                "maximum": "5"
            },
            "cvStatus": {
                "type": "string",
                "description": "循环伏安法-是否检测",
                "enum": [
                    {
                        "label": "不检测",
                        "value": "0"
                    },
                    {
                        "label": "检测",
                        "value": "1"
                    }
                ]
            },
            "cvInitE": {
                "type": "string",
                "description": "循环伏安法-初始电位（单位：伏特）",
                "minimum": "-10",
                "maximum": "10"
            },
            "cvHighE": {
                "type": "string",
                "description": "循环伏安法-上限电位（单位：伏特）",
                "minimum": "-10",
                "maximum": "10"
            },
            "cvLowE": {
                "type": "string",
                "description": "循环伏安法-下限电位（单位：伏特）",
                "minimum": "-10",
                "maximum": "10"
            },
            "cvFinalE": {
                "type": "string",
                "description": "循环伏安法-终点电位（单位：伏特）",
                "minimum": "-10",
                "maximum": "10"
            },
            "cvInitialScanPolarity": {
                "type": "string",
                "description": "循环伏安法-初始化扫码方向",
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
            "cvScanRate": {
                "type": "string",
                "description": "循环伏安法-扫描速度",
                "minimum": "1e-6",
                "maximum": "10000"
            },
            "cvSweepSegments": {
                "type": "string",
                "description": "循环伏安法-扫描段数",
                "minimum": "1",
                "maximum": "1000000"
            },
            "cvSampleInterval": {
                "type": "string",
                "description": "循环伏安法-采样间隔",
                "minimum": "0.001",
                "maximum": "0.064"
            },
            "cvQuietTime": {
                "type": "string",
                "description": "循环伏安法-静置时间",
                "minimum": "1",
                "maximum": "1000000"
            },
            "cvSensitivity": {
                "type": "string",
                "description": "循环伏安法-灵敏度",
                "enum": [
                    "1e-001",
                    "1e-002",
                    "1e-003",
                    "1e-004",
                    "1e-005",
                    "1e-006",
                    "1e-007",
                    "1e-008",
                    "1e-009",
                    "1e-010",
                    "1e-011",
                    "1e-012"
                ]
            },
            "lsvStatus": {
                "type": "string",
                "description": "线性扫描伏安法-是否检测",
                "enum": [
                    {
                        "label": "不检测",
                        "value": "0"
                    },
                    {
                        "label": "检测",
                        "value": "1"
                    }
                ]
            },
            "lsvInitE": {
                "type": "string",
                "description": "线性扫描伏安法-初始电位（单位：伏特）",
                "minimum": "-10",
                "maximum": "10"
            },
            "lsvFinalE": {
                "type": "string",
                "description": "线性扫描伏安法-终点电位（单位：伏特）",
                "minimum": "-10",
                "maximum": "10"
            },
            "lsvScanRate": {
                "type": "string",
                "description": "线性扫描伏安法-扫描速度",
                "minimum": "1e-6",
                "maximum": "20000"
            },
            "lsvSampleInterval": {
                "type": "string",
                "description": "线性扫描伏安法-采样间隔",
                "minimum": "0.001",
                "maximum": "0.064"
            },
            "lsvQuietTime": {
                "type": "string",
                "description": "线性扫描伏安法-静置时间",
                "minimum": "1",
                "maximum": "1000000"
            },
            "lsvSensitivity": {
                "type": "string",
                "description": "线性扫描伏安法-灵敏度",
                "enum": [
                    "1e-001",
                    "1e-002",
                    "1e-003",
                    "1e-004",
                    "1e-005",
                    "1e-006",
                    "1e-007",
                    "1e-008",
                    "1e-009",
                    "1e-010",
                    "1e-011",
                    "1e-012"
                ]
            },
            "etcStatus": {
                "type": "string",
                "description": "电流/时间曲线-是否检测",
                "enum": [
                    {
                        "label": "不检测",
                        "value": "0"
                    },
                    {
                        "label": "检测",
                        "value": "1"
                    }
                ]
            },
            "etcInitE": {
                "type": "string",
                "description": "电流/时间曲线-初始电位（单位：伏特）",
                "minimum": "-10",
                "maximum": "10"
            },
            "etcSampleInterval": {
                "type": "string",
                "description": "电流/时间曲线-采样间隔",
                "minimum": "1e-6",
                "maximum": "50"
            },
            "etcRunTime": {
                "type": "string",
                "description": "电流/时间曲线-运行时间",
                "minimum": "0.001",
                "maximum": "500000"
            },
            "etcQuietTime": {
                "type": "string",
                "description": "电流/时间曲线-静置时间",
                "minimum": "1",
                "maximum": "1000000"
            },
            "etcScalesDuringRun": {
                "type": "string",
                "description": "电流/时间曲线-电流量程档数",
                "enum": 1
            },
            "etcSensitivity": {
                "type": "string",
                "description": "电流/时间曲线-灵敏度",
                "enum": [
                    "1e-001",
                    "1e-002",
                    "1e-003",
                    "1e-004",
                    "1e-005",
                    "1e-006",
                    "1e-007",
                    "1e-008",
                    "1e-009",
                    "1e-010",
                    "1e-011",
                    "1e-012"
                ]
            },
            "acimStatus": {
                "type": "string",
                "description": "交流阻抗测量-是否检测",
                "enum": [
                    {
                        "label": "不检测",
                        "value": "0"
                    },
                    {
                        "label": "检测",
                        "value": "1"
                    }
                ]
            },
            "acimInitE": {
                "type": "string",
                "description": "交流阻抗测量-初始电位（单位：伏特）",
                "minimum": "-10",
                "maximum": "10"
            },
            "acimHighFrequency": {
                "type": "string",
                "description": "交流阻抗测量-上限频率（单位：赫兹）",
                "minimum": "1e-4",
                "maximum": "2e6"
            },
            "acimLowFrequency": {
                "type": "string",
                "description": "交流阻抗测量-下限频率（单位：赫兹）",
                "minimum": "1e-5",
                "maximum": "1e5"
            },
            "acimAmplitude": {
                "type": "string",
                "description": "交流阻抗测量-振幅",
                "minimum": "1e-5",
                "maximum": "0.7"
            },
            "acimQuietTime": {
                "type": "string",
                "description": "交流阻抗测量-静置时间",
                "minimum": "1",
                "maximum": "1000000"
            }
        },
        "required": [
            "joinStatus",
            "bottleType",
            "bottleCathode",
            "bottleAnode",
            "bottleCatalyst",
            "catalystCapacity",
            "catalystDropletVolume",
            "carbonPaperType",
            "dryerType",
            "dryerTime",
            "dryerPower",
            "electrolyteCycleSpeed",
            "ventilationTime",
            "cleaningFrequency",
            "cvStatus",
            "lsvStatus",
            "etcStatus",
            "acimStatus"
        ]
    },
    "poolTwo.joinStatus": {
        "type": "string",
        "description": "是否参与实验",
        "enum": [
            {
                "label": "否",
                "value": "0"
            },
            {
                "label": "是",
                "value": "1"
            }
        ]
    },
    "poolTwo.bottleType": {
        "type": "string",
        "description": "西林瓶类型",
        "enum": [
            {
                "label": "关盖螺口瓶",
                "value": "closedCapScrewBottle"
            },
            {
                "label": "无盖螺口瓶",
                "value": "uncapScrewBottle"
            },
            {
                "label": "无盖平口瓶",
                "value": "uncapFlatMouthedBottle"
            }
        ]
    },
    "poolTwo.bottleCathode": {
        "type": "string",
        "description": "阴极西林瓶",
        "enum": 2
    },
    "poolTwo.bottleAnode": {
        "type": "string",
        "description": "阳极西林瓶",
        "enum": 2
    },
    "poolTwo.bottleCatalyst": {
        "type": "string",
        "description": "催化剂瓶",
        "enum": 2
    },
    "poolTwo.catalystCapacity": {
        "type": "string",
        "description": "催化剂容量（单位：微升）",
        "minimum": "10",
        "maximum": "15000"
    },
    "poolTwo.catalystDropletVolume": {
        "type": "string",
        "description": "催化剂滴液量（单位：微升）",
        "minimum": "10",
        "maximum": "300"
    },
    "poolTwo.carbonPaperType": {
        "type": "string",
        "description": "碳纸类型",
        "enum": [
            {
                "label": "亲水性碳纸",
                "value": "hydrophilicity"
            },
            {
                "label": "疏水性碳纸",
                "value": "hydrophobicity"
            }
        ]
    },
    "poolTwo.dryerType": {
        "type": "string",
        "description": "碳纸晾干方式",
        "enum": [
            {
                "label": "加热晾干",
                "value": "heat"
            },
            {
                "label": "自然晾干",
                "value": "naturalDry"
            }
        ]
    },
    "poolTwo.dryerTime": {
        "type": "string",
        "description": "碳纸晾干时间（单位：分钟）",
        "minimum": "1",
        "maximum": "90"
    },
    "poolTwo.dryerPower": {
        "type": "string",
        "description": "碳纸晾干温度（单位：摄氏度）",
        "minimum": "0",
        "maximum": "70"
    },
    "poolTwo.electrolyteCycleSpeed": {
        "type": "string",
        "description": "电解池循环速度（单位：毫升/分钟）",
        "minimum": "5",
        "maximum": "35"
    },
    "poolTwo.ventilationTime": {
        "type": "string",
        "description": "通气时长（单位：秒）",
        "minimum": "1",
        "maximum": "60"
    },
    "poolTwo.cleaningFrequency": {
        "type": "string",
        "description": "电解液清洗次数",
        "minimum": "1",
        "maximum": "5"
    },
    "poolTwo.cvStatus": {
        "type": "string",
        "description": "循环伏安法-是否检测",
        "enum": [
            {
                "label": "不检测",
                "value": "0"
            },
            {
                "label": "检测",
                "value": "1"
            }
        ]
    },
    "poolTwo.cvInitE": {
        "type": "string",
        "description": "循环伏安法-初始电位（单位：伏特）",
        "minimum": "-10",
        "maximum": "10"
    },
    "poolTwo.cvHighE": {
        "type": "string",
        "description": "循环伏安法-上限电位（单位：伏特）",
        "minimum": "-10",
        "maximum": "10"
    },
    "poolTwo.cvLowE": {
        "type": "string",
        "description": "循环伏安法-下限电位（单位：伏特）",
        "minimum": "-10",
        "maximum": "10"
    },
    "poolTwo.cvFinalE": {
        "type": "string",
        "description": "循环伏安法-终点电位（单位：伏特）",
        "minimum": "-10",
        "maximum": "10"
    },
    "poolTwo.cvInitialScanPolarity": {
        "type": "string",
        "description": "循环伏安法-初始化扫码方向",
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
    "poolTwo.cvScanRate": {
        "type": "string",
        "description": "循环伏安法-扫描速度",
        "minimum": "1e-6",
        "maximum": "10000"
    },
    "poolTwo.cvSweepSegments": {
        "type": "string",
        "description": "循环伏安法-扫描段数",
        "minimum": "1",
        "maximum": "1000000"
    },
    "poolTwo.cvSampleInterval": {
        "type": "string",
        "description": "循环伏安法-采样间隔",
        "minimum": "0.001",
        "maximum": "0.064"
    },
    "poolTwo.cvQuietTime": {
        "type": "string",
        "description": "循环伏安法-静置时间",
        "minimum": "1",
        "maximum": "1000000"
    },
    "poolTwo.cvSensitivity": {
        "type": "string",
        "description": "循环伏安法-灵敏度",
        "enum": [
            "1e-001",
            "1e-002",
            "1e-003",
            "1e-004",
            "1e-005",
            "1e-006",
            "1e-007",
            "1e-008",
            "1e-009",
            "1e-010",
            "1e-011",
            "1e-012"
        ]
    },
    "poolTwo.lsvStatus": {
        "type": "string",
        "description": "线性扫描伏安法-是否检测",
        "enum": [
            {
                "label": "不检测",
                "value": "0"
            },
            {
                "label": "检测",
                "value": "1"
            }
        ]
    },
    "poolTwo.lsvInitE": {
        "type": "string",
        "description": "线性扫描伏安法-初始电位（单位：伏特）",
        "minimum": "-10",
        "maximum": "10"
    },
    "poolTwo.lsvFinalE": {
        "type": "string",
        "description": "线性扫描伏安法-终点电位（单位：伏特）",
        "minimum": "-10",
        "maximum": "10"
    },
    "poolTwo.lsvScanRate": {
        "type": "string",
        "description": "线性扫描伏安法-扫描速度",
        "minimum": "1e-6",
        "maximum": "20000"
    },
    "poolTwo.lsvSampleInterval": {
        "type": "string",
        "description": "线性扫描伏安法-采样间隔",
        "minimum": "0.001",
        "maximum": "0.064"
    },
    "poolTwo.lsvQuietTime": {
        "type": "string",
        "description": "线性扫描伏安法-静置时间",
        "minimum": "1",
        "maximum": "1000000"
    },
    "poolTwo.lsvSensitivity": {
        "type": "string",
        "description": "线性扫描伏安法-灵敏度",
        "enum": [
            "1e-001",
            "1e-002",
            "1e-003",
            "1e-004",
            "1e-005",
            "1e-006",
            "1e-007",
            "1e-008",
            "1e-009",
            "1e-010",
            "1e-011",
            "1e-012"
        ]
    },
    "poolTwo.etcStatus": {
        "type": "string",
        "description": "电流/时间曲线-是否检测",
        "enum": [
            {
                "label": "不检测",
                "value": "0"
            },
            {
                "label": "检测",
                "value": "1"
            }
        ]
    },
    "poolTwo.etcInitE": {
        "type": "string",
        "description": "电流/时间曲线-初始电位（单位：伏特）",
        "minimum": "-10",
        "maximum": "10"
    },
    "poolTwo.etcSampleInterval": {
        "type": "string",
        "description": "电流/时间曲线-采样间隔",
        "minimum": "1e-6",
        "maximum": "50"
    },
    "poolTwo.etcRunTime": {
        "type": "string",
        "description": "电流/时间曲线-运行时间",
        "minimum": "0.001",
        "maximum": "500000"
    },
    "poolTwo.etcQuietTime": {
        "type": "string",
        "description": "电流/时间曲线-静置时间",
        "minimum": "1",
        "maximum": "1000000"
    },
    "poolTwo.etcScalesDuringRun": {
        "type": "string",
        "description": "电流/时间曲线-电流量程档数",
        "enum": 1
    },
    "poolTwo.etcSensitivity": {
        "type": "string",
        "description": "电流/时间曲线-灵敏度",
        "enum": [
            "1e-001",
            "1e-002",
            "1e-003",
            "1e-004",
            "1e-005",
            "1e-006",
            "1e-007",
            "1e-008",
            "1e-009",
            "1e-010",
            "1e-011",
            "1e-012"
        ]
    },
    "poolTwo.acimStatus": {
        "type": "string",
        "description": "交流阻抗测量-是否检测",
        "enum": [
            {
                "label": "不检测",
                "value": "0"
            },
            {
                "label": "检测",
                "value": "1"
            }
        ]
    },
    "poolTwo.acimInitE": {
        "type": "string",
        "description": "交流阻抗测量-初始电位（单位：伏特）",
        "minimum": "-10",
        "maximum": "10"
    },
    "poolTwo.acimHighFrequency": {
        "type": "string",
        "description": "交流阻抗测量-上限频率（单位：赫兹）",
        "minimum": "1e-4",
        "maximum": "2e6"
    },
    "poolTwo.acimLowFrequency": {
        "type": "string",
        "description": "交流阻抗测量-下限频率（单位：赫兹）",
        "minimum": "1e-5",
        "maximum": "1e5"
    },
    "poolTwo.acimAmplitude": {
        "type": "string",
        "description": "交流阻抗测量-振幅",
        "minimum": "1e-5",
        "maximum": "0.7"
    },
    "poolTwo.acimQuietTime": {
        "type": "string",
        "description": "交流阻抗测量-静置时间",
        "minimum": "1",
        "maximum": "1000000"
    },
    "poolThree": {
        "type": "object",
        "description": "电解池3号",
        "properties": {
            "joinStatus": {
                "type": "string",
                "description": "是否参与实验",
                "enum": [
                    {
                        "label": "否",
                        "value": "0"
                    },
                    {
                        "label": "是",
                        "value": "1"
                    }
                ]
            },
            "bottleType": {
                "type": "string",
                "description": "西林瓶类型",
                "enum": [
                    {
                        "label": "关盖螺口瓶",
                        "value": "closedCapScrewBottle"
                    },
                    {
                        "label": "无盖螺口瓶",
                        "value": "uncapScrewBottle"
                    },
                    {
                        "label": "无盖平口瓶",
                        "value": "uncapFlatMouthedBottle"
                    }
                ]
            },
            "bottleCathode": {
                "type": "string",
                "description": "阴极西林瓶",
                "enum": 3
            },
            "bottleAnode": {
                "type": "string",
                "description": "阳极西林瓶",
                "enum": 3
            },
            "bottleCatalyst": {
                "type": "string",
                "description": "催化剂瓶",
                "enum": 3
            },
            "catalystCapacity": {
                "type": "string",
                "description": "催化剂容量（单位：微升）",
                "minimum": "10",
                "maximum": "15000"
            },
            "catalystDropletVolume": {
                "type": "string",
                "description": "催化剂滴液量（单位：微升）",
                "minimum": "10",
                "maximum": "300"
            },
            "carbonPaperType": {
                "type": "string",
                "description": "碳纸类型",
                "enum": [
                    {
                        "label": "亲水性碳纸",
                        "value": "hydrophilicity"
                    },
                    {
                        "label": "疏水性碳纸",
                        "value": "hydrophobicity"
                    }
                ]
            },
            "dryerType": {
                "type": "string",
                "description": "碳纸晾干方式",
                "enum": [
                    {
                        "label": "加热晾干",
                        "value": "heat"
                    },
                    {
                        "label": "自然晾干",
                        "value": "naturalDry"
                    }
                ]
            },
            "dryerTime": {
                "type": "string",
                "description": "碳纸晾干时间（单位：分钟）",
                "minimum": "1",
                "maximum": "90"
            },
            "dryerPower": {
                "type": "string",
                "description": "碳纸晾干温度（单位：摄氏度）",
                "minimum": "0",
                "maximum": "70"
            },
            "electrolyteCycleSpeed": {
                "type": "string",
                "description": "电解池循环速度（单位：毫升/分钟）",
                "minimum": "5",
                "maximum": "35"
            },
            "ventilationTime": {
                "type": "string",
                "description": "通气时长（单位：秒）",
                "minimum": "1",
                "maximum": "60"
            },
            "cleaningFrequency": {
                "type": "string",
                "description": "电解液清洗次数",
                "minimum": "1",
                "maximum": "5"
            },
            "cvStatus": {
                "type": "string",
                "description": "循环伏安法-是否检测",
                "enum": [
                    {
                        "label": "不检测",
                        "value": "0"
                    },
                    {
                        "label": "检测",
                        "value": "1"
                    }
                ]
            },
            "cvInitE": {
                "type": "string",
                "description": "循环伏安法-初始电位（单位：伏特）",
                "minimum": "-10",
                "maximum": "10"
            },
            "cvHighE": {
                "type": "string",
                "description": "循环伏安法-上限电位（单位：伏特）",
                "minimum": "-10",
                "maximum": "10"
            },
            "cvLowE": {
                "type": "string",
                "description": "循环伏安法-下限电位（单位：伏特）",
                "minimum": "-10",
                "maximum": "10"
            },
            "cvFinalE": {
                "type": "string",
                "description": "循环伏安法-终点电位（单位：伏特）",
                "minimum": "-10",
                "maximum": "10"
            },
            "cvInitialScanPolarity": {
                "type": "string",
                "description": "循环伏安法-初始化扫码方向",
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
            "cvScanRate": {
                "type": "string",
                "description": "循环伏安法-扫描速度",
                "minimum": "1e-6",
                "maximum": "10000"
            },
            "cvSweepSegments": {
                "type": "string",
                "description": "循环伏安法-扫描段数",
                "minimum": "1",
                "maximum": "1000000"
            },
            "cvSampleInterval": {
                "type": "string",
                "description": "循环伏安法-采样间隔",
                "minimum": "0.001",
                "maximum": "0.064"
            },
            "cvQuietTime": {
                "type": "string",
                "description": "循环伏安法-静置时间",
                "minimum": "1",
                "maximum": "1000000"
            },
            "cvSensitivity": {
                "type": "string",
                "description": "循环伏安法-灵敏度",
                "enum": [
                    "1e-001",
                    "1e-002",
                    "1e-003",
                    "1e-004",
                    "1e-005",
                    "1e-006",
                    "1e-007",
                    "1e-008",
                    "1e-009",
                    "1e-010",
                    "1e-011",
                    "1e-012"
                ]
            },
            "lsvStatus": {
                "type": "string",
                "description": "线性扫描伏安法-是否检测",
                "enum": [
                    {
                        "label": "不检测",
                        "value": "0"
                    },
                    {
                        "label": "检测",
                        "value": "1"
                    }
                ]
            },
            "lsvInitE": {
                "type": "string",
                "description": "线性扫描伏安法-初始电位（单位：伏特）",
                "minimum": "-10",
                "maximum": "10"
            },
            "lsvFinalE": {
                "type": "string",
                "description": "线性扫描伏安法-终点电位（单位：伏特）",
                "minimum": "-10",
                "maximum": "10"
            },
            "lsvScanRate": {
                "type": "string",
                "description": "线性扫描伏安法-扫描速度",
                "minimum": "1e-6",
                "maximum": "20000"
            },
            "lsvSampleInterval": {
                "type": "string",
                "description": "线性扫描伏安法-采样间隔",
                "minimum": "0.001",
                "maximum": "0.064"
            },
            "lsvQuietTime": {
                "type": "string",
                "description": "线性扫描伏安法-静置时间",
                "minimum": "1",
                "maximum": "1000000"
            },
            "lsvSensitivity": {
                "type": "string",
                "description": "线性扫描伏安法-灵敏度",
                "enum": [
                    "1e-001",
                    "1e-002",
                    "1e-003",
                    "1e-004",
                    "1e-005",
                    "1e-006",
                    "1e-007",
                    "1e-008",
                    "1e-009",
                    "1e-010",
                    "1e-011",
                    "1e-012"
                ]
            },
            "etcStatus": {
                "type": "string",
                "description": "电流/时间曲线-是否检测",
                "enum": [
                    {
                        "label": "不检测",
                        "value": "0"
                    },
                    {
                        "label": "检测",
                        "value": "1"
                    }
                ]
            },
            "etcInitE": {
                "type": "string",
                "description": "电流/时间曲线-初始电位（单位：伏特）",
                "minimum": "-10",
                "maximum": "10"
            },
            "etcSampleInterval": {
                "type": "string",
                "description": "电流/时间曲线-采样间隔",
                "minimum": "1e-6",
                "maximum": "50"
            },
            "etcRunTime": {
                "type": "string",
                "description": "电流/时间曲线-运行时间",
                "minimum": "0.001",
                "maximum": "500000"
            },
            "etcQuietTime": {
                "type": "string",
                "description": "电流/时间曲线-静置时间",
                "minimum": "1",
                "maximum": "1000000"
            },
            "etcScalesDuringRun": {
                "type": "string",
                "description": "电流/时间曲线-电流量程档数",
                "enum": 1
            },
            "etcSensitivity": {
                "type": "string",
                "description": "电流/时间曲线-灵敏度",
                "enum": [
                    "1e-001",
                    "1e-002",
                    "1e-003",
                    "1e-004",
                    "1e-005",
                    "1e-006",
                    "1e-007",
                    "1e-008",
                    "1e-009",
                    "1e-010",
                    "1e-011",
                    "1e-012"
                ]
            },
            "acimStatus": {
                "type": "string",
                "description": "交流阻抗测量-是否检测",
                "enum": [
                    {
                        "label": "不检测",
                        "value": "0"
                    },
                    {
                        "label": "检测",
                        "value": "1"
                    }
                ]
            },
            "acimInitE": {
                "type": "string",
                "description": "交流阻抗测量-初始电位（单位：伏特）",
                "minimum": "-10",
                "maximum": "10"
            },
            "acimHighFrequency": {
                "type": "string",
                "description": "交流阻抗测量-上限频率（单位：赫兹）",
                "minimum": "1e-4",
                "maximum": "2e6"
            },
            "acimLowFrequency": {
                "type": "string",
                "description": "交流阻抗测量-下限频率（单位：赫兹）",
                "minimum": "1e-5",
                "maximum": "1e5"
            },
            "acimAmplitude": {
                "type": "string",
                "description": "交流阻抗测量-振幅",
                "minimum": "1e-5",
                "maximum": "0.7"
            },
            "acimQuietTime": {
                "type": "string",
                "description": "交流阻抗测量-静置时间",
                "minimum": "1",
                "maximum": "1000000"
            }
        },
        "required": [
            "joinStatus",
            "bottleType",
            "bottleCathode",
            "bottleAnode",
            "bottleCatalyst",
            "catalystCapacity",
            "catalystDropletVolume",
            "carbonPaperType",
            "dryerType",
            "dryerTime",
            "dryerPower",
            "electrolyteCycleSpeed",
            "ventilationTime",
            "cleaningFrequency",
            "cvStatus",
            "lsvStatus",
            "etcStatus",
            "acimStatus"
        ]
    },
    "poolThree.joinStatus": {
        "type": "string",
        "description": "是否参与实验",
        "enum": [
            {
                "label": "否",
                "value": "0"
            },
            {
                "label": "是",
                "value": "1"
            }
        ]
    },
    "poolThree.bottleType": {
        "type": "string",
        "description": "西林瓶类型",
        "enum": [
            {
                "label": "关盖螺口瓶",
                "value": "closedCapScrewBottle"
            },
            {
                "label": "无盖螺口瓶",
                "value": "uncapScrewBottle"
            },
            {
                "label": "无盖平口瓶",
                "value": "uncapFlatMouthedBottle"
            }
        ]
    },
    "poolThree.bottleCathode": {
        "type": "string",
        "description": "阴极西林瓶",
        "enum": 3
    },
    "poolThree.bottleAnode": {
        "type": "string",
        "description": "阳极西林瓶",
        "enum": 3
    },
    "poolThree.bottleCatalyst": {
        "type": "string",
        "description": "催化剂瓶",
        "enum": 3
    },
    "poolThree.catalystCapacity": {
        "type": "string",
        "description": "催化剂容量（单位：微升）",
        "minimum": "10",
        "maximum": "15000"
    },
    "poolThree.catalystDropletVolume": {
        "type": "string",
        "description": "催化剂滴液量（单位：微升）",
        "minimum": "10",
        "maximum": "300"
    },
    "poolThree.carbonPaperType": {
        "type": "string",
        "description": "碳纸类型",
        "enum": [
            {
                "label": "亲水性碳纸",
                "value": "hydrophilicity"
            },
            {
                "label": "疏水性碳纸",
                "value": "hydrophobicity"
            }
        ]
    },
    "poolThree.dryerType": {
        "type": "string",
        "description": "碳纸晾干方式",
        "enum": [
            {
                "label": "加热晾干",
                "value": "heat"
            },
            {
                "label": "自然晾干",
                "value": "naturalDry"
            }
        ]
    },
    "poolThree.dryerTime": {
        "type": "string",
        "description": "碳纸晾干时间（单位：分钟）",
        "minimum": "1",
        "maximum": "90"
    },
    "poolThree.dryerPower": {
        "type": "string",
        "description": "碳纸晾干温度（单位：摄氏度）",
        "minimum": "0",
        "maximum": "70"
    },
    "poolThree.electrolyteCycleSpeed": {
        "type": "string",
        "description": "电解池循环速度（单位：毫升/分钟）",
        "minimum": "5",
        "maximum": "35"
    },
    "poolThree.ventilationTime": {
        "type": "string",
        "description": "通气时长（单位：秒）",
        "minimum": "1",
        "maximum": "60"
    },
    "poolThree.cleaningFrequency": {
        "type": "string",
        "description": "电解液清洗次数",
        "minimum": "1",
        "maximum": "5"
    },
    "poolThree.cvStatus": {
        "type": "string",
        "description": "循环伏安法-是否检测",
        "enum": [
            {
                "label": "不检测",
                "value": "0"
            },
            {
                "label": "检测",
                "value": "1"
            }
        ]
    },
    "poolThree.cvInitE": {
        "type": "string",
        "description": "循环伏安法-初始电位（单位：伏特）",
        "minimum": "-10",
        "maximum": "10"
    },
    "poolThree.cvHighE": {
        "type": "string",
        "description": "循环伏安法-上限电位（单位：伏特）",
        "minimum": "-10",
        "maximum": "10"
    },
    "poolThree.cvLowE": {
        "type": "string",
        "description": "循环伏安法-下限电位（单位：伏特）",
        "minimum": "-10",
        "maximum": "10"
    },
    "poolThree.cvFinalE": {
        "type": "string",
        "description": "循环伏安法-终点电位（单位：伏特）",
        "minimum": "-10",
        "maximum": "10"
    },
    "poolThree.cvInitialScanPolarity": {
        "type": "string",
        "description": "循环伏安法-初始化扫码方向",
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
    "poolThree.cvScanRate": {
        "type": "string",
        "description": "循环伏安法-扫描速度",
        "minimum": "1e-6",
        "maximum": "10000"
    },
    "poolThree.cvSweepSegments": {
        "type": "string",
        "description": "循环伏安法-扫描段数",
        "minimum": "1",
        "maximum": "1000000"
    },
    "poolThree.cvSampleInterval": {
        "type": "string",
        "description": "循环伏安法-采样间隔",
        "minimum": "0.001",
        "maximum": "0.064"
    },
    "poolThree.cvQuietTime": {
        "type": "string",
        "description": "循环伏安法-静置时间",
        "minimum": "1",
        "maximum": "1000000"
    },
    "poolThree.cvSensitivity": {
        "type": "string",
        "description": "循环伏安法-灵敏度",
        "enum": [
            "1e-001",
            "1e-002",
            "1e-003",
            "1e-004",
            "1e-005",
            "1e-006",
            "1e-007",
            "1e-008",
            "1e-009",
            "1e-010",
            "1e-011",
            "1e-012"
        ]
    },
    "poolThree.lsvStatus": {
        "type": "string",
        "description": "线性扫描伏安法-是否检测",
        "enum": [
            {
                "label": "不检测",
                "value": "0"
            },
            {
                "label": "检测",
                "value": "1"
            }
        ]
    },
    "poolThree.lsvInitE": {
        "type": "string",
        "description": "线性扫描伏安法-初始电位（单位：伏特）",
        "minimum": "-10",
        "maximum": "10"
    },
    "poolThree.lsvFinalE": {
        "type": "string",
        "description": "线性扫描伏安法-终点电位（单位：伏特）",
        "minimum": "-10",
        "maximum": "10"
    },
    "poolThree.lsvScanRate": {
        "type": "string",
        "description": "线性扫描伏安法-扫描速度",
        "minimum": "1e-6",
        "maximum": "20000"
    },
    "poolThree.lsvSampleInterval": {
        "type": "string",
        "description": "线性扫描伏安法-采样间隔",
        "minimum": "0.001",
        "maximum": "0.064"
    },
    "poolThree.lsvQuietTime": {
        "type": "string",
        "description": "线性扫描伏安法-静置时间",
        "minimum": "1",
        "maximum": "1000000"
    },
    "poolThree.lsvSensitivity": {
        "type": "string",
        "description": "线性扫描伏安法-灵敏度",
        "enum": [
            "1e-001",
            "1e-002",
            "1e-003",
            "1e-004",
            "1e-005",
            "1e-006",
            "1e-007",
            "1e-008",
            "1e-009",
            "1e-010",
            "1e-011",
            "1e-012"
        ]
    },
    "poolThree.etcStatus": {
        "type": "string",
        "description": "电流/时间曲线-是否检测",
        "enum": [
            {
                "label": "不检测",
                "value": "0"
            },
            {
                "label": "检测",
                "value": "1"
            }
        ]
    },
    "poolThree.etcInitE": {
        "type": "string",
        "description": "电流/时间曲线-初始电位（单位：伏特）",
        "minimum": "-10",
        "maximum": "10"
    },
    "poolThree.etcSampleInterval": {
        "type": "string",
        "description": "电流/时间曲线-采样间隔",
        "minimum": "1e-6",
        "maximum": "50"
    },
    "poolThree.etcRunTime": {
        "type": "string",
        "description": "电流/时间曲线-运行时间",
        "minimum": "0.001",
        "maximum": "500000"
    },
    "poolThree.etcQuietTime": {
        "type": "string",
        "description": "电流/时间曲线-静置时间",
        "minimum": "1",
        "maximum": "1000000"
    },
    "poolThree.etcScalesDuringRun": {
        "type": "string",
        "description": "电流/时间曲线-电流量程档数",
        "enum": 1
    },
    "poolThree.etcSensitivity": {
        "type": "string",
        "description": "电流/时间曲线-灵敏度",
        "enum": [
            "1e-001",
            "1e-002",
            "1e-003",
            "1e-004",
            "1e-005",
            "1e-006",
            "1e-007",
            "1e-008",
            "1e-009",
            "1e-010",
            "1e-011",
            "1e-012"
        ]
    },
    "poolThree.acimStatus": {
        "type": "string",
        "description": "交流阻抗测量-是否检测",
        "enum": [
            {
                "label": "不检测",
                "value": "0"
            },
            {
                "label": "检测",
                "value": "1"
            }
        ]
    },
    "poolThree.acimInitE": {
        "type": "string",
        "description": "交流阻抗测量-初始电位（单位：伏特）",
        "minimum": "-10",
        "maximum": "10"
    },
    "poolThree.acimHighFrequency": {
        "type": "string",
        "description": "交流阻抗测量-上限频率（单位：赫兹）",
        "minimum": "1e-4",
        "maximum": "2e6"
    },
    "poolThree.acimLowFrequency": {
        "type": "string",
        "description": "交流阻抗测量-下限频率（单位：赫兹）",
        "minimum": "1e-5",
        "maximum": "1e5"
    },
    "poolThree.acimAmplitude": {
        "type": "string",
        "description": "交流阻抗测量-振幅",
        "minimum": "1e-5",
        "maximum": "0.7"
    },
    "poolThree.acimQuietTime": {
        "type": "string",
        "description": "交流阻抗测量-静置时间",
        "minimum": "1",
        "maximum": "1000000"
    },
    "poolFour": {
        "type": "object",
        "description": "电解池4号",
        "properties": {
            "joinStatus": {
                "type": "string",
                "description": "是否参与实验",
                "enum": [
                    {
                        "label": "否",
                        "value": "0"
                    },
                    {
                        "label": "是",
                        "value": "1"
                    }
                ]
            },
            "bottleType": {
                "type": "string",
                "description": "西林瓶类型",
                "enum": [
                    {
                        "label": "关盖螺口瓶",
                        "value": "closedCapScrewBottle"
                    },
                    {
                        "label": "无盖螺口瓶",
                        "value": "uncapScrewBottle"
                    },
                    {
                        "label": "无盖平口瓶",
                        "value": "uncapFlatMouthedBottle"
                    }
                ]
            },
            "bottleCathode": {
                "type": "string",
                "description": "阴极西林瓶",
                "enum": 4
            },
            "bottleAnode": {
                "type": "string",
                "description": "阳极西林瓶",
                "enum": 4
            },
            "bottleCatalyst": {
                "type": "string",
                "description": "催化剂瓶",
                "enum": 4
            },
            "catalystCapacity": {
                "type": "string",
                "description": "催化剂容量（单位：微升）",
                "minimum": "10",
                "maximum": "15000"
            },
            "catalystDropletVolume": {
                "type": "string",
                "description": "催化剂滴液量（单位：微升）",
                "minimum": "10",
                "maximum": "300"
            },
            "carbonPaperType": {
                "type": "string",
                "description": "碳纸类型",
                "enum": [
                    {
                        "label": "亲水性碳纸",
                        "value": "hydrophilicity"
                    },
                    {
                        "label": "疏水性碳纸",
                        "value": "hydrophobicity"
                    }
                ]
            },
            "dryerType": {
                "type": "string",
                "description": "碳纸晾干方式",
                "enum": [
                    {
                        "label": "加热晾干",
                        "value": "heat"
                    },
                    {
                        "label": "自然晾干",
                        "value": "naturalDry"
                    }
                ]
            },
            "dryerTime": {
                "type": "string",
                "description": "碳纸晾干时间（单位：分钟）",
                "minimum": "1",
                "maximum": "90"
            },
            "dryerPower": {
                "type": "string",
                "description": "碳纸晾干温度（单位：摄氏度）",
                "minimum": "0",
                "maximum": "70"
            },
            "electrolyteCycleSpeed": {
                "type": "string",
                "description": "电解池循环速度（单位：毫升/分钟）",
                "minimum": "5",
                "maximum": "35"
            },
            "ventilationTime": {
                "type": "string",
                "description": "通气时长（单位：秒）",
                "minimum": "1",
                "maximum": "60"
            },
            "cleaningFrequency": {
                "type": "string",
                "description": "电解液清洗次数",
                "minimum": "1",
                "maximum": "5"
            },
            "cvStatus": {
                "type": "string",
                "description": "循环伏安法-是否检测",
                "enum": [
                    {
                        "label": "不检测",
                        "value": "0"
                    },
                    {
                        "label": "检测",
                        "value": "1"
                    }
                ]
            },
            "cvInitE": {
                "type": "string",
                "description": "循环伏安法-初始电位（单位：伏特）",
                "minimum": "-10",
                "maximum": "10"
            },
            "cvHighE": {
                "type": "string",
                "description": "循环伏安法-上限电位（单位：伏特）",
                "minimum": "-10",
                "maximum": "10"
            },
            "cvLowE": {
                "type": "string",
                "description": "循环伏安法-下限电位（单位：伏特）",
                "minimum": "-10",
                "maximum": "10"
            },
            "cvFinalE": {
                "type": "string",
                "description": "循环伏安法-终点电位（单位：伏特）",
                "minimum": "-10",
                "maximum": "10"
            },
            "cvInitialScanPolarity": {
                "type": "string",
                "description": "循环伏安法-初始化扫码方向",
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
            "cvScanRate": {
                "type": "string",
                "description": "循环伏安法-扫描速度",
                "minimum": "1e-6",
                "maximum": "10000"
            },
            "cvSweepSegments": {
                "type": "string",
                "description": "循环伏安法-扫描段数",
                "minimum": "1",
                "maximum": "1000000"
            },
            "cvSampleInterval": {
                "type": "string",
                "description": "循环伏安法-采样间隔",
                "minimum": "0.001",
                "maximum": "0.064"
            },
            "cvQuietTime": {
                "type": "string",
                "description": "循环伏安法-静置时间",
                "minimum": "1",
                "maximum": "1000000"
            },
            "cvSensitivity": {
                "type": "string",
                "description": "循环伏安法-灵敏度",
                "enum": [
                    "1e-001",
                    "1e-002",
                    "1e-003",
                    "1e-004",
                    "1e-005",
                    "1e-006",
                    "1e-007",
                    "1e-008",
                    "1e-009",
                    "1e-010",
                    "1e-011",
                    "1e-012"
                ]
            },
            "lsvStatus": {
                "type": "string",
                "description": "线性扫描伏安法-是否检测",
                "enum": [
                    {
                        "label": "不检测",
                        "value": "0"
                    },
                    {
                        "label": "检测",
                        "value": "1"
                    }
                ]
            },
            "lsvInitE": {
                "type": "string",
                "description": "线性扫描伏安法-初始电位（单位：伏特）",
                "minimum": "-10",
                "maximum": "10"
            },
            "lsvFinalE": {
                "type": "string",
                "description": "线性扫描伏安法-终点电位（单位：伏特）",
                "minimum": "-10",
                "maximum": "10"
            },
            "lsvScanRate": {
                "type": "string",
                "description": "线性扫描伏安法-扫描速度",
                "minimum": "1e-6",
                "maximum": "20000"
            },
            "lsvSampleInterval": {
                "type": "string",
                "description": "线性扫描伏安法-采样间隔",
                "minimum": "0.001",
                "maximum": "0.064"
            },
            "lsvQuietTime": {
                "type": "string",
                "description": "线性扫描伏安法-静置时间",
                "minimum": "1",
                "maximum": "1000000"
            },
            "lsvSensitivity": {
                "type": "string",
                "description": "线性扫描伏安法-灵敏度",
                "enum": [
                    "1e-001",
                    "1e-002",
                    "1e-003",
                    "1e-004",
                    "1e-005",
                    "1e-006",
                    "1e-007",
                    "1e-008",
                    "1e-009",
                    "1e-010",
                    "1e-011",
                    "1e-012"
                ]
            },
            "etcStatus": {
                "type": "string",
                "description": "电流/时间曲线-是否检测",
                "enum": [
                    {
                        "label": "不检测",
                        "value": "0"
                    },
                    {
                        "label": "检测",
                        "value": "1"
                    }
                ]
            },
            "etcInitE": {
                "type": "string",
                "description": "电流/时间曲线-初始电位（单位：伏特）",
                "minimum": "-10",
                "maximum": "10"
            },
            "etcSampleInterval": {
                "type": "string",
                "description": "电流/时间曲线-采样间隔",
                "minimum": "1e-6",
                "maximum": "50"
            },
            "etcRunTime": {
                "type": "string",
                "description": "电流/时间曲线-运行时间",
                "minimum": "0.001",
                "maximum": "500000"
            },
            "etcQuietTime": {
                "type": "string",
                "description": "电流/时间曲线-静置时间",
                "minimum": "1",
                "maximum": "1000000"
            },
            "etcScalesDuringRun": {
                "type": "string",
                "description": "电流/时间曲线-电流量程档数",
                "enum": 1
            },
            "etcSensitivity": {
                "type": "string",
                "description": "电流/时间曲线-灵敏度",
                "enum": [
                    "1e-001",
                    "1e-002",
                    "1e-003",
                    "1e-004",
                    "1e-005",
                    "1e-006",
                    "1e-007",
                    "1e-008",
                    "1e-009",
                    "1e-010",
                    "1e-011",
                    "1e-012"
                ]
            },
            "acimStatus": {
                "type": "string",
                "description": "交流阻抗测量-是否检测",
                "enum": [
                    {
                        "label": "不检测",
                        "value": "0"
                    },
                    {
                        "label": "检测",
                        "value": "1"
                    }
                ]
            },
            "acimInitE": {
                "type": "string",
                "description": "交流阻抗测量-初始电位（单位：伏特）",
                "minimum": "-10",
                "maximum": "10"
            },
            "acimHighFrequency": {
                "type": "string",
                "description": "交流阻抗测量-上限频率（单位：赫兹）",
                "minimum": "1e-4",
                "maximum": "2e6"
            },
            "acimLowFrequency": {
                "type": "string",
                "description": "交流阻抗测量-下限频率（单位：赫兹）",
                "minimum": "1e-5",
                "maximum": "1e5"
            },
            "acimAmplitude": {
                "type": "string",
                "description": "交流阻抗测量-振幅",
                "minimum": "1e-5",
                "maximum": "0.7"
            },
            "acimQuietTime": {
                "type": "string",
                "description": "交流阻抗测量-静置时间",
                "minimum": "1",
                "maximum": "1000000"
            }
        },
        "required": [
            "joinStatus",
            "bottleType",
            "bottleCathode",
            "bottleAnode",
            "bottleCatalyst",
            "catalystCapacity",
            "catalystDropletVolume",
            "carbonPaperType",
            "dryerType",
            "dryerTime",
            "dryerPower",
            "electrolyteCycleSpeed",
            "ventilationTime",
            "cleaningFrequency",
            "cvStatus",
            "lsvStatus",
            "etcStatus",
            "acimStatus"
        ]
    },
    "poolFour.joinStatus": {
        "type": "string",
        "description": "是否参与实验",
        "enum": [
            {
                "label": "否",
                "value": "0"
            },
            {
                "label": "是",
                "value": "1"
            }
        ]
    },
    "poolFour.bottleType": {
        "type": "string",
        "description": "西林瓶类型",
        "enum": [
            {
                "label": "关盖螺口瓶",
                "value": "closedCapScrewBottle"
            },
            {
                "label": "无盖螺口瓶",
                "value": "uncapScrewBottle"
            },
            {
                "label": "无盖平口瓶",
                "value": "uncapFlatMouthedBottle"
            }
        ]
    },
    "poolFour.bottleCathode": {
        "type": "string",
        "description": "阴极西林瓶",
        "enum": 4
    },
    "poolFour.bottleAnode": {
        "type": "string",
        "description": "阳极西林瓶",
        "enum": 4
    },
    "poolFour.bottleCatalyst": {
        "type": "string",
        "description": "催化剂瓶",
        "enum": 4
    },
    "poolFour.catalystCapacity": {
        "type": "string",
        "description": "催化剂容量（单位：微升）",
        "minimum": "10",
        "maximum": "15000"
    },
    "poolFour.catalystDropletVolume": {
        "type": "string",
        "description": "催化剂滴液量（单位：微升）",
        "minimum": "10",
        "maximum": "300"
    },
    "poolFour.carbonPaperType": {
        "type": "string",
        "description": "碳纸类型",
        "enum": [
            {
                "label": "亲水性碳纸",
                "value": "hydrophilicity"
            },
            {
                "label": "疏水性碳纸",
                "value": "hydrophobicity"
            }
        ]
    },
    "poolFour.dryerType": {
        "type": "string",
        "description": "碳纸晾干方式",
        "enum": [
            {
                "label": "加热晾干",
                "value": "heat"
            },
            {
                "label": "自然晾干",
                "value": "naturalDry"
            }
        ]
    },
    "poolFour.dryerTime": {
        "type": "string",
        "description": "碳纸晾干时间（单位：分钟）",
        "minimum": "1",
        "maximum": "90"
    },
    "poolFour.dryerPower": {
        "type": "string",
        "description": "碳纸晾干温度（单位：摄氏度）",
        "minimum": "0",
        "maximum": "70"
    },
    "poolFour.electrolyteCycleSpeed": {
        "type": "string",
        "description": "电解池循环速度（单位：毫升/分钟）",
        "minimum": "5",
        "maximum": "35"
    },
    "poolFour.ventilationTime": {
        "type": "string",
        "description": "通气时长（单位：秒）",
        "minimum": "1",
        "maximum": "60"
    },
    "poolFour.cleaningFrequency": {
        "type": "string",
        "description": "电解液清洗次数",
        "minimum": "1",
        "maximum": "5"
    },
    "poolFour.cvStatus": {
        "type": "string",
        "description": "循环伏安法-是否检测",
        "enum": [
            {
                "label": "不检测",
                "value": "0"
            },
            {
                "label": "检测",
                "value": "1"
            }
        ]
    },
    "poolFour.cvInitE": {
        "type": "string",
        "description": "循环伏安法-初始电位（单位：伏特）",
        "minimum": "-10",
        "maximum": "10"
    },
    "poolFour.cvHighE": {
        "type": "string",
        "description": "循环伏安法-上限电位（单位：伏特）",
        "minimum": "-10",
        "maximum": "10"
    },
    "poolFour.cvLowE": {
        "type": "string",
        "description": "循环伏安法-下限电位（单位：伏特）",
        "minimum": "-10",
        "maximum": "10"
    },
    "poolFour.cvFinalE": {
        "type": "string",
        "description": "循环伏安法-终点电位（单位：伏特）",
        "minimum": "-10",
        "maximum": "10"
    },
    "poolFour.cvInitialScanPolarity": {
        "type": "string",
        "description": "循环伏安法-初始化扫码方向",
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
    "poolFour.cvScanRate": {
        "type": "string",
        "description": "循环伏安法-扫描速度",
        "minimum": "1e-6",
        "maximum": "10000"
    },
    "poolFour.cvSweepSegments": {
        "type": "string",
        "description": "循环伏安法-扫描段数",
        "minimum": "1",
        "maximum": "1000000"
    },
    "poolFour.cvSampleInterval": {
        "type": "string",
        "description": "循环伏安法-采样间隔",
        "minimum": "0.001",
        "maximum": "0.064"
    },
    "poolFour.cvQuietTime": {
        "type": "string",
        "description": "循环伏安法-静置时间",
        "minimum": "1",
        "maximum": "1000000"
    },
    "poolFour.cvSensitivity": {
        "type": "string",
        "description": "循环伏安法-灵敏度",
        "enum": [
            "1e-001",
            "1e-002",
            "1e-003",
            "1e-004",
            "1e-005",
            "1e-006",
            "1e-007",
            "1e-008",
            "1e-009",
            "1e-010",
            "1e-011",
            "1e-012"
        ]
    },
    "poolFour.lsvStatus": {
        "type": "string",
        "description": "线性扫描伏安法-是否检测",
        "enum": [
            {
                "label": "不检测",
                "value": "0"
            },
            {
                "label": "检测",
                "value": "1"
            }
        ]
    },
    "poolFour.lsvInitE": {
        "type": "string",
        "description": "线性扫描伏安法-初始电位（单位：伏特）",
        "minimum": "-10",
        "maximum": "10"
    },
    "poolFour.lsvFinalE": {
        "type": "string",
        "description": "线性扫描伏安法-终点电位（单位：伏特）",
        "minimum": "-10",
        "maximum": "10"
    },
    "poolFour.lsvScanRate": {
        "type": "string",
        "description": "线性扫描伏安法-扫描速度",
        "minimum": "1e-6",
        "maximum": "20000"
    },
    "poolFour.lsvSampleInterval": {
        "type": "string",
        "description": "线性扫描伏安法-采样间隔",
        "minimum": "0.001",
        "maximum": "0.064"
    },
    "poolFour.lsvQuietTime": {
        "type": "string",
        "description": "线性扫描伏安法-静置时间",
        "minimum": "1",
        "maximum": "1000000"
    },
    "poolFour.lsvSensitivity": {
        "type": "string",
        "description": "线性扫描伏安法-灵敏度",
        "enum": [
            "1e-001",
            "1e-002",
            "1e-003",
            "1e-004",
            "1e-005",
            "1e-006",
            "1e-007",
            "1e-008",
            "1e-009",
            "1e-010",
            "1e-011",
            "1e-012"
        ]
    },
    "poolFour.etcStatus": {
        "type": "string",
        "description": "电流/时间曲线-是否检测",
        "enum": [
            {
                "label": "不检测",
                "value": "0"
            },
            {
                "label": "检测",
                "value": "1"
            }
        ]
    },
    "poolFour.etcInitE": {
        "type": "string",
        "description": "电流/时间曲线-初始电位（单位：伏特）",
        "minimum": "-10",
        "maximum": "10"
    },
    "poolFour.etcSampleInterval": {
        "type": "string",
        "description": "电流/时间曲线-采样间隔",
        "minimum": "1e-6",
        "maximum": "50"
    },
    "poolFour.etcRunTime": {
        "type": "string",
        "description": "电流/时间曲线-运行时间",
        "minimum": "0.001",
        "maximum": "500000"
    },
    "poolFour.etcQuietTime": {
        "type": "string",
        "description": "电流/时间曲线-静置时间",
        "minimum": "1",
        "maximum": "1000000"
    },
    "poolFour.etcScalesDuringRun": {
        "type": "string",
        "description": "电流/时间曲线-电流量程档数",
        "enum": 1
    },
    "poolFour.etcSensitivity": {
        "type": "string",
        "description": "电流/时间曲线-灵敏度",
        "enum": [
            "1e-001",
            "1e-002",
            "1e-003",
            "1e-004",
            "1e-005",
            "1e-006",
            "1e-007",
            "1e-008",
            "1e-009",
            "1e-010",
            "1e-011",
            "1e-012"
        ]
    },
    "poolFour.acimStatus": {
        "type": "string",
        "description": "交流阻抗测量-是否检测",
        "enum": [
            {
                "label": "不检测",
                "value": "0"
            },
            {
                "label": "检测",
                "value": "1"
            }
        ]
    },
    "poolFour.acimInitE": {
        "type": "string",
        "description": "交流阻抗测量-初始电位（单位：伏特）",
        "minimum": "-10",
        "maximum": "10"
    },
    "poolFour.acimHighFrequency": {
        "type": "string",
        "description": "交流阻抗测量-上限频率（单位：赫兹）",
        "minimum": "1e-4",
        "maximum": "2e6"
    },
    "poolFour.acimLowFrequency": {
        "type": "string",
        "description": "交流阻抗测量-下限频率（单位：赫兹）",
        "minimum": "1e-5",
        "maximum": "1e5"
    },
    "poolFour.acimAmplitude": {
        "type": "string",
        "description": "交流阻抗测量-振幅",
        "minimum": "1e-5",
        "maximum": "0.7"
    },
    "poolFour.acimQuietTime": {
        "type": "string",
        "description": "交流阻抗测量-静置时间",
        "minimum": "1",
        "maximum": "1000000"
    },
    "poolFive": {
        "type": "object",
        "description": "电解池5号",
        "properties": {
            "joinStatus": {
                "type": "string",
                "description": "是否参与实验",
                "enum": [
                    {
                        "label": "否",
                        "value": "0"
                    },
                    {
                        "label": "是",
                        "value": "1"
                    }
                ]
            },
            "bottleType": {
                "type": "string",
                "description": "西林瓶类型",
                "enum": [
                    {
                        "label": "关盖螺口瓶",
                        "value": "closedCapScrewBottle"
                    },
                    {
                        "label": "无盖螺口瓶",
                        "value": "uncapScrewBottle"
                    },
                    {
                        "label": "无盖平口瓶",
                        "value": "uncapFlatMouthedBottle"
                    }
                ]
            },
            "bottleCathode": {
                "type": "string",
                "description": "阴极西林瓶",
                "enum": 5
            },
            "bottleAnode": {
                "type": "string",
                "description": "阳极西林瓶",
                "enum": 5
            },
            "bottleCatalyst": {
                "type": "string",
                "description": "催化剂瓶",
                "enum": 5
            },
            "catalystCapacity": {
                "type": "string",
                "description": "催化剂容量（单位：微升）",
                "minimum": "10",
                "maximum": "15000"
            },
            "catalystDropletVolume": {
                "type": "string",
                "description": "催化剂滴液量（单位：微升）",
                "minimum": "10",
                "maximum": "300"
            },
            "carbonPaperType": {
                "type": "string",
                "description": "碳纸类型",
                "enum": [
                    {
                        "label": "亲水性碳纸",
                        "value": "hydrophilicity"
                    },
                    {
                        "label": "疏水性碳纸",
                        "value": "hydrophobicity"
                    }
                ]
            },
            "dryerType": {
                "type": "string",
                "description": "碳纸晾干方式",
                "enum": [
                    {
                        "label": "加热晾干",
                        "value": "heat"
                    },
                    {
                        "label": "自然晾干",
                        "value": "naturalDry"
                    }
                ]
            },
            "dryerTime": {
                "type": "string",
                "description": "碳纸晾干时间（单位：分钟）",
                "minimum": "1",
                "maximum": "90"
            },
            "dryerPower": {
                "type": "string",
                "description": "碳纸晾干温度（单位：摄氏度）",
                "minimum": "0",
                "maximum": "70"
            },
            "electrolyteCycleSpeed": {
                "type": "string",
                "description": "电解池循环速度（单位：毫升/分钟）",
                "minimum": "5",
                "maximum": "35"
            },
            "ventilationTime": {
                "type": "string",
                "description": "通气时长（单位：秒）",
                "minimum": "1",
                "maximum": "60"
            },
            "cleaningFrequency": {
                "type": "string",
                "description": "电解液清洗次数",
                "minimum": "1",
                "maximum": "5"
            },
            "cvStatus": {
                "type": "string",
                "description": "循环伏安法-是否检测",
                "enum": [
                    {
                        "label": "不检测",
                        "value": "0"
                    },
                    {
                        "label": "检测",
                        "value": "1"
                    }
                ]
            },
            "cvInitE": {
                "type": "string",
                "description": "循环伏安法-初始电位（单位：伏特）",
                "minimum": "-10",
                "maximum": "10"
            },
            "cvHighE": {
                "type": "string",
                "description": "循环伏安法-上限电位（单位：伏特）",
                "minimum": "-10",
                "maximum": "10"
            },
            "cvLowE": {
                "type": "string",
                "description": "循环伏安法-下限电位（单位：伏特）",
                "minimum": "-10",
                "maximum": "10"
            },
            "cvFinalE": {
                "type": "string",
                "description": "循环伏安法-终点电位（单位：伏特）",
                "minimum": "-10",
                "maximum": "10"
            },
            "cvInitialScanPolarity": {
                "type": "string",
                "description": "循环伏安法-初始化扫码方向",
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
            "cvScanRate": {
                "type": "string",
                "description": "循环伏安法-扫描速度",
                "minimum": "1e-6",
                "maximum": "10000"
            },
            "cvSweepSegments": {
                "type": "string",
                "description": "循环伏安法-扫描段数",
                "minimum": "1",
                "maximum": "1000000"
            },
            "cvSampleInterval": {
                "type": "string",
                "description": "循环伏安法-采样间隔",
                "minimum": "0.001",
                "maximum": "0.064"
            },
            "cvQuietTime": {
                "type": "string",
                "description": "循环伏安法-静置时间",
                "minimum": "1",
                "maximum": "1000000"
            },
            "cvSensitivity": {
                "type": "string",
                "description": "循环伏安法-灵敏度",
                "enum": [
                    "1e-001",
                    "1e-002",
                    "1e-003",
                    "1e-004",
                    "1e-005",
                    "1e-006",
                    "1e-007",
                    "1e-008",
                    "1e-009",
                    "1e-010",
                    "1e-011",
                    "1e-012"
                ]
            },
            "lsvStatus": {
                "type": "string",
                "description": "线性扫描伏安法-是否检测",
                "enum": [
                    {
                        "label": "不检测",
                        "value": "0"
                    },
                    {
                        "label": "检测",
                        "value": "1"
                    }
                ]
            },
            "lsvInitE": {
                "type": "string",
                "description": "线性扫描伏安法-初始电位（单位：伏特）",
                "minimum": "-10",
                "maximum": "10"
            },
            "lsvFinalE": {
                "type": "string",
                "description": "线性扫描伏安法-终点电位（单位：伏特）",
                "minimum": "-10",
                "maximum": "10"
            },
            "lsvScanRate": {
                "type": "string",
                "description": "线性扫描伏安法-扫描速度",
                "minimum": "1e-6",
                "maximum": "20000"
            },
            "lsvSampleInterval": {
                "type": "string",
                "description": "线性扫描伏安法-采样间隔",
                "minimum": "0.001",
                "maximum": "0.064"
            },
            "lsvQuietTime": {
                "type": "string",
                "description": "线性扫描伏安法-静置时间",
                "minimum": "1",
                "maximum": "1000000"
            },
            "lsvSensitivity": {
                "type": "string",
                "description": "线性扫描伏安法-灵敏度",
                "enum": [
                    "1e-001",
                    "1e-002",
                    "1e-003",
                    "1e-004",
                    "1e-005",
                    "1e-006",
                    "1e-007",
                    "1e-008",
                    "1e-009",
                    "1e-010",
                    "1e-011",
                    "1e-012"
                ]
            },
            "etcStatus": {
                "type": "string",
                "description": "电流/时间曲线-是否检测",
                "enum": [
                    {
                        "label": "不检测",
                        "value": "0"
                    },
                    {
                        "label": "检测",
                        "value": "1"
                    }
                ]
            },
            "etcInitE": {
                "type": "string",
                "description": "电流/时间曲线-初始电位（单位：伏特）",
                "minimum": "-10",
                "maximum": "10"
            },
            "etcSampleInterval": {
                "type": "string",
                "description": "电流/时间曲线-采样间隔",
                "minimum": "1e-6",
                "maximum": "50"
            },
            "etcRunTime": {
                "type": "string",
                "description": "电流/时间曲线-运行时间",
                "minimum": "0.001",
                "maximum": "500000"
            },
            "etcQuietTime": {
                "type": "string",
                "description": "电流/时间曲线-静置时间",
                "minimum": "1",
                "maximum": "1000000"
            },
            "etcScalesDuringRun": {
                "type": "string",
                "description": "电流/时间曲线-电流量程档数",
                "enum": 1
            },
            "etcSensitivity": {
                "type": "string",
                "description": "电流/时间曲线-灵敏度",
                "enum": [
                    "1e-001",
                    "1e-002",
                    "1e-003",
                    "1e-004",
                    "1e-005",
                    "1e-006",
                    "1e-007",
                    "1e-008",
                    "1e-009",
                    "1e-010",
                    "1e-011",
                    "1e-012"
                ]
            },
            "acimStatus": {
                "type": "string",
                "description": "交流阻抗测量-是否检测",
                "enum": [
                    {
                        "label": "不检测",
                        "value": "0"
                    },
                    {
                        "label": "检测",
                        "value": "1"
                    }
                ]
            },
            "acimInitE": {
                "type": "string",
                "description": "交流阻抗测量-初始电位（单位：伏特）",
                "minimum": "-10",
                "maximum": "10"
            },
            "acimHighFrequency": {
                "type": "string",
                "description": "交流阻抗测量-上限频率（单位：赫兹）",
                "minimum": "1e-4",
                "maximum": "2e6"
            },
            "acimLowFrequency": {
                "type": "string",
                "description": "交流阻抗测量-下限频率（单位：赫兹）",
                "minimum": "1e-5",
                "maximum": "1e5"
            },
            "acimAmplitude": {
                "type": "string",
                "description": "交流阻抗测量-振幅",
                "minimum": "1e-5",
                "maximum": "0.7"
            },
            "acimQuietTime": {
                "type": "string",
                "description": "交流阻抗测量-静置时间",
                "minimum": "1",
                "maximum": "1000000"
            }
        },
        "required": [
            "joinStatus",
            "bottleType",
            "bottleCathode",
            "bottleAnode",
            "bottleCatalyst",
            "catalystCapacity",
            "catalystDropletVolume",
            "carbonPaperType",
            "dryerType",
            "dryerTime",
            "dryerPower",
            "electrolyteCycleSpeed",
            "ventilationTime",
            "cleaningFrequency",
            "cvStatus",
            "lsvStatus",
            "etcStatus",
            "acimStatus"
        ]
    },
    "poolFive.joinStatus": {
        "type": "string",
        "description": "是否参与实验",
        "enum": [
            {
                "label": "否",
                "value": "0"
            },
            {
                "label": "是",
                "value": "1"
            }
        ]
    },
    "poolFive.bottleType": {
        "type": "string",
        "description": "西林瓶类型",
        "enum": [
            {
                "label": "关盖螺口瓶",
                "value": "closedCapScrewBottle"
            },
            {
                "label": "无盖螺口瓶",
                "value": "uncapScrewBottle"
            },
            {
                "label": "无盖平口瓶",
                "value": "uncapFlatMouthedBottle"
            }
        ]
    },
    "poolFive.bottleCathode": {
        "type": "string",
        "description": "阴极西林瓶",
        "enum": 5
    },
    "poolFive.bottleAnode": {
        "type": "string",
        "description": "阳极西林瓶",
        "enum": 5
    },
    "poolFive.bottleCatalyst": {
        "type": "string",
        "description": "催化剂瓶",
        "enum": 5
    },
    "poolFive.catalystCapacity": {
        "type": "string",
        "description": "催化剂容量（单位：微升）",
        "minimum": "10",
        "maximum": "15000"
    },
    "poolFive.catalystDropletVolume": {
        "type": "string",
        "description": "催化剂滴液量（单位：微升）",
        "minimum": "10",
        "maximum": "300"
    },
    "poolFive.carbonPaperType": {
        "type": "string",
        "description": "碳纸类型",
        "enum": [
            {
                "label": "亲水性碳纸",
                "value": "hydrophilicity"
            },
            {
                "label": "疏水性碳纸",
                "value": "hydrophobicity"
            }
        ]
    },
    "poolFive.dryerType": {
        "type": "string",
        "description": "碳纸晾干方式",
        "enum": [
            {
                "label": "加热晾干",
                "value": "heat"
            },
            {
                "label": "自然晾干",
                "value": "naturalDry"
            }
        ]
    },
    "poolFive.dryerTime": {
        "type": "string",
        "description": "碳纸晾干时间（单位：分钟）",
        "minimum": "1",
        "maximum": "90"
    },
    "poolFive.dryerPower": {
        "type": "string",
        "description": "碳纸晾干温度（单位：摄氏度）",
        "minimum": "0",
        "maximum": "70"
    },
    "poolFive.electrolyteCycleSpeed": {
        "type": "string",
        "description": "电解池循环速度（单位：毫升/分钟）",
        "minimum": "5",
        "maximum": "35"
    },
    "poolFive.ventilationTime": {
        "type": "string",
        "description": "通气时长（单位：秒）",
        "minimum": "1",
        "maximum": "60"
    },
    "poolFive.cleaningFrequency": {
        "type": "string",
        "description": "电解液清洗次数",
        "minimum": "1",
        "maximum": "5"
    },
    "poolFive.cvStatus": {
        "type": "string",
        "description": "循环伏安法-是否检测",
        "enum": [
            {
                "label": "不检测",
                "value": "0"
            },
            {
                "label": "检测",
                "value": "1"
            }
        ]
    },
    "poolFive.cvInitE": {
        "type": "string",
        "description": "循环伏安法-初始电位（单位：伏特）",
        "minimum": "-10",
        "maximum": "10"
    },
    "poolFive.cvHighE": {
        "type": "string",
        "description": "循环伏安法-上限电位（单位：伏特）",
        "minimum": "-10",
        "maximum": "10"
    },
    "poolFive.cvLowE": {
        "type": "string",
        "description": "循环伏安法-下限电位（单位：伏特）",
        "minimum": "-10",
        "maximum": "10"
    },
    "poolFive.cvFinalE": {
        "type": "string",
        "description": "循环伏安法-终点电位（单位：伏特）",
        "minimum": "-10",
        "maximum": "10"
    },
    "poolFive.cvInitialScanPolarity": {
        "type": "string",
        "description": "循环伏安法-初始化扫码方向",
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
    "poolFive.cvScanRate": {
        "type": "string",
        "description": "循环伏安法-扫描速度",
        "minimum": "1e-6",
        "maximum": "10000"
    },
    "poolFive.cvSweepSegments": {
        "type": "string",
        "description": "循环伏安法-扫描段数",
        "minimum": "1",
        "maximum": "1000000"
    },
    "poolFive.cvSampleInterval": {
        "type": "string",
        "description": "循环伏安法-采样间隔",
        "minimum": "0.001",
        "maximum": "0.064"
    },
    "poolFive.cvQuietTime": {
        "type": "string",
        "description": "循环伏安法-静置时间",
        "minimum": "1",
        "maximum": "1000000"
    },
    "poolFive.cvSensitivity": {
        "type": "string",
        "description": "循环伏安法-灵敏度",
        "enum": [
            "1e-001",
            "1e-002",
            "1e-003",
            "1e-004",
            "1e-005",
            "1e-006",
            "1e-007",
            "1e-008",
            "1e-009",
            "1e-010",
            "1e-011",
            "1e-012"
        ]
    },
    "poolFive.lsvStatus": {
        "type": "string",
        "description": "线性扫描伏安法-是否检测",
        "enum": [
            {
                "label": "不检测",
                "value": "0"
            },
            {
                "label": "检测",
                "value": "1"
            }
        ]
    },
    "poolFive.lsvInitE": {
        "type": "string",
        "description": "线性扫描伏安法-初始电位（单位：伏特）",
        "minimum": "-10",
        "maximum": "10"
    },
    "poolFive.lsvFinalE": {
        "type": "string",
        "description": "线性扫描伏安法-终点电位（单位：伏特）",
        "minimum": "-10",
        "maximum": "10"
    },
    "poolFive.lsvScanRate": {
        "type": "string",
        "description": "线性扫描伏安法-扫描速度",
        "minimum": "1e-6",
        "maximum": "20000"
    },
    "poolFive.lsvSampleInterval": {
        "type": "string",
        "description": "线性扫描伏安法-采样间隔",
        "minimum": "0.001",
        "maximum": "0.064"
    },
    "poolFive.lsvQuietTime": {
        "type": "string",
        "description": "线性扫描伏安法-静置时间",
        "minimum": "1",
        "maximum": "1000000"
    },
    "poolFive.lsvSensitivity": {
        "type": "string",
        "description": "线性扫描伏安法-灵敏度",
        "enum": [
            "1e-001",
            "1e-002",
            "1e-003",
            "1e-004",
            "1e-005",
            "1e-006",
            "1e-007",
            "1e-008",
            "1e-009",
            "1e-010",
            "1e-011",
            "1e-012"
        ]
    },
    "poolFive.etcStatus": {
        "type": "string",
        "description": "电流/时间曲线-是否检测",
        "enum": [
            {
                "label": "不检测",
                "value": "0"
            },
            {
                "label": "检测",
                "value": "1"
            }
        ]
    },
    "poolFive.etcInitE": {
        "type": "string",
        "description": "电流/时间曲线-初始电位（单位：伏特）",
        "minimum": "-10",
        "maximum": "10"
    },
    "poolFive.etcSampleInterval": {
        "type": "string",
        "description": "电流/时间曲线-采样间隔",
        "minimum": "1e-6",
        "maximum": "50"
    },
    "poolFive.etcRunTime": {
        "type": "string",
        "description": "电流/时间曲线-运行时间",
        "minimum": "0.001",
        "maximum": "500000"
    },
    "poolFive.etcQuietTime": {
        "type": "string",
        "description": "电流/时间曲线-静置时间",
        "minimum": "1",
        "maximum": "1000000"
    },
    "poolFive.etcScalesDuringRun": {
        "type": "string",
        "description": "电流/时间曲线-电流量程档数",
        "enum": 1
    },
    "poolFive.etcSensitivity": {
        "type": "string",
        "description": "电流/时间曲线-灵敏度",
        "enum": [
            "1e-001",
            "1e-002",
            "1e-003",
            "1e-004",
            "1e-005",
            "1e-006",
            "1e-007",
            "1e-008",
            "1e-009",
            "1e-010",
            "1e-011",
            "1e-012"
        ]
    },
    "poolFive.acimStatus": {
        "type": "string",
        "description": "交流阻抗测量-是否检测",
        "enum": [
            {
                "label": "不检测",
                "value": "0"
            },
            {
                "label": "检测",
                "value": "1"
            }
        ]
    },
    "poolFive.acimInitE": {
        "type": "string",
        "description": "交流阻抗测量-初始电位（单位：伏特）",
        "minimum": "-10",
        "maximum": "10"
    },
    "poolFive.acimHighFrequency": {
        "type": "string",
        "description": "交流阻抗测量-上限频率（单位：赫兹）",
        "minimum": "1e-4",
        "maximum": "2e6"
    },
    "poolFive.acimLowFrequency": {
        "type": "string",
        "description": "交流阻抗测量-下限频率（单位：赫兹）",
        "minimum": "1e-5",
        "maximum": "1e5"
    },
    "poolFive.acimAmplitude": {
        "type": "string",
        "description": "交流阻抗测量-振幅",
        "minimum": "1e-5",
        "maximum": "0.7"
    },
    "poolFive.acimQuietTime": {
        "type": "string",
        "description": "交流阻抗测量-静置时间",
        "minimum": "1",
        "maximum": "1000000"
    },
    "elecTestResult": {
        "type": "string",
        "description": "电化学实验结果"
    }
},
                "required": ["poolOne", "poolOne.joinStatus", "poolOne.bottleType", "poolOne.bottleCathode", "poolOne.bottleAnode", "poolOne.bottleCatalyst", "poolOne.catalystCapacity", "poolOne.catalystDropletVolume", "poolOne.carbonPaperType", "poolOne.dryerType", "poolOne.dryerTime", "poolOne.dryerPower", "poolOne.electrolyteCycleSpeed", "poolOne.ventilationTime", "poolOne.cleaningFrequency", "poolOne.cvStatus", "poolOne.lsvStatus", "poolOne.etcStatus", "poolOne.acimStatus", "poolTwo", "poolTwo.joinStatus", "poolTwo.bottleType", "poolTwo.bottleCathode", "poolTwo.bottleAnode", "poolTwo.bottleCatalyst", "poolTwo.catalystCapacity", "poolTwo.catalystDropletVolume", "poolTwo.carbonPaperType", "poolTwo.dryerType", "poolTwo.dryerTime", "poolTwo.dryerPower", "poolTwo.electrolyteCycleSpeed", "poolTwo.ventilationTime", "poolTwo.cleaningFrequency", "poolTwo.cvStatus", "poolTwo.lsvStatus", "poolTwo.etcStatus", "poolTwo.acimStatus", "poolThree", "poolThree.joinStatus", "poolThree.bottleType", "poolThree.bottleCathode", "poolThree.bottleAnode", "poolThree.bottleCatalyst", "poolThree.catalystCapacity", "poolThree.catalystDropletVolume", "poolThree.carbonPaperType", "poolThree.dryerType", "poolThree.dryerTime", "poolThree.dryerPower", "poolThree.electrolyteCycleSpeed", "poolThree.ventilationTime", "poolThree.cleaningFrequency", "poolThree.cvStatus", "poolThree.lsvStatus", "poolThree.etcStatus", "poolThree.acimStatus", "poolFour", "poolFour.joinStatus", "poolFour.bottleType", "poolFour.bottleCathode", "poolFour.bottleAnode", "poolFour.bottleCatalyst", "poolFour.catalystCapacity", "poolFour.catalystDropletVolume", "poolFour.carbonPaperType", "poolFour.dryerType", "poolFour.dryerTime", "poolFour.dryerPower", "poolFour.electrolyteCycleSpeed", "poolFour.ventilationTime", "poolFour.cleaningFrequency", "poolFour.cvStatus", "poolFour.lsvStatus", "poolFour.etcStatus", "poolFour.acimStatus", "poolFive", "poolFive.joinStatus", "poolFive.bottleType", "poolFive.bottleCathode", "poolFive.bottleAnode", "poolFive.bottleCatalyst", "poolFive.catalystCapacity", "poolFive.catalystDropletVolume", "poolFive.carbonPaperType", "poolFive.dryerType", "poolFive.dryerTime", "poolFive.dryerPower", "poolFive.electrolyteCycleSpeed", "poolFive.ventilationTime", "poolFive.cleaningFrequency", "poolFive.cvStatus", "poolFive.lsvStatus", "poolFive.etcStatus", "poolFive.acimStatus"]
            }
        }
                    ]
                }
            }
        }
    }
    print(json.dumps(adv_message, ensure_ascii=False), flush=True)
    print(f"--- [five_electrochemical_Server] 五工位电化学工作站 is ready. ---", file=sys.stderr, flush=True)


if __name__ == "__main__":
    # 启动流程：先广播能力，再进入主循环
    five_electrochemical_server_advertise_capabilities()
    five_electrochemical_server_main_loop()
