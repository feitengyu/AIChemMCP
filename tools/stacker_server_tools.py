"""
stacker 设备工具类
功能：定义设备所有动作的工具方法接口，需手动实现具体逻辑
生成时间：2025-08-07 10:08:38
"""

class ActionServerTools:
    """设备动作工具管理器：每个方法对应一个设备动作"""
    def tool_test1(self, **params):
        """码垛机指令（动作标识：test1）- 需实现具体逻辑"""
        raise NotImplementedError(f"未实现 码垛机指令(test1) 的工具逻辑")
