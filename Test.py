# 导入库
import subprocess
import platform

# 定义颜色变量
RED = "\033[31m"       # 红
GREEN = '\033[1;32m'     # 绿
YELLOW = '\033[1;33m'    # 黄
NONE = '\033[0m'         # 清除颜色

# 设置运行Linux命令
def exec(com: str):
    try:
        result = subprocess.run(com, shell=True, capture_output=True, text=True)
        return result.stdout.strip()  # 返回标准输出的字符串
    except Exception as e:
        print(f"{RED}[ {NONE}ERROR{RED} ]{NONE} Failed to execute command: {e}")
        return None

def get_system_type():
    # 判断系统类型
    try:
        system_name = platform.system()
        if system_name == "Linux":
            return "isLinux"
        elif system_name == "Windows":
            return "isWindows"
        elif system_name == "Java":
            return "isTermux"
        else:
            return "isOther"
    except Exception as e:
        print(f"{RED}[ {NONE}ERROR{RED} ]{NONE} Error while determining system type: {e}")
        return "ERROR"

def main():
    system_type = get_system_type()
    Termux_print = f"""{RED}========================================{NONE}
Welcome to Minecraft Server Manager for Termux!
In Termux Version. You can't install or remove Minecraft Server.
You must install a rootfs container to run with Linux and you can install or remove Minecraft Server
Please input what do you want to do:
{YELLOW}---------------------------------
{GREEN}0. {NONE}Update Script.
{YELLOW}---------------------------------
{GREEN}1. {NONE}Install rootfs container.
{GREEN}2. {NONE}Remove rootfs container.
{YELLOW}---------------------------------
{GREEN}4. {NONE}Exit script.
{YELLOW}=================================
> 
"""
    Linux_print = f"""{RED}========================================{NONE}
Welcome to Minecraft Server Manager for Linux!
Please input what do you want to do:
{YELLOW}---------------------------------
{GREEN}0. {NONE}Update Script.
{YELLOW}---------------------------------
{GREEN}1. {NONE}Install Minecraft Server.
{GREEN}2. {NONE}Remove Minecraft Server.
{GREEN}3. {NONE}Edit Minecraft Server.
{YELLOW}---------------------------------
{GREEN}4. {NONE}Change install mirror.
{YELLOW}---------------------------------
{GREEN}5. {NONE}About Script.
{GREEN}6. {NONE}Exit Script.
{YELLOW}=================================
> 
"""
    Windows_print = f"""{RED}========================================{NONE}
Welcome to Minecraft Server Manager for Windows!
Please input what do you want to do:
{YELLOW}---------------------------------
{GREEN}0. {NONE}Update Script.
{YELLOW}---------------------------------
{GREEN}1. {NONE}Install Minecraft Server.
{GREEN}2. {NONE}Remove Minecraft Server.
{GREEN}3. {NONE}Edit Minecraft Server.
{YELLOW}---------------------------------
{GREEN}4. {NONE}Exit Script.
{YELLOW}=================================
> 
"""
    if system_type == "isLinux":
        print(f"{GREEN}[ {NONE}INFO{GREEN} ]{NONE} Successfully loaded Linux program!")
        result = input(Linux_print)
    elif system_type == "isWindows":
        print(f"{GREEN}[ {NONE}INFO{GREEN} ]{NONE} Successfully loaded Windows program!")
        result = input(Windows_print)
    elif system_type == "isTermux":
        print(f"{GREEN}[ {NONE}INFO{GREEN} ]{NONE} Successfully loaded Android program!")
        result = input(Termux_print)
    elif system_type == "isOther":
        print(f"{RED}[ {NONE}ERROR{RED} ]{NONE} Unsupported system type!")
    else:
        print(f"{RED}[ {NONE}ERROR{RED} ]{NONE} Unknown error occurred!")

if __name__ == "__main__":
    main()
