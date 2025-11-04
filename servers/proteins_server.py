import sys
import json
# 动态导入当前设备对应的工具类（与主服务器文件同目录）
from tools.proteins_server_tools import ActionServerTools


# 创建全局工具管理器实例
tool_manager = ActionServerTools()


# --- 定义设备动作函数（自动生成，与工具类方法对应）---
def tool_take_test_tube(**params):
    return tool_manager.tool_take_test_tube(**params)


def tool_Receive_peptide(**params):
    return tool_manager.tool_Receive_peptide(**params)


def tool_Move_toN(**params):
    return tool_manager.tool_Move_toN(**params)


def tool_N_blow(**params):
    return tool_manager.tool_N_blow(**params)


def tool_to_ethyl_ether(**params):
    return tool_manager.tool_to_ethyl_ether(**params)


def tool_inject_ether(**params):
    return tool_manager.tool_inject_ether(**params)


def tool_open_centrifuge(**params):
    return tool_manager.tool_open_centrifuge(**params)


def tool_ether_to_centrifuge(**params):
    return tool_manager.tool_ether_to_centrifuge(**params)


def tool_to_Aspirate(**params):
    return tool_manager.tool_to_Aspirate(**params)


def tool_to_water(**params):
    return tool_manager.tool_to_water(**params)


def tool_to_Shaker(**params):
    return tool_manager.tool_to_Shaker(**params)


def tool_to_LC(**params):
    return tool_manager.tool_to_LC(**params)


def tool_to_liquid_nitrogen(**params):
    return tool_manager.tool_to_liquid_nitrogen(**params)


def tool_to_Lyophilization_chamber(**params):
    return tool_manager.tool_to_Lyophilization_chamber(**params)


def tool_to_shaker_dissolve(**params):
    return tool_manager.tool_to_shaker_dissolve(**params)


def tool_to_shaker_Dialysis_card(**params):
    return tool_manager.tool_to_shaker_Dialysis_card(**params)


def tool_Solution_to_shaker_Dialysis_card(**params):
    return tool_manager.tool_Solution_to_shaker_Dialysis_card(**params)


def tool_Centrifuge_positioning(**params):
    return tool_manager.tool_Centrifuge_positioning(**params)


def tool_Dialysis_card_to_Centrifuge(**params):
    return tool_manager.tool_Dialysis_card_to_Centrifuge(**params)


def tool_Dialysis_card_to_out(**params):
    return tool_manager.tool_Dialysis_card_to_out(**params)


def tool_Centrifuge_tubes_to_out(**params):
    return tool_manager.tool_Centrifuge_tubes_to_out(**params)


def tool_start_Centrifuge(**params):
    return tool_manager.tool_start_Centrifuge(**params)


def tool_millipore_ELISA_PLATE(**params):
    return tool_manager.tool_millipore_ELISA_PLATE(**params)


def tool_start_microplate_reader(**params):
    return tool_manager.tool_start_microplate_reader(**params)


def tool_blance(**params):
    return tool_manager.tool_blance(**params)


def tool_request(**params):
    return tool_manager.tool_request(**params)


def tool_balance_to_out(**params):
    return tool_manager.tool_balance_to_out(**params)


def tool_ethyl_ether_to_N(**params):
    return tool_manager.tool_ethyl_ether_to_N(**params)


def tool_N_to_ethyl_ether(**params):
    return tool_manager.tool_N_to_ethyl_ether(**params)


def tool_add_water(**params):
    return tool_manager.tool_add_water(**params)


def tool_Centrifuge_tubes_to_LC(**params):
    return tool_manager.tool_Centrifuge_tubes_to_LC(**params)


def tool_start_mass_spectrometer(**params):
    return tool_manager.tool_start_mass_spectrometer(**params)


def tool_from_liquid_chromatography_to_mass_spectrometry(**params):
    return tool_manager.tool_from_liquid_chromatography_to_mass_spectrometry(**params)


def tool_from_liquid_chromatography_to_liquid_nitorgen(**params):
    return tool_manager.tool_from_liquid_chromatography_to_liquid_nitorgen(**params)



AVAILABLE_TOOLS_ACTION = {
    "take_test_tube": tool_take_test_tube,
    "Receive_peptide": tool_Receive_peptide,
    "Move_toN": tool_Move_toN,
    "N_blow": tool_N_blow,
    "to_ethyl_ether": tool_to_ethyl_ether,
    "inject_ether": tool_inject_ether,
    "open_centrifuge": tool_open_centrifuge,
    "ether_to_centrifuge": tool_ether_to_centrifuge,
    "to_Aspirate": tool_to_Aspirate,
    "to_water": tool_to_water,
    "to_Shaker": tool_to_Shaker,
    "to_LC": tool_to_LC,
    "to_liquid_nitrogen": tool_to_liquid_nitrogen,
    "to_Lyophilization_chamber": tool_to_Lyophilization_chamber,
    "to_shaker_dissolve": tool_to_shaker_dissolve,
    "to_shaker_Dialysis_card": tool_to_shaker_Dialysis_card,
    "Solution_to_shaker_Dialysis_card": tool_Solution_to_shaker_Dialysis_card,
    "Centrifuge_positioning": tool_Centrifuge_positioning,
    "Dialysis_card_to_Centrifuge": tool_Dialysis_card_to_Centrifuge,
    "Dialysis_card_to_out": tool_Dialysis_card_to_out,
    "Centrifuge_tubes_to_out": tool_Centrifuge_tubes_to_out,
    "start_Centrifuge": tool_start_Centrifuge,
    "millipore_ELISA_PLATE": tool_millipore_ELISA_PLATE,
    "start_microplate_reader": tool_start_microplate_reader,
    "blance": tool_blance,
    "request": tool_request,
    "balance_to_out": tool_balance_to_out,
    "ethyl_ether_to_N": tool_ethyl_ether_to_N,
    "N_to_ethyl_ether": tool_N_to_ethyl_ether,
    "add_water": tool_add_water,
    "Centrifuge_tubes_to_LC": tool_Centrifuge_tubes_to_LC,
    "start_mass_spectrometer": tool_start_mass_spectrometer,
    "from_liquid_chromatography_to_mass_spectrometry": tool_from_liquid_chromatography_to_mass_spectrometry,
    "from_liquid_chromatography_to_liquid_nitorgen": tool_from_liquid_chromatography_to_liquid_nitorgen
}


# --- MCP协议通信主逻辑（自动适配当前设备）---
def proteins_server_main_loop():
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
            print(f"--- [proteins_Server] Critical Error: {str(e)} ---", file=sys.stderr, flush=True)


def proteins_server_advertise_capabilities():
    """广播当前设备的MCP能力（设备信息、支持的动作）"""
    adv_message = {
        "jsonrpc": "2.0",
        "method": "protocol/advertise",
        "params": {
            "type": "server",
            "server": {
                "protocolVersion": "0.1.0",
                "displayName": "多肽合成",
                "capabilities": {
                    "tools": [
        {
            "name": "take_test_tube",
            "description": "取一个瓶子放在接收切割试剂的工位，并旋开瓶盖准备接收",
            "parameters": {
                "type": "object",
                "properties": {
    "data": {
        "type": "string",
        "description": "data"
    },
    "temp": {
        "type": "string",
        "description": "temp"
    }
},
                "required": ["data"]
            }
        },
        {
            "name": "Receive_peptide",
            "description": "接收多肽溶液",
            "parameters": {
                "type": "object",
                "properties": {
    "data": {
        "type": "string",
        "description": "data"
    },
    "temp": {
        "type": "string",
        "description": "temp"
    }
},
                "required": ["data"]
            }
        },
        {
            "name": "Move_toN",
            "description": "将接收的多肽溶液转移至氮吹工位",
            "parameters": {
                "type": "object",
                "properties": {
    "data": {
        "type": "string",
        "description": "data"
    },
    "temp": {
        "type": "string",
        "description": "temp"
    }
},
                "required": ["data"]
            }
        },
        {
            "name": "N_blow",
            "description": "启动氮吹-氮吹时间min",
            "parameters": {
                "type": "object",
                "properties": {
    "data": {
        "type": "string",
        "description": "data"
    },
    "time": {
        "type": "int",
        "description": "time"
    }
},
                "required": ["data", "time"]
            }
        },
        {
            "name": "to_ethyl_ether",
            "description": "转移至注入乙醚工位",
            "parameters": {
                "type": "object",
                "properties": {
    "data": {
        "type": "string",
        "description": "data"
    },
    "temp": {
        "type": "string",
        "description": "temp"
    }
},
                "required": ["data"]
            }
        },
        {
            "name": "inject_ether",
            "description": "启动注入乙醚",
            "parameters": {
                "type": "object",
                "properties": {
    "data": {
        "type": "string",
        "description": "data"
    },
    "ml": {
        "type": "float",
        "description": "ml"
    }
},
                "required": ["data", "ml"]
            }
        },
        {
            "name": "open_centrifuge",
            "description": "开启离心机门后定位到id号孔位",
            "parameters": {
                "type": "object",
                "properties": {
    "data": {
        "type": "string",
        "description": "data"
    },
    "id": {
        "type": "int",
        "description": "id"
    }
},
                "required": ["data", "id"]
            }
        },
        {
            "name": "ether_to_centrifuge",
            "description": "把乙醚工位的瓶子转移至离心机",
            "parameters": {
                "type": "object",
                "properties": {
    "data": {
        "type": "string",
        "description": "data"
    },
    "temp": {
        "type": "string",
        "description": "temp"
    }
},
                "required": ["data"]
            }
        },
        {
            "name": "to_Aspirate",
            "description": "将离心机里的瓶子转移至吸液工位后启动吸液",
            "parameters": {
                "type": "object",
                "properties": {
    "data": {
        "type": "string",
        "description": "data"
    },
    "temp": {
        "type": "string",
        "description": "temp"
    }
},
                "required": ["data"]
            }
        },
        {
            "name": "to_water",
            "description": "将吸液工位的瓶子转移至注水工位并注水溶解",
            "parameters": {
                "type": "object",
                "properties": {
    "data": {
        "type": "string",
        "description": "data"
    },
    "temp": {
        "type": "string",
        "description": "temp"
    }
},
                "required": ["data"]
            }
        },
        {
            "name": "to_Shaker",
            "description": "加水之后转移至摇床溶解后将瓶子转移至液相色谱进样工位",
            "parameters": {
                "type": "object",
                "properties": {
    "data": {
        "type": "string",
        "description": "data"
    },
    "time": {
        "type": "int",
        "description": "time"
    }
},
                "required": ["data", "time"]
            }
        },
        {
            "name": "to_LC",
            "description": "启动进样并开始液相色谱指令",
            "parameters": {
                "type": "object",
                "properties": {
    "data": {
        "type": "string",
        "description": "data"
    },
    "temp": {
        "type": "string",
        "description": "temp"
    },
    "resultCode": {
        "type": "file",
        "description": "输出结果参数"
    }
},
                "required": ["data"]
            }
        },
        {
            "name": "to_liquid_nitrogen",
            "description": "将液相色谱仪纯化后的num个瓶子转移至液氮盆(num数量从request里的LC_num获取)，从start_num个瓶子开始（因为纯化后可能瓶子数量超过十个，冷冻盆里只有十个工位）转移多少数量，冷冻多少时间，可以分批冷冻",
            "parameters": {
                "type": "object",
                "properties": {
    "data": {
        "type": "string",
        "description": "data"
    },
    "start_num": {
        "type": "int",
        "description": "start_num"
    },
    "num": {
        "type": "int",
        "description": "num"
    },
    "time": {
        "type": "int",
        "description": "time"
    }
},
                "required": ["data", "start_num", "num", "time"]
            }
        },
        {
            "name": "to_Lyophilization_chamber",
            "description": "将液氮盆里的num个瓶子，放置到冻干仓并冷冻time分钟",
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
    "time": {
        "type": "int",
        "description": "time"
    }
},
                "required": ["data", "num", "time"]
            }
        },
        {
            "name": "to_shaker_dissolve",
            "description": "将冻干仓里的num个瓶子，加注ml毫升溶解剂，放置到15.摇床摇动time分钟",
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
    "ml": {
        "type": "int",
        "description": "ml"
    },
    "time": {
        "type": "int",
        "description": "time"
    }
},
                "required": ["data", "num", "ml", "time"]
            }
        },
        {
            "name": "to_shaker_Dialysis_card",
            "description": "将num个透析卡转移至摇床",
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
    }
},
                "required": ["data", "num"]
            }
        },
        {
            "name": "Solution_to_shaker_Dialysis_card",
            "description": "将num个瓶子里的溶液转移至透析卡里并透析多少分钟",
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
    "time": {
        "type": "int",
        "description": "time"
    }
},
                "required": ["data", "num", "time"]
            }
        },
        {
            "name": "Centrifuge_positioning",
            "description": "把离心机门打开并定位到num位置",
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
    }
},
                "required": ["data", "num"]
            }
        },
        {
            "name": "Dialysis_card_to_Centrifuge",
            "description": "将第num号透析卡内的溶液转移至第num号浓缩管，并旋紧瓶盖，后转移至离心机正对着进样口的孔位",
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
    }
},
                "required": ["data", "num"]
            }
        },
        {
            "name": "Dialysis_card_to_out",
            "description": "将第num号透析卡放置回收口",
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
    }
},
                "required": ["data", "num"]
            }
        },
        {
            "name": "Centrifuge_tubes_to_out",
            "description": "将第num号离心管放置回收口",
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
    }
},
                "required": ["data", "num"]
            }
        },
        {
            "name": "start_Centrifuge",
            "description": "将离心机设置速度，时间后启动",
            "parameters": {
                "type": "object",
                "properties": {
    "data": {
        "type": "string",
        "description": "data"
    },
    "speed": {
        "type": "float",
        "description": "speed"
    },
    "time": {
        "type": "int",
        "description": "time"
    }
},
                "required": ["data", "speed", "time"]
            }
        },
        {
            "name": "millipore_ELISA_PLATE",
            "description": "将离心机的正对窗口的孔位的浓缩管转移至夹持工位，并开盖，后将试剂转移至酶标板的num号孔位（前提：离心机小门开着且放瓶子的孔位处于复位状态）",
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
    }
},
                "required": ["data", "num"]
            }
        },
        {
            "name": "start_microplate_reader",
            "description": "启动酶标仪，机械臂将酶标板夹进酶标仪进行测试",
            "parameters": {
                "type": "object",
                "properties": {
    "data": {
        "type": "string",
        "description": "data"
    },
    "temp": {
        "type": "string",
        "description": "temp"
    },
    "resultCode": {
        "type": "file",
        "description": "输出结果文件"
    }
},
                "required": ["data"]
            }
        },
        {
            "name": "blance",
            "description": "取瓶子加ml毫升水，配平后转移至离心机",
            "parameters": {
                "type": "object",
                "properties": {
    "data": {
        "type": "string",
        "description": "balance"
    },
    "ml": {
        "type": "int",
        "description": "ml"
    },
    "num": {
        "type": "int",
        "description": "num"
    }
},
                "required": ["data", "ml", "num"]
            }
        },
        {
            "name": "request",
            "description": "状态查询指令",
            "parameters": {
                "type": "object",
                "properties": {
    "data": {
        "type": "string",
        "description": "data"
    }
},
                "required": ["data"]
            }
        },
        {
            "name": "balance_to_out",
            "description": "将配平离心机的瓶子丢进回收口",
            "parameters": {
                "type": "object",
                "properties": {
    "data": {
        "type": "string",
        "description": "data"
    },
    "temp": {
        "type": "string",
        "description": "temp"
    }
},
                "required": ["data"]
            }
        },
        {
            "name": "ethyl_ether_to_N",
            "description": "将瓶子从乙醚工位转移至氮吹工位",
            "parameters": {
                "type": "object",
                "properties": {
    "data": {
        "type": "string",
        "description": "data"
    },
    "temp": {
        "type": "string",
        "description": "temp"
    }
},
                "required": ["data"]
            }
        },
        {
            "name": "N_to_ethyl_ether",
            "description": "将瓶子从氮吹工位转移至乙醚工位进行后续旋盖",
            "parameters": {
                "type": "object",
                "properties": {
    "data": {
        "type": "string",
        "description": "data"
    },
    "temp": {
        "type": "string",
        "description": "temp"
    }
},
                "required": ["data"]
            }
        },
        {
            "name": "add_water",
            "description": "注水溶解",
            "parameters": {
                "type": "object",
                "properties": {
    "data": {
        "type": "string",
        "description": "data"
    },
    "ml": {
        "type": "int",
        "description": "ml"
    }
},
                "required": ["data", "ml"]
            }
        },
        {
            "name": "Centrifuge_tubes_to_LC",
            "description": "从离心管仓储位置取一个瓶子放置到液相接样的第num个位置",
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
    }
},
                "required": ["data", "num"]
            }
        },
        {
            "name": "start_mass_spectrometer",
            "description": "启动质谱仪",
            "parameters": {
                "type": "object",
                "properties": {
    "data": {
        "type": "string",
        "description": "data"
    },
    "temp": {
        "type": "string",
        "description": "temp"
    },
    "resultCode": {
        "type": "file",
        "description": "输出结果文件"
    }
},
                "required": ["data", "resultCode"]
            }
        },
        {
            "name": "from_liquid_chromatography_to_mass_spectrometry",
            "description": "从液相色谱仪纯化后的num个瓶子转移到质谱仪的西林瓶中(num数量从request里的LC_num字段获取",
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
    }
},
                "required": ["data", "num"]
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
    }
},
                "required": ["data", "num"]
            }
        }
                    ]
                }
            }
        }
    }
    print(json.dumps(adv_message, ensure_ascii=False), flush=True)
    print(f"--- [proteins_Server] 多肽合成 is ready. ---", file=sys.stderr, flush=True)


if __name__ == "__main__":
    # 启动流程：先广播能力，再进入主循环
    proteins_server_advertise_capabilities()
    proteins_server_main_loop()
