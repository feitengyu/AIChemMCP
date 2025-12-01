"""
spotting_workstation 统一能力工作站工具类
设备名称: 电化学-点样仪
设备描述: 自动点样仪主要用于将微量样品精确地点加到特定的载体上，如薄层色谱板、微孔板等。它可以按照预设的程序，控制点样的位置、体积和速度，实现高精度的点样操作。在生物分析中，可用于核酸杂交、蛋白质免疫印迹等实验的样品点样；在化学分析中，可用于薄层色谱分析的样品点样。自动点样仪提高了点样的准确性和重复性，减少了人工点样的误差，有利于提高实验结果的可靠性。
生成时间: 2025-11-07 19:42:38
"""

class UnifiedWorkstationTools:
    """统一能力工作站工具管理器"""
    
    def tool_spotting_workstation(self, task_description: str, **params):
        """
        电化学-点样仪 - 自动点样仪主要用于将微量样品精确地点加到特定的载体上，如薄层色谱板、微孔板等。它可以按照预设的程序，控制点样的位置、体积和速度，实现高精度的点样操作。在生物分析中，可用于核酸杂交、蛋白质免疫印迹等实验的样品点样；在化学分析中，可用于薄层色谱分析的样品点样。自动点样仪提高了点样的准确性和重复性，减少了人工点样的误差，有利于提高实验结果的可靠性。
        
        可用操作:
        - 开门 (opendoor): 开门
        - 关门 (closedoor): 关门
        - 点样实验 (start): 点样实验
        - 启动真空泵 (SlideLock): 启动真空泵
        - 关闭真空泵 (SlideUnLock): 关闭真空泵
        
        参数:
            task_description: 任务描述
            **params: 其他参数
        """
        # 根据任务描述执行相应的操作
        # 这里需要实现任务编排逻辑
        result = {
            "workstation": "电化学-点样仪",
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
        "code": "opendoor",
        "id": 1897802271654929,
        "name": "开门",
        "noteCn": "开门",
        "noteEn": "opendoor",
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
                "defaultValue": "DianYangYi",
                "elementDataType": null,
                "flatten": false,
                "ioType": "CONSTANT",
                "noteCn": "点样仪",
                "noteEn": null,
                "paramCode": "type",
                "paramName": "仪器类型",
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
                "defaultValue": "ScriptRun",
                "elementDataType": null,
                "flatten": false,
                "ioType": "CONSTANT",
                "noteCn": "运行脚本",
                "noteEn": null,
                "paramCode": "cmd",
                "paramName": "指令名称",
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
                "defaultValue": "OpenDoor",
                "elementDataType": null,
                "flatten": false,
                "ioType": "CONSTANT",
                "noteCn": "开门",
                "noteEn": null,
                "paramCode": "Name",
                "paramName": "脚本名称",
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
            "url": "/script/DianYangYi"
        }
    },
    {
        "code": "closedoor",
        "id": 1897802271654930,
        "name": "关门",
        "noteCn": "关门",
        "noteEn": "closedoor",
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
                "defaultValue": "DianYangYi",
                "elementDataType": null,
                "flatten": false,
                "ioType": "CONSTANT",
                "noteCn": "点样仪",
                "noteEn": null,
                "paramCode": "type",
                "paramName": "仪器类型",
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
                "defaultValue": "ScriptRun",
                "elementDataType": null,
                "flatten": false,
                "ioType": "CONSTANT",
                "noteCn": "运行脚本",
                "noteEn": null,
                "paramCode": "cmd",
                "paramName": "指令名称",
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
                "defaultValue": "CloseDoor",
                "elementDataType": null,
                "flatten": false,
                "ioType": "CONSTANT",
                "noteCn": "关门",
                "noteEn": null,
                "paramCode": "Name",
                "paramName": "脚本名称",
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
            "url": "/script/DianYangYi"
        }
    },
    {
        "code": "start",
        "id": 1897802271654931,
        "name": "点样实验",
        "noteCn": "点样实验",
        "noteEn": "start",
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
                "defaultValue": "DianYangYi",
                "elementDataType": null,
                "flatten": false,
                "ioType": "CONSTANT",
                "noteCn": "点样仪",
                "noteEn": null,
                "paramCode": "type",
                "paramName": "仪器类型",
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
                "defaultValue": "ScriptRun",
                "elementDataType": null,
                "flatten": false,
                "ioType": "CONSTANT",
                "noteCn": "运行脚本",
                "noteEn": null,
                "paramCode": "cmd",
                "paramName": "指令名称",
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
                "defaultValue": "experiment",
                "elementDataType": null,
                "flatten": false,
                "ioType": "CONSTANT",
                "noteCn": "实验",
                "noteEn": null,
                "paramCode": "Name",
                "paramName": "脚本名称",
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
                "ioType": "INPUT",
                "noteCn": null,
                "noteEn": null,
                "paramCode": "definitionParamUrl",
                "paramName": "配置文件路径",
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
            "url": "/script/DianYangYi"
        }
    },
    {
        "code": "SlideLock",
        "id": 1897802271654932,
        "name": "启动真空泵",
        "noteCn": "启动真空泵",
        "noteEn": "SlideLock",
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
                "defaultValue": "DianYangYi",
                "elementDataType": null,
                "flatten": false,
                "ioType": "CONSTANT",
                "noteCn": "点样仪",
                "noteEn": null,
                "paramCode": "type",
                "paramName": "仪器类型",
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
                "defaultValue": "ScriptRun",
                "elementDataType": null,
                "flatten": false,
                "ioType": "CONSTANT",
                "noteCn": "运行脚本",
                "noteEn": null,
                "paramCode": "cmd",
                "paramName": "指令名称",
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
                "defaultValue": "SlideLock",
                "elementDataType": null,
                "flatten": false,
                "ioType": "CONSTANT",
                "noteCn": "开门",
                "noteEn": null,
                "paramCode": "Name",
                "paramName": "脚本名称",
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
            "url": "/script/DianYangYi"
        }
    },
    {
        "code": "SlideUnLock",
        "id": 1897802271654933,
        "name": "关闭真空泵",
        "noteCn": "关闭真空泵",
        "noteEn": "SlideUnLock",
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
                "defaultValue": "DianYangYi",
                "elementDataType": null,
                "flatten": false,
                "ioType": "CONSTANT",
                "noteCn": "点样仪",
                "noteEn": null,
                "paramCode": "type",
                "paramName": "仪器类型",
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
                "defaultValue": "ScriptRun",
                "elementDataType": null,
                "flatten": false,
                "ioType": "CONSTANT",
                "noteCn": "运行脚本",
                "noteEn": null,
                "paramCode": "cmd",
                "paramName": "指令名称",
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
                "defaultValue": "SlideUnLock",
                "elementDataType": null,
                "flatten": false,
                "ioType": "CONSTANT",
                "noteCn": "开门",
                "noteEn": null,
                "paramCode": "Name",
                "paramName": "脚本名称",
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
            "url": "/script/DianYangYi"
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
