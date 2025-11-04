"""
furnace_workstation 设备工具类
功能：定义设备所有动作的工具方法接口，需手动实现具体逻辑
生成时间：2025-08-13 10:05:28
"""

class ActionServerTools:
    """设备动作工具管理器：每个方法对应一个设备动作"""
    def tool_start(self, **params):
        """流程开始（动作标识：start）- 需实现具体逻辑"""
        raise NotImplementedError(f"未实现 流程开始(start) 的工具逻辑")
    def tool_start_new(self, **params):
        """流程开始（只做3个位置）（动作标识：start_new）- 需实现具体逻辑"""
        raise NotImplementedError(f"未实现 流程开始（只做3个位置）(start_new) 的工具逻辑")
