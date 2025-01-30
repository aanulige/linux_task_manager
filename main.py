import process
import system_info

def main():
    while True:
        print("\n===== Linux 任务管理系统 =====")
        print("1. 列出所有进程")
        print("2. 终止进程")
        print("3. 查看进程详情")
        print("4. 查看系统资源使用情况")
        print("5. 退出")
        choice = input("请输入选项: ")

        if choice == "1":
            process.list_processes()
        elif choice == "2":
            pid = input("请输入要终止的进程 PID: ")
            process.kill_process(pid)
        elif choice == "3":
            pid = input("请输入要查看的进程 PID: ")
            process.process_info(pid)
        elif choice == "4":
            system_info.system_usage()
        elif choice == "5":
            break
        else:
            print(" Invaild input. Please try again.")

    if __name__ == "__main__":
        main()


