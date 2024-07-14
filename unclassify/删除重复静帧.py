import os

# 设置当前目录
directory = os.getcwd()

# 用于保留每组中的第一个文件
first_files = set()

# 遍历目录中的所有文件
for filename in os.listdir(directory):
    # 生成一个关键字，基于文件名中的前三部分（以"_"分割）
    key = '_'.join(filename.split('_', 3)[:3])
    
    # 如果关键字尚未添加到集合中，则将其添加
    if key not in first_files:
        first_files.add(key)
    else:
        # 如果已存在，则删除文件
        os.remove(os.path.join(directory, filename))
        print(f"Deleted {filename}")

print("Cleanup complete.")