from subprocess import *
from sys import argv
from getpass import getpass

from common import *

if len(argv) > 1:
    url = argv[1]

def getTargets(javalocation, submitterlocation, url):
    targets = check_output([javalocation, "-jar", submitterlocation, "-t", url, "-l"]).decode()
    return targets[:-1]

def submit(javalocation, submitterlocation, url, assignment, username, password, filelocation):
    returnhtml = check_output([
        javalocation, "-jar",
        submitterlocation, 
        "-t", url,
        "-u", username,
        "-p", password,
        "-a", assignment,
        filelocation])
    return returnhtml.decode()[:-1]

def main():
    call("rm result.html", shell=True)
    java, submitter, url, snarf, web_browser = getInfo()
    html = submit(
        java,
        submitter,
        url,
        testassignment,
        getInput("Username? "),
        getpass(),
        testsubmission
    )
    with open("result.html", "w+") as fout:
        fout.write(html)
    viewInBrowser("result.html")
    
if __name__ == "__main__":
    main()
