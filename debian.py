#fanction Debian distro
import os
def PPA():
    try:
        os.system("echo '# Compiz&emerald repositories | Added by esayINSTALLER\ndeb http://ppa.launchpad.net/adamsmith/compiz-reloaded/ubuntu xenial main' >> /etc/apt/sources.list")
        os.system("echo '# Fusion-icon repositories | Added by esayINSTALLER\ndeb http://ppa.launchpad.net/paquetes-tuquito/main/ubuntu YOUR_UBUNTU_VERSION_HERE main' >> /etc/apt/sources.list")
        os.system("echo '# Conky repositories | Added by esayINSTALLER\ndeb http://ppa.launchpad.net/vincent-c/conky/ubuntu YOUR_UBUNTU_VERSION_HERE main' >> /etc/apt/sources.list")
        os.system("apt-get update -m")
        print("Successfully resolved")
    except EnvironmentError:
        print("EnvironmentError")
def compiz():
    try:
        os.system("apt-get install -y compiz ccsm")
        print("Successfully resolved")
    except EnvironmentError:
        print("EnvironmentError")
def emerald():
    try:
        os.system("apt-get install -y emerald emerald-themes")
        print("Successfully resolved")
    except EnvironmentError:
        print("EnvironmentError")
def Fusion_icon():
    try:
        os.system("dnf install -y fusion-icon")
        print("Successfully resolved")
    except EnvironmentError:
        print("EnvironmentError")
def font_manager():
    try:
        os.system("apt-get install -y fint-manager")
        print("Successfully resolved")
    except EnvironmentError:
        print("EnvironmentError")
def conky():
    try:
        os.systeme("apt-get install -y conky")
        print("Successfully resolved")
    except EnvironmentError:
        print("EnvironmentError")
