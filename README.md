# py_search

## Description

Command line tool to search pattern in files according to a path.

## Requirements

### Python lib:

- os
- PyPDF2
- re
- argparse
- openpyxl
- termcolor

### LibreOffice:

- unoconv

## Usage 

`python3 grepall.py -i a -p b -d c -r d -e f -E g`

`-i a`: path, defaults to `"."`

`-p b`: pattern to find ex: "pattern1,pattern2,...", defaults to `""`

`-d c`: depth of files according to path, defaults to `"max"`, max depth

`-r d`: is the get row flag, if set to `True`, the row of the file where the patterns will be find will be displayed, defaults to `False`

`-e f`: is the files or folder to be excluded during the search ex: `"dir,dir2/a.txt"`, defaults to `""`

`-E G`: is the pattern contained in the excluded file or dir, can be filetype ex: `".pdf,..."` , defaults to `""`

By default the programm won't search in the file with those filetypes:

`[".jpg", ".jpeg", ".gif", ".png", ".mp4", ".mp3", ".avi", ".mkv", ".tar", ".zip", ".dvi", ".gz", ".log"]`

Do not hesitate to add more filetypes to this list if there is an error, in the conf variables, at the top of `grepall.py`
