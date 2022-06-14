import requests as req
import sys
import os
import pathlib
from bs4 import BeautifulSoup
import functions





"""
* WURPM version: 1.1
* Open source
* WURPM => Windows Users Repository Package Manager
* Dev : MRX
* GitHub : https://github.com/Arsen-Ber/
TOEACH:  WURPM GitHub : https://github.com/Arsen-Ber/wurpm
TOEACH:  I think, I will also create a telegram channel, where you can join the development of this and future projects
"""


DISK = "C"  #* Name of your disk to install packages in PC. Edit, if name of your disk =/= C


downloads_packages = f"{ DISK }:\\Users\\{os.getlogin()}\\Downloads"

path = pathlib.Path().resolve()
does = sys.argv[1]


#########################################################################


#########################################################################



print(f"This packet manager install packages from WUR : Windows Users Repository.")
print( "[ Users Repository from \"Windows\" (unofficial) ]")
print()





package_name = input( f"[{ path }] package >> " )




if does in [ "install-package", "in-pkg", "i-p", "installpackage", "inpkg", "ip" ]:


    print(f"Package : { package_name }")

    WUR = req.get(f"https://arsen-ber.github.io/wurpm/").text


    BSPL = BeautifulSoup(WUR, "lxml")
    FIFP = BSPL.find('a', { "id" : f"{ package_name }"}).get_text()  #* Frontend Info For Package *#

    LTIP = functions.get_link(FIFP, 107)  #* Link To Install Package
    real = input( f"Install package { package_name }? [Y/n]: " )
    


    if real == "y" or real == "Y" or real == "yes" or real == "Yes":
        print(LTIP, package_name, downloads_packages)
        functions.install_package(LTIP, package_name, downloads_packages)


    elif real == "n" or real == "N" or real == "no" or real == "No":
        print("Stopping the installation...")


    else:
        print("!Emergency stop!")




    print()
elif does in [ "remove-package", "rm-pkg", "r-p", "removepackage", "rmpkg", "rp" ]:

    # print("Removing package ", end='')
    os.system(f"rd /s { downloads }\\{ package_name }")

