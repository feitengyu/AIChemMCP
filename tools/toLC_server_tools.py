"""
toLC 设备工具类
功能：定义设备所有动作的工具方法接口，需手动实现具体逻辑
生成时间：2025-09-02 10:39:17
"""

class ActionServerTools:
    """设备动作工具管理器：每个方法对应一个设备动作"""
    def tool_to_LC(self, **params):
        """启动进样并开始液相色谱指令（动作标识：to_LC）- 需实现具体逻辑"""
        raise NotImplementedError(f"未实现 启动进样并开始液相色谱指令(to_LC) 的工具逻辑")
    def tool_from_liquid_chromatography_to_mass_spectrometry(self, **params):
        """从液相色谱仪纯化后的num个瓶子转移到质谱仪的西林瓶中（动作标识：from_liquid_chromatography_to_mass_spectrometry）- 需实现具体逻辑"""
        raise NotImplementedError(f"未实现 从液相色谱仪纯化后的num个瓶子转移到质谱仪的西林瓶中(from_liquid_chromatography_to_mass_spectrometry) 的工具逻辑")
