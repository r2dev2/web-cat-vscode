import xml.etree.ElementTree as ET
from subprocess import call

import wget

from common import *

def snarfBrowser():
    snarfurl = getInfo()[3]
    snarffile = wget.download(snarfurl, bar = None)
    tree = ET.parse(snarffile)
    root = tree.getroot()
    urls = []
    for i, package in enumerate(root.findall("package")):
        name = package.get("name")
        description = package.find("description").text
        url = package.find("entry").attrib["url"]
        urls.append(url)
        output(f"{i} {name}:\n\t{description}\n")
    call(f"rm '{snarffile}'", shell=True)
    return urls

def main():
    u = snarfBrowser()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print()
