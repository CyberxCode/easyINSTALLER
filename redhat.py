#fanction RedHat distro
import os
def compiz():
    try:
        os.system("dnf install -y compiz*")
        print("Successfully resolved")
    except EnvironmentError:
        print("EnvironmentError")
def emerald():
    try:
        os.system("dnf install -y emerald*")
        print("Successfully resolved")
    except EnvironmentError:
        print("EnvironmentError")
def Fusion_icon():
    try:
        os.system("dnf install -y fusion-icon*")
        print("Successfully resolved")
    except EnvironmentError:
        print("EnvironmentError")
def font_manager():
    try:
        os.system("dnf install -y fint-manager*")
        print("Successfully resolved")
    except EnvironmentError:
        print("EnvironmentError")
def conky():
    try:
        os.system("dnf install -y conky*")
        print("Successfully resolved")
    except EnvironmentError:
        print("EnvironmentError")
