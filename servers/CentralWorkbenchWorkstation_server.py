import sys
import json
# 动态导入当前设备对应的工具类（与主服务器文件同目录）
from tools.CentralWorkbenchWorkstation_server_tools import ActionServerTools


# 创建全局工具管理器实例
tool_manager = ActionServerTools()


# --- 定义设备动作函数（自动生成，与工具类方法对应）---
def tool_test(**params):
    return tool_manager.tool_test(**params)


def tool_sampleMovementFirst(**params):
    return tool_manager.tool_sampleMovementFirst(**params)


def tool_sampleMovementSecond_3(**params):
    return tool_manager.tool_sampleMovementSecond_3(**params)


def tool_sampleMovementThird(**params):
    return tool_manager.tool_sampleMovementThird(**params)


def tool_sampleMovementFourth(**params):
    return tool_manager.tool_sampleMovementFourth(**params)


def tool_funnelOnTheDistributionTable(**params):
    return tool_manager.tool_funnelOnTheDistributionTable(**params)


def tool_removeTheSampleTrayCoverPort1(**params):
    return tool_manager.tool_removeTheSampleTrayCoverPort1(**params)


def tool_putItInTheWashingMachine(**params):
    return tool_manager.tool_putItInTheWashingMachine(**params)


def tool_putInTheTemporaryStoragePosition(**params):
    return tool_manager.tool_putInTheTemporaryStoragePosition(**params)


def tool_takeReleaseMedicationFirst(**params):
    return tool_manager.tool_takeReleaseMedicationFirst(**params)


def tool_takeReleaseMedicationFirstSecond(**params):
    return tool_manager.tool_takeReleaseMedicationFirstSecond(**params)


def tool_dischargePortFirst(**params):
    return tool_manager.tool_dischargePortFirst(**params)


def tool_dischargePortSecond(**params):
    return tool_manager.tool_dischargePortSecond(**params)


def tool_dischargePortThird(**params):
    return tool_manager.tool_dischargePortThird(**params)


def tool_dischargePortFourth(**params):
    return tool_manager.tool_dischargePortFourth(**params)


def tool_dischargePortFifth(**params):
    return tool_manager.tool_dischargePortFifth(**params)


def tool_dischargePortSixth(**params):
    return tool_manager.tool_dischargePortSixth(**params)


def tool_dischargePortSeventh(**params):
    return tool_manager.tool_dischargePortSeventh(**params)


def tool_PutTheWasherFirst(**params):
    return tool_manager.tool_PutTheWasherFirst(**params)


def tool_PutTheWasherSecond(**params):
    return tool_manager.tool_PutTheWasherSecond(**params)


def tool_putStagingBit(**params):
    return tool_manager.tool_putStagingBit(**params)


def tool_squareCrucibleIsDividedFirst(**params):
    return tool_manager.tool_squareCrucibleIsDividedFirst(**params)


def tool_squareCrucibleIsDividedSecond(**params):
    return tool_manager.tool_squareCrucibleIsDividedSecond(**params)


def tool_afterTheSampleIsDivided(**params):
    return tool_manager.tool_afterTheSampleIsDivided(**params)


def tool_XRDPlacedInTheCleaningMachine(**params):
    return tool_manager.tool_XRDPlacedInTheCleaningMachine(**params)


def tool_XRDPourIntoTemporaryStoragePosition(**params):
    return tool_manager.tool_XRDPourIntoTemporaryStoragePosition(**params)


def tool_washingAfterSampling(**params):
    return tool_manager.tool_washingAfterSampling(**params)


def tool_circularCrucibleTemporaryStoragePosition(**params):
    return tool_manager.tool_circularCrucibleTemporaryStoragePosition(**params)


def tool_dirtyFunnelIntoWashingMachine(**params):
    return tool_manager.tool_dirtyFunnelIntoWashingMachine(**params)


def tool_dirtyFunnelStoragePosition(**params):
    return tool_manager.tool_dirtyFunnelStoragePosition(**params)


def tool_overallSampleAddition(**params):
    return tool_manager.tool_overallSampleAddition(**params)


def tool_sampleMovementSecond(**params):
    return tool_manager.tool_sampleMovementSecond(**params)



AVAILABLE_TOOLS_ACTION = {
    "test": tool_test,
    "sampleMovementFirst": tool_sampleMovementFirst,
    "sampleMovementSecond_3": tool_sampleMovementSecond_3,
    "sampleMovementThird": tool_sampleMovementThird,
    "sampleMovementFourth": tool_sampleMovementFourth,
    "funnelOnTheDistributionTable": tool_funnelOnTheDistributionTable,
    "removeTheSampleTrayCoverPort1": tool_removeTheSampleTrayCoverPort1,
    "putItInTheWashingMachine": tool_putItInTheWashingMachine,
    "putInTheTemporaryStoragePosition": tool_putInTheTemporaryStoragePosition,
    "takeReleaseMedicationFirst": tool_takeReleaseMedicationFirst,
    "takeReleaseMedicationFirstSecond": tool_takeReleaseMedicationFirstSecond,
    "dischargePortFirst": tool_dischargePortFirst,
    "dischargePortSecond": tool_dischargePortSecond,
    "dischargePortThird": tool_dischargePortThird,
    "dischargePortFourth": tool_dischargePortFourth,
    "dischargePortFifth": tool_dischargePortFifth,
    "dischargePortSixth": tool_dischargePortSixth,
    "dischargePortSeventh": tool_dischargePortSeventh,
    "PutTheWasherFirst": tool_PutTheWasherFirst,
    "PutTheWasherSecond": tool_PutTheWasherSecond,
    "putStagingBit": tool_putStagingBit,
    "squareCrucibleIsDividedFirst": tool_squareCrucibleIsDividedFirst,
    "squareCrucibleIsDividedSecond": tool_squareCrucibleIsDividedSecond,
    "afterTheSampleIsDivided": tool_afterTheSampleIsDivided,
    "XRDPlacedInTheCleaningMachine": tool_XRDPlacedInTheCleaningMachine,
    "XRDPourIntoTemporaryStoragePosition": tool_XRDPourIntoTemporaryStoragePosition,
    "washingAfterSampling": tool_washingAfterSampling,
    "circularCrucibleTemporaryStoragePosition": tool_circularCrucibleTemporaryStoragePosition,
    "dirtyFunnelIntoWashingMachine": tool_dirtyFunnelIntoWashingMachine,
    "dirtyFunnelStoragePosition": tool_dirtyFunnelStoragePosition,
    "overallSampleAddition": tool_overallSampleAddition,
    "sampleMovementSecond": tool_sampleMovementSecond
}


# --- MCP协议通信主逻辑（自动适配当前设备）---
def CentralWorkbenchWorkstation_server_main_loop():
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
            print(f"--- [CentralWorkbenchWorkstation_Server] Critical Error: {str(e)} ---", file=sys.stderr, flush=True)


def CentralWorkbenchWorkstation_server_advertise_capabilities():
    """广播当前设备的MCP能力（设备信息、支持的动作）"""
    adv_message = {
        "jsonrpc": "2.0",
        "method": "protocol/advertise",
        "params": {
            "type": "server",
            "server": {
                "protocolVersion": "0.1.0",
                "displayName": "中央工作台工作站",
                "capabilities": {
                    "tools": [
        {
            "name": "test",
            "description": "测试空指令",
            "parameters": {
                "type": "object",
                "properties": {
    "data": {
        "type": "int",
        "description": "data"
    }
},
                "required": []
            }
        },
        {
            "name": "sampleMovementFirst",
            "description": "检测并取走样品盘放置到固体进样仪里",
            "parameters": {
                "type": "object",
                "properties": {
    "chainName": {
        "type": "string",
        "description": "chainName"
    },
    "ifAsynchronous": {
        "type": "boolean",
        "description": "ifAsynchronous"
    },
    "sn": {
        "type": "string",
        "description": "sn"
    },
    "method": {
        "type": "string",
        "description": "method"
    }
},
                "required": ["chainName", "ifAsynchronous", "sn", "method"]
            }
        },
        {
            "name": "sampleMovementSecond_3",
            "description": "检测并取走圆形坩埚放置到分料台里",
            "parameters": {
                "type": "object",
                "properties": {
    "chainName": {
        "type": "string",
        "description": "chainName"
    },
    "ifAsynchronous": {
        "type": "boolean",
        "description": "ifAsynchronous"
    },
    "sn": {
        "type": "string",
        "description": "sn"
    },
    "method": {
        "type": "string",
        "description": "method"
    }
},
                "required": ["chainName", "ifAsynchronous", "sn", "method"]
            }
        },
        {
            "name": "sampleMovementThird",
            "description": "检测并取走方形坩埚放置到分料台里",
            "parameters": {
                "type": "object",
                "properties": {
    "chainName": {
        "type": "string",
        "description": "chainName"
    },
    "ifAsynchronous": {
        "type": "boolean",
        "description": "ifAsynchronous"
    },
    "sn": {
        "type": "string",
        "description": "sn"
    },
    "method": {
        "type": "string",
        "description": "method"
    }
},
                "required": ["chainName", "ifAsynchronous", "sn", "method"]
            }
        },
        {
            "name": "sampleMovementFourth",
            "description": "检测并取走XRD放置到分料台里",
            "parameters": {
                "type": "object",
                "properties": {
    "chainName": {
        "type": "string",
        "description": "chainName"
    },
    "ifAsynchronous": {
        "type": "boolean",
        "description": "ifAsynchronous"
    },
    "sn": {
        "type": "string",
        "description": "sn"
    },
    "method": {
        "type": "string",
        "description": "method"
    }
},
                "required": ["chainName", "ifAsynchronous", "sn", "method"]
            }
        },
        {
            "name": "funnelOnTheDistributionTable",
            "description": "取干净漏斗放到分料台",
            "parameters": {
                "type": "object",
                "properties": {
    "chainName": {
        "type": "string",
        "description": "chainName"
    },
    "ifAsynchronous": {
        "type": "boolean",
        "description": "ifAsynchronous"
    },
    "sn": {
        "type": "string",
        "description": "sn"
    },
    "method": {
        "type": "string",
        "description": "method"
    }
},
                "required": ["chainName", "ifAsynchronous", "sn", "method"]
            }
        },
        {
            "name": "removeTheSampleTrayCoverPort1",
            "description": "检测并取走样品盘盖板盖到出料口的样品盘上1",
            "parameters": {
                "type": "object",
                "properties": {
    "chainName": {
        "type": "string",
        "description": "chainName"
    },
    "ifAsynchronous": {
        "type": "boolean",
        "description": "ifAsynchronous"
    },
    "sn": {
        "type": "string",
        "description": "sn"
    },
    "method": {
        "type": "string",
        "description": "method"
    }
},
                "required": ["chainName", "ifAsynchronous", "sn", "method"]
            }
        },
        {
            "name": "putItInTheWashingMachine",
            "description": "检测并取走玻璃板压料再放清洗机里",
            "parameters": {
                "type": "object",
                "properties": {
    "chainName": {
        "type": "string",
        "description": "chainName"
    },
    "ifAsynchronous": {
        "type": "boolean",
        "description": "ifAsynchronous"
    },
    "sn": {
        "type": "string",
        "description": "sn"
    },
    "method": {
        "type": "string",
        "description": "method"
    }
},
                "required": ["chainName", "ifAsynchronous", "sn", "method"]
            }
        },
        {
            "name": "putInTheTemporaryStoragePosition",
            "description": "检测并取走玻璃板压料再放暂存位",
            "parameters": {
                "type": "object",
                "properties": {
    "chainName": {
        "type": "string",
        "description": "chainName"
    },
    "ifAsynchronous": {
        "type": "boolean",
        "description": "ifAsynchronous"
    },
    "sn": {
        "type": "string",
        "description": "sn"
    },
    "method": {
        "type": "string",
        "description": "method"
    }
},
                "required": ["chainName", "ifAsynchronous", "sn", "method"]
            }
        },
        {
            "name": "takeReleaseMedicationFirst",
            "description": "检测并添加第一种药剂后放回原位",
            "parameters": {
                "type": "object",
                "properties": {
    "chainName": {
        "type": "string",
        "description": "chainName"
    },
    "ifAsynchronous": {
        "type": "boolean",
        "description": "ifAsynchronous"
    },
    "sn": {
        "type": "string",
        "description": "sn"
    },
    "method": {
        "type": "string",
        "description": "method"
    }
},
                "required": ["chainName", "ifAsynchronous", "sn", "method"]
            }
        },
        {
            "name": "takeReleaseMedicationFirstSecond",
            "description": "检测并添加第一种药剂后放回原位 后半部分",
            "parameters": {
                "type": "object",
                "properties": {
    "chainName": {
        "type": "string",
        "description": "chainName"
    },
    "ifAsynchronous": {
        "type": "boolean",
        "description": "ifAsynchronous"
    },
    "sn": {
        "type": "string",
        "description": "sn"
    },
    "method": {
        "type": "string",
        "description": "method"
    }
},
                "required": ["chainName", "ifAsynchronous", "sn", "method"]
            }
        },
        {
            "name": "dischargePortFirst",
            "description": "从固体进样仪里取走放置振平盘里振平，再放置到出料口1",
            "parameters": {
                "type": "object",
                "properties": {
    "chainName": {
        "type": "string",
        "description": "chainName"
    },
    "ifAsynchronous": {
        "type": "boolean",
        "description": "ifAsynchronous"
    },
    "sn": {
        "type": "string",
        "description": "sn"
    },
    "method": {
        "type": "string",
        "description": "method"
    }
},
                "required": ["chainName", "ifAsynchronous", "sn", "method"]
            }
        },
        {
            "name": "dischargePortSecond",
            "description": "从固体进样仪里取走放置振平盘里振平，再放置到出料口2",
            "parameters": {
                "type": "object",
                "properties": {
    "chainName": {
        "type": "string",
        "description": "chainName"
    },
    "ifAsynchronous": {
        "type": "boolean",
        "description": "ifAsynchronous"
    },
    "sn": {
        "type": "string",
        "description": "sn"
    },
    "method": {
        "type": "string",
        "description": "method"
    }
},
                "required": ["chainName", "ifAsynchronous", "sn", "method"]
            }
        },
        {
            "name": "dischargePortThird",
            "description": "方形坩埚从分料台取到出料口1",
            "parameters": {
                "type": "object",
                "properties": {
    "chainName": {
        "type": "string",
        "description": "chainName"
    },
    "ifAsynchronous": {
        "type": "boolean",
        "description": "ifAsynchronous"
    },
    "sn": {
        "type": "string",
        "description": "sn"
    },
    "method": {
        "type": "string",
        "description": "method"
    }
},
                "required": ["chainName", "ifAsynchronous", "sn", "method"]
            }
        },
        {
            "name": "dischargePortFourth",
            "description": "方形坩埚从分料台取到出料口2",
            "parameters": {
                "type": "object",
                "properties": {
    "chainName": {
        "type": "string",
        "description": "chainName"
    },
    "ifAsynchronous": {
        "type": "boolean",
        "description": "ifAsynchronous"
    },
    "sn": {
        "type": "string",
        "description": "sn"
    },
    "method": {
        "type": "string",
        "description": "method"
    }
},
                "required": ["chainName", "ifAsynchronous", "sn", "method"]
            }
        },
        {
            "name": "dischargePortFifth",
            "description": "XRD从分料台取到出料口1",
            "parameters": {
                "type": "object",
                "properties": {
    "chainName": {
        "type": "string",
        "description": "chainName"
    },
    "ifAsynchronous": {
        "type": "boolean",
        "description": "ifAsynchronous"
    },
    "sn": {
        "type": "string",
        "description": "sn"
    },
    "method": {
        "type": "string",
        "description": "method"
    }
},
                "required": ["chainName", "ifAsynchronous", "sn", "method"]
            }
        },
        {
            "name": "dischargePortSixth",
            "description": "XRD从分料台取到出料口2",
            "parameters": {
                "type": "object",
                "properties": {
    "chainName": {
        "type": "string",
        "description": "chainName"
    },
    "ifAsynchronous": {
        "type": "boolean",
        "description": "ifAsynchronous"
    },
    "sn": {
        "type": "string",
        "description": "sn"
    },
    "method": {
        "type": "string",
        "description": "method"
    }
},
                "required": ["chainName", "ifAsynchronous", "sn", "method"]
            }
        },
        {
            "name": "dischargePortSeventh",
            "description": "圆形坩埚从分料台取到出料口1",
            "parameters": {
                "type": "object",
                "properties": {
    "chainName": {
        "type": "string",
        "description": "chainName"
    },
    "ifAsynchronous": {
        "type": "boolean",
        "description": "ifAsynchronous"
    },
    "sn": {
        "type": "string",
        "description": "sn"
    },
    "method": {
        "type": "string",
        "description": "method"
    }
},
                "required": ["chainName", "ifAsynchronous", "sn", "method"]
            }
        },
        {
            "name": "PutTheWasherFirst",
            "description": "样品盘分样后放清洗机位置1",
            "parameters": {
                "type": "object",
                "properties": {
    "chainName": {
        "type": "string",
        "description": "chainName"
    },
    "ifAsynchronous": {
        "type": "boolean",
        "description": "ifAsynchronous"
    },
    "sn": {
        "type": "string",
        "description": "sn"
    },
    "method": {
        "type": "string",
        "description": "method"
    }
},
                "required": ["chainName", "ifAsynchronous", "sn", "method"]
            }
        },
        {
            "name": "PutTheWasherSecond",
            "description": "样品盘分样后放清洗机位置2",
            "parameters": {
                "type": "object",
                "properties": {
    "chainName": {
        "type": "string",
        "description": "chainName"
    },
    "ifAsynchronous": {
        "type": "boolean",
        "description": "ifAsynchronous"
    },
    "sn": {
        "type": "string",
        "description": "sn"
    },
    "method": {
        "type": "string",
        "description": "method"
    }
},
                "required": ["chainName", "ifAsynchronous", "sn", "method"]
            }
        },
        {
            "name": "putStagingBit",
            "description": "样品盘分样后放暂存位",
            "parameters": {
                "type": "object",
                "properties": {
    "chainName": {
        "type": "string",
        "description": "chainName"
    },
    "ifAsynchronous": {
        "type": "boolean",
        "description": "ifAsynchronous"
    },
    "sn": {
        "type": "string",
        "description": "sn"
    },
    "method": {
        "type": "string",
        "description": "method"
    }
},
                "required": ["chainName", "ifAsynchronous", "sn", "method"]
            }
        },
        {
            "name": "squareCrucibleIsDividedFirst",
            "description": "方形坩埚分样后放清洗机位置1",
            "parameters": {
                "type": "object",
                "properties": {
    "chainName": {
        "type": "string",
        "description": "chainName"
    },
    "ifAsynchronous": {
        "type": "boolean",
        "description": "ifAsynchronous"
    },
    "sn": {
        "type": "string",
        "description": "sn"
    },
    "method": {
        "type": "string",
        "description": "method"
    }
},
                "required": ["chainName", "ifAsynchronous", "sn", "method"]
            }
        },
        {
            "name": "squareCrucibleIsDividedSecond",
            "description": "方形坩埚分样后放清洗机位置2",
            "parameters": {
                "type": "object",
                "properties": {
    "chainName": {
        "type": "string",
        "description": "chainName"
    },
    "ifAsynchronous": {
        "type": "boolean",
        "description": "ifAsynchronous"
    },
    "sn": {
        "type": "string",
        "description": "sn"
    },
    "method": {
        "type": "string",
        "description": "method"
    }
},
                "required": ["chainName", "ifAsynchronous", "sn", "method"]
            }
        },
        {
            "name": "afterTheSampleIsDivided",
            "description": "方形坩埚分样后放暂存位（待定）",
            "parameters": {
                "type": "object",
                "properties": {
    "chainName": {
        "type": "string",
        "description": "chainName"
    },
    "ifAsynchronous": {
        "type": "boolean",
        "description": "ifAsynchronous"
    },
    "sn": {
        "type": "string",
        "description": "sn"
    },
    "method": {
        "type": "string",
        "description": "method"
    }
},
                "required": ["chainName", "ifAsynchronous", "sn", "method"]
            }
        },
        {
            "name": "XRDPlacedInTheCleaningMachine",
            "description": "XRD倒废药剂后放清洗机",
            "parameters": {
                "type": "object",
                "properties": {
    "chainName": {
        "type": "string",
        "description": "chainName"
    },
    "ifAsynchronous": {
        "type": "boolean",
        "description": "ifAsynchronous"
    },
    "sn": {
        "type": "string",
        "description": "sn"
    },
    "method": {
        "type": "string",
        "description": "method"
    }
},
                "required": ["chainName", "ifAsynchronous", "sn", "method"]
            }
        },
        {
            "name": "XRDPourIntoTemporaryStoragePosition",
            "description": "XRD倒废药剂后放暂存位（待定）",
            "parameters": {
                "type": "object",
                "properties": {
    "chainName": {
        "type": "string",
        "description": "chainName"
    },
    "ifAsynchronous": {
        "type": "boolean",
        "description": "ifAsynchronous"
    },
    "sn": {
        "type": "string",
        "description": "sn"
    },
    "method": {
        "type": "string",
        "description": "method"
    }
},
                "required": ["chainName", "ifAsynchronous", "sn", "method"]
            }
        },
        {
            "name": "washingAfterSampling",
            "description": "圆形坩埚分样后放清洗机位置1",
            "parameters": {
                "type": "object",
                "properties": {
    "chainName": {
        "type": "string",
        "description": "chainName"
    },
    "ifAsynchronous": {
        "type": "boolean",
        "description": "ifAsynchronous"
    },
    "sn": {
        "type": "string",
        "description": "sn"
    },
    "method": {
        "type": "string",
        "description": "method"
    }
},
                "required": ["chainName", "ifAsynchronous", "sn", "method"]
            }
        },
        {
            "name": "circularCrucibleTemporaryStoragePosition",
            "description": "圆形坩埚分样后放暂存位",
            "parameters": {
                "type": "object",
                "properties": {
    "chainName": {
        "type": "string",
        "description": "chainName"
    },
    "ifAsynchronous": {
        "type": "boolean",
        "description": "ifAsynchronous"
    },
    "sn": {
        "type": "string",
        "description": "sn"
    },
    "method": {
        "type": "string",
        "description": "method"
    }
},
                "required": ["chainName", "ifAsynchronous", "sn", "method"]
            }
        },
        {
            "name": "dirtyFunnelIntoWashingMachine",
            "description": "脏漏斗取出放清洗机里",
            "parameters": {
                "type": "object",
                "properties": {
    "chainName": {
        "type": "string",
        "description": "chainName"
    },
    "ifAsynchronous": {
        "type": "boolean",
        "description": "ifAsynchronous"
    },
    "sn": {
        "type": "string",
        "description": "sn"
    },
    "method": {
        "type": "string",
        "description": "method"
    }
},
                "required": ["chainName", "ifAsynchronous", "sn", "method"]
            }
        },
        {
            "name": "dirtyFunnelStoragePosition",
            "description": "脏漏斗取出放脏漏斗暂存位",
            "parameters": {
                "type": "object",
                "properties": {
    "chainName": {
        "type": "string",
        "description": "chainName"
    },
    "ifAsynchronous": {
        "type": "boolean",
        "description": "ifAsynchronous"
    },
    "sn": {
        "type": "string",
        "description": "sn"
    },
    "method": {
        "type": "string",
        "description": "method"
    }
},
                "required": ["chainName", "ifAsynchronous", "sn", "method"]
            }
        },
        {
            "name": "overallSampleAddition",
            "description": "整体制样",
            "parameters": {
                "type": "object",
                "properties": {
    "chainName": {
        "type": "string",
        "description": "chainName"
    },
    "ifAsynchronous": {
        "type": "boolean",
        "description": "ifAsynchronous"
    },
    "sn": {
        "type": "string",
        "description": "sn"
    },
    "method": {
        "type": "string",
        "description": "method"
    },
    "index": {
        "type": "int",
        "description": "添加的第几种药剂(1-6)"
    },
    "value": {
        "type": "float",
        "description": "添加克数"
    },
    "position": {
        "type": "int",
        "description": "样品盘几号位置"
    }
},
                "required": ["chainName", "ifAsynchronous", "sn", "method", "value", "position"]
            }
        },
        {
            "name": "sampleMovementSecond",
            "description": "整体分样",
            "parameters": {
                "type": "object",
                "properties": {
    "chainName": {
        "type": "string",
        "description": "chainName"
    },
    "ifAsynchronous": {
        "type": "boolean",
        "description": "ifAsynchronous"
    },
    "sn": {
        "type": "string",
        "description": "sn"
    },
    "method": {
        "type": "string",
        "description": "method"
    },
    "oneStep": {
        "type": "int",
        "description": "oneStep"
    },
    "threeStep": {
        "type": "int",
        "description": "threeStep"
    },
    "fiveStep": {
        "type": "int",
        "description": "fiveStep"
    }
},
                "required": ["chainName", "ifAsynchronous", "sn", "method", "oneStep", "threeStep", "fiveStep"]
            }
        }
                    ]
                }
            }
        }
    }
    print(json.dumps(adv_message, ensure_ascii=False), flush=True)
    print(f"--- [CentralWorkbenchWorkstation_Server] 中央工作台工作站 is ready. ---", file=sys.stderr, flush=True)


if __name__ == "__main__":
    # 启动流程：先广播能力，再进入主循环
    CentralWorkbenchWorkstation_server_advertise_capabilities()
    CentralWorkbenchWorkstation_server_main_loop()
