import zipfile
from subprocess import *
import sys

import wget

from snarfBrowser import *
from common import *

def extractZIP(url, directory):
    zipname = wget.download(url, bar=None)
    with zipfile.ZipFile(zipname, 'r') as zip_ref:
        zip_ref.extractall(directory)
    call(f"rm '{zipname}'", shell=True)

def main(destination="Testing/"):
    urls = snarfBrowser()
    u = urls[int(getInput("Which snarf? "))]
    extractZIP(u, destination)

if __name__ == "__main__":
    try:
        main(sys.argv[1])
    except IndexError:
        main()
