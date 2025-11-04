"""
high_flux_xrd_workstation 设备工具类
功能：定义设备所有动作的工具方法接口，需手动实现具体逻辑
生成时间：2025-08-25 19:42:55
"""

class ActionServerTools:
    """设备动作工具管理器：每个方法对应一个设备动作"""
    def tool_start_check(self, **params):
        """开始检测（动作标识：start_check）- 需实现具体逻辑"""
        raise NotImplementedError(f"未实现 开始检测(start_check) 的工具逻辑")
    def tool_prefix_operate(self, **params):
        """检测前处理（动作标识：prefix_operate）- 需实现具体逻辑"""
        raise NotImplementedError(f"未实现 检测前处理(prefix_operate) 的工具逻辑")
    def tool_sleep(self, **params):
        """静置晾干（动作标识：sleep）- 需实现具体逻辑"""
        raise NotImplementedError(f"未实现 静置晾干(sleep) 的工具逻辑")
    def tool_confirm_tip_position(self, **params):
        """确认tip头位置（动作标识：confirm_tip_position）- 需实现具体逻辑"""
        raise NotImplementedError(f"未实现 确认tip头位置(confirm_tip_position) 的工具逻辑")
    def tool_auto_confirm_tip_position(self, **params):
        """自动确认tip头位置（动作标识：auto_confirm_tip_position）- 需实现具体逻辑"""
        raise NotImplementedError(f"未实现 自动确认tip头位置(auto_confirm_tip_position) 的工具逻辑")
