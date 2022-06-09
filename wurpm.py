import requests as req
import sys
import os
import pathlib
from bs4 import BeautifulSoup




path = pathlib.Path().resolve()
does = sys.argv[1]





print(f"This packet manager install packages from WUR : Windows User Repository.")
print( "[ User Repository from \"Windows\" (unofficial) ]")
print()





packageName = input( f"[{ path }] package >> " )




if does in [ "install-package", "in-pkg", "i-p", "installpackage", "inpkg", "ip" ]:

    # try:





    WUR = req.get(f"https://arsen-ber.github.io/wurpm/").text


    BSPL = BeautifulSoup(WUR, "lxml")
    IPL = BSPL.find('a', { "id" : f"{ packageName }"})#.get_text()
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

