"""
spraying_workstation 设备工具类
功能：定义设备所有动作的工具方法接口，需手动实现具体逻辑
生成时间：2025-09-03 21:59:01
"""

class ActionServerTools:
    """设备动作工具管理器：每个方法对应一个设备动作"""
    def tool_start_atomize(self, **params):
        """开始喷涂（动作标识：start_atomize）- 需实现具体逻辑"""
        raise NotImplementedError(f"未实现 开始喷涂(start_atomize) 的工具逻辑")
