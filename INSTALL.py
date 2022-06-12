import os
import sys





main_disk = input( "Enter name for first disk on PC (standart=C): " )
if (main_disk == ""): main_disk = "C"
else: main_disk = main_disk



    
try:    
    config_file = f"{main_disk}:/Windows/WURPM/wurpm-config.py"
    print(config_file)
    os.system(f"cd {config_file}")
    # print(config_file)
    # pass

except:
    print("Config File not Found!\nConfig File created...")



