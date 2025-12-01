"""
toLC 统一能力工作站工具类
设备名称: 色谱工作站
设备描述: 制备型液相色谱仪主要用于从复杂混合物中分离和制备大量的目标化合物。它具有较大的分离柱和较高的样品负载能力。在天然产物研究中，可从植物提取物等复杂样品中分离出具有生物活性的化合物，为药物研发提供足够量的纯品进行进一步的研究和开发。通过优化色谱条件，可以实现高纯度和高产量的目标化合物制备，满足科研和生产对大量纯化合物的需求。
生成时间: 2025-11-07 19:42:38
"""

class UnifiedWorkstationTools:
    """统一能力工作站工具管理器"""
    
    def tool_toLC(self, task_description: str, **params):
        """
        色谱工作站 - 制备型液相色谱仪主要用于从复杂混合物中分离和制备大量的目标化合物。它具有较大的分离柱和较高的样品负载能力。在天然产物研究中，可从植物提取物等复杂样品中分离出具有生物活性的化合物，为药物研发提供足够量的纯品进行进一步的研究和开发。通过优化色谱条件，可以实现高纯度和高产量的目标化合物制备，满足科研和生产对大量纯化合物的需求。
        
        可用操作:
        - 启动进样并开始液相色谱指令 (to_LC): None
        - 测试 (test): None
        - 从液相色谱仪纯化后的num个瓶子转移到质谱仪的西林瓶中 (from_liquid_chromatography_to_mass_spectrometry): None
        
        参数:
            task_description: 任务描述
            **params: 其他参数
        """
        # 根据任务描述执行相应的操作
        # 这里需要实现任务编排逻辑
        result = {
            "workstation": "色谱工作站",
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
        "code": "to_LC",
        "id": 1897802271261697,
        "name": "启动进样并开始液相色谱指令",
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
                "defaultValue": "to_LC",
                "elementDataType": null,
                "flatten": false,
                "ioType": "CONSTANT",
                "noteCn": null,
                "noteEn": null,
                "paramCode": "data",
                "paramName": "data",
                "property": null,
                "required": 1,
                "script": null,
                "selection": null,
                "selectorType": null,
                "timeFlag": 0,
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
                "defaultValue": "7",
                "elementDataType": "",
                "flatten": false,
                "ioType": "CONSTANT",
                "noteCn": null,
                "noteEn": null,
                "paramCode": "temp",
                "paramName": "temp",
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
                "paramCode": "resultCode",
                "paramName": "resultCode",
                "property": null,
                "required": 0,
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
                "noteCn": null,
                "noteEn": null,
                "paramCode": "usedTime",
                "paramName": "使用时长(s)",
                "property": null,
                "required": 0,
                "script": null,
                "selection": null,
                "selectorType": null,
                "timeFlag": 1,
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
                "dataType": "boolean",
                "defaultValue": "true",
                "elementDataType": "",
                "flatten": false,
                "ioType": "INPUT",
                "noteCn": null,
                "noteEn": null,
                "paramCode": "first",
                "paramName": "first",
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
            "url": "/send"
        }
    },
    {
        "code": "test",
        "id": 1897802271261698,
        "name": "测试",
        "noteCn": null,
        "noteEn": null,
        "params": null,
        "recommend": null,
        "translator": "default",
        "translatorArgs": {
            "method": "POST",
            "url": "/send"
        }
    },
    {
        "code": "from_liquid_chromatography_to_mass_spectrometry",
        "id": 1897802271261699,
        "name": "从液相色谱仪纯化后的num个瓶子转移到质谱仪的西林瓶中",
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
                "defaultValue": "from_liquid_chromatography_to_mass_spectrometry",
                "elementDataType": null,
                "flatten": false,
                "ioType": "CONSTANT",
                "noteCn": null,
                "noteEn": null,
                "paramCode": "data",
                "paramName": "data",
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
                "defaultValue": null,
                "elementDataType": "",
                "flatten": false,
                "ioType": "INPUT",
                "noteCn": null,
                "noteEn": null,
                "paramCode": "num",
                "paramName": "num",
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
                "defaultValue": "7",
                "elementDataType": "",
                "flatten": false,
                "ioType": "CONSTANT",
                "noteCn": null,
                "noteEn": null,
                "paramCode": "temp",
                "paramName": "temp",
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
            "url": "/send"
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
