# 导入库
import random
import time
import subprocess

# 定义颜色变量
RED='\E[1;31m'     # 红
GREEN='\E[1;32m'    # 绿
YELLOW='\E[1;33m'    # 黄
BLUE='\E[1;34m'     # 蓝
PINK='\E[1;35m'     # 粉红
NONE='\E[0m'         # 清除颜色

# 设置运行Linux命令
def exec(com: str):
    result = subprocess.run(com)
    return result

def get_system_type():
    # 判断是Linux还是Termux
    # 获取系统类型
    type = exec("uname -a")
    # 判断
    if "GNU/Linux" in type:
        return "isLinux"
    elif "Android" in type:
        return "isTermux"
    else:
        print(f"{RED}[ {NONE}ERROR{RED} ]{NONE} Unknown system type!")
        return "ERROR"

# 不用介绍
def main():
    type = get_system_type()
    Termux_print = f"""========================================
    Welcome to 
"""
    Linux_print = f""""""
    if type == "isLinux":
        print(f"{GREEN}[ {NONE}INFO{GREEN} ]{NONE} Successfully load Linux program!")
    elif type == "isTermux":
        print(f"{GREEN}[ {NONE}INFO{GREEN} ]{NONE} Successfully load Android program!")
    else:
        return

# 同上
if __name__ == "__main__":
    main()