import os
import sys




WURPM_version = 1.1
user = os.getlogin()



# TOEACH: ITAR = Install, Tune Or Remove  (wurpm)

def main():

    main_disk = input( "Enter name for first disk on PC (standart=C): " )
    if (main_disk == ""): main_disk = "C"
    else: main_disk = main_disk


    param = input("Choose action.\n1. Create config dir / file \n2. None \n3. None \n>>> ")


    config_dir = f"{main_disk}:\\Users\\{user}\\WURPM-{WURPM_version}"
    print(config_dir)
    config_file = f"{config_dir}\\wurpm-config.py"
    # print(config_file)
        

    print()


    if param == "1":
        print(f"Path to config file: { config_file }")
        
        if os.path.exists(config_file):
            print("Config File has Found.")
            with open(f"{ config_file }", "r") as CF:
                CFtext = CF.read()
                print()
                print(CFtext)

        elif os.path.exists(config_file) == False:
            print("Config File not Found!")
            #print(config_file)
            if os.path.exists(config_dir) == False:
                os.system(f"mkdir { config_dir }")
            elif os.path.exists(config_dir):
                print("Config File created...")





if __name__ == '__main__':
    main()



