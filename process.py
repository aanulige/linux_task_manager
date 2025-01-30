import os
import signal


def list_processes():
    "List all processes running on this machine"
    print(f"{'PID':<8}{'进程名':<25}{'状态':<10}{'父进程PID'}")
    print("=" * 50)
    for pid in os.listdir("/proc"):
        if pid.isdigit():  # 只处理进程 ID
            try:
                with open(f"/proc/{pid}/status") as f:
                    lines = f.readlines()
                    names = lines[0].split(":")[1].strip()
                    status = lines[1].split(":")[1].strip()
                    ppid = lines[2].split(":")[1].strip()
                    print(f"{pid:<8}{names:<25}{status:<10}{ppid}")
            except Exception as e:
                continue

def process_info(pid):
    """get the info of a pid"""
    try:
        with open(f"/proc/{pid}/status") as f:
            print(f.read())  #直接打印所有进程信息
    except FileNotFoundError:
        print(f" 进程 {pid} 不存在")

def kill_process(pid):
    """kill a process"""
    try:
        os.kill(pid, signal.SIGTERM)
        print(f"进程 {pid} 已终止")
    except ProcessLookupError:
        print(f" 进程 {pid} 不存在")
    except PermissionError:
        print(" 没有权限终止此进程，请使用 sudo 运行")








