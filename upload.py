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
    output(getTargets("/usr/bin/java", "/home/rbadhe/Webcat/lib/webcat-submitter-1.0.5.jar", url))
    output(submit(
        "/usr/bin/java",
        "/home/rbadhe/Webcat/lib/webcat-submitter-1.0.5.jar",
        lhsurl,
        testassignment,
        "5180165",
        getpass(),
        testsubmission
        ))
    
if __name__ == "__main__":
    main()
