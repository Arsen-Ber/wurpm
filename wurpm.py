import requests as req
import sys
import os
import pathlib
from bs4 import BeautifulSoup
import re
import urllib.request



""" 
* Open source
* WURPM => Windows Users Repository Package Manager
* Dev : MRX , real name : "Arsen"
TOEACH: You can visit my youtube channel, most importantly, do not pay attention to videos that are not about programming) 
TOEACH: I think, I will also create a telegram channel in which you can post ideas for open source projects
"""






path = pathlib.Path().resolve()
does = sys.argv[1]





print(f"This packet manager install packages from WUR : Windows Users Repository.")
print( "[ Users Repository from \"Windows\" (unofficial) ]")
print()





packageName = input( f"[{ path }] package >> " )




if does in [ "install-package", "in-pkg", "i-p", "installpackage", "inpkg", "ip" ]:



    WUR = req.get(f"https://arsen-ber.github.io/wurpm/").text


    BSPL = BeautifulSoup(WUR, "lxml")
    IPL = BSPL.find('a', { "id" : f"{ packageName }"}).get_text()
    
    LIPL = []       #* link : 53 symbols before package name *#
    print (IPL)




elif does in [ "remove-package", "rm-pkg", "r-p", "removepackage", "rmpkg", "rp" ]:

    # print("Removing package ", end='')
    os.system(f"rd /s { packageName }")

