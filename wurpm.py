import requests as req
import sys
import os
import pathlib
from bs4 import BeautifulSoup




path = pathlib.Path().resolve()
does = sys.argv[1]





print("This packet manager install packages from AUR : Arch User Repository.")
print( "( User Repository from \"GNU/Linux Arch\" )")
print()






packageName = input( f"[{ path }] package >> " )




if does in [ "install-package", "in-pkg", "i-p", "installpackage", "inpkg", "ip" ]:

    # try:





    WUR = req.get(f"https://arsen-ber.github.io/wurpm/").text


    BSPL = BeautifulSoup(WUR, "lxml")
    IPL = BSPL.find('a')#.get_text()
    # HIPL = IPL.find('a')
    print(IPL)
    # IPL


    try:


        pass




    except:
        print(f"Error: package \"{ packageName }\" not found!")


    # print(GPL)






    # except AttributeError:
    #     print(f"Error: Package '{ packageName }' not found!")






elif does in [ "remove-package", "rm-pkg", "r-p", "removepackage", "rmpkg", "rp" ]:

    # print("Removing package ", end='')
    os.system(f"rd /s { packageName }")

