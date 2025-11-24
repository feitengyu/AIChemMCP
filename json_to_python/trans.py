import json
import os
import glob
import argparse
import sys

def format_json_files(directory, backup=True, output_dir=None):
    """
    格式化指定目录中的所有JSON文件
    
    参数:
    directory: 包含JSON文件的目录路径
    backup: 是否创建备份文件
    output_dir: 输出目录（如果为None，则覆盖原文件）
    """
    # 确保目录存在
    if not os.path.isdir(directory):
        print(f"错误: 目录 '{directory}' 不存在")
        return
    
    # 如果指定了输出目录，确保它存在
    if output_dir and not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # 获取目录下所有JSON文件
    json_files = glob.glob(os.path.join(directory, '*.json'))
    
    if not json_files:
        print(f"在 '{directory}' 中没有找到JSON文件")
        return
    
    print(f"找到 {len(json_files)} 个JSON文件")
    
    processed_count = 0
    error_count = 0
    
    for file_path in json_files:
        try:
            # 读取JSON文件
            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            # 确定输出路径
            if output_dir:
                output_path = os.path.join(output_dir, os.path.basename(file_path))
            else:
                output_path = file_path
                
            # 如果需要备份且是覆盖原文件
            if backup and not output_dir:
                backup_path = file_path + '.bak'
                os.rename(file_path, backup_path)
                print(f"已创建备份: {backup_path}")
            
            # 格式化并写回文件（ensure_ascii=False将Unicode转义序列转换为实际字符）
            with open(output_path, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=4, sort_keys=True)
            
            processed_count += 1
            print(f"已格式化: {os.path.basename(file_path)}")
            
        except json.JSONDecodeError as e:
            error_count += 1
            print(f"JSON解析错误 ({os.path.basename(file_path)}): {str(e)}")
        except Exception as e:
            error_count += 1
            print(f"处理文件 {os.path.basename(file_path)} 时出错: {str(e)}")
    
    print(f"\n处理完成: {processed_count} 个文件成功, {error_count} 个文件失败")

def main():
    # 设置命令行参数解析
    parser = argparse.ArgumentParser(description='批量格式化JSON文件')
    parser.add_argument('directory', help='包含JSON文件的目录路径')
    parser.add_argument('--output', '-o', help='输出目录（如果不指定则覆盖原文件）')
    parser.add_argument('--no-backup', action='store_true', help='不创建备份文件')
    
    # 解析参数
    if len(sys.argv) > 1:
        args = parser.parse_args()
        format_json_files(
            directory=args.directory,
            backup=not args.no_backup,
            output_dir=args.output
        )
    else:
        # 如果没有提供命令行参数，则使用交互模式
        directory = input("请输入JSON文件所在目录的路径: ").strip()
        if not directory:
            directory = '.'  # 当前目录
            
        backup_choice = input("是否创建备份文件? (y/n, 默认: y): ").strip().lower()
        backup = backup_choice != 'n'
        
        output_dir = input("输出目录 (直接回车覆盖原文件): ").strip()
        if not output_dir:
            output_dir = None
            
        format_json_files(directory, backup, output_dir)

if __name__ == '__main__':
    main()