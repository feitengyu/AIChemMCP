"""
flow_inj 统一能力工作站工具类
设备名称: 流动注射仪
设备描述: SUPEC 5011流动注射分析系统主要适用于饮用水、地表水、地下水生活污水和工业废水中硫化物的分析。其中，使用亚甲基蓝分光光度法的测定范围为0.016mg/L~2.00mg/L，检出限为0.004mg/L(以S2-计)。
其工作原理为：在封闭的管路中，将一定体积的样品注射到一个流动的、无空气间隔的连续载流中，样品与试剂在分析模块中按选定的顺序和比例混合、反应，在非完全反应的条件下，进入流动检测池进行光度检测，定量测定样品中被测物质的含量。
其性能优势在于：便携性：体积小，重量轻，方便携带；灵动性：仪器可搭配不同型号的自动进样器，应用于常规实验室；同时配合便携箱，用于现场应急监测。实现批量自动、在线连续检测。
生成时间: 2025-11-07 19:42:38
"""

class UnifiedWorkstationTools:
    """统一能力工作站工具管理器"""
    
    def tool_flow_inj(self, task_description: str, **params):
        """
        流动注射仪 - SUPEC 5011流动注射分析系统主要适用于饮用水、地表水、地下水生活污水和工业废水中硫化物的分析。其中，使用亚甲基蓝分光光度法的测定范围为0.016mg/L~2.00mg/L，检出限为0.004mg/L(以S2-计)。
其工作原理为：在封闭的管路中，将一定体积的样品注射到一个流动的、无空气间隔的连续载流中，样品与试剂在分析模块中按选定的顺序和比例混合、反应，在非完全反应的条件下，进入流动检测池进行光度检测，定量测定样品中被测物质的含量。
其性能优势在于：便携性：体积小，重量轻，方便携带；灵动性：仪器可搭配不同型号的自动进样器，应用于常规实验室；同时配合便携箱，用于现场应急监测。实现批量自动、在线连续检测。
        
        可用操作:
        - 启动测样 (start_flow_injection): 启动测样
        - 样品下发 (sample_issuse): 样品下发
        - 结束测样 (stop_flow_injection): 结束测样
        - 获取结果 (obtain_result): 获取结果
        - 清空样品列表 (clear_sample_list): 清空样品列表
        - 批量录入样品信息 (enter_sample_info): 批量录入样品信息
        - 批量下发样品 (send_sample_list): 批量下发样品
        - 等待就绪 (wait_device_ready): 等待就绪
        - 容器分配 (wait_loop): 
        
        参数:
            task_description: 任务描述
            **params: 其他参数
        """
        # 根据任务描述执行相应的操作
        # 这里需要实现任务编排逻辑
        result = {
            "workstation": "流动注射仪",
            "task": task_description,
            "status": "pending_implementation",
            "message": "任务编排功能待实现 - 需要根据任务描述解析并执行相应的动作序列"
        }
        
        # 简单的任务匹配逻辑
        task_lower = task_description.lower()
        
        # 尝试匹配已有的动作
        matched_actions = []
        actions_list = [
    {
        "code": "start_flow_injection",
        "id": 1897802271163392,
        "name": "启动测样",
        "noteCn": "启动测样",
        "noteEn": null,
        "params": [
            {
                "advanced": null,
                "bindDataType": null,
                "bindDataTypeProperty": null,
                "childParams": [],
                "constraintType": null,
                "constraintValue": "",
                "constraintValueEn": "",
                "dataType": "string",
                "defaultValue": "start_flow_injection",
                "elementDataType": null,
                "flatten": false,
                "ioType": "CONSTANT",
                "noteCn": null,
                "noteEn": null,
                "paramCode": "operate",
                "paramName": "指令编码",
                "property": null,
                "required": 1,
                "script": null,
                "selection": null,
                "selectorType": null,
                "timeFlag": null,
                "unitTypeCode": null,
                "unitTypeName": null,
                "value": null
            }
        ],
        "recommend": null,
        "translator": "default",
        "translatorArgs": {
            "method": "POST",
            "url": "/flow/operate"
        }
    },
    {
        "code": "sample_issuse",
        "id": 1897802271163393,
        "name": "样品下发",
        "noteCn": "样品下发",
        "noteEn": null,
        "params": [
            {
                "advanced": null,
                "bindDataType": null,
                "bindDataTypeProperty": null,
                "childParams": [],
                "constraintType": null,
                "constraintValue": "",
                "constraintValueEn": "",
                "dataType": "string",
                "defaultValue": "sample_issuse",
                "elementDataType": null,
                "flatten": false,
                "ioType": "CONSTANT",
                "noteCn": null,
                "noteEn": null,
                "paramCode": "operate",
                "paramName": "指令编码",
                "property": null,
                "required": 1,
                "script": null,
                "selection": null,
                "selectorType": null,
                "timeFlag": null,
                "unitTypeCode": null,
                "unitTypeName": null,
                "value": null
            },
            {
                "advanced": null,
                "bindDataType": "",
                "bindDataTypeProperty": null,
                "childParams": [],
                "constraintType": null,
                "constraintValue": "",
                "constraintValueEn": "",
                "dataType": "int",
                "defaultValue": "",
                "elementDataType": "",
                "flatten": false,
                "ioType": "INPUT",
                "noteCn": "",
                "noteEn": null,
                "paramCode": "action_type",
                "paramName": "1：增加样品 2：删除样品",
                "property": null,
                "required": 1,
                "script": null,
                "selection": null,
                "selectorType": null,
                "timeFlag": null,
                "unitTypeCode": null,
                "unitTypeName": null,
                "value": null
            },
            {
                "advanced": null,
                "bindDataType": "",
                "bindDataTypeProperty": null,
                "childParams": [],
                "constraintType": null,
                "constraintValue": "[1,66]",
                "constraintValueEn": "",
                "dataType": "int",
                "defaultValue": null,
                "elementDataType": "",
                "flatten": false,
                "ioType": "INPUT",
                "noteCn": null,
                "noteEn": null,
                "paramCode": "hole_num",
                "paramName": "孔位",
                "property": null,
                "required": 1,
                "script": null,
                "selection": null,
                "selectorType": null,
                "timeFlag": null,
                "unitTypeCode": null,
                "unitTypeName": null,
                "value": null
            },
            {
                "advanced": null,
                "bindDataType": null,
                "bindDataTypeProperty": null,
                "childParams": [],
                "constraintType": null,
                "constraintValue": "",
                "constraintValueEn": "",
                "dataType": "string",
                "defaultValue": null,
                "elementDataType": null,
                "flatten": false,
                "ioType": "INPUT",
                "noteCn": null,
                "noteEn": null,
                "paramCode": "sample_no",
                "paramName": "样品编号(唯一标识不可重复)",
                "property": null,
                "required": 1,
                "script": null,
                "selection": null,
                "selectorType": null,
                "timeFlag": null,
                "unitTypeCode": null,
                "unitTypeName": null,
                "value": null
            },
            {
                "advanced": null,
                "bindDataType": null,
                "bindDataTypeProperty": null,
                "childParams": [],
                "constraintType": null,
                "constraintValue": "",
                "constraintValueEn": "",
                "dataType": "string",
                "defaultValue": null,
                "elementDataType": null,
                "flatten": false,
                "ioType": "INPUT",
                "noteCn": null,
                "noteEn": null,
                "paramCode": "sample_name",
                "paramName": "样品名称",
                "property": null,
                "required": 1,
                "script": null,
                "selection": null,
                "selectorType": null,
                "timeFlag": null,
                "unitTypeCode": null,
                "unitTypeName": null,
                "value": null
            },
            {
                "advanced": null,
                "bindDataType": "",
                "bindDataTypeProperty": null,
                "childParams": [],
                "constraintType": "ENUM",
                "constraintValue": "[{\"label\":\"未知样\",\"value\":1},{\"label\":\"水样\",\"value\":2},{\"label\":\"标样\",\"value\":3},{\"label\":\"空白样\",\"value\":4},{\"label\":\"质控样\",\"value\":5},{\"label\":\"平行样\",\"value\":6},{\"label\":\"加标回收样\",\"value\":7},{\"label\":\"校准点核查样\",\"value\":8}]",
                "constraintValueEn": "",
                "dataType": "int",
                "defaultValue": null,
                "elementDataType": "",
                "flatten": false,
                "ioType": "INPUT",
                "noteCn": null,
                "noteEn": null,
                "paramCode": "sample_type",
                "paramName": "样品类型",
                "property": null,
                "required": 1,
                "script": null,
                "selection": null,
                "selectorType": null,
                "timeFlag": null,
                "unitTypeCode": null,
                "unitTypeName": null,
                "value": null
            },
            {
                "advanced": null,
                "bindDataType": null,
                "bindDataTypeProperty": null,
                "childParams": [],
                "constraintType": null,
                "constraintValue": "",
                "constraintValueEn": "",
                "dataType": "string",
                "defaultValue": "w21019",
                "elementDataType": null,
                "flatten": false,
                "ioType": "CONSTANT",
                "noteCn": null,
                "noteEn": null,
                "paramCode": "factor_code",
                "paramName": "因子名称",
                "property": null,
                "required": 1,
                "script": null,
                "selection": null,
                "selectorType": null,
                "timeFlag": null,
                "unitTypeCode": null,
                "unitTypeName": null,
                "value": null
            }
        ],
        "recommend": null,
        "translator": "default",
        "translatorArgs": {
            "method": "POST",
            "url": "/flow/operate"
        }
    },
    {
        "code": "stop_flow_injection",
        "id": 1897802271163394,
        "name": "结束测样",
        "noteCn": "结束测样",
        "noteEn": null,
        "params": [
            {
                "advanced": null,
                "bindDataType": null,
                "bindDataTypeProperty": null,
                "childParams": [],
                "constraintType": null,
                "constraintValue": "",
                "constraintValueEn": "",
                "dataType": "string",
                "defaultValue": "stop_flow_injection",
                "elementDataType": null,
                "flatten": false,
                "ioType": "CONSTANT",
                "noteCn": null,
                "noteEn": null,
                "paramCode": "operate",
                "paramName": "指令编码",
                "property": null,
                "required": 1,
                "script": null,
                "selection": null,
                "selectorType": null,
                "timeFlag": null,
                "unitTypeCode": null,
                "unitTypeName": null,
                "value": null
            }
        ],
        "recommend": null,
        "translator": "default",
        "translatorArgs": {
            "method": "POST",
            "url": "/flow/operate"
        }
    },
    {
        "code": "obtain_result",
        "id": 1897802271163395,
        "name": "获取结果",
        "noteCn": "获取结果",
        "noteEn": null,
        "params": [
            {
                "advanced": null,
                "bindDataType": null,
                "bindDataTypeProperty": null,
                "childParams": [],
                "constraintType": null,
                "constraintValue": "",
                "constraintValueEn": "",
                "dataType": "string",
                "defaultValue": "obtain_result",
                "elementDataType": null,
                "flatten": false,
                "ioType": "CONSTANT",
                "noteCn": null,
                "noteEn": null,
                "paramCode": "operate",
                "paramName": "指令编码",
                "property": null,
                "required": 1,
                "script": null,
                "selection": null,
                "selectorType": null,
                "timeFlag": null,
                "unitTypeCode": null,
                "unitTypeName": null,
                "value": null
            },
            {
                "advanced": null,
                "bindDataType": "",
                "bindDataTypeProperty": null,
                "childParams": [],
                "constraintType": null,
                "constraintValue": "",
                "constraintValueEn": "",
                "dataType": "file",
                "defaultValue": null,
                "elementDataType": "",
                "flatten": false,
                "ioType": "OUTPUT",
                "noteCn": null,
                "noteEn": null,
                "paramCode": "result",
                "paramName": "测量结果",
                "property": null,
                "required": 1,
                "script": null,
                "selection": null,
                "selectorType": null,
                "timeFlag": null,
                "unitTypeCode": null,
                "unitTypeName": null,
                "value": null
            }
        ],
        "recommend": null,
        "translator": "default",
        "translatorArgs": {
            "method": "POST",
            "url": "/flow/operate"
        }
    },
    {
        "code": "clear_sample_list",
        "id": 1897802271163396,
        "name": "清空样品列表",
        "noteCn": "清空样品列表",
        "noteEn": null,
        "params": [
            {
                "advanced": null,
                "bindDataType": null,
                "bindDataTypeProperty": null,
                "childParams": [],
                "constraintType": null,
                "constraintValue": "",
                "constraintValueEn": "",
                "dataType": "string",
                "defaultValue": "clear_sample_list",
                "elementDataType": null,
                "flatten": false,
                "ioType": "CONSTANT",
                "noteCn": null,
                "noteEn": null,
                "paramCode": "operate",
                "paramName": "指令编码",
                "property": null,
                "required": 1,
                "script": null,
                "selection": null,
                "selectorType": null,
                "timeFlag": null,
                "unitTypeCode": null,
                "unitTypeName": null,
                "value": null
            }
        ],
        "recommend": null,
        "translator": "default",
        "translatorArgs": {
            "method": "POST",
            "url": "/flow/operate"
        }
    },
    {
        "code": "enter_sample_info",
        "id": 1897802271163397,
        "name": "批量录入样品信息",
        "noteCn": "批量录入样品信息",
        "noteEn": "",
        "params": [
            {
                "advanced": null,
                "bindDataType": null,
                "bindDataTypeProperty": null,
                "childParams": [],
                "constraintType": null,
                "constraintValue": "",
                "constraintValueEn": "",
                "dataType": "string",
                "defaultValue": "enter_sample_info",
                "elementDataType": null,
                "flatten": false,
                "ioType": "CONSTANT",
                "noteCn": null,
                "noteEn": null,
                "paramCode": "operate",
                "paramName": "批量录入样品信息",
                "property": null,
                "required": 1,
                "script": null,
                "selection": null,
                "selectorType": null,
                "timeFlag": null,
                "unitTypeCode": null,
                "unitTypeName": null,
                "value": null
            },
            {
                "advanced": null,
                "bindDataType": "",
                "bindDataTypeProperty": null,
                "childParams": [
                    {
                        "advanced": null,
                        "bindDataType": null,
                        "bindDataTypeProperty": null,
                        "childParams": null,
                        "constraintType": null,
                        "constraintValue": "",
                        "constraintValueEn": "",
                        "dataType": "string",
                        "defaultValue": null,
                        "elementDataType": null,
                        "flatten": false,
                        "ioType": "INPUT",
                        "noteCn": null,
                        "noteEn": null,
                        "paramCode": "sample_no",
                        "paramName": "样品编码",
                        "property": null,
                        "required": 1,
                        "script": null,
                        "selection": null,
                        "selectorType": null,
                        "timeFlag": null,
                        "unitTypeCode": null,
                        "unitTypeName": null,
                        "value": null
                    },
                    {
                        "advanced": null,
                        "bindDataType": null,
                        "bindDataTypeProperty": null,
                        "childParams": null,
                        "constraintType": null,
                        "constraintValue": "",
                        "constraintValueEn": "",
                        "dataType": "string",
                        "defaultValue": null,
                        "elementDataType": null,
                        "flatten": false,
                        "ioType": "INPUT",
                        "noteCn": null,
                        "noteEn": null,
                        "paramCode": "sample_name",
                        "paramName": "样品名称",
                        "property": null,
                        "required": 1,
                        "script": null,
                        "selection": null,
                        "selectorType": null,
                        "timeFlag": null,
                        "unitTypeCode": null,
                        "unitTypeName": null,
                        "value": null
                    },
                    {
                        "advanced": null,
                        "bindDataType": null,
                        "bindDataTypeProperty": null,
                        "childParams": null,
                        "constraintType": "ENUM",
                        "constraintValue": "[{\"label\":\"未知样\",\"value\":1},{\"label\":\"水样\",\"value\":2},{\"label\":\"标样\",\"value\":3},{\"label\":\"空白样\",\"value\":4},{\"label\":\"质控样\",\"value\":5},{\"label\":\"平行样\",\"value\":6},{\"label\":\"加标回收样\",\"value\":7},{\"label\":\"校准点核查样\",\"value\":8}]",
                        "constraintValueEn": "",
                        "dataType": "int",
                        "defaultValue": "2",
                        "elementDataType": null,
                        "flatten": false,
                        "ioType": "INPUT",
                        "noteCn": null,
                        "noteEn": null,
                        "paramCode": "sample_type",
                        "paramName": "样品类型",
                        "property": null,
                        "required": 1,
                        "script": null,
                        "selection": null,
                        "selectorType": null,
                        "timeFlag": null,
                        "unitTypeCode": null,
                        "unitTypeName": null,
                        "value": null
                    },
                    {
                        "advanced": null,
                        "bindDataType": null,
                        "bindDataTypeProperty": null,
                        "childParams": null,
                        "constraintType": null,
                        "constraintValue": "",
                        "constraintValueEn": "",
                        "dataType": "string",
                        "defaultValue": "w21019",
                        "elementDataType": null,
                        "flatten": false,
                        "ioType": "CONSTANT",
                        "noteCn": null,
                        "noteEn": null,
                        "paramCode": "factor_code",
                        "paramName": "因子编码",
                        "property": null,
                        "required": 1,
                        "script": null,
                        "selection": null,
                        "selectorType": null,
                        "timeFlag": null,
                        "unitTypeCode": null,
                        "unitTypeName": null,
                        "value": null
                    },
                    {
                        "advanced": null,
                        "bindDataType": null,
                        "bindDataTypeProperty": null,
                        "childParams": null,
                        "constraintType": "RANGE",
                        "constraintValue": "(0,66]",
                        "constraintValueEn": "",
                        "dataType": "int",
                        "defaultValue": "",
                        "elementDataType": null,
                        "flatten": false,
                        "ioType": "INPUT",
                        "noteCn": null,
                        "noteEn": null,
                        "paramCode": "slot_num",
                        "paramName": "孔位",
                        "property": null,
                        "required": 0,
                        "script": null,
                        "selection": null,
                        "selectorType": null,
                        "timeFlag": null,
                        "unitTypeCode": null,
                        "unitTypeName": null,
                        "value": null
                    }
                ],
                "constraintType": null,
                "constraintValue": "",
                "constraintValueEn": "",
                "dataType": "array",
                "defaultValue": null,
                "elementDataType": "object",
                "flatten": false,
                "ioType": "INPUT",
                "noteCn": null,
                "noteEn": null,
                "paramCode": "sample_info_list",
                "paramName": "样品信息列表",
                "property": null,
                "required": 0,
                "script": null,
                "selection": null,
                "selectorType": null,
                "timeFlag": null,
                "unitTypeCode": null,
                "unitTypeName": null,
                "value": null
            }
        ],
        "recommend": null,
        "translator": "default",
        "translatorArgs": {
            "method": "POST",
            "url": "/flow/operate"
        }
    },
    {
        "code": "send_sample_list",
        "id": 1897802271163398,
        "name": "批量下发样品",
        "noteCn": "批量下发样品",
        "noteEn": "",
        "params": [
            {
                "advanced": null,
                "bindDataType": null,
                "bindDataTypeProperty": null,
                "childParams": [],
                "constraintType": null,
                "constraintValue": "",
                "constraintValueEn": "",
                "dataType": "string",
                "defaultValue": "send_sample_list",
                "elementDataType": null,
                "flatten": false,
                "ioType": "CONSTANT",
                "noteCn": null,
                "noteEn": null,
                "paramCode": "operate",
                "paramName": "批量下发样品",
                "property": null,
                "required": 1,
                "script": null,
                "selection": null,
                "selectorType": null,
                "timeFlag": null,
                "unitTypeCode": null,
                "unitTypeName": null,
                "value": null
            }
        ],
        "recommend": null,
        "translator": "default",
        "translatorArgs": {
            "method": "POST",
            "url": "/flow/operate"
        }
    },
    {
        "code": "wait_device_ready",
        "id": 1897802271163399,
        "name": "等待就绪",
        "noteCn": "等待就绪",
        "noteEn": null,
        "params": null,
        "recommend": null,
        "translator": "default",
        "translatorArgs": {
            "method": "POST",
            "url": "/wait_device_ready"
        }
    },
    {
        "code": "wait_loop",
        "id": 1897802271163400,
        "name": "容器分配",
        "noteCn": "",
        "noteEn": null,
        "params": null,
        "recommend": null,
        "translator": "default",
        "translatorArgs": {
            "method": "POST",
            "url": "/flow/wait_loop"
        }
    }
]
        
        for action in actions_list:
            action_name = action.get("name", "")
            action_code = action.get("code", "")
            if (action_name and action_name.lower() in task_lower) or (action_code and action_code.lower() in task_lower):
                matched_actions.append({
                    "action_name": action_name,
                    "action_code": action_code,
                    "description": action.get("noteCn", "")
                })
        
        if matched_actions:
            result["matched_actions"] = matched_actions
            result["message"] = f"识别到 {len(matched_actions)} 个相关操作，请完善任务编排逻辑"
        
        return result
