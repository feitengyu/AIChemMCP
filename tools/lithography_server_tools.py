"""
lithography 设备工具类
功能：定义设备所有动作的工具方法接口，需手动实现具体逻辑
生成时间：2025-11-07 19:42:38
"""

class ActionServerTools:
    """设备动作工具管理器：每个方法对应一个设备动作"""
    def tool_init_communication(self, **params):
        """选择通信串口（动作标识：init_communication）- 需实现具体逻辑"""
        raise NotImplementedError(f"未实现 选择通信串口(init_communication) 的工具逻辑")
    def tool_laser_on(self, **params):
        """出光（动作标识：laser_on）- 需实现具体逻辑"""
        raise NotImplementedError(f"未实现 出光(laser_on) 的工具逻辑")
    def tool_take_samples(self, **params):
        """取出样品（动作标识：take_samples）- 需实现具体逻辑"""
        raise NotImplementedError(f"未实现 取出样品(take_samples) 的工具逻辑")
    def tool_open_vacuum_cupule(self, **params):
        """打开真空吸盘（动作标识：open_vacuum_cupule）- 需实现具体逻辑"""
        raise NotImplementedError(f"未实现 打开真空吸盘(open_vacuum_cupule) 的工具逻辑")
    def tool_close_vacuum_cupule(self, **params):
        """关闭真空吸盘（动作标识：close_vacuum_cupule）- 需实现具体逻辑"""
        raise NotImplementedError(f"未实现 关闭真空吸盘(close_vacuum_cupule) 的工具逻辑")
    def tool_open_camera(self, **params):
        """开启相机（动作标识：open_camera）- 需实现具体逻辑"""
        raise NotImplementedError(f"未实现 开启相机(open_camera) 的工具逻辑")
    def tool_pos_light(self, **params):
        """设置投射照明值（动作标识：pos_light）- 需实现具体逻辑"""
        raise NotImplementedError(f"未实现 设置投射照明值(pos_light) 的工具逻辑")
    def tool_raise_stage(self, **params):
        """抬升样品（动作标识：raise_stage）- 需实现具体逻辑"""
        raise NotImplementedError(f"未实现 抬升样品(raise_stage) 的工具逻辑")
    def tool_interface_detect(self, **params):
        """界面探测（动作标识：interface_detect）- 需实现具体逻辑"""
        raise NotImplementedError(f"未实现 界面探测(interface_detect) 的工具逻辑")
    def tool_load_samples(self, **params):
        """载入样品（动作标识：load_samples）- 需实现具体逻辑"""
        raise NotImplementedError(f"未实现 载入样品(load_samples) 的工具逻辑")
    def tool_start_lithography(self, **params):
        """开始光刻（动作标识：start_lithography）- 需实现具体逻辑"""
        raise NotImplementedError(f"未实现 开始光刻(start_lithography) 的工具逻辑")
    def tool_down_stage(self, **params):
        """下降样品台（动作标识：down_stage）- 需实现具体逻辑"""
        raise NotImplementedError(f"未实现 下降样品台(down_stage) 的工具逻辑")
    def tool_neg_light(self, **params):
        """设置反射照明值（动作标识：neg_light）- 需实现具体逻辑"""
        raise NotImplementedError(f"未实现 设置反射照明值(neg_light) 的工具逻辑")
    def tool_close_camera(self, **params):
        """关闭相机（动作标识：close_camera）- 需实现具体逻辑"""
        raise NotImplementedError(f"未实现 关闭相机(close_camera) 的工具逻辑")
    def tool_close_door(self, **params):
        """关门（动作标识：close_door）- 需实现具体逻辑"""
        raise NotImplementedError(f"未实现 关门(close_door) 的工具逻辑")
    def tool_open_door(self, **params):
        """开门（动作标识：open_door）- 需实现具体逻辑"""
        raise NotImplementedError(f"未实现 开门(open_door) 的工具逻辑")
