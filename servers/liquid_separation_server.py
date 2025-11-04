import sys
import json
# 动态导入当前设备对应的工具类（与主服务器文件同目录）
from tools.liquid_separation_server_tools import ActionServerTools


# 创建全局工具管理器实例
tool_manager = ActionServerTools()


# --- 定义设备动作函数（自动生成，与工具类方法对应）---
def tool_init_station(**params):
    return tool_manager.tool_init_station(**params)


def tool_send_sample_info(**params):
    return tool_manager.tool_send_sample_info(**params)


def tool_notice_sample_leave(**params):
    return tool_manager.tool_notice_sample_leave(**params)


def tool_sample_apply_enter(**params):
    return tool_manager.tool_sample_apply_enter(**params)


def tool_start_liquid_station(**params):
    return tool_manager.tool_start_liquid_station(**params)


def tool_release_target_station_slot(**params):
    return tool_manager.tool_release_target_station_slot(**params)


def tool_release_all_slot(**params):
    return tool_manager.tool_release_all_slot(**params)



AVAILABLE_TOOLS_ACTION = {
    "init_station": tool_init_station,
    "send_sample_info": tool_send_sample_info,
    "notice_sample_leave": tool_notice_sample_leave,
    "sample_apply_enter": tool_sample_apply_enter,
    "start_liquid_station": tool_start_liquid_station,
    "release_target_station_slot": tool_release_target_station_slot,
    "release_all_slot": tool_release_all_slot
}


# --- MCP协议通信主逻辑（自动适配当前设备）---
def liquid_separation_server_main_loop():
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
            print(f"--- [liquid_separation_Server] Critical Error: {str(e)} ---", file=sys.stderr, flush=True)


def liquid_separation_server_advertise_capabilities():
    """广播当前设备的MCP能力（设备信息、支持的动作）"""
    adv_message = {
        "jsonrpc": "2.0",
        "method": "protocol/advertise",
        "params": {
            "type": "server",
            "server": {
                "protocolVersion": "0.1.0",
                "displayName": "分液工作站",
                "capabilities": {
                    "tools": [
        {
            "name": "init_station",
            "description": "初始化分液站",
            "parameters": {
                "type": "object",
                "properties": {
    "operate": {
        "type": "string",
        "description": "指令编码"
    }
},
                "required": ["operate"]
            }
        },
        {
            "name": "send_sample_info",
            "description": "发送样品信息",
            "parameters": {
                "type": "object",
                "properties": {
    "operate": {
        "type": "string",
        "description": "指令编码"
    },
    "separateInfo": {
        "type": "array",
        "description": "分液信息",
        "properties": {
            "sampleNo": {
                "type": "string",
                "description": "样品编码"
            },
            "cupType": {
                "type": "int",
                "description": "样品杯类型",
                "enum": [
                    {
                        "label": "离子色谱",
                        "value": 1
                    },
                    {
                        "label": "氨氮",
                        "value": 2
                    },
                    {
                        "label": "总磷总氮",
                        "value": 3
                    },
                    {
                        "label": "COD",
                        "value": 4
                    },
                    {
                        "label": "流动注射",
                        "value": 5
                    },
                    {
                        "label": "ICPMS",
                        "value": 6
                    }
                ]
            },
            "planVolume": {
                "type": "float",
                "description": "计划分液体积（单位：毫升）"
            },
            "dilutionMultiple": {
                "type": "float",
                "description": "稀释倍数"
            },
            "phVolume": {
                "type": "float",
                "description": "PH中和体积（单位：毫升）"
            },
            "subSmapleNo": {
                "type": "string",
                "description": "子样品编码"
            }
        },
        "required": [
            "sampleNo",
            "cupType",
            "planVolume",
            "dilutionMultiple",
            "phVolume",
            "subSmapleNo"
        ]
    },
    "separateInfo.sampleNo": {
        "type": "string",
        "description": "样品编码"
    },
    "separateInfo.cupType": {
        "type": "int",
        "description": "样品杯类型",
        "enum": [
            {
                "label": "离子色谱",
                "value": 1
            },
            {
                "label": "氨氮",
                "value": 2
            },
            {
                "label": "总磷总氮",
                "value": 3
            },
            {
                "label": "COD",
                "value": 4
            },
            {
                "label": "流动注射",
                "value": 5
            },
            {
                "label": "ICPMS",
                "value": 6
            }
        ]
    },
    "separateInfo.planVolume": {
        "type": "float",
        "description": "计划分液体积（单位：毫升）"
    },
    "separateInfo.dilutionMultiple": {
        "type": "float",
        "description": "稀释倍数"
    },
    "separateInfo.phVolume": {
        "type": "float",
        "description": "PH中和体积（单位：毫升）"
    },
    "separateInfo.subSmapleNo": {
        "type": "string",
        "description": "子样品编码"
    },
    "sampleParam": {
        "type": "array",
        "description": "样品参数",
        "properties": {
            "sampleNo": {
                "type": "string",
                "description": "样品编码"
            },
            "isConductivity": {
                "type": "int",
                "description": "是否电导率",
                "enum": [
                    {
                        "label": "是",
                        "value": 1
                    },
                    {
                        "label": "否",
                        "value": 0
                    }
                ]
            },
            "isChloride": {
                "type": "string",
                "description": "是否氯离子",
                "enum": [
                    {
                        "label": "是",
                        "value": 1
                    },
                    {
                        "label": "否",
                        "value": 0
                    }
                ]
            },
            "isPH": {
                "type": "int",
                "description": "是否PH",
                "enum": [
                    {
                        "label": "是",
                        "value": 1
                    },
                    {
                        "label": "否",
                        "value": 0
                    }
                ]
            },
            "isHomogenized": {
                "type": "int",
                "description": "是否混匀",
                "enum": [
                    {
                        "label": "是",
                        "value": 1
                    },
                    {
                        "label": "否",
                        "value": 0
                    }
                ]
            }
        },
        "required": [
            "sampleNo",
            "isConductivity",
            "isChloride",
            "isPH",
            "isHomogenized"
        ]
    },
    "sampleParam.sampleNo": {
        "type": "string",
        "description": "样品编码"
    },
    "sampleParam.isConductivity": {
        "type": "int",
        "description": "是否电导率",
        "enum": [
            {
                "label": "是",
                "value": 1
            },
            {
                "label": "否",
                "value": 0
            }
        ]
    },
    "sampleParam.isChloride": {
        "type": "string",
        "description": "是否氯离子",
        "enum": [
            {
                "label": "是",
                "value": 1
            },
            {
                "label": "否",
                "value": 0
            }
        ]
    },
    "sampleParam.isPH": {
        "type": "int",
        "description": "是否PH",
        "enum": [
            {
                "label": "是",
                "value": 1
            },
            {
                "label": "否",
                "value": 0
            }
        ]
    },
    "sampleParam.isHomogenized": {
        "type": "int",
        "description": "是否混匀",
        "enum": [
            {
                "label": "是",
                "value": 1
            },
            {
                "label": "否",
                "value": 0
            }
        ]
    },
    "subsample_id": {
        "type": "string",
        "description": "参数 subsample_id"
    }
},
                "required": ["operate", "separateInfo", "separateInfo.sampleNo", "separateInfo.cupType", "separateInfo.planVolume", "separateInfo.dilutionMultiple", "separateInfo.phVolume", "separateInfo.subSmapleNo", "sampleParam", "sampleParam.sampleNo", "sampleParam.isConductivity", "sampleParam.isChloride", "sampleParam.isPH", "sampleParam.isHomogenized"]
            }
        },
        {
            "name": "notice_sample_leave",
            "description": "离开分液站通知",
            "parameters": {
                "type": "object",
                "properties": {
    "operate": {
        "type": "string",
        "description": "指令编码"
    }
},
                "required": ["operate"]
            }
        },
        {
            "name": "sample_apply_enter",
            "description": "进入分液站申请",
            "parameters": {
                "type": "object",
                "properties": {
    "operate": {
        "type": "string",
        "description": "指令编码"
    }
},
                "required": ["operate"]
            }
        },
        {
            "name": "start_liquid_station",
            "description": "开始运行分液站",
            "parameters": {
                "type": "object",
                "properties": {
    "operate": {
        "type": "string",
        "description": "指令编码"
    }
},
                "required": ["operate"]
            }
        },
        {
            "name": "release_target_station_slot",
            "description": "释放指定工作站容器",
            "parameters": {
                "type": "object",
                "properties": {
    "operate": {
        "type": "string",
        "description": "指令编码"
    },
    "workstation_code": {
        "type": "string",
        "description": "工作站编码",
        "enum": [
            {
                "label": "离子色谱",
                "value": "ic_workstation"
            },
            {
                "label": "氨氮",
                "value": "nh3n_workstation"
            },
            {
                "label": "总磷总氮",
                "value": "tptn_workstation"
            },
            {
                "label": "COD",
                "value": "cod_cod_workstation"
            },
            {
                "label": "流动注射仪",
                "value": "flow_inj_workstation"
            },
            {
                "label": "等离子体质谱仪",
                "value": "icpms_workstation_icpms_workstation"
            }
        ]
    }
},
                "required": ["operate", "workstation_code"]
            }
        },
        {
            "name": "release_all_slot",
            "description": "释放所有工作站容器",
            "parameters": {
                "type": "object",
                "properties": {
    "operate": {
        "type": "string",
        "description": "指令编码"
    }
},
                "required": ["operate"]
            }
        }
                    ]
                }
            }
        }
    }
    print(json.dumps(adv_message, ensure_ascii=False), flush=True)
    print(f"--- [liquid_separation_Server] 分液工作站 is ready. ---", file=sys.stderr, flush=True)


if __name__ == "__main__":
    # 启动流程：先广播能力，再进入主循环
    liquid_separation_server_advertise_capabilities()
    liquid_separation_server_main_loop()
