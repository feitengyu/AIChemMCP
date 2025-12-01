"""
confecting_workstation 统一能力工作站工具类
设备名称: 电化学-配液仪
设备描述: 高通量自动配液仪能够快速、准确地配制不同浓度和体积的溶液。它可以按照预设的配方，自动吸取不同体积的试剂和溶剂，进行混合和稀释操作。在生物实验中，可用于配制细胞培养液、缓冲液等；在化学分析中，可用于配制标准溶液。相比于手动配液，自动配液仪具有更高的精度和重复性，能够同时处理多个样品，大大提高了配液的效率，适用于高通量的实验需求。
生成时间: 2025-11-07 19:42:38
"""

class UnifiedWorkstationTools:
    """统一能力工作站工具管理器"""
    
    def tool_confecting_workstation(self, task_description: str, **params):
        """
        电化学-配液仪 - 高通量自动配液仪能够快速、准确地配制不同浓度和体积的溶液。它可以按照预设的配方，自动吸取不同体积的试剂和溶剂，进行混合和稀释操作。在生物实验中，可用于配制细胞培养液、缓冲液等；在化学分析中，可用于配制标准溶液。相比于手动配液，自动配液仪具有更高的精度和重复性，能够同时处理多个样品，大大提高了配液的效率，适用于高通量的实验需求。
        
        可用操作:
        - 开门 (opendoor): 开门
        - 关门 (closedoor): 关门
        - 运行指定脚本 (start): 开始
        - 开门 (open): None
        - 关门 (close): None
        - 开始配液 (run): None
        - 强制上线 (online): 
        
        参数:
            task_description: 任务描述
            **params: 其他参数
        """
        # 根据任务描述执行相应的操作
        # 这里需要实现任务编排逻辑
        result = {
            "workstation": "电化学-配液仪",
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
        "id": 1897802271851530,
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
                "defaultValue": "PeiYeYi",
                "elementDataType": null,
                "flatten": false,
                "ioType": "CONSTANT",
                "noteCn": "配液仪",
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
                "paramName": "指令",
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
            "url": "/script/PeiYeYi"
        }
    },
    {
        "code": "closedoor",
        "id": 1897802271851531,
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
                "defaultValue": "PeiYeYi",
                "elementDataType": null,
                "flatten": false,
                "ioType": "CONSTANT",
                "noteCn": "配液仪",
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
                "paramName": "指令",
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
            "url": "/script/PeiYeYi"
        }
    },
    {
        "code": "start",
        "id": 1897802271851532,
        "name": "运行指定脚本",
        "noteCn": "开始",
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
                "defaultValue": "PeiYeYi",
                "elementDataType": null,
                "flatten": false,
                "ioType": "CONSTANT",
                "noteCn": "配液仪",
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
                "paramName": "指令",
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
                "noteCn": "脚本名称",
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
                "defaultValue": "",
                "elementDataType": "",
                "flatten": false,
                "ioType": "INPUT",
                "noteCn": null,
                "noteEn": null,
                "paramCode": "resultCode",
                "paramName": "配方文件",
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
            "url": "/script/PeiYeYi"
        }
    },
    {
        "code": "open",
        "id": 1897802271851533,
        "name": "开门",
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
                "defaultValue": "open",
                "elementDataType": null,
                "flatten": false,
                "ioType": "CONSTANT",
                "noteCn": null,
                "noteEn": null,
                "paramCode": "operation",
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
            }
        ],
        "recommend": null,
        "translator": "default",
        "translatorArgs": {
            "method": "POST",
            "url": "/command"
        }
    },
    {
        "code": "close",
        "id": 1897802271851534,
        "name": "关门",
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
                "defaultValue": "close",
                "elementDataType": null,
                "flatten": false,
                "ioType": "CONSTANT",
                "noteCn": null,
                "noteEn": null,
                "paramCode": "operation",
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
            }
        ],
        "recommend": null,
        "translator": "default",
        "translatorArgs": {
            "method": "POST",
            "url": "/command"
        }
    },
    {
        "code": "run",
        "id": 1897802271851535,
        "name": "开始配液",
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
                "defaultValue": "start",
                "elementDataType": null,
                "flatten": false,
                "ioType": "CONSTANT",
                "noteCn": null,
                "noteEn": null,
                "paramCode": "operation",
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
                "constraintType": "RANGE",
                "constraintValue": "[1,16]",
                "constraintValueEn": "",
                "dataType": "int",
                "defaultValue": "",
                "elementDataType": "",
                "flatten": false,
                "ioType": "INPUT",
                "noteCn": null,
                "noteEn": null,
                "paramCode": "file_num",
                "paramName": "需要加载文件数量",
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
                "defaultValue": "\"C:/Users/fuyi/Desktop/配液.zip\"",
                "elementDataType": "",
                "flatten": false,
                "ioType": "INPUT",
                "noteCn": null,
                "noteEn": null,
                "paramCode": "fileName",
                "paramName": "配液文件",
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
            "url": "/command"
        }
    },
    {
        "code": "online",
        "id": 1897802271851536,
        "name": "强制上线",
        "noteCn": "",
        "noteEn": null,
        "params": null,
        "recommend": null,
        "translator": "default",
        "translatorArgs": {
            "method": "GET",
            "url": "/online"
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
