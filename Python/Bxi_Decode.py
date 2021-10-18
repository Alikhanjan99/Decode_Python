try:
    import os
    import sys
    import subprocess
    import requests
except ImportError:
    os.system("pip install requests")
import requests

v="2.4"
arch=subprocess.check_output("uname -om", shell=True).decode()
os.system("clear")
print(" Checking Update . . .")
vf=(requests.get("https://raw.githubusercontent.com/Binyamin-binni/bxi/main/version").text).rstrip()

if os.path.isfile("bxi") and v==vf:
    os.system("chmod 777 bxi && ./bxi")
else:
    os.system("rm -rf bxi bxi.py")
    os.system("curl -L -o bxi.py https://raw.githubusercontent.com/Binyamin-binni/bxi/main/bxi.py")
    if "Android" in arch:
        if "arm" in arch:
            os.system("curl -L -o bxi https://raw.githubusercontent.com/Binyamin-binni/dynamic/main/bxi/arm/bxi")
            os.system("chmod 777 bxi && ./bxi")
        elif "aarch" in arch:
            os.system("curl -L -o bxi https://raw.githubusercontent.com/Binyamin-binni/dynamic/main/bxi/aarch64/bxi")
            os.system("chmod 777 bxi && ./bxi")
        else:
            print(" Unknown architecture, contact with owner.")
    else:
        print(" Unknown machine, contact with owner.")
