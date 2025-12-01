"""
ultrasonic_cleaning 统一能力工作站工具类
设备名称: 超声清洗
设备描述: 超声波处理工作站利用超声波的空化效应、机械效应等对样品进行处理。超声波在液体中传播时产生的微小气泡的形成和破裂，能够产生强大的冲击力和剪切力，可用于细胞破碎、样品分散、加速化学反应等。在生物、化学等实验中有着广泛应用。例如在生物样品处理中，可用于提取细胞内的蛋白质、核酸等生物大分子；在化学合成中，能够加速反应速率，提高反应产率。
生成时间: 2025-11-07 19:42:38
"""

class UnifiedWorkstationTools:
    """统一能力工作站工具管理器"""
    
    def tool_ultrasonic_cleaning(self, task_description: str, **params):
        """
        超声清洗 - 超声波处理工作站利用超声波的空化效应、机械效应等对样品进行处理。超声波在液体中传播时产生的微小气泡的形成和破裂，能够产生强大的冲击力和剪切力，可用于细胞破碎、样品分散、加速化学反应等。在生物、化学等实验中有着广泛应用。例如在生物样品处理中，可用于提取细胞内的蛋白质、核酸等生物大分子；在化学合成中，能够加速反应速率，提高反应产率。
        
        可用操作:
        - 加水 (add-water): None
        - 排水 (drain-water): None
        - 开启超声清洗 (start_clean): None
        - 停⽌超声清洗 (stop_clean): None
        - 开启加热 (open-heat): None
        - 停⽌加热 (close-heat): None
        
        参数:
            task_description: 任务描述
            **params: 其他参数
        """
        # 根据任务描述执行相应的操作
        # 这里需要实现任务编排逻辑
        result = {
            "workstation": "超声清洗",
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
        "code": "add-water",
        "id": 1897802271425540,
        "name": "加水",
        "noteCn": null,
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
                "defaultValue": "add-water",
                "elementDataType": null,
                "flatten": false,
                "ioType": "CONSTANT",
                "noteCn": null,
                "noteEn": null,
                "paramCode": "op",
                "paramName": "操作符",
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
                "defaultValue": "30",
                "elementDataType": "",
                "flatten": false,
                "ioType": "INPUT",
                "noteCn": "",
                "noteEn": null,
                "paramCode": "value",
                "paramName": "加水时间",
                "property": null,
                "required": 1,
                "script": null,
                "selection": null,
                "selectorType": null,
                "timeFlag": null,
                "unitTypeCode": "s",
                "unitTypeName": "秒",
                "value": null
            }
        ],
        "recommend": null,
        "translator": "default",
        "translatorArgs": {
            "method": "POST",
            "url": "/cmd"
        }
    },
    {
        "code": "drain-water",
        "id": 1897802271425541,
        "name": "排水",
        "noteCn": null,
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
                "defaultValue": "drain-water",
                "elementDataType": null,
                "flatten": false,
                "ioType": "CONSTANT",
                "noteCn": null,
                "noteEn": null,
                "paramCode": "op",
                "paramName": "操作符",
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
                "defaultValue": "30",
                "elementDataType": "",
                "flatten": false,
                "ioType": "INPUT",
                "noteCn": null,
                "noteEn": null,
                "paramCode": "value",
                "paramName": "排水时间",
                "property": null,
                "required": 1,
                "script": null,
                "selection": null,
                "selectorType": null,
                "timeFlag": null,
                "unitTypeCode": "s",
                "unitTypeName": "秒",
                "value": null
            }
        ],
        "recommend": null,
        "translator": "default",
        "translatorArgs": {
            "method": "POST",
            "url": "/cmd"
        }
    },
    {
        "code": "start_clean",
        "id": 1897802271425542,
        "name": "开启超声清洗",
        "noteCn": null,
        "noteEn": null,
        "params": [
            {
                "advanced": null,
                "bindDataType": "",
                "bindDataTypeProperty": null,
                "childParams": [],
                "constraintType": null,
                "constraintValue": "",
                "constraintValueEn": "",
                "dataType": "int",
                "defaultValue": "30",
                "elementDataType": "",
                "flatten": false,
                "ioType": "INPUT",
                "noteCn": "",
                "noteEn": "",
                "paramCode": "value",
                "paramName": "清洗时间",
                "property": null,
                "required": 1,
                "script": null,
                "selection": null,
                "selectorType": null,
                "timeFlag": null,
                "unitTypeCode": "s",
                "unitTypeName": "秒",
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
                "defaultValue": "start",
                "elementDataType": null,
                "flatten": false,
                "ioType": "CONSTANT",
                "noteCn": null,
                "noteEn": null,
                "paramCode": "op",
                "paramName": "操作",
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
            "url": "/cmd"
        }
    },
    {
        "code": "stop_clean",
        "id": 1897802271425543,
        "name": "停⽌超声清洗",
        "noteCn": null,
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
                "defaultValue": "stop",
                "elementDataType": null,
                "flatten": false,
                "ioType": "CONSTANT",
                "noteCn": null,
                "noteEn": null,
                "paramCode": "op",
                "paramName": "操作符",
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
                "defaultValue": "1",
                "elementDataType": "",
                "flatten": false,
                "ioType": "CONSTANT",
                "noteCn": null,
                "noteEn": null,
                "paramCode": "value",
                "paramName": "数值",
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
            "url": "/cmd"
        }
    },
    {
        "code": "open-heat",
        "id": 1897802271425544,
        "name": "开启加热",
        "noteCn": null,
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
                "defaultValue": "open-heat",
                "elementDataType": null,
                "flatten": false,
                "ioType": "CONSTANT",
                "noteCn": "",
                "noteEn": null,
                "paramCode": "op",
                "paramName": "操作符",
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
                "defaultValue": "30",
                "elementDataType": "",
                "flatten": false,
                "ioType": "INPUT",
                "noteCn": null,
                "noteEn": null,
                "paramCode": "value",
                "paramName": "数值",
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
            "url": "/cmd"
        }
    },
    {
        "code": "close-heat",
        "id": 1897802271425545,
        "name": "停⽌加热",
        "noteCn": null,
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
                "defaultValue": "close-heat",
                "elementDataType": null,
                "flatten": false,
                "ioType": "CONSTANT",
                "noteCn": null,
                "noteEn": null,
                "paramCode": "op",
                "paramName": "操作符",
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
                "defaultValue": "1",
                "elementDataType": "",
                "flatten": false,
                "ioType": "CONSTANT",
                "noteCn": null,
                "noteEn": null,
                "paramCode": "value",
                "paramName": "数值",
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
            "url": "/cmd"
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
