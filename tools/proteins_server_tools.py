"""
proteins 设备工具类
功能：定义设备所有动作的工具方法接口，需手动实现具体逻辑
生成时间：2025-04-15 14:25:14
"""

class ActionServerTools:
    """设备动作工具管理器：每个方法对应一个设备动作"""
    def tool_take_test_tube(self, **params):
        """取一个瓶子放在接收切割试剂的工位，并旋开瓶盖准备接收（动作标识：take_test_tube）- 需实现具体逻辑"""
        raise NotImplementedError(f"未实现 取一个瓶子放在接收切割试剂的工位，并旋开瓶盖准备接收(take_test_tube) 的工具逻辑")
    def tool_Receive_peptide(self, **params):
        """接收多肽溶液（动作标识：Receive_peptide）- 需实现具体逻辑"""
        raise NotImplementedError(f"未实现 接收多肽溶液(Receive_peptide) 的工具逻辑")
    def tool_Move_toN(self, **params):
        """将接收的多肽溶液转移至氮吹工位（动作标识：Move_toN）- 需实现具体逻辑"""
        raise NotImplementedError(f"未实现 将接收的多肽溶液转移至氮吹工位(Move_toN) 的工具逻辑")
    def tool_N_blow(self, **params):
        """启动氮吹-氮吹时间min（动作标识：N_blow）- 需实现具体逻辑"""
        raise NotImplementedError(f"未实现 启动氮吹-氮吹时间min(N_blow) 的工具逻辑")
    def tool_to_ethyl_ether(self, **params):
        """转移至注入乙醚工位（动作标识：to_ethyl_ether）- 需实现具体逻辑"""
        raise NotImplementedError(f"未实现 转移至注入乙醚工位(to_ethyl_ether) 的工具逻辑")
    def tool_inject_ether(self, **params):
        """启动注入乙醚（动作标识：inject_ether）- 需实现具体逻辑"""
        raise NotImplementedError(f"未实现 启动注入乙醚(inject_ether) 的工具逻辑")
    def tool_open_centrifuge(self, **params):
        """开启离心机门后定位到id号孔位（动作标识：open_centrifuge）- 需实现具体逻辑"""
        raise NotImplementedError(f"未实现 开启离心机门后定位到id号孔位(open_centrifuge) 的工具逻辑")
    def tool_ether_to_centrifuge(self, **params):
        """把乙醚工位的瓶子转移至离心机（动作标识：ether_to_centrifuge）- 需实现具体逻辑"""
        raise NotImplementedError(f"未实现 把乙醚工位的瓶子转移至离心机(ether_to_centrifuge) 的工具逻辑")
    def tool_to_Aspirate(self, **params):
        """将离心机里的瓶子转移至吸液工位后启动吸液（动作标识：to_Aspirate）- 需实现具体逻辑"""
        raise NotImplementedError(f"未实现 将离心机里的瓶子转移至吸液工位后启动吸液(to_Aspirate) 的工具逻辑")
    def tool_to_water(self, **params):
        """将吸液工位的瓶子转移至注水工位并注水溶解（动作标识：to_water）- 需实现具体逻辑"""
        raise NotImplementedError(f"未实现 将吸液工位的瓶子转移至注水工位并注水溶解(to_water) 的工具逻辑")
    def tool_to_Shaker(self, **params):
        """加水之后转移至摇床溶解后将瓶子转移至液相色谱进样工位（动作标识：to_Shaker）- 需实现具体逻辑"""
        raise NotImplementedError(f"未实现 加水之后转移至摇床溶解后将瓶子转移至液相色谱进样工位(to_Shaker) 的工具逻辑")
    def tool_to_LC(self, **params):
        """启动进样并开始液相色谱指令（动作标识：to_LC）- 需实现具体逻辑"""
        raise NotImplementedError(f"未实现 启动进样并开始液相色谱指令(to_LC) 的工具逻辑")
    def tool_to_liquid_nitrogen(self, **params):
        """将液相色谱仪纯化后的num个瓶子转移至液氮盆(num数量从request里的LC_num获取)，从start_num个瓶子开始（因为纯化后可能瓶子数量超过十个，冷冻盆里只有十个工位）转移多少数量，冷冻多少时间，可以分批冷冻（动作标识：to_liquid_nitrogen）- 需实现具体逻辑"""
        raise NotImplementedError(f"未实现 将液相色谱仪纯化后的num个瓶子转移至液氮盆(num数量从request里的LC_num获取)，从start_num个瓶子开始（因为纯化后可能瓶子数量超过十个，冷冻盆里只有十个工位）转移多少数量，冷冻多少时间，可以分批冷冻(to_liquid_nitrogen) 的工具逻辑")
    def tool_to_Lyophilization_chamber(self, **params):
        """将液氮盆里的num个瓶子，放置到冻干仓并冷冻time分钟（动作标识：to_Lyophilization_chamber）- 需实现具体逻辑"""
        raise NotImplementedError(f"未实现 将液氮盆里的num个瓶子，放置到冻干仓并冷冻time分钟(to_Lyophilization_chamber) 的工具逻辑")
    def tool_to_shaker_dissolve(self, **params):
        """将冻干仓里的num个瓶子，加注ml毫升溶解剂，放置到15.摇床摇动time分钟（动作标识：to_shaker_dissolve）- 需实现具体逻辑"""
        raise NotImplementedError(f"未实现 将冻干仓里的num个瓶子，加注ml毫升溶解剂，放置到15.摇床摇动time分钟(to_shaker_dissolve) 的工具逻辑")
    def tool_to_shaker_Dialysis_card(self, **params):
        """将num个透析卡转移至摇床（动作标识：to_shaker_Dialysis_card）- 需实现具体逻辑"""
        raise NotImplementedError(f"未实现 将num个透析卡转移至摇床(to_shaker_Dialysis_card) 的工具逻辑")
    def tool_Solution_to_shaker_Dialysis_card(self, **params):
        """将num个瓶子里的溶液转移至透析卡里并透析多少分钟（动作标识：Solution_to_shaker_Dialysis_card）- 需实现具体逻辑"""
        raise NotImplementedError(f"未实现 将num个瓶子里的溶液转移至透析卡里并透析多少分钟(Solution_to_shaker_Dialysis_card) 的工具逻辑")
    def tool_Centrifuge_positioning(self, **params):
        """把离心机门打开并定位到num位置（动作标识：Centrifuge_positioning）- 需实现具体逻辑"""
        raise NotImplementedError(f"未实现 把离心机门打开并定位到num位置(Centrifuge_positioning) 的工具逻辑")
    def tool_Dialysis_card_to_Centrifuge(self, **params):
        """将第num号透析卡内的溶液转移至第num号浓缩管，并旋紧瓶盖，后转移至离心机正对着进样口的孔位（动作标识：Dialysis_card_to_Centrifuge）- 需实现具体逻辑"""
        raise NotImplementedError(f"未实现 将第num号透析卡内的溶液转移至第num号浓缩管，并旋紧瓶盖，后转移至离心机正对着进样口的孔位(Dialysis_card_to_Centrifuge) 的工具逻辑")
    def tool_Dialysis_card_to_out(self, **params):
        """将第num号透析卡放置回收口（动作标识：Dialysis_card_to_out）- 需实现具体逻辑"""
        raise NotImplementedError(f"未实现 将第num号透析卡放置回收口(Dialysis_card_to_out) 的工具逻辑")
    def tool_Centrifuge_tubes_to_out(self, **params):
        """将第num号离心管放置回收口（动作标识：Centrifuge_tubes_to_out）- 需实现具体逻辑"""
        raise NotImplementedError(f"未实现 将第num号离心管放置回收口(Centrifuge_tubes_to_out) 的工具逻辑")
    def tool_start_Centrifuge(self, **params):
        """将离心机设置速度，时间后启动（动作标识：start_Centrifuge）- 需实现具体逻辑"""
        raise NotImplementedError(f"未实现 将离心机设置速度，时间后启动(start_Centrifuge) 的工具逻辑")
    def tool_millipore_ELISA_PLATE(self, **params):
        """将离心机的正对窗口的孔位的浓缩管转移至夹持工位，并开盖，后将试剂转移至酶标板的num号孔位（前提：离心机小门开着且放瓶子的孔位处于复位状态）（动作标识：millipore_ELISA_PLATE）- 需实现具体逻辑"""
        raise NotImplementedError(f"未实现 将离心机的正对窗口的孔位的浓缩管转移至夹持工位，并开盖，后将试剂转移至酶标板的num号孔位（前提：离心机小门开着且放瓶子的孔位处于复位状态）(millipore_ELISA_PLATE) 的工具逻辑")
    def tool_start_microplate_reader(self, **params):
        """启动酶标仪，机械臂将酶标板夹进酶标仪进行测试（动作标识：start_microplate_reader）- 需实现具体逻辑"""
        raise NotImplementedError(f"未实现 启动酶标仪，机械臂将酶标板夹进酶标仪进行测试(start_microplate_reader) 的工具逻辑")
    def tool_blance(self, **params):
        """取瓶子加ml毫升水，配平后转移至离心机（动作标识：blance）- 需实现具体逻辑"""
        raise NotImplementedError(f"未实现 取瓶子加ml毫升水，配平后转移至离心机(blance) 的工具逻辑")
    def tool_request(self, **params):
        """状态查询指令（动作标识：request）- 需实现具体逻辑"""
        raise NotImplementedError(f"未实现 状态查询指令(request) 的工具逻辑")
    def tool_balance_to_out(self, **params):
        """将配平离心机的瓶子丢进回收口（动作标识：balance_to_out）- 需实现具体逻辑"""
        raise NotImplementedError(f"未实现 将配平离心机的瓶子丢进回收口(balance_to_out) 的工具逻辑")
    def tool_ethyl_ether_to_N(self, **params):
        """将瓶子从乙醚工位转移至氮吹工位（动作标识：ethyl_ether_to_N）- 需实现具体逻辑"""
        raise NotImplementedError(f"未实现 将瓶子从乙醚工位转移至氮吹工位(ethyl_ether_to_N) 的工具逻辑")
    def tool_N_to_ethyl_ether(self, **params):
        """将瓶子从氮吹工位转移至乙醚工位进行后续旋盖（动作标识：N_to_ethyl_ether）- 需实现具体逻辑"""
        raise NotImplementedError(f"未实现 将瓶子从氮吹工位转移至乙醚工位进行后续旋盖(N_to_ethyl_ether) 的工具逻辑")
    def tool_add_water(self, **params):
        """注水溶解（动作标识：add_water）- 需实现具体逻辑"""
        raise NotImplementedError(f"未实现 注水溶解(add_water) 的工具逻辑")
    def tool_Centrifuge_tubes_to_LC(self, **params):
        """从离心管仓储位置取一个瓶子放置到液相接样的第num个位置（动作标识：Centrifuge_tubes_to_LC）- 需实现具体逻辑"""
        raise NotImplementedError(f"未实现 从离心管仓储位置取一个瓶子放置到液相接样的第num个位置(Centrifuge_tubes_to_LC) 的工具逻辑")
    def tool_start_mass_spectrometer(self, **params):
        """启动质谱仪（动作标识：start_mass_spectrometer）- 需实现具体逻辑"""
        raise NotImplementedError(f"未实现 启动质谱仪(start_mass_spectrometer) 的工具逻辑")
    def tool_from_liquid_chromatography_to_mass_spectrometry(self, **params):
        """从液相色谱仪纯化后的num个瓶子转移到质谱仪的西林瓶中(num数量从request里的LC_num字段获取（动作标识：from_liquid_chromatography_to_mass_spectrometry）- 需实现具体逻辑"""
        raise NotImplementedError(f"未实现 从液相色谱仪纯化后的num个瓶子转移到质谱仪的西林瓶中(num数量从request里的LC_num字段获取(from_liquid_chromatography_to_mass_spectrometry) 的工具逻辑")
    def tool_from_liquid_chromatography_to_liquid_nitorgen(self, **params):
        """质谱仪运行出结果后，从液相色谱仪纯化后的第几号瓶子转移到液氮盆（动作标识：from_liquid_chromatography_to_liquid_nitorgen）- 需实现具体逻辑"""
        raise NotImplementedError(f"未实现 质谱仪运行出结果后，从液相色谱仪纯化后的第几号瓶子转移到液氮盆(from_liquid_chromatography_to_liquid_nitorgen) 的工具逻辑")
