"""
ustc_photocatalysis 设备工具类
功能：定义设备所有动作的工具方法接口，需手动实现具体逻辑
生成时间：2025-08-31 10:34:50
"""

class ActionServerTools:
    """设备动作工具管理器：每个方法对应一个设备动作"""
    def tool_open(self, **params):
        """开灯（动作标识：open）- 需实现具体逻辑"""
        raise NotImplementedError(f"未实现 开灯(open) 的工具逻辑")
    def tool_time(self, **params):
        """照射时间（动作标识：time）- 需实现具体逻辑"""
        raise NotImplementedError(f"未实现 照射时间(time) 的工具逻辑")
    def tool_closeall(self, **params):
        """关闭所有灯（动作标识：closeall）- 需实现具体逻辑"""
        raise NotImplementedError(f"未实现 关闭所有灯(closeall) 的工具逻辑")
