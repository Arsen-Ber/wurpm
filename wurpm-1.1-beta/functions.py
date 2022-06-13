import os




def install_package(link, package_name, download_path):
    os.system(f"curl -o { download_path }\\{ package_name } { link }")
    print(f"Package:  { package_name }   Installed as: { download_path }\\{ package_name }")
### end func ###


def get_link(frontend_info_for_package, symbols_about_start):
    LIPL = []              #* List Install Package Link *#
    LIPL = list(frontend_info_for_package)      #* List Link IPL   #* link : 54 symbols before start  (and "\r" "\n" in start from bs4 parser)*#
    del LIPL[0:symbols_about_start]
    STRIPL = ''.join(LIPL) #* String Link IPL (link to install package)
    return STRIPL
### end func ###





