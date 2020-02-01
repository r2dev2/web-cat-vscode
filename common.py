from subprocess import *

lhsurl="http://205.173.41.10/Web-CAT/WebObjects/Web-CAT.woa/wa/assignments/eclipse"
testassignment = "CS 2370/Python Test Case: Basic Function"
testsubmission = "/home/rbadhe/Dropbox/workspacePython/Basic Function/"

def output(msg):
    print(msg)

def getInput(prompt = ''):
    return input(prompt)

def viewInBrowser(htmlFile):
    browser = getInfo()[3]
    call([browser, htmlFile])

# Returns java installation, submitter, testingurl, web browser location
def getInfo(filename = "web-cat.conf"):
    f = open(filename, "a+")
    f.close()
    f = open(filename, 'r')
    contents = f.readlines()
    f.close()
    for i, s in enumerate(contents):
        if "$lhs" in s:
            new = lhsurl
        elif len(s) <=1:
            contents.pop(i)
            continue
        elif s[-1] == '\n':
            new = s[:-1]
        else:
            new = s
        contents[i] = new
    return tuple(contents)

def setInfo(filename = "web-cat.conf"):
    f = open(filename, "a+")
    f.close()
    call(f"rm {filename}", shell = True)
    java_location = getInput("Java location? ")
    submitter_location = getInput("Submitter location? ")
    target_url = getInput("Target url? ")
    web_browser_location = getInput("Web browser location? ")
    with open(filename, "w+") as fout:
        fout.write(java_location + '\n')
        fout.write(submitter_location + '\n')
        fout.write(target_url + '\n')
        fout.write(web_browser_location + '\n'*2)
