"""
MixingDripWorkstation 设备工具类
功能：定义设备所有动作的工具方法接口，需手动实现具体逻辑
生成时间：2025-07-09 18:56:47
"""

class ActionServerTools:
    """设备动作工具管理器：每个方法对应一个设备动作"""
    def tool_group5(self, **params):
        """吸取混匀后的液体 50 uL，滴加至玻片中间（动作标识：group5）- 需实现具体逻辑"""
        raise NotImplementedError(f"未实现 吸取混匀后的液体 50 uL，滴加至玻片中间(group5) 的工具逻辑")
