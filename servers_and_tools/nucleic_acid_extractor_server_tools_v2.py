"""
nucleic_acid_extractor 统一能力工作站工具类
设备名称: 核酸提取仪
设备描述: 核酸提取仪是一种用于从生物样本中自动提取核酸（DNA 或 RNA）的设备。它利用磁珠法，通过自动化的操作流程，快速、高效地从样本中分离出纯净的核酸。在临床诊断、分子生物学研究等领域广泛应用。例如在新冠病毒检测中，核酸提取仪可以快速从咽拭子等样本中提取病毒核酸，为后续的核酸检测提供高质量的样本，提高检测效率和准确性。
生成时间: 2025-11-07 19:42:38
"""

class UnifiedWorkstationTools:
    """统一能力工作站工具管理器"""
    
    def tool_nucleic_acid_extractor(self, task_description: str, **params):
        """
        核酸提取仪 - 核酸提取仪是一种用于从生物样本中自动提取核酸（DNA 或 RNA）的设备。它利用磁珠法，通过自动化的操作流程，快速、高效地从样本中分离出纯净的核酸。在临床诊断、分子生物学研究等领域广泛应用。例如在新冠病毒检测中，核酸提取仪可以快速从咽拭子等样本中提取病毒核酸，为后续的核酸检测提供高质量的样本，提高检测效率和准确性。
        
        可用操作:
        - 获取方法列表 (getProcedureList): None
        - 获取当前使用的方法 (getCurrentProcedure): None
        - 设置当前使用的方法 (setCurrentProcedure): None
        - 启动方法 (startScanSample): None
        - 停止方法 (stopProcedure): None
        - 获取设备状态 (getState): None
        
        参数:
            task_description: 任务描述
            **params: 其他参数
        """
        # 根据任务描述执行相应的操作
        # 这里需要实现任务编排逻辑
        result = {
            "workstation": "核酸提取仪",
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
        "code": "getProcedureList",
        "id": 1897802271196178,
        "name": "获取方法列表",
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
                "defaultValue": "getProcedureList",
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
            "url": "/operate"
        }
    },
    {
        "code": "getCurrentProcedure",
        "id": 1897802271196179,
        "name": "获取当前使用的方法",
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
                "defaultValue": "getCurrentProcedure",
                "elementDataType": null,
                "flatten": false,
                "ioType": "CONSTANT",
                "noteCn": "",
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
            "url": "/operate"
        }
    },
    {
        "code": "setCurrentProcedure",
        "id": 1897802271228928,
        "name": "设置当前使用的方法",
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
                "defaultValue": "setCurrentProcedure",
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
                "bindDataType": null,
                "bindDataTypeProperty": null,
                "childParams": [],
                "constraintType": "ENUM",
                "constraintValue": "[{\"label\":\"DP713\",\"value\":\"DP713\"},{\"label\":\"test\",\"value\":\"test\"},{\"label\":\"磁吸测试\",\"value\":\"磁吸测试\"},{\"label\":\"DP802\",\"value\":\"DP802\"},{\"label\":\"DP802 副本\",\"value\":\"DP802 副本\"}]",
                "constraintValueEn": "",
                "dataType": "string",
                "defaultValue": null,
                "elementDataType": null,
                "flatten": false,
                "ioType": "INPUT",
                "noteCn": null,
                "noteEn": null,
                "paramCode": "Name",
                "paramName": "方法名称",
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
            "url": "/operate"
        }
    },
    {
        "code": "startScanSample",
        "id": 1897802271228929,
        "name": "启动方法",
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
                "defaultValue": "startScanSample",
                "elementDataType": null,
                "flatten": false,
                "ioType": "CONSTANT",
                "noteCn": "",
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
            "url": "/operate"
        }
    },
    {
        "code": "stopProcedure",
        "id": 1897802271228930,
        "name": "停止方法",
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
                "defaultValue": "stopProcedure",
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
            "url": "/operate"
        }
    },
    {
        "code": "getState",
        "id": 1897802271228931,
        "name": "获取设备状态",
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
                "defaultValue": "getState",
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
            "url": "/operate"
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
