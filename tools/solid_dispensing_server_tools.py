"""
solid_dispensing 设备工具类
功能：定义设备所有动作的工具方法接口，需手动实现具体逻辑
生成时间：2025-11-07 19:42:38
"""

class ActionServerTools:
    """设备动作工具管理器：每个方法对应一个设备动作"""
    def tool_door_open(self, **params):
        """开门（动作标识：door_open）- 需实现具体逻辑"""
        raise NotImplementedError(f"未实现 开门(door_open) 的工具逻辑")
    def tool_door_close(self, **params):
        """关门（动作标识：door_close）- 需实现具体逻辑"""
        raise NotImplementedError(f"未实现 关门(door_close) 的工具逻辑")
    def tool_set_balance(self, **params):
        """进样（动作标识：set_balance）- 需实现具体逻辑"""
        raise NotImplementedError(f"未实现 进样(set_balance) 的工具逻辑")
    def tool_force_online(self, **params):
        """强制上线（动作标识：force_online）- 需实现具体逻辑"""
        raise NotImplementedError(f"未实现 强制上线(force_online) 的工具逻辑")
    def tool_force_offline(self, **params):
        """强制下线（动作标识：force_offline）- 需实现具体逻辑"""
        raise NotImplementedError(f"未实现 强制下线(force_offline) 的工具逻辑")
