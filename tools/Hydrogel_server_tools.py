"""
Hydrogel 设备工具类
功能：定义设备所有动作的工具方法接口，需手动实现具体逻辑
生成时间：2025-04-18 13:44:36
"""

class ActionServerTools:
    """设备动作工具管理器：每个方法对应一个设备动作"""
    def tool_start(self, **params):
        """start（动作标识：start）- 需实现具体逻辑"""
        raise NotImplementedError(f"未实现 start(start) 的工具逻辑")
    def tool_getResult(self, **params):
        """getResult（动作标识：getResult）- 需实现具体逻辑"""
        raise NotImplementedError(f"未实现 getResult(getResult) 的工具逻辑")
