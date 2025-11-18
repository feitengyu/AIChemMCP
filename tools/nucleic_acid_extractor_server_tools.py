"""
nucleic_acid_extractor 设备工具类
功能：定义设备所有动作的工具方法接口，需手动实现具体逻辑
生成时间：2025-11-07 19:42:38
"""

class ActionServerTools:
    """设备动作工具管理器：每个方法对应一个设备动作"""
    def tool_getProcedureList(self, **params):
        """获取方法列表（动作标识：getProcedureList）- 需实现具体逻辑"""
        raise NotImplementedError(f"未实现 获取方法列表(getProcedureList) 的工具逻辑")
    def tool_getCurrentProcedure(self, **params):
        """获取当前使用的方法（动作标识：getCurrentProcedure）- 需实现具体逻辑"""
        raise NotImplementedError(f"未实现 获取当前使用的方法(getCurrentProcedure) 的工具逻辑")
    def tool_setCurrentProcedure(self, **params):
        """设置当前使用的方法（动作标识：setCurrentProcedure）- 需实现具体逻辑"""
        raise NotImplementedError(f"未实现 设置当前使用的方法(setCurrentProcedure) 的工具逻辑")
    def tool_startScanSample(self, **params):
        """启动方法（动作标识：startScanSample）- 需实现具体逻辑"""
        raise NotImplementedError(f"未实现 启动方法(startScanSample) 的工具逻辑")
    def tool_stopProcedure(self, **params):
        """停止方法（动作标识：stopProcedure）- 需实现具体逻辑"""
        raise NotImplementedError(f"未实现 停止方法(stopProcedure) 的工具逻辑")
    def tool_getState(self, **params):
        """获取设备状态（动作标识：getState）- 需实现具体逻辑"""
        raise NotImplementedError(f"未实现 获取设备状态(getState) 的工具逻辑")
