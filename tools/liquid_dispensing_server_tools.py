"""
liquid_dispensing 设备工具类
功能：定义设备所有动作的工具方法接口，需手动实现具体逻辑
生成时间：2025-08-23 15:06:27
"""

class ActionServerTools:
    """设备动作工具管理器：每个方法对应一个设备动作"""
    def tool_add_liquid(self, **params):
        """加样（动作标识：add_liquid）- 需实现具体逻辑"""
        raise NotImplementedError(f"未实现 加样(add_liquid) 的工具逻辑")
    def tool_tip_init(self, **params):
        """tip头复位（动作标识：tip_init）- 需实现具体逻辑"""
        raise NotImplementedError(f"未实现 tip头复位(tip_init) 的工具逻辑")
    def tool_online(self, **params):
        """强制上线（动作标识：online）- 需实现具体逻辑"""
        raise NotImplementedError(f"未实现 强制上线(online) 的工具逻辑")
    def tool_offline(self, **params):
        """强制下线（动作标识：offline）- 需实现具体逻辑"""
        raise NotImplementedError(f"未实现 强制下线(offline) 的工具逻辑")
    def tool_reset_init(self, **params):
        """枪头夹抓复位（动作标识：reset_init）- 需实现具体逻辑"""
        raise NotImplementedError(f"未实现 枪头夹抓复位(reset_init) 的工具逻辑")
