import requests as req
import sys
import os
import pathlib
from bs4 import BeautifulSoup



"""
* Open source
* WURPM => Windows Users Repository Package Manager
* Dev : MRX
* GitHub : https://github.com/Arsen-Ber/
TOEACH:  WURPM GitHub : https://github.com/Arsen-Ber/wurpm
TOEACH:  I think, I will also create a telegram channel, where you can join the development of this and future projects
"""


path = pathlib.Path().resolve()
does = sys.argv[1]


#########################################################################

def get_link(frontend_info_for_package, symbols_about_start):
    LIPL = []              #* List Install Package Link *#
    LIPL = list(frontend_info_for_package)      #* List Link IPL   #* link : 54 symbols before start  (and "\r" "\n" in start from bs4 parser)*#
    del LIPL[0:symbols_about_start]
    STRIPL = ''.join(LIPL) #* String Link IPL (link to install package)
    return STRIPL
    # print(STRIPL)
## end func ##

def install_package(link, package_name):
    # os.system(f"curl -O { package_name } { link }")
    os.system(f"echo { path }/{ package_name }")
## end func ##

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

    LTIP = get_link(FIFP, 106)  #* Link To Install Package
    print(LTIP)
    install_package(LTIP, package_name)




    print()
elif does in [ "remove-package", "rm-pkg", "r-p", "removepackage", "rmpkg", "rp" ]:

    # print("Removing package ", end='')
    os.system(f"rd /s { package_name }")

