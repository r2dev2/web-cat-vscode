from subprocess import *
import os
from sys import argv
from getpass import getpass

from common import *
from score import get_score

def getUsername():
    try:
        username = os.environ["WEBCATUSER"]
    except KeyError:
        print("Set a username with ENV var WEBCATUSER")
        username = input("Username? ")
    return username

def getPassword():
    try:
        password = os.environ["WEBCATPASS"]
    except KeyError:
        print("Set a password with ENV var WEBCATUSER")
        password = getpass()
    return password

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

def main(filepath):
    try:
        os.remove("result.html")
    except FileNotFoundError:
        pass
    java, submitter, url, snarf, web_browser = getInfo()
    targets = getTargets(java, submitter, url).split('\n')
    for i, target in enumerate(targets):
        print(f"{i}\t{target}")
    submission_target = targets[int(input("Which number? "))]
    html = submit(
        java,
        submitter,
        url,
        submission_target,
        getUsername(),
        getPassword(),
        filepath
    )
    # with open("result.html", "w+") as fout:
    #     fout.write(html)
    # viewInBrowser("result.html")
    html = html[html.find("url="):]
    url = html[4:html.find('"')]
    print(repr(url))
    try:
        call(f"echo {url} "
              "| /mnt/c/Windows/System32/WindowsPowerShell/v1.0//powershell.exe "
              "-c clip", shell=True)
        # powershell.exe -c "& \"C:\\Program Files\\Mozilla Firefox\\firefox.exe\" $url"
        call([
            "/mnt/c/Windows/System32/WindowsPowerShell/v1.0//powershell.exe",
            '-c',
            "& \"C:\\Program Files\\Mozilla Firefox\\firefox.exe\"",
            url
        ])
    except:
        pass
    try:
        try:
            correctness, final = get_score(url)
        except:
            correctness, final = get_score(url)
        print("Correctness/Testing:", correctness)
        print("Final score:", final)
    except:
        pass

    
if __name__ == "__main__":
    try:
        main(argv[1])
    except IndexError:
        print("Please give a submission folder")
