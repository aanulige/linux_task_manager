import os

def system_usage():
    """获取 CPU 和 内存使用情况（从 /proc 读取）"""
    with open('/proc/meminfo') as f:
        meminfo = f.readlines()
        mem_total = int(meminfo[0].split()[1])
        mem_free = int(meminfo[1].split()[1])  # 空闲内存
        mem_used = mem_total - mem_free  # 已用内存

    with open("/proc/stat") as f:
        cpu_line = f.readline().split()
        cpu_usage = sum(map(int, cpu_line[1:8]))  # 计算 CPU 使用量

    print("=" * 30)
    print("💻 系统资源使用情况")
    print("=" * 30)
    print(f"内存使用: {mem_used / 1024:.2f} MB / {mem_total / 1024:.2f} MB")
    print(f"CPU 使用量: {cpu_usage} jiffies（时间片单位）")