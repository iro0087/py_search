# py_search

## Description

Command line tool to search patterns in files according to a path.

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

`python3 grepall.py -i arg1 -p arg2 -d arg3 -r arg4 -e arg5 -E arg6`

`-i arg1`: path, defaults to `"."`

`-p arg2`: pattern to find ex: "pattern1,pattern2,...", defaults to `""`

`-d arg3`: depth of files according to path, defaults to `"max"`, max depth

`-r arg4`: is the get row flag, if set to `True`, the row of the file where the patterns will be find will be displayed, defaults to `False`

`-e arg5`: is the files or folder to be excluded during the search ex: `"dir,dir2/a.txt"`, defaults to `""`

`-E arg6`: is the pattern contained in the excluded file or dir, can be filetype ex: `".pdf,..."` , defaults to `""`

By default the programm won't search in the file with those filetypes:

`[".jpg", ".jpeg", ".gif", ".png", ".mp4", ".mp3", ".avi", ".mkv", ".tar", ".zip", ".dvi", ".gz", ".log"]`

Do not hesitate to add more filetypes to this list if there is an error, in the conf variables, at the top of `grepall.py`
