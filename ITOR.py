import os
import sys


# TOEACH: ITAR = Install, Tune Or Remove  (wurpm)


main_disk = input( "Enter name for first disk on PC (standart=C): " )
if (main_disk == ""): main_disk = "C"
else: main_disk = main_disk


config_dir = f"{main_disk}:\\Windows\\WURPM"
config_file = f"{main_disk}:\\Windows\\WURPM\\wurpm-config.py"
# print(config_file)
    

if os.path.exists(config_file):
    with open(f"{ config_file }", "r") as CF:
        CFtext = CF.read()

else:
    print("Config File not Found!\nConfig File created...")
    os.sytem(f"mkdir {}")