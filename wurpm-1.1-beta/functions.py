import os
import requests as req
import wget
from time import sleep
import pathlib




def install_package(link, package_name, download_path=f"{ pathlib.Path().resolve() }"):
    try:
        print(f"Package:  { package_name } \nInstalling package...")
        sleep(1.2)
        wget.download(link, f"{download_path}/{package_name}")
        print()
        print(f"Installed as: { download_path }/{ package_name }")
    except FileNotFoundError:
        print(f"Directory \'{ download_path }\' not Found!")
        # print("Error 404")
        # print(f"URL: \"{ link }\" not Found!")
        # print(f"Package: \"{ package_name }\" not Found!")
        print()
        return
### end func ###


def get_link(frontend_info_for_package, symbols_about_start):
    LIPL = []              #* List Install Package Link *#
    LIPL = list(frontend_info_for_package)      #* List Link IPL   #* link : 54 symbols before start  (and "\r" "\n" in start from bs4 parser)*#
    del LIPL[0:symbols_about_start]
    STRIPL = ''.join(LIPL) #* String Link IPL (link to install package) *#
    STRIPLS = STRIPL.strip() #* STRPL strip *#
    return STRIPLS
### end func ###





# Error URL: install_package("https://www.python.org/ftp/python/3.10.5/python-3dghgf.10.5-amd64.exe", "pyyyy.exe", "C:\\Users\\arsen\\Downloads")

def main():
    pylink = "https://www.python.org/ftp/python/3.10.5/python-3.10.5-amd64.exe"
    install_package(pylink, "pylink.exe")

if __name__ == '__main__':
    main()
