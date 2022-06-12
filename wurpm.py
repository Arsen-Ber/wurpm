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





print(f"This packet manager install packages from WUR : Windows Users Repository.")
print( "[ Users Repository from \"Windows\" (unofficial) ]")
print()





packageName = input( f"[{ path }] package >> " )




if does in [ "install-package", "in-pkg", "i-p", "installpackage", "inpkg", "ip" ]:


    print(f"Package : { packageName }")

    WUR = req.get(f"https://arsen-ber.github.io/wurpm/").text


    BSPL = BeautifulSoup(WUR, "lxml")
    FIFP = BSPL.find('a', { "id" : f"{ packageName }"}).get_text()  #* Frontend Info For Package *#
    
    LIPL = []               #* List Install Package Link *#
    LIPL = list(FIFP)    #* List Link IPL   #* link : 54 symbols before start  (and "\r" "\n" in start from bs4 parser)*#
    del LIPL[0:55]
    STRIPL = ''.join(LIPL) #* String Link IPL (link to install package)
    #print(STRIPL)
    





    print()
elif does in [ "remove-package", "rm-pkg", "r-p", "removepackage", "rmpkg", "rp" ]:

    # print("Removing package ", end='')
    os.system(f"rd /s { packageName }")

