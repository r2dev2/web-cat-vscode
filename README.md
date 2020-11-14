# WebCat Commandline

Commandline utility for webcat submissions

## Setup

File: web-cat.conf
```
path to java
path to webcat submitter jarfile
url of submission upload
url of snarf
path to browser
```

Example conf file:
```
/usr/bin/java
/home/rbadhe/webcat/web-cat-vscode/jar/webcat-submitter-1.0.5.jar
$lhs
http://cs.lhs.fuhsd.org/apcssnarf/snarf.xml
/Applications/Firefox.app/Contents/MacOS/firefox
```

### Upload

```shell
python3 upload.py path_to_submission_folder
```

### Snarf

```shell
python3 download.py path_to_download_target_folder
```

