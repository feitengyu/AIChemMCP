"""
ic 统一能力工作站工具类
设备名称: 离子色谱
设备描述: 离子色谱仪主要用于分离和检测溶液中的各种离子。它利用离子交换树脂对不同离子的亲和力差异，将混合溶液中的离子进行分离，然后通过检测器对分离后的离子进行定量分析。在环境监测等领域广泛应用。例如在环境水样检测中，可以检测水中的常见阴离子（如氯离子、硝酸根离子、硫酸根离子等）的含量，评估水质的污染程度；在食品检测中，可检测食品中的添加剂、营养成分等所含的离子。
生成时间: 2025-11-07 19:42:38
"""

class UnifiedWorkstationTools:
    """统一能力工作站工具管理器"""
    
    def tool_ic(self, task_description: str, **params):
        """
        离子色谱 - 离子色谱仪主要用于分离和检测溶液中的各种离子。它利用离子交换树脂对不同离子的亲和力差异，将混合溶液中的离子进行分离，然后通过检测器对分离后的离子进行定量分析。在环境监测等领域广泛应用。例如在环境水样检测中，可以检测水中的常见阴离子（如氯离子、硝酸根离子、硫酸根离子等）的含量，评估水质的污染程度；在食品检测中，可检测食品中的添加剂、营养成分等所含的离子。
        
        可用操作:
        - 样品下发 (ControlSample): 样品下发
        - 启动序列 (StartSequence): 启动序列
        - 获取结果 (ObtainResult): 获取结果
        - 结束序列 (StopSequence): 结束序列
        - 批量录入样品 (EntrySampleList): 批量录入样品
        - 批量下发样品 (SendSampleList): 批量下发样品
        - 获取结果（多个） (ObtainResultList): 获取结果（多个）
        - 等待就绪 (wait_device_ready): 等待就绪
        - 容器分配 (wait_loop): 
        
        参数:
            task_description: 任务描述
            **params: 其他参数
        """
        # 根据任务描述执行相应的操作
        # 这里需要实现任务编排逻辑
        result = {
            "workstation": "离子色谱",
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
        "code": "ControlSample",
        "id": 1897802271360012,
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
                "defaultValue": "ControlSample",
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
                "defaultValue": null,
                "elementDataType": "",
                "flatten": false,
                "ioType": "INPUT",
                "noteCn": null,
                "noteEn": null,
                "paramCode": "cup_position",
                "paramName": "仪器端杯位信息",
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
                "paramCode": "sample_code",
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
            }
        ],
        "recommend": null,
        "translator": "default",
        "translatorArgs": {
            "method": "POST",
            "url": "/ic/operate"
        }
    },
    {
        "code": "StartSequence",
        "id": 1897802271360013,
        "name": "启动序列",
        "noteCn": "启动序列",
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
                "defaultValue": "StartSequence",
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
            "url": "/ic/operate"
        }
    },
    {
        "code": "ObtainResult",
        "id": 1897802271360014,
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
                "defaultValue": "ObtainResult",
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
                "constraintType": null,
                "constraintValue": "",
                "constraintValueEn": "",
                "dataType": "string",
                "defaultValue": "",
                "elementDataType": null,
                "flatten": false,
                "ioType": "INPUT",
                "noteCn": null,
                "noteEn": null,
                "paramCode": "sample_code",
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
                "paramName": "测试结果",
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
            "url": "/ic/operate"
        }
    },
    {
        "code": "StopSequence",
        "id": 1897802271360015,
        "name": "结束序列",
        "noteCn": "结束序列",
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
                "defaultValue": "StopSequence",
                "elementDataType": null,
                "flatten": false,
                "ioType": "CONSTANT",
                "noteCn": null,
                "noteEn": null,
                "paramCode": "StopSequence",
                "paramName": "结束序列",
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
            "url": "/ic/operate"
        }
    },
    {
        "code": "EntrySampleList",
        "id": 1897802271360016,
        "name": "批量录入样品",
        "noteCn": "批量录入样品",
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
                "defaultValue": "EntrySampleList",
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
                        "constraintType": "RANGE",
                        "constraintValue": "(0,66]",
                        "constraintValueEn": "",
                        "dataType": "int",
                        "defaultValue": null,
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
                "defaultValue": "",
                "elementDataType": "object",
                "flatten": false,
                "ioType": "INPUT",
                "noteCn": null,
                "noteEn": null,
                "paramCode": "sample_info_list",
                "paramName": "样品信息列表",
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
            "url": "/ic/operate"
        }
    },
    {
        "code": "SendSampleList",
        "id": 1897802271360017,
        "name": "批量下发样品",
        "noteCn": "批量下发样品",
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
                "defaultValue": "SendSampleList",
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
            "url": "/ic/operate"
        }
    },
    {
        "code": "ObtainResultList",
        "id": 1897802271360018,
        "name": "获取结果（多个）",
        "noteCn": "获取结果（多个）",
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
                "defaultValue": "ObtainResultList",
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
            "url": "/ic/operate"
        }
    },
    {
        "code": "wait_device_ready",
        "id": 1897802271360019,
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
        "id": 1897802271360020,
        "name": "容器分配",
        "noteCn": "",
        "noteEn": null,
        "params": null,
        "recommend": null,
        "translator": "default",
        "translatorArgs": {
            "method": "POST",
            "url": "/ic/wait_loop"
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
