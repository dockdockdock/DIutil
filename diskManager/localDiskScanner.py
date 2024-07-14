from flask import Flask, jsonify
import psutil
import sqlite3

app = Flask(__name__)

# 创建数据库连接
def get_db_connection():
    conn = sqlite3.connect('disk_usage.db')
    conn.row_factory = sqlite3.Row
    return conn

# 保存硬盘信息到数据库
def save_disk_info():
    conn = get_db_connection()
    disks = psutil.disk_partitions()
    for disk in disks:
        conn.execute('INSERT INTO disk_info (device, mountpoint) VALUES (?, ?)',
                     (disk.device, disk.mountpoint))
    conn.commit()
    conn.close()

# API端点，返回所有硬盘信息
@app.route('/disks', methods=['GET'])
def get_disks():
    conn = get_db_connection()
    disks = conn.execute('SELECT * FROM disk_info').fetchall()
    conn.close()
    return jsonify([dict(disk) for disk in disks])

# 主函数
if __name__ == '__main__':
    # save_disk_info()  # 启动时保存一次硬盘信息
    app.run(host='0.0.0.0', port=5000)