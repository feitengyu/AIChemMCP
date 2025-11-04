"""
tensiometer 设备工具类
功能：定义设备所有动作的工具方法接口，需手动实现具体逻辑
生成时间：2025-07-07 16:45:49
"""

class ActionServerTools:
    """设备动作工具管理器：每个方法对应一个设备动作"""
    def tool_movingSampleA(self, **params):
        """移动样品到张力仪（动作标识：movingSampleA）- 需实现具体逻辑"""
        raise NotImplementedError(f"未实现 移动样品到张力仪(movingSampleA) 的工具逻辑")
    def tool_performAdhesionTest(self, **params):
        """测量粘附力（废弃）（动作标识：performAdhesionTest）- 需实现具体逻辑"""
        raise NotImplementedError(f"未实现 测量粘附力（废弃）(performAdhesionTest) 的工具逻辑")
    def tool_tensionerMaterialCollection(self, **params):
        """机械臂去张力仪取料（动作标识：tensionerMaterialCollection）- 需实现具体逻辑"""
        raise NotImplementedError(f"未实现 机械臂去张力仪取料(tensionerMaterialCollection) 的工具逻辑")
    def tool_putTurntable(self, **params):
        """机械臂请求到中转台碳纸放在电解池转台上（动作标识：putTurntable）- 需实现具体逻辑"""
        raise NotImplementedError(f"未实现 机械臂请求到中转台碳纸放在电解池转台上(putTurntable) 的工具逻辑")
    def tool_rotate(self, **params):
        """电解池转台旋转一格（动作标识：rotate）- 需实现具体逻辑"""
        raise NotImplementedError(f"未实现 电解池转台旋转一格(rotate) 的工具逻辑")
    def tool_measuringAdhesion2(self, **params):
        """测量粘附力（动作标识：measuringAdhesion2）- 需实现具体逻辑"""
        raise NotImplementedError(f"未实现 测量粘附力(measuringAdhesion2) 的工具逻辑")
    def tool_getTemplateList(self, **params):
        """获取模版列表（动作标识：getTemplateList）- 需实现具体逻辑"""
        raise NotImplementedError(f"未实现 获取模版列表(getTemplateList) 的工具逻辑")
