"""
ustc_mul_solid 设备工具类
功能：定义设备所有动作的工具方法接口，需手动实现具体逻辑
生成时间：2025-11-06 08:39:39
"""

class ActionServerTools:
    """设备动作工具管理器：每个方法对应一个设备动作"""
    def tool_project(self, **params):
        """进料方案（动作标识：project）- 需实现具体逻辑"""
        raise NotImplementedError(f"未实现 进料方案(project) 的工具逻辑")
    def tool_start_handle(self, **params):
        """手动上样（动作标识：start_handle）- 需实现具体逻辑"""
        raise NotImplementedError(f"未实现 手动上样(start_handle) 的工具逻辑")
    def tool_put_over(self, **params):
        """本轮放置结束（动作标识：put_over）- 需实现具体逻辑"""
        raise NotImplementedError(f"未实现 本轮放置结束(put_over) 的工具逻辑")
    def tool_take_over(self, **params):
        """本轮拿取结束（动作标识：take_over）- 需实现具体逻辑"""
        raise NotImplementedError(f"未实现 本轮拿取结束(take_over) 的工具逻辑")
    def tool_start_auto(self, **params):
        """自动开始（动作标识：start_auto）- 需实现具体逻辑"""
        raise NotImplementedError(f"未实现 自动开始(start_auto) 的工具逻辑")
    def tool_set_solid_inject_auto(self, **params):
        """自动加样（动作标识：set_solid_inject_auto）- 需实现具体逻辑"""
        raise NotImplementedError(f"未实现 自动加样(set_solid_inject_auto) 的工具逻辑")
