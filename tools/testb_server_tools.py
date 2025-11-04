"""
testb 设备工具类
功能：定义设备所有动作的工具方法接口，需手动实现具体逻辑
生成时间：2025-01-08 17:37:01
"""

class ActionServerTools:
    """设备动作工具管理器：每个方法对应一个设备动作"""
    def tool_dispensing(self, **params):
        """参数设置（动作标识：dispensing）- 需实现具体逻辑"""
        raise NotImplementedError(f"未实现 参数设置(dispensing) 的工具逻辑")
