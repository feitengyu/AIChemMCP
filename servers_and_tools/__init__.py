"""
AIChemMCP 服务器和工具文件导入助手
自动生成的文件 - 用于方便地导入所有工作站服务器
"""

import os
import sys

# 添加当前目录到Python路径
current_dir = os.path.dirname(os.path.abspath(__file__))
if current_dir not in sys.path:
    sys.path.insert(0, current_dir)

# 自动导入所有服务器函数
def get_available_servers():
    """获取所有可用的服务器函数"""
    servers = {}
    
    # 导入 flow_inj 服务器
    try:
        from flow_inj_server_v2 import flow_inj_server_main_loop, flow_inj_server_advertise_capabilities
        servers['flow_inj'] = {
            'main_loop': flow_inj_server_main_loop,
            'advertise': flow_inj_server_advertise_capabilities
        }
    except ImportError as e:
        print(f"⚠️ 无法导入 flow_inj 服务器: {e}")
    except Exception as e:
        print(f"⚠️ 导入 flow_inj 服务器时出错: {e}")

    # 导入 fluorescence_spectrometry_workstation 服务器
    try:
        from fluorescence_spectrometry_workstation_server_v2 import fluorescence_spectrometry_workstation_server_main_loop, fluorescence_spectrometry_workstation_server_advertise_capabilities
        servers['fluorescence_spectrometry_workstation'] = {
            'main_loop': fluorescence_spectrometry_workstation_server_main_loop,
            'advertise': fluorescence_spectrometry_workstation_server_advertise_capabilities
        }
    except ImportError as e:
        print(f"⚠️ 无法导入 fluorescence_spectrometry_workstation 服务器: {e}")
    except Exception as e:
        print(f"⚠️ 导入 fluorescence_spectrometry_workstation 服务器时出错: {e}")

    # 导入 magnetic_stirring 服务器
    try:
        from magnetic_stirring_server_v2 import magnetic_stirring_server_main_loop, magnetic_stirring_server_advertise_capabilities
        servers['magnetic_stirring'] = {
            'main_loop': magnetic_stirring_server_main_loop,
            'advertise': magnetic_stirring_server_advertise_capabilities
        }
    except ImportError as e:
        print(f"⚠️ 无法导入 magnetic_stirring 服务器: {e}")
    except Exception as e:
        print(f"⚠️ 导入 magnetic_stirring 服务器时出错: {e}")

    # 导入 furnace_workstation 服务器
    try:
        from furnace_workstation_server_v2 import furnace_workstation_server_main_loop, furnace_workstation_server_advertise_capabilities
        servers['furnace_workstation'] = {
            'main_loop': furnace_workstation_server_main_loop,
            'advertise': furnace_workstation_server_advertise_capabilities
        }
    except ImportError as e:
        print(f"⚠️ 无法导入 furnace_workstation 服务器: {e}")
    except Exception as e:
        print(f"⚠️ 导入 furnace_workstation 服务器时出错: {e}")

    # 导入 ustc_mul_solid 服务器
    try:
        from ustc_mul_solid_server_v2 import ustc_mul_solid_server_main_loop, ustc_mul_solid_server_advertise_capabilities
        servers['ustc_mul_solid'] = {
            'main_loop': ustc_mul_solid_server_main_loop,
            'advertise': ustc_mul_solid_server_advertise_capabilities
        }
    except ImportError as e:
        print(f"⚠️ 无法导入 ustc_mul_solid 服务器: {e}")
    except Exception as e:
        print(f"⚠️ 导入 ustc_mul_solid 服务器时出错: {e}")

    # 导入 pure 服务器
    try:
        from pure_server_v2 import pure_server_main_loop, pure_server_advertise_capabilities
        servers['pure'] = {
            'main_loop': pure_server_main_loop,
            'advertise': pure_server_advertise_capabilities
        }
    except ImportError as e:
        print(f"⚠️ 无法导入 pure 服务器: {e}")
    except Exception as e:
        print(f"⚠️ 导入 pure 服务器时出错: {e}")

    # 导入 microplate_reader_303 服务器
    try:
        from microplate_reader_303_server_v2 import microplate_reader_303_server_main_loop, microplate_reader_303_server_advertise_capabilities
        servers['microplate_reader_303'] = {
            'main_loop': microplate_reader_303_server_main_loop,
            'advertise': microplate_reader_303_server_advertise_capabilities
        }
    except ImportError as e:
        print(f"⚠️ 无法导入 microplate_reader_303 服务器: {e}")
    except Exception as e:
        print(f"⚠️ 导入 microplate_reader_303 服务器时出错: {e}")

    # 导入 photothermal_catalytic_reaction_workstation 服务器
    try:
        from photothermal_catalytic_reaction_workstation_server_v2 import photothermal_catalytic_reaction_workstation_server_main_loop, photothermal_catalytic_reaction_workstation_server_advertise_capabilities
        servers['photothermal_catalytic_reaction_workstation'] = {
            'main_loop': photothermal_catalytic_reaction_workstation_server_main_loop,
            'advertise': photothermal_catalytic_reaction_workstation_server_advertise_capabilities
        }
    except ImportError as e:
        print(f"⚠️ 无法导入 photothermal_catalytic_reaction_workstation 服务器: {e}")
    except Exception as e:
        print(f"⚠️ 导入 photothermal_catalytic_reaction_workstation 服务器时出错: {e}")

    # 导入 hts 服务器
    try:
        from hts_server_v2 import hts_server_main_loop, hts_server_advertise_capabilities
        servers['hts'] = {
            'main_loop': hts_server_main_loop,
            'advertise': hts_server_advertise_capabilities
        }
    except ImportError as e:
        print(f"⚠️ 无法导入 hts 服务器: {e}")
    except Exception as e:
        print(f"⚠️ 导入 hts 服务器时出错: {e}")

    # 导入 dryer 服务器
    try:
        from dryer_server_v2 import dryer_server_main_loop, dryer_server_advertise_capabilities
        servers['dryer'] = {
            'main_loop': dryer_server_main_loop,
            'advertise': dryer_server_advertise_capabilities
        }
    except ImportError as e:
        print(f"⚠️ 无法导入 dryer 服务器: {e}")
    except Exception as e:
        print(f"⚠️ 导入 dryer 服务器时出错: {e}")

    # 导入 ustc_photocatalysis 服务器
    try:
        from ustc_photocatalysis_server_v2 import ustc_photocatalysis_server_main_loop, ustc_photocatalysis_server_advertise_capabilities
        servers['ustc_photocatalysis'] = {
            'main_loop': ustc_photocatalysis_server_main_loop,
            'advertise': ustc_photocatalysis_server_advertise_capabilities
        }
    except ImportError as e:
        print(f"⚠️ 无法导入 ustc_photocatalysis 服务器: {e}")
    except Exception as e:
        print(f"⚠️ 导入 ustc_photocatalysis 服务器时出错: {e}")

    # 导入 toLC 服务器
    try:
        from toLC_server_v2 import toLC_server_main_loop, toLC_server_advertise_capabilities
        servers['toLC'] = {
            'main_loop': toLC_server_main_loop,
            'advertise': toLC_server_advertise_capabilities
        }
    except ImportError as e:
        print(f"⚠️ 无法导入 toLC 服务器: {e}")
    except Exception as e:
        print(f"⚠️ 导入 toLC 服务器时出错: {e}")

    # 导入 angularContact 服务器
    try:
        from angularContact_server_v2 import angularContact_server_main_loop, angularContact_server_advertise_capabilities
        servers['angularContact'] = {
            'main_loop': angularContact_server_main_loop,
            'advertise': angularContact_server_advertise_capabilities
        }
    except ImportError as e:
        print(f"⚠️ 无法导入 angularContact 服务器: {e}")
    except Exception as e:
        print(f"⚠️ 导入 angularContact 服务器时出错: {e}")

    # 导入 reaction_platform 服务器
    try:
        from reaction_platform_server_v2 import reaction_platform_server_main_loop, reaction_platform_server_advertise_capabilities
        servers['reaction_platform'] = {
            'main_loop': reaction_platform_server_main_loop,
            'advertise': reaction_platform_server_advertise_capabilities
        }
    except ImportError as e:
        print(f"⚠️ 无法导入 reaction_platform 服务器: {e}")
    except Exception as e:
        print(f"⚠️ 导入 reaction_platform 服务器时出错: {e}")

    # 导入 NitrogenBlowing 服务器
    try:
        from NitrogenBlowing_server_v2 import NitrogenBlowing_server_main_loop, NitrogenBlowing_server_advertise_capabilities
        servers['NitrogenBlowing'] = {
            'main_loop': NitrogenBlowing_server_main_loop,
            'advertise': NitrogenBlowing_server_advertise_capabilities
        }
    except ImportError as e:
        print(f"⚠️ 无法导入 NitrogenBlowing 服务器: {e}")
    except Exception as e:
        print(f"⚠️ 导入 NitrogenBlowing 服务器时出错: {e}")

    # 导入 TubeFurnace 服务器
    try:
        from TubeFurnace_server_v2 import TubeFurnace_server_main_loop, TubeFurnace_server_advertise_capabilities
        servers['TubeFurnace'] = {
            'main_loop': TubeFurnace_server_main_loop,
            'advertise': TubeFurnace_server_advertise_capabilities
        }
    except ImportError as e:
        print(f"⚠️ 无法导入 TubeFurnace 服务器: {e}")
    except Exception as e:
        print(f"⚠️ 导入 TubeFurnace 服务器时出错: {e}")

    # 导入 tptn 服务器
    try:
        from tptn_server_v2 import tptn_server_main_loop, tptn_server_advertise_capabilities
        servers['tptn'] = {
            'main_loop': tptn_server_main_loop,
            'advertise': tptn_server_advertise_capabilities
        }
    except ImportError as e:
        print(f"⚠️ 无法导入 tptn 服务器: {e}")
    except Exception as e:
        print(f"⚠️ 导入 tptn 服务器时出错: {e}")

    # 导入 gn_centrifugation_workstation 服务器
    try:
        from gn_centrifugation_workstation_server_v2 import gn_centrifugation_workstation_server_main_loop, gn_centrifugation_workstation_server_advertise_capabilities
        servers['gn_centrifugation_workstation'] = {
            'main_loop': gn_centrifugation_workstation_server_main_loop,
            'advertise': gn_centrifugation_workstation_server_advertise_capabilities
        }
    except ImportError as e:
        print(f"⚠️ 无法导入 gn_centrifugation_workstation 服务器: {e}")
    except Exception as e:
        print(f"⚠️ 导入 gn_centrifugation_workstation 服务器时出错: {e}")

    # 导入 high_throughput_advanced_material_screening_workstation 服务器
    try:
        from high_throughput_advanced_material_screening_workstation_server_v2 import high_throughput_advanced_material_screening_workstation_server_main_loop, high_throughput_advanced_material_screening_workstation_server_advertise_capabilities
        servers['high_throughput_advanced_material_screening_workstation'] = {
            'main_loop': high_throughput_advanced_material_screening_workstation_server_main_loop,
            'advertise': high_throughput_advanced_material_screening_workstation_server_advertise_capabilities
        }
    except ImportError as e:
        print(f"⚠️ 无法导入 high_throughput_advanced_material_screening_workstation 服务器: {e}")
    except Exception as e:
        print(f"⚠️ 导入 high_throughput_advanced_material_screening_workstation 服务器时出错: {e}")

    # 导入 lithography 服务器
    try:
        from lithography_server_v2 import lithography_server_main_loop, lithography_server_advertise_capabilities
        servers['lithography'] = {
            'main_loop': lithography_server_main_loop,
            'advertise': lithography_server_advertise_capabilities
        }
    except ImportError as e:
        print(f"⚠️ 无法导入 lithography 服务器: {e}")
    except Exception as e:
        print(f"⚠️ 导入 lithography 服务器时出错: {e}")

    # 导入 spps_workstation 服务器
    try:
        from spps_workstation_server_v2 import spps_workstation_server_main_loop, spps_workstation_server_advertise_capabilities
        servers['spps_workstation'] = {
            'main_loop': spps_workstation_server_main_loop,
            'advertise': spps_workstation_server_advertise_capabilities
        }
    except ImportError as e:
        print(f"⚠️ 无法导入 spps_workstation 服务器: {e}")
    except Exception as e:
        print(f"⚠️ 导入 spps_workstation 服务器时出错: {e}")

    # 导入 cod 服务器
    try:
        from cod_server_v2 import cod_server_main_loop, cod_server_advertise_capabilities
        servers['cod'] = {
            'main_loop': cod_server_main_loop,
            'advertise': cod_server_advertise_capabilities
        }
    except ImportError as e:
        print(f"⚠️ 无法导入 cod 服务器: {e}")
    except Exception as e:
        print(f"⚠️ 导入 cod 服务器时出错: {e}")

    # 导入 peptideSynthesizer 服务器
    try:
        from peptideSynthesizer_server_v2 import peptideSynthesizer_server_main_loop, peptideSynthesizer_server_advertise_capabilities
        servers['peptideSynthesizer'] = {
            'main_loop': peptideSynthesizer_server_main_loop,
            'advertise': peptideSynthesizer_server_advertise_capabilities
        }
    except ImportError as e:
        print(f"⚠️ 无法导入 peptideSynthesizer 服务器: {e}")
    except Exception as e:
        print(f"⚠️ 导入 peptideSynthesizer 服务器时出错: {e}")

    # 导入 starting_station 服务器
    try:
        from starting_station_server_v2 import starting_station_server_main_loop, starting_station_server_advertise_capabilities
        servers['starting_station'] = {
            'main_loop': starting_station_server_main_loop,
            'advertise': starting_station_server_advertise_capabilities
        }
    except ImportError as e:
        print(f"⚠️ 无法导入 starting_station 服务器: {e}")
    except Exception as e:
        print(f"⚠️ 导入 starting_station 服务器时出错: {e}")

    # 导入 ultrasonic_cleaning 服务器
    try:
        from ultrasonic_cleaning_server_v2 import ultrasonic_cleaning_server_main_loop, ultrasonic_cleaning_server_advertise_capabilities
        servers['ultrasonic_cleaning'] = {
            'main_loop': ultrasonic_cleaning_server_main_loop,
            'advertise': ultrasonic_cleaning_server_advertise_capabilities
        }
    except ImportError as e:
        print(f"⚠️ 无法导入 ultrasonic_cleaning 服务器: {e}")
    except Exception as e:
        print(f"⚠️ 导入 ultrasonic_cleaning 服务器时出错: {e}")

    # 导入 microplate_reader 服务器
    try:
        from microplate_reader_server_v2 import microplate_reader_server_main_loop, microplate_reader_server_advertise_capabilities
        servers['microplate_reader'] = {
            'main_loop': microplate_reader_server_main_loop,
            'advertise': microplate_reader_server_advertise_capabilities
        }
    except ImportError as e:
        print(f"⚠️ 无法导入 microplate_reader 服务器: {e}")
    except Exception as e:
        print(f"⚠️ 导入 microplate_reader 服务器时出错: {e}")

    # 导入 solid_dispensing 服务器
    try:
        from solid_dispensing_server_v2 import solid_dispensing_server_main_loop, solid_dispensing_server_advertise_capabilities
        servers['solid_dispensing'] = {
            'main_loop': solid_dispensing_server_main_loop,
            'advertise': solid_dispensing_server_advertise_capabilities
        }
    except ImportError as e:
        print(f"⚠️ 无法导入 solid_dispensing 服务器: {e}")
    except Exception as e:
        print(f"⚠️ 导入 solid_dispensing 服务器时出错: {e}")

    # 导入 ustc_combine_comfirm 服务器
    try:
        from ustc_combine_comfirm_server_v2 import ustc_combine_comfirm_server_main_loop, ustc_combine_comfirm_server_advertise_capabilities
        servers['ustc_combine_comfirm'] = {
            'main_loop': ustc_combine_comfirm_server_main_loop,
            'advertise': ustc_combine_comfirm_server_advertise_capabilities
        }
    except ImportError as e:
        print(f"⚠️ 无法导入 ustc_combine_comfirm 服务器: {e}")
    except Exception as e:
        print(f"⚠️ 导入 ustc_combine_comfirm 服务器时出错: {e}")

    # 导入 liquid_handling_workstation 服务器
    try:
        from liquid_handling_workstation_server_v2 import liquid_handling_workstation_server_main_loop, liquid_handling_workstation_server_advertise_capabilities
        servers['liquid_handling_workstation'] = {
            'main_loop': liquid_handling_workstation_server_main_loop,
            'advertise': liquid_handling_workstation_server_advertise_capabilities
        }
    except ImportError as e:
        print(f"⚠️ 无法导入 liquid_handling_workstation 服务器: {e}")
    except Exception as e:
        print(f"⚠️ 导入 liquid_handling_workstation 服务器时出错: {e}")

    # 导入 nh3n 服务器
    try:
        from nh3n_server_v2 import nh3n_server_main_loop, nh3n_server_advertise_capabilities
        servers['nh3n'] = {
            'main_loop': nh3n_server_main_loop,
            'advertise': nh3n_server_advertise_capabilities
        }
    except ImportError as e:
        print(f"⚠️ 无法导入 nh3n 服务器: {e}")
    except Exception as e:
        print(f"⚠️ 导入 nh3n 服务器时出错: {e}")

    # 导入 high_flux_ir_workstation 服务器
    try:
        from high_flux_ir_workstation_server_v2 import high_flux_ir_workstation_server_main_loop, high_flux_ir_workstation_server_advertise_capabilities
        servers['high_flux_ir_workstation'] = {
            'main_loop': high_flux_ir_workstation_server_main_loop,
            'advertise': high_flux_ir_workstation_server_advertise_capabilities
        }
    except ImportError as e:
        print(f"⚠️ 无法导入 high_flux_ir_workstation 服务器: {e}")
    except Exception as e:
        print(f"⚠️ 导入 high_flux_ir_workstation 服务器时出错: {e}")

    # 导入 confecting_workstation 服务器
    try:
        from confecting_workstation_server_v2 import confecting_workstation_server_main_loop, confecting_workstation_server_advertise_capabilities
        servers['confecting_workstation'] = {
            'main_loop': confecting_workstation_server_main_loop,
            'advertise': confecting_workstation_server_advertise_capabilities
        }
    except ImportError as e:
        print(f"⚠️ 无法导入 confecting_workstation 服务器: {e}")
    except Exception as e:
        print(f"⚠️ 导入 confecting_workstation 服务器时出错: {e}")

    # 导入 ElectrochemicalWorkstation_(including_high_speed_camera) 服务器
    try:
        from ElectrochemicalWorkstation_(including_high_speed_camera)_server_v2 import ElectrochemicalWorkstation_(including_high_speed_camera)_server_main_loop, ElectrochemicalWorkstation_(including_high_speed_camera)_server_advertise_capabilities
        servers['ElectrochemicalWorkstation_(including_high_speed_camera)'] = {
            'main_loop': ElectrochemicalWorkstation_(including_high_speed_camera)_server_main_loop,
            'advertise': ElectrochemicalWorkstation_(including_high_speed_camera)_server_advertise_capabilities
        }
    except ImportError as e:
        print(f"⚠️ 无法导入 ElectrochemicalWorkstation_(including_high_speed_camera) 服务器: {e}")
    except Exception as e:
        print(f"⚠️ 导入 ElectrochemicalWorkstation_(including_high_speed_camera) 服务器时出错: {e}")

    # 导入 elec_chem_storage_workstation 服务器
    try:
        from elec_chem_storage_workstation_server_v2 import elec_chem_storage_workstation_server_main_loop, elec_chem_storage_workstation_server_advertise_capabilities
        servers['elec_chem_storage_workstation'] = {
            'main_loop': elec_chem_storage_workstation_server_main_loop,
            'advertise': elec_chem_storage_workstation_server_advertise_capabilities
        }
    except ImportError as e:
        print(f"⚠️ 无法导入 elec_chem_storage_workstation 服务器: {e}")
    except Exception as e:
        print(f"⚠️ 导入 elec_chem_storage_workstation 服务器时出错: {e}")

    # 导入 to_Lyophilization_chamber 服务器
    try:
        from to_Lyophilization_chamber_server_v2 import to_Lyophilization_chamber_server_main_loop, to_Lyophilization_chamber_server_advertise_capabilities
        servers['to_Lyophilization_chamber'] = {
            'main_loop': to_Lyophilization_chamber_server_main_loop,
            'advertise': to_Lyophilization_chamber_server_advertise_capabilities
        }
    except ImportError as e:
        print(f"⚠️ 无法导入 to_Lyophilization_chamber 服务器: {e}")
    except Exception as e:
        print(f"⚠️ 导入 to_Lyophilization_chamber 服务器时出错: {e}")

    # 导入 spraying_workstation 服务器
    try:
        from spraying_workstation_server_v2 import spraying_workstation_server_main_loop, spraying_workstation_server_advertise_capabilities
        servers['spraying_workstation'] = {
            'main_loop': spraying_workstation_server_main_loop,
            'advertise': spraying_workstation_server_advertise_capabilities
        }
    except ImportError as e:
        print(f"⚠️ 无法导入 spraying_workstation 服务器: {e}")
    except Exception as e:
        print(f"⚠️ 导入 spraying_workstation 服务器时出错: {e}")

    # 导入 sintering_workstation 服务器
    try:
        from sintering_workstation_server_v2 import sintering_workstation_server_main_loop, sintering_workstation_server_advertise_capabilities
        servers['sintering_workstation'] = {
            'main_loop': sintering_workstation_server_main_loop,
            'advertise': sintering_workstation_server_advertise_capabilities
        }
    except ImportError as e:
        print(f"⚠️ 无法导入 sintering_workstation 服务器: {e}")
    except Exception as e:
        print(f"⚠️ 导入 sintering_workstation 服务器时出错: {e}")

    # 导入 ALDWorkstation 服务器
    try:
        from ALDWorkstation_server_v2 import ALDWorkstation_server_main_loop, ALDWorkstation_server_advertise_capabilities
        servers['ALDWorkstation'] = {
            'main_loop': ALDWorkstation_server_main_loop,
            'advertise': ALDWorkstation_server_advertise_capabilities
        }
    except ImportError as e:
        print(f"⚠️ 无法导入 ALDWorkstation 服务器: {e}")
    except Exception as e:
        print(f"⚠️ 导入 ALDWorkstation 服务器时出错: {e}")

    # 导入 nucleic_acid_extractor 服务器
    try:
        from nucleic_acid_extractor_server_v2 import nucleic_acid_extractor_server_main_loop, nucleic_acid_extractor_server_advertise_capabilities
        servers['nucleic_acid_extractor'] = {
            'main_loop': nucleic_acid_extractor_server_main_loop,
            'advertise': nucleic_acid_extractor_server_advertise_capabilities
        }
    except ImportError as e:
        print(f"⚠️ 无法导入 nucleic_acid_extractor 服务器: {e}")
    except Exception as e:
        print(f"⚠️ 导入 nucleic_acid_extractor 服务器时出错: {e}")

    # 导入 federation_k_confirm 服务器
    try:
        from federation_k_confirm_server_v2 import federation_k_confirm_server_main_loop, federation_k_confirm_server_advertise_capabilities
        servers['federation_k_confirm'] = {
            'main_loop': federation_k_confirm_server_main_loop,
            'advertise': federation_k_confirm_server_advertise_capabilities
        }
    except ImportError as e:
        print(f"⚠️ 无法导入 federation_k_confirm 服务器: {e}")
    except Exception as e:
        print(f"⚠️ 导入 federation_k_confirm 服务器时出错: {e}")

    # 导入 massSpectrometer 服务器
    try:
        from massSpectrometer_server_v2 import massSpectrometer_server_main_loop, massSpectrometer_server_advertise_capabilities
        servers['massSpectrometer'] = {
            'main_loop': massSpectrometer_server_main_loop,
            'advertise': massSpectrometer_server_advertise_capabilities
        }
    except ImportError as e:
        print(f"⚠️ 无法导入 massSpectrometer 服务器: {e}")
    except Exception as e:
        print(f"⚠️ 导入 massSpectrometer 服务器时出错: {e}")

    # 导入 transfer_workstation 服务器
    try:
        from transfer_workstation_server_v2 import transfer_workstation_server_main_loop, transfer_workstation_server_advertise_capabilities
        servers['transfer_workstation'] = {
            'main_loop': transfer_workstation_server_main_loop,
            'advertise': transfer_workstation_server_advertise_capabilities
        }
    except ImportError as e:
        print(f"⚠️ 无法导入 transfer_workstation 服务器: {e}")
    except Exception as e:
        print(f"⚠️ 导入 transfer_workstation 服务器时出错: {e}")

    # 导入 single_atom_enzyme_mimicking 服务器
    try:
        from single_atom_enzyme_mimicking_server_v2 import single_atom_enzyme_mimicking_server_main_loop, single_atom_enzyme_mimicking_server_advertise_capabilities
        servers['single_atom_enzyme_mimicking'] = {
            'main_loop': single_atom_enzyme_mimicking_server_main_loop,
            'advertise': single_atom_enzyme_mimicking_server_advertise_capabilities
        }
    except ImportError as e:
        print(f"⚠️ 无法导入 single_atom_enzyme_mimicking 服务器: {e}")
    except Exception as e:
        print(f"⚠️ 导入 single_atom_enzyme_mimicking 服务器时出错: {e}")

    # 导入 high_flux_xrd_workstation 服务器
    try:
        from high_flux_xrd_workstation_server_v2 import high_flux_xrd_workstation_server_main_loop, high_flux_xrd_workstation_server_advertise_capabilities
        servers['high_flux_xrd_workstation'] = {
            'main_loop': high_flux_xrd_workstation_server_main_loop,
            'advertise': high_flux_xrd_workstation_server_advertise_capabilities
        }
    except ImportError as e:
        print(f"⚠️ 无法导入 high_flux_xrd_workstation 服务器: {e}")
    except Exception as e:
        print(f"⚠️ 导入 high_flux_xrd_workstation 服务器时出错: {e}")

    # 导入 Shaker 服务器
    try:
        from Shaker_server_v2 import Shaker_server_main_loop, Shaker_server_advertise_capabilities
        servers['Shaker'] = {
            'main_loop': Shaker_server_main_loop,
            'advertise': Shaker_server_advertise_capabilities
        }
    except ImportError as e:
        print(f"⚠️ 无法导入 Shaker 服务器: {e}")
    except Exception as e:
        print(f"⚠️ 导入 Shaker 服务器时出错: {e}")

    # 导入 battery_assemble_workstation 服务器
    try:
        from battery_assemble_workstation_server_v2 import battery_assemble_workstation_server_main_loop, battery_assemble_workstation_server_advertise_capabilities
        servers['battery_assemble_workstation'] = {
            'main_loop': battery_assemble_workstation_server_main_loop,
            'advertise': battery_assemble_workstation_server_advertise_capabilities
        }
    except ImportError as e:
        print(f"⚠️ 无法导入 battery_assemble_workstation 服务器: {e}")
    except Exception as e:
        print(f"⚠️ 导入 battery_assemble_workstation 服务器时出错: {e}")

    # 导入 electrode_assembly_workstation 服务器
    try:
        from electrode_assembly_workstation_server_v2 import electrode_assembly_workstation_server_main_loop, electrode_assembly_workstation_server_advertise_capabilities
        servers['electrode_assembly_workstation'] = {
            'main_loop': electrode_assembly_workstation_server_main_loop,
            'advertise': electrode_assembly_workstation_server_advertise_capabilities
        }
    except ImportError as e:
        print(f"⚠️ 无法导入 electrode_assembly_workstation 服务器: {e}")
    except Exception as e:
        print(f"⚠️ 导入 electrode_assembly_workstation 服务器时出错: {e}")

    # 导入 imbibition 服务器
    try:
        from imbibition_server_v2 import imbibition_server_main_loop, imbibition_server_advertise_capabilities
        servers['imbibition'] = {
            'main_loop': imbibition_server_main_loop,
            'advertise': imbibition_server_advertise_capabilities
        }
    except ImportError as e:
        print(f"⚠️ 无法导入 imbibition 服务器: {e}")
    except Exception as e:
        print(f"⚠️ 导入 imbibition 服务器时出错: {e}")

    # 导入 XRD_workstation 服务器
    try:
        from XRD_workstation_server_v2 import XRD_workstation_server_main_loop, XRD_workstation_server_advertise_capabilities
        servers['XRD_workstation'] = {
            'main_loop': XRD_workstation_server_main_loop,
            'advertise': XRD_workstation_server_advertise_capabilities
        }
    except ImportError as e:
        print(f"⚠️ 无法导入 XRD_workstation 服务器: {e}")
    except Exception as e:
        print(f"⚠️ 导入 XRD_workstation 服务器时出错: {e}")

    # 导入 new_centrifugation 服务器
    try:
        from new_centrifugation_server_v2 import new_centrifugation_server_main_loop, new_centrifugation_server_advertise_capabilities
        servers['new_centrifugation'] = {
            'main_loop': new_centrifugation_server_main_loop,
            'advertise': new_centrifugation_server_advertise_capabilities
        }
    except ImportError as e:
        print(f"⚠️ 无法导入 new_centrifugation 服务器: {e}")
    except Exception as e:
        print(f"⚠️ 导入 new_centrifugation 服务器时出错: {e}")

    # 导入 UV_spectrophotometer_workstation 服务器
    try:
        from UV_spectrophotometer_workstation_server_v2 import UV_spectrophotometer_workstation_server_main_loop, UV_spectrophotometer_workstation_server_advertise_capabilities
        servers['UV_spectrophotometer_workstation'] = {
            'main_loop': UV_spectrophotometer_workstation_server_main_loop,
            'advertise': UV_spectrophotometer_workstation_server_advertise_capabilities
        }
    except ImportError as e:
        print(f"⚠️ 无法导入 UV_spectrophotometer_workstation 服务器: {e}")
    except Exception as e:
        print(f"⚠️ 导入 UV_spectrophotometer_workstation 服务器时出错: {e}")

    # 导入 DialysisWorkstation 服务器
    try:
        from DialysisWorkstation_server_v2 import DialysisWorkstation_server_main_loop, DialysisWorkstation_server_advertise_capabilities
        servers['DialysisWorkstation'] = {
            'main_loop': DialysisWorkstation_server_main_loop,
            'advertise': DialysisWorkstation_server_advertise_capabilities
        }
    except ImportError as e:
        print(f"⚠️ 无法导入 DialysisWorkstation 服务器: {e}")
    except Exception as e:
        print(f"⚠️ 导入 DialysisWorkstation 服务器时出错: {e}")

    # 导入 liquid_dispensing 服务器
    try:
        from liquid_dispensing_server_v2 import liquid_dispensing_server_main_loop, liquid_dispensing_server_advertise_capabilities
        servers['liquid_dispensing'] = {
            'main_loop': liquid_dispensing_server_main_loop,
            'advertise': liquid_dispensing_server_advertise_capabilities
        }
    except ImportError as e:
        print(f"⚠️ 无法导入 liquid_dispensing 服务器: {e}")
    except Exception as e:
        print(f"⚠️ 导入 liquid_dispensing 服务器时出错: {e}")

    # 导入 spotting_workstation 服务器
    try:
        from spotting_workstation_server_v2 import spotting_workstation_server_main_loop, spotting_workstation_server_advertise_capabilities
        servers['spotting_workstation'] = {
            'main_loop': spotting_workstation_server_main_loop,
            'advertise': spotting_workstation_server_advertise_capabilities
        }
    except ImportError as e:
        print(f"⚠️ 无法导入 spotting_workstation 服务器: {e}")
    except Exception as e:
        print(f"⚠️ 导入 spotting_workstation 服务器时出错: {e}")

    # 导入 ic 服务器
    try:
        from ic_server_v2 import ic_server_main_loop, ic_server_advertise_capabilities
        servers['ic'] = {
            'main_loop': ic_server_main_loop,
            'advertise': ic_server_advertise_capabilities
        }
    except ImportError as e:
        print(f"⚠️ 无法导入 ic 服务器: {e}")
    except Exception as e:
        print(f"⚠️ 导入 ic 服务器时出错: {e}")

    # 导入 icpms_workstation 服务器
    try:
        from icpms_workstation_server_v2 import icpms_workstation_server_main_loop, icpms_workstation_server_advertise_capabilities
        servers['icpms_workstation'] = {
            'main_loop': icpms_workstation_server_main_loop,
            'advertise': icpms_workstation_server_advertise_capabilities
        }
    except ImportError as e:
        print(f"⚠️ 无法导入 icpms_workstation 服务器: {e}")
    except Exception as e:
        print(f"⚠️ 导入 icpms_workstation 服务器时出错: {e}")

    return servers

# 自动导入所有工具类
def get_available_tools():
    """获取所有可用的工具类"""
    tools = {}
    
    # 导入 photothermal_catalytic_reaction_workstation 工具类
    try:
        from photothermal_catalytic_reaction_workstation_server_tools_v2 import UnifiedWorkstationTools
        tools['photothermal_catalytic_reaction_workstation'] = UnifiedWorkstationTools
    except ImportError as e:
        print(f"⚠️ 无法导入 photothermal_catalytic_reaction_workstation 工具类: {e}")
    except Exception as e:
        print(f"⚠️ 导入 photothermal_catalytic_reaction_workstation 工具类时出错: {e}")

    # 导入 fluorescence_spectrometry_workstation 工具类
    try:
        from fluorescence_spectrometry_workstation_server_tools_v2 import UnifiedWorkstationTools
        tools['fluorescence_spectrometry_workstation'] = UnifiedWorkstationTools
    except ImportError as e:
        print(f"⚠️ 无法导入 fluorescence_spectrometry_workstation 工具类: {e}")
    except Exception as e:
        print(f"⚠️ 导入 fluorescence_spectrometry_workstation 工具类时出错: {e}")

    # 导入 to_Lyophilization_chamber 工具类
    try:
        from to_Lyophilization_chamber_server_tools_v2 import UnifiedWorkstationTools
        tools['to_Lyophilization_chamber'] = UnifiedWorkstationTools
    except ImportError as e:
        print(f"⚠️ 无法导入 to_Lyophilization_chamber 工具类: {e}")
    except Exception as e:
        print(f"⚠️ 导入 to_Lyophilization_chamber 工具类时出错: {e}")

    # 导入 spps_workstation 工具类
    try:
        from spps_workstation_server_tools_v2 import UnifiedWorkstationTools
        tools['spps_workstation'] = UnifiedWorkstationTools
    except ImportError as e:
        print(f"⚠️ 无法导入 spps_workstation 工具类: {e}")
    except Exception as e:
        print(f"⚠️ 导入 spps_workstation 工具类时出错: {e}")

    # 导入 ic 工具类
    try:
        from ic_server_tools_v2 import UnifiedWorkstationTools
        tools['ic'] = UnifiedWorkstationTools
    except ImportError as e:
        print(f"⚠️ 无法导入 ic 工具类: {e}")
    except Exception as e:
        print(f"⚠️ 导入 ic 工具类时出错: {e}")

    # 导入 single_atom_enzyme_mimicking 工具类
    try:
        from single_atom_enzyme_mimicking_server_tools_v2 import UnifiedWorkstationTools
        tools['single_atom_enzyme_mimicking'] = UnifiedWorkstationTools
    except ImportError as e:
        print(f"⚠️ 无法导入 single_atom_enzyme_mimicking 工具类: {e}")
    except Exception as e:
        print(f"⚠️ 导入 single_atom_enzyme_mimicking 工具类时出错: {e}")

    # 导入 microplate_reader_303 工具类
    try:
        from microplate_reader_303_server_tools_v2 import UnifiedWorkstationTools
        tools['microplate_reader_303'] = UnifiedWorkstationTools
    except ImportError as e:
        print(f"⚠️ 无法导入 microplate_reader_303 工具类: {e}")
    except Exception as e:
        print(f"⚠️ 导入 microplate_reader_303 工具类时出错: {e}")

    # 导入 high_flux_xrd_workstation 工具类
    try:
        from high_flux_xrd_workstation_server_tools_v2 import UnifiedWorkstationTools
        tools['high_flux_xrd_workstation'] = UnifiedWorkstationTools
    except ImportError as e:
        print(f"⚠️ 无法导入 high_flux_xrd_workstation 工具类: {e}")
    except Exception as e:
        print(f"⚠️ 导入 high_flux_xrd_workstation 工具类时出错: {e}")

    # 导入 spraying_workstation 工具类
    try:
        from spraying_workstation_server_tools_v2 import UnifiedWorkstationTools
        tools['spraying_workstation'] = UnifiedWorkstationTools
    except ImportError as e:
        print(f"⚠️ 无法导入 spraying_workstation 工具类: {e}")
    except Exception as e:
        print(f"⚠️ 导入 spraying_workstation 工具类时出错: {e}")

    # 导入 battery_assemble_workstation 工具类
    try:
        from battery_assemble_workstation_server_tools_v2 import UnifiedWorkstationTools
        tools['battery_assemble_workstation'] = UnifiedWorkstationTools
    except ImportError as e:
        print(f"⚠️ 无法导入 battery_assemble_workstation 工具类: {e}")
    except Exception as e:
        print(f"⚠️ 导入 battery_assemble_workstation 工具类时出错: {e}")

    # 导入 high_throughput_advanced_material_screening_workstation 工具类
    try:
        from high_throughput_advanced_material_screening_workstation_server_tools_v2 import UnifiedWorkstationTools
        tools['high_throughput_advanced_material_screening_workstation'] = UnifiedWorkstationTools
    except ImportError as e:
        print(f"⚠️ 无法导入 high_throughput_advanced_material_screening_workstation 工具类: {e}")
    except Exception as e:
        print(f"⚠️ 导入 high_throughput_advanced_material_screening_workstation 工具类时出错: {e}")

    # 导入 pure 工具类
    try:
        from pure_server_tools_v2 import UnifiedWorkstationTools
        tools['pure'] = UnifiedWorkstationTools
    except ImportError as e:
        print(f"⚠️ 无法导入 pure 工具类: {e}")
    except Exception as e:
        print(f"⚠️ 导入 pure 工具类时出错: {e}")

    # 导入 nh3n 工具类
    try:
        from nh3n_server_tools_v2 import UnifiedWorkstationTools
        tools['nh3n'] = UnifiedWorkstationTools
    except ImportError as e:
        print(f"⚠️ 无法导入 nh3n 工具类: {e}")
    except Exception as e:
        print(f"⚠️ 导入 nh3n 工具类时出错: {e}")

    # 导入 reaction_platform 工具类
    try:
        from reaction_platform_server_tools_v2 import UnifiedWorkstationTools
        tools['reaction_platform'] = UnifiedWorkstationTools
    except ImportError as e:
        print(f"⚠️ 无法导入 reaction_platform 工具类: {e}")
    except Exception as e:
        print(f"⚠️ 导入 reaction_platform 工具类时出错: {e}")

    # 导入 furnace_workstation 工具类
    try:
        from furnace_workstation_server_tools_v2 import UnifiedWorkstationTools
        tools['furnace_workstation'] = UnifiedWorkstationTools
    except ImportError as e:
        print(f"⚠️ 无法导入 furnace_workstation 工具类: {e}")
    except Exception as e:
        print(f"⚠️ 导入 furnace_workstation 工具类时出错: {e}")

    # 导入 DialysisWorkstation 工具类
    try:
        from DialysisWorkstation_server_tools_v2 import UnifiedWorkstationTools
        tools['DialysisWorkstation'] = UnifiedWorkstationTools
    except ImportError as e:
        print(f"⚠️ 无法导入 DialysisWorkstation 工具类: {e}")
    except Exception as e:
        print(f"⚠️ 导入 DialysisWorkstation 工具类时出错: {e}")

    # 导入 new_centrifugation 工具类
    try:
        from new_centrifugation_server_tools_v2 import UnifiedWorkstationTools
        tools['new_centrifugation'] = UnifiedWorkstationTools
    except ImportError as e:
        print(f"⚠️ 无法导入 new_centrifugation 工具类: {e}")
    except Exception as e:
        print(f"⚠️ 导入 new_centrifugation 工具类时出错: {e}")

    # 导入 angularContact 工具类
    try:
        from angularContact_server_tools_v2 import UnifiedWorkstationTools
        tools['angularContact'] = UnifiedWorkstationTools
    except ImportError as e:
        print(f"⚠️ 无法导入 angularContact 工具类: {e}")
    except Exception as e:
        print(f"⚠️ 导入 angularContact 工具类时出错: {e}")

    # 导入 ultrasonic_cleaning 工具类
    try:
        from ultrasonic_cleaning_server_tools_v2 import UnifiedWorkstationTools
        tools['ultrasonic_cleaning'] = UnifiedWorkstationTools
    except ImportError as e:
        print(f"⚠️ 无法导入 ultrasonic_cleaning 工具类: {e}")
    except Exception as e:
        print(f"⚠️ 导入 ultrasonic_cleaning 工具类时出错: {e}")

    # 导入 TubeFurnace 工具类
    try:
        from TubeFurnace_server_tools_v2 import UnifiedWorkstationTools
        tools['TubeFurnace'] = UnifiedWorkstationTools
    except ImportError as e:
        print(f"⚠️ 无法导入 TubeFurnace 工具类: {e}")
    except Exception as e:
        print(f"⚠️ 导入 TubeFurnace 工具类时出错: {e}")

    # 导入 ElectrochemicalWorkstation_(including_high_speed_camera) 工具类
    try:
        from ElectrochemicalWorkstation_(including_high_speed_camera)_server_tools_v2 import UnifiedWorkstationTools
        tools['ElectrochemicalWorkstation_(including_high_speed_camera)'] = UnifiedWorkstationTools
    except ImportError as e:
        print(f"⚠️ 无法导入 ElectrochemicalWorkstation_(including_high_speed_camera) 工具类: {e}")
    except Exception as e:
        print(f"⚠️ 导入 ElectrochemicalWorkstation_(including_high_speed_camera) 工具类时出错: {e}")

    # 导入 transfer_workstation 工具类
    try:
        from transfer_workstation_server_tools_v2 import UnifiedWorkstationTools
        tools['transfer_workstation'] = UnifiedWorkstationTools
    except ImportError as e:
        print(f"⚠️ 无法导入 transfer_workstation 工具类: {e}")
    except Exception as e:
        print(f"⚠️ 导入 transfer_workstation 工具类时出错: {e}")

    # 导入 sintering_workstation 工具类
    try:
        from sintering_workstation_server_tools_v2 import UnifiedWorkstationTools
        tools['sintering_workstation'] = UnifiedWorkstationTools
    except ImportError as e:
        print(f"⚠️ 无法导入 sintering_workstation 工具类: {e}")
    except Exception as e:
        print(f"⚠️ 导入 sintering_workstation 工具类时出错: {e}")

    # 导入 starting_station 工具类
    try:
        from starting_station_server_tools_v2 import UnifiedWorkstationTools
        tools['starting_station'] = UnifiedWorkstationTools
    except ImportError as e:
        print(f"⚠️ 无法导入 starting_station 工具类: {e}")
    except Exception as e:
        print(f"⚠️ 导入 starting_station 工具类时出错: {e}")

    # 导入 ALDWorkstation 工具类
    try:
        from ALDWorkstation_server_tools_v2 import UnifiedWorkstationTools
        tools['ALDWorkstation'] = UnifiedWorkstationTools
    except ImportError as e:
        print(f"⚠️ 无法导入 ALDWorkstation 工具类: {e}")
    except Exception as e:
        print(f"⚠️ 导入 ALDWorkstation 工具类时出错: {e}")

    # 导入 lithography 工具类
    try:
        from lithography_server_tools_v2 import UnifiedWorkstationTools
        tools['lithography'] = UnifiedWorkstationTools
    except ImportError as e:
        print(f"⚠️ 无法导入 lithography 工具类: {e}")
    except Exception as e:
        print(f"⚠️ 导入 lithography 工具类时出错: {e}")

    # 导入 tptn 工具类
    try:
        from tptn_server_tools_v2 import UnifiedWorkstationTools
        tools['tptn'] = UnifiedWorkstationTools
    except ImportError as e:
        print(f"⚠️ 无法导入 tptn 工具类: {e}")
    except Exception as e:
        print(f"⚠️ 导入 tptn 工具类时出错: {e}")

    # 导入 solid_dispensing 工具类
    try:
        from solid_dispensing_server_tools_v2 import UnifiedWorkstationTools
        tools['solid_dispensing'] = UnifiedWorkstationTools
    except ImportError as e:
        print(f"⚠️ 无法导入 solid_dispensing 工具类: {e}")
    except Exception as e:
        print(f"⚠️ 导入 solid_dispensing 工具类时出错: {e}")

    # 导入 liquid_dispensing 工具类
    try:
        from liquid_dispensing_server_tools_v2 import UnifiedWorkstationTools
        tools['liquid_dispensing'] = UnifiedWorkstationTools
    except ImportError as e:
        print(f"⚠️ 无法导入 liquid_dispensing 工具类: {e}")
    except Exception as e:
        print(f"⚠️ 导入 liquid_dispensing 工具类时出错: {e}")

    # 导入 magnetic_stirring 工具类
    try:
        from magnetic_stirring_server_tools_v2 import UnifiedWorkstationTools
        tools['magnetic_stirring'] = UnifiedWorkstationTools
    except ImportError as e:
        print(f"⚠️ 无法导入 magnetic_stirring 工具类: {e}")
    except Exception as e:
        print(f"⚠️ 导入 magnetic_stirring 工具类时出错: {e}")

    # 导入 liquid_handling_workstation 工具类
    try:
        from liquid_handling_workstation_server_tools_v2 import UnifiedWorkstationTools
        tools['liquid_handling_workstation'] = UnifiedWorkstationTools
    except ImportError as e:
        print(f"⚠️ 无法导入 liquid_handling_workstation 工具类: {e}")
    except Exception as e:
        print(f"⚠️ 导入 liquid_handling_workstation 工具类时出错: {e}")

    # 导入 gn_centrifugation_workstation 工具类
    try:
        from gn_centrifugation_workstation_server_tools_v2 import UnifiedWorkstationTools
        tools['gn_centrifugation_workstation'] = UnifiedWorkstationTools
    except ImportError as e:
        print(f"⚠️ 无法导入 gn_centrifugation_workstation 工具类: {e}")
    except Exception as e:
        print(f"⚠️ 导入 gn_centrifugation_workstation 工具类时出错: {e}")

    # 导入 ustc_mul_solid 工具类
    try:
        from ustc_mul_solid_server_tools_v2 import UnifiedWorkstationTools
        tools['ustc_mul_solid'] = UnifiedWorkstationTools
    except ImportError as e:
        print(f"⚠️ 无法导入 ustc_mul_solid 工具类: {e}")
    except Exception as e:
        print(f"⚠️ 导入 ustc_mul_solid 工具类时出错: {e}")

    # 导入 imbibition 工具类
    try:
        from imbibition_server_tools_v2 import UnifiedWorkstationTools
        tools['imbibition'] = UnifiedWorkstationTools
    except ImportError as e:
        print(f"⚠️ 无法导入 imbibition 工具类: {e}")
    except Exception as e:
        print(f"⚠️ 导入 imbibition 工具类时出错: {e}")

    # 导入 toLC 工具类
    try:
        from toLC_server_tools_v2 import UnifiedWorkstationTools
        tools['toLC'] = UnifiedWorkstationTools
    except ImportError as e:
        print(f"⚠️ 无法导入 toLC 工具类: {e}")
    except Exception as e:
        print(f"⚠️ 导入 toLC 工具类时出错: {e}")

    # 导入 ustc_photocatalysis 工具类
    try:
        from ustc_photocatalysis_server_tools_v2 import UnifiedWorkstationTools
        tools['ustc_photocatalysis'] = UnifiedWorkstationTools
    except ImportError as e:
        print(f"⚠️ 无法导入 ustc_photocatalysis 工具类: {e}")
    except Exception as e:
        print(f"⚠️ 导入 ustc_photocatalysis 工具类时出错: {e}")

    # 导入 ustc_combine_comfirm 工具类
    try:
        from ustc_combine_comfirm_server_tools_v2 import UnifiedWorkstationTools
        tools['ustc_combine_comfirm'] = UnifiedWorkstationTools
    except ImportError as e:
        print(f"⚠️ 无法导入 ustc_combine_comfirm 工具类: {e}")
    except Exception as e:
        print(f"⚠️ 导入 ustc_combine_comfirm 工具类时出错: {e}")

    # 导入 XRD_workstation 工具类
    try:
        from XRD_workstation_server_tools_v2 import UnifiedWorkstationTools
        tools['XRD_workstation'] = UnifiedWorkstationTools
    except ImportError as e:
        print(f"⚠️ 无法导入 XRD_workstation 工具类: {e}")
    except Exception as e:
        print(f"⚠️ 导入 XRD_workstation 工具类时出错: {e}")

    # 导入 high_flux_ir_workstation 工具类
    try:
        from high_flux_ir_workstation_server_tools_v2 import UnifiedWorkstationTools
        tools['high_flux_ir_workstation'] = UnifiedWorkstationTools
    except ImportError as e:
        print(f"⚠️ 无法导入 high_flux_ir_workstation 工具类: {e}")
    except Exception as e:
        print(f"⚠️ 导入 high_flux_ir_workstation 工具类时出错: {e}")

    # 导入 UV_spectrophotometer_workstation 工具类
    try:
        from UV_spectrophotometer_workstation_server_tools_v2 import UnifiedWorkstationTools
        tools['UV_spectrophotometer_workstation'] = UnifiedWorkstationTools
    except ImportError as e:
        print(f"⚠️ 无法导入 UV_spectrophotometer_workstation 工具类: {e}")
    except Exception as e:
        print(f"⚠️ 导入 UV_spectrophotometer_workstation 工具类时出错: {e}")

    # 导入 massSpectrometer 工具类
    try:
        from massSpectrometer_server_tools_v2 import UnifiedWorkstationTools
        tools['massSpectrometer'] = UnifiedWorkstationTools
    except ImportError as e:
        print(f"⚠️ 无法导入 massSpectrometer 工具类: {e}")
    except Exception as e:
        print(f"⚠️ 导入 massSpectrometer 工具类时出错: {e}")

    # 导入 icpms_workstation 工具类
    try:
        from icpms_workstation_server_tools_v2 import UnifiedWorkstationTools
        tools['icpms_workstation'] = UnifiedWorkstationTools
    except ImportError as e:
        print(f"⚠️ 无法导入 icpms_workstation 工具类: {e}")
    except Exception as e:
        print(f"⚠️ 导入 icpms_workstation 工具类时出错: {e}")

    # 导入 Shaker 工具类
    try:
        from Shaker_server_tools_v2 import UnifiedWorkstationTools
        tools['Shaker'] = UnifiedWorkstationTools
    except ImportError as e:
        print(f"⚠️ 无法导入 Shaker 工具类: {e}")
    except Exception as e:
        print(f"⚠️ 导入 Shaker 工具类时出错: {e}")

    # 导入 hts 工具类
    try:
        from hts_server_tools_v2 import UnifiedWorkstationTools
        tools['hts'] = UnifiedWorkstationTools
    except ImportError as e:
        print(f"⚠️ 无法导入 hts 工具类: {e}")
    except Exception as e:
        print(f"⚠️ 导入 hts 工具类时出错: {e}")

    # 导入 peptideSynthesizer 工具类
    try:
        from peptideSynthesizer_server_tools_v2 import UnifiedWorkstationTools
        tools['peptideSynthesizer'] = UnifiedWorkstationTools
    except ImportError as e:
        print(f"⚠️ 无法导入 peptideSynthesizer 工具类: {e}")
    except Exception as e:
        print(f"⚠️ 导入 peptideSynthesizer 工具类时出错: {e}")

    # 导入 electrode_assembly_workstation 工具类
    try:
        from electrode_assembly_workstation_server_tools_v2 import UnifiedWorkstationTools
        tools['electrode_assembly_workstation'] = UnifiedWorkstationTools
    except ImportError as e:
        print(f"⚠️ 无法导入 electrode_assembly_workstation 工具类: {e}")
    except Exception as e:
        print(f"⚠️ 导入 electrode_assembly_workstation 工具类时出错: {e}")

    # 导入 cod 工具类
    try:
        from cod_server_tools_v2 import UnifiedWorkstationTools
        tools['cod'] = UnifiedWorkstationTools
    except ImportError as e:
        print(f"⚠️ 无法导入 cod 工具类: {e}")
    except Exception as e:
        print(f"⚠️ 导入 cod 工具类时出错: {e}")

    # 导入 flow_inj 工具类
    try:
        from flow_inj_server_tools_v2 import UnifiedWorkstationTools
        tools['flow_inj'] = UnifiedWorkstationTools
    except ImportError as e:
        print(f"⚠️ 无法导入 flow_inj 工具类: {e}")
    except Exception as e:
        print(f"⚠️ 导入 flow_inj 工具类时出错: {e}")

    # 导入 elec_chem_storage_workstation 工具类
    try:
        from elec_chem_storage_workstation_server_tools_v2 import UnifiedWorkstationTools
        tools['elec_chem_storage_workstation'] = UnifiedWorkstationTools
    except ImportError as e:
        print(f"⚠️ 无法导入 elec_chem_storage_workstation 工具类: {e}")
    except Exception as e:
        print(f"⚠️ 导入 elec_chem_storage_workstation 工具类时出错: {e}")

    # 导入 microplate_reader 工具类
    try:
        from microplate_reader_server_tools_v2 import UnifiedWorkstationTools
        tools['microplate_reader'] = UnifiedWorkstationTools
    except ImportError as e:
        print(f"⚠️ 无法导入 microplate_reader 工具类: {e}")
    except Exception as e:
        print(f"⚠️ 导入 microplate_reader 工具类时出错: {e}")

    # 导入 federation_k_confirm 工具类
    try:
        from federation_k_confirm_server_tools_v2 import UnifiedWorkstationTools
        tools['federation_k_confirm'] = UnifiedWorkstationTools
    except ImportError as e:
        print(f"⚠️ 无法导入 federation_k_confirm 工具类: {e}")
    except Exception as e:
        print(f"⚠️ 导入 federation_k_confirm 工具类时出错: {e}")

    # 导入 nucleic_acid_extractor 工具类
    try:
        from nucleic_acid_extractor_server_tools_v2 import UnifiedWorkstationTools
        tools['nucleic_acid_extractor'] = UnifiedWorkstationTools
    except ImportError as e:
        print(f"⚠️ 无法导入 nucleic_acid_extractor 工具类: {e}")
    except Exception as e:
        print(f"⚠️ 导入 nucleic_acid_extractor 工具类时出错: {e}")

    # 导入 dryer 工具类
    try:
        from dryer_server_tools_v2 import UnifiedWorkstationTools
        tools['dryer'] = UnifiedWorkstationTools
    except ImportError as e:
        print(f"⚠️ 无法导入 dryer 工具类: {e}")
    except Exception as e:
        print(f"⚠️ 导入 dryer 工具类时出错: {e}")

    # 导入 NitrogenBlowing 工具类
    try:
        from NitrogenBlowing_server_tools_v2 import UnifiedWorkstationTools
        tools['NitrogenBlowing'] = UnifiedWorkstationTools
    except ImportError as e:
        print(f"⚠️ 无法导入 NitrogenBlowing 工具类: {e}")
    except Exception as e:
        print(f"⚠️ 导入 NitrogenBlowing 工具类时出错: {e}")

    # 导入 spotting_workstation 工具类
    try:
        from spotting_workstation_server_tools_v2 import UnifiedWorkstationTools
        tools['spotting_workstation'] = UnifiedWorkstationTools
    except ImportError as e:
        print(f"⚠️ 无法导入 spotting_workstation 工具类: {e}")
    except Exception as e:
        print(f"⚠️ 导入 spotting_workstation 工具类时出错: {e}")

    # 导入 confecting_workstation 工具类
    try:
        from confecting_workstation_server_tools_v2 import UnifiedWorkstationTools
        tools['confecting_workstation'] = UnifiedWorkstationTools
    except ImportError as e:
        print(f"⚠️ 无法导入 confecting_workstation 工具类: {e}")
    except Exception as e:
        print(f"⚠️ 导入 confecting_workstation 工具类时出错: {e}")

    return tools

if __name__ == "__main__":
    # 测试导入
    servers = get_available_servers()
    tools = get_available_tools()
    
    print("="*50)
    print("🔧 AIChemMCP 服务器和工具导入测试")
    print("="*50)
    print(f"✅ 成功导入服务器数量: {len(servers)}")
    print(f"✅ 成功导入工具类数量: {len(tools)}")
    print(f"📋 可用服务器: {', '.join(servers.keys())}")
    print(f"📋 可用工具类: {', '.join(tools.keys())}")
