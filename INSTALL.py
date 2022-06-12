import os
import sys





main_disk = input( "Enter name for first disk on PC (standart=C): " )
if (main_disk == ""): main_disk = "C"
else: main_disk = main_disk


config_file = f"{main_disk}:\\\\Windows\\wurpm-config.py"
# os.system(f"")
# print(config_file)


