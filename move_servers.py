import os
import shutil

# 你的项目路径
BASE_DIR = r"AIChemMCP"
JSON_TO_PY_DIR = os.path.join(BASE_DIR, "json_to_python")   # 生成代码的文件夹
SERVERS_DIR = os.path.join(BASE_DIR, "servers")                  # 目标文件夹

def main():
    # 创建目标文件夹（若不存在）
    os.makedirs(SERVERS_DIR, exist_ok=True)

    # 遍历 json_to_python 文件夹
    for filename in os.listdir(JSON_TO_PY_DIR):
        if filename.endswith("_server.py"):
            src = os.path.join(JSON_TO_PY_DIR, filename)
            dst = os.path.join(SERVERS_DIR, filename)

            print(f"移动 {filename} → servers/ ...")

            try:
                shutil.move(src, dst)
                print(f"  ✔ 成功移动到 {dst}")
            except Exception as e:
                print(f"  ❌ 移动失败：{e}")

    print("\n🎉 所有服务器类文件移动完成！")


if __name__ == "__main__":
    main()
