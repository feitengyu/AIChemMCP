import os
import shutil
import glob

def organize_generated_files():
    """
    将生成的服务器和工具文件移动到指定目录
    """
    # 当前工作目录（AIChemMCP根目录）
    current_dir = os.getcwd()
    
    # 目标目录
    target_dir = os.path.join(current_dir, "servers_and_tools")
    
    # 创建目标目录（如果不存在）
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)
        print(f"📁 创建目标目录: {target_dir}")
    
    # 定义要移动的文件模式
    file_patterns = [
        "*_server_v2.py",      # 统一能力服务器文件
        "*_server_tools_v2.py" # 统一能力工具类文件
    ]
    
    moved_files = []
    
    # 移动文件
    for pattern in file_patterns:
        matching_files = glob.glob(pattern)
        
        for file_path in matching_files:
            if os.path.isfile(file_path):
                target_path = os.path.join(target_dir, file_path)
                
                # 如果目标文件已存在，先删除（或者可以选择备份）
                if os.path.exists(target_path):
                    os.remove(target_path)
                    print(f"🔄 覆盖已存在的文件: {file_path}")
                
                # 移动文件
                shutil.move(file_path, target_path)
                moved_files.append(file_path)
                print(f"✅ 移动文件: {file_path} -> {target_path}")
    
    # 统计结果
    print("\n" + "="*50)
    print(f"📊 文件整理完成！")
    print(f"目标目录: {target_dir}")
    print(f"移动文件数量: {len(moved_files)}")
    
    # 显示移动的文件列表
    if moved_files:
        print("\n📄 移动的文件列表:")
        for file in moved_files:
            print(f"  - {file}")
    else:
        print("❌ 没有找到需要移动的文件")
    
    return moved_files

def check_directory_structure():
    """
    检查目录结构并显示统计信息
    """
    target_dir = os.path.join(os.getcwd(), "servers_and_tools")
    
    if not os.path.exists(target_dir):
        print(f"❌ 目标目录不存在: {target_dir}")
        return
    
    # 统计文件类型
    server_files = glob.glob(os.path.join(target_dir, "*_server_v2.py"))
    tools_files = glob.glob(os.path.join(target_dir, "*_server_tools_v2.py"))
    
    print("\n" + "="*50)
    print("📁 目录结构统计:")
    print(f"目标目录: {target_dir}")
    print(f"服务器文件数量: {len(server_files)}")
    print(f"工具类文件数量: {len(tools_files)}")
    print(f"总文件数量: {len(server_files) + len(tools_files)}")
    
    # 显示设备列表
    devices = set()
    for file in server_files + tools_files:
        filename = os.path.basename(file)
        if "_server_v2.py" in filename:
            device = filename.replace("_server_v2.py", "")
        elif "_server_tools_v2.py" in filename:
            device = filename.replace("_server_tools_v2.py", "")
        else:
            continue
        devices.add(device)
    
    if devices:
        print(f"\n🔧 设备列表 ({len(devices)}个设备):")
        for device in sorted(devices):
            print(f"  - {device}")

def create_import_helper():
    """
    创建一个导入辅助文件，方便后续使用
    """
    target_dir = os.path.join(os.getcwd(), "servers_and_tools")
    
    if not os.path.exists(target_dir):
        print(f"❌ 目标目录不存在: {target_dir}")
        return
    
    # 获取所有服务器文件
    server_files = glob.glob(os.path.join(target_dir, "*_server_v2.py"))
    
    helper_content = """\"\"\"
AIChemMCP 服务器和工具文件导入助手
自动生成的文件 - 用于方便地导入所有工作站服务器
\"\"\"

import os
import sys

# 添加当前目录到Python路径
current_dir = os.path.dirname(os.path.abspath(__file__))
if current_dir not in sys.path:
    sys.path.insert(0, current_dir)

# 自动导入所有服务器函数
def get_available_servers():
    \"\"\"获取所有可用的服务器函数\"\"\"
    servers = {}
    \n"""
    
    # 为每个服务器文件添加导入语句
    for server_file in server_files:
        filename = os.path.basename(server_file)
        device_name = filename.replace("_server_v2.py", "")
        
        # 添加到导入内容
        helper_content += f"    # 导入 {device_name} 服务器\n"
        helper_content += f"    try:\n"
        helper_content += f"        from {device_name}_server_v2 import {device_name}_server_main_loop, {device_name}_server_advertise_capabilities\n"
        helper_content += f"        servers['{device_name}'] = {{\n"
        helper_content += f"            'main_loop': {device_name}_server_main_loop,\n"
        helper_content += f"            'advertise': {device_name}_server_advertise_capabilities\n"
        helper_content += f"        }}\n"
        helper_content += f"    except ImportError as e:\n"
        helper_content += f"        print(f\"⚠️ 无法导入 {device_name} 服务器: {{e}}\")\n"
        helper_content += f"    except Exception as e:\n"
        helper_content += f"        print(f\"⚠️ 导入 {device_name} 服务器时出错: {{e}}\")\n\n"
    
    helper_content += """    return servers

# 自动导入所有工具类
def get_available_tools():
    \"\"\"获取所有可用的工具类\"\"\"
    tools = {}
    \n"""
    
    # 为每个工具文件添加导入语句
    tools_files = glob.glob(os.path.join(target_dir, "*_server_tools_v2.py"))
    for tools_file in tools_files:
        filename = os.path.basename(tools_file)
        device_name = filename.replace("_server_tools_v2.py", "")
        
        helper_content += f"    # 导入 {device_name} 工具类\n"
        helper_content += f"    try:\n"
        helper_content += f"        from {device_name}_server_tools_v2 import UnifiedWorkstationTools\n"
        helper_content += f"        tools['{device_name}'] = UnifiedWorkstationTools\n"
        helper_content += f"    except ImportError as e:\n"
        helper_content += f"        print(f\"⚠️ 无法导入 {device_name} 工具类: {{e}}\")\n"
        helper_content += f"    except Exception as e:\n"
        helper_content += f"        print(f\"⚠️ 导入 {device_name} 工具类时出错: {{e}}\")\n\n"
    
    helper_content += """    return tools

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
"""
    
    # 写入辅助文件
    helper_file = os.path.join(target_dir, "__init__.py")
    with open(helper_file, "w", encoding="utf-8") as f:
        f.write(helper_content)
    
    print(f"✅ 创建导入辅助文件: {helper_file}")

if __name__ == "__main__":
    print("🚀 开始整理生成的服务器和工具文件...")
    print("="*50)
    
    # 第一步：移动文件
    moved_files = organize_generated_files()
    
    # 第二步：检查目录结构
    check_directory_structure()
    
    # 第三步：创建导入辅助文件
    create_import_helper()
    
    print("\n🎉 所有文件整理完成！")
    print("📁 文件已移动到: servers_and_tools/")
    print("🔧 可以使用 import_helper.py 来方便地导入所有服务器和工具")