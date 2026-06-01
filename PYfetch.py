from os.path import basename
import sys
import os
import subprocess
import platform
import psutil

WINDOWS_ASCII_ART = r"""
       _.-;;-._
'-..-'|   ||   |
'-..-'|_.-;;-._|
'-..-'|   ||   |
'-..-'|_.-''-._|
"""
LINUX_ASCII_ART = r"""
    .---.
   /     \
   \.@-@./
   /`\_/`\
  //  _  \\
 | \     )|_
/`\_`>  <_/ \
\__/'---'\__/
"""

def pc_info():
    host = os.uname().nodename.strip()
    if platform.system() == "Linux":
        try:
            info = platform.freedesktop_os_release()
            os_name = info.get("NAME", "Linux").strip()
        except (AttributeError, OSError):
            os_name = "Linux"

    else:
        os_name = platform.system().strip()

        # CPU
    cpu_info = platform.processor()
    cpu_info_usage = psutil.cpu_percent(interval=1)

        # GPU
    get_gpu = subprocess.run("lspci | grep VGA", shell=True, text=True, capture_output=True)
    gpu_info = get_gpu.stdout.strip()

        # RAM
    virtual_mem = psutil.virtual_memory()
    total_ram = virtual_mem.total // (1024**3)

        # DISK
    disk = psutil.disk_usage("/")
    disk_total_gb = disk.total / (1024**3)
    disk_used_gb = disk.used / (1024**3)
    disk_string = f"{disk_used_gb:.1f} GB | {disk_total_gb:.1f} GB ({disk.percent}%)"

        # kernel
    get_kernel= subprocess.run("uname -r", shell=True, text=True, capture_output=True)
    kernel_info = get_kernel.stdout.strip()


    print(f"Host name: {host}")
    print(f"OS name: {os_name} <- /etc/os-release")
    print(f"CPU: {cpu_info} | usage: {cpu_info_usage}")
    print(f"GPU: {gpu_info}")
    print(f"RAM: {total_ram} GB")
    print(f"Disk: {disk_string}")
    print(f"Kernel: {kernel_info}")
    

def user_info():
    # user + uid 
    user = os.getlogin().strip()
    user_uid = os.getuid()

    # shell
    get_shell = subprocess.run("echo $SHELL", shell=True, text=True, capture_output=True)
    shell = get_shell.stdout.strip()

    # env 
    def get_term_env():
        env_path = os.environ.get("VIRTUAL_ENV")
        if env_path:
            env_name = os.path.basename(env_path)
            print(f"Env: {env_name}")
        else: print("Env: env not actived")

    # term type - 'Term: kitty' or 'Term: tmux'
    def get_term_type():
        term_type = os.environ.get('TERM')
        print(f"Term: {term_type}")


    print(f"User: {user} | uID: {user_uid}")
    print(f"Shell: {shell}")
    get_term_env()
    get_term_type()


def main():
    print("PYfetch | By !amnez1a!")
    print("==" * 50)

    if platform.system() == "Linux":
        print(LINUX_ASCII_ART)
    elif platform.system() == "Windows":
        print(WINDOWS_ASCII_ART)

    print("!PC INFO!")
    print("--" * 25)
    pc_info()
    print("--" * 25 + "\n")
    print("!USER INFO!")
    print("--" * 25) 
    user_info()
    print("--" * 25 + "\n")
    print("==" * 50)


if __name__ == "__main__":
    main()

