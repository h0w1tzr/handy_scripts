#!/bin/bash
COMMAND="grep -i -l -r -i -F"
#PHP RCE functions
$COMMAND putenv > /tmp/results.txt
$COMMAND system >> /tmp/results.txt
$COMMAND passthru >> /tmp/results.txt
$COMMAND popen >> /tmp/results.txt
$COMMAND shell_exec >> /tmp/results.txt
$COMMAND proc_open >> /tmp/results.txt
$COMMAND dl >> /tmp/results.txt
$COMMAND pcntl_exec >> /tmp/results.txt
$COMMAND exec >> /tmp/results.txt

# Database
$COMMAND database >> /tmp/results.txt
$COMMAND dbase >> /tmp/results.txt
$COMMAND postgres >> /tmp/results.txt
$COMMAND alchemy >> /tmp/results.txt
$COMMAND eval >> /tmp/results.txt
$COMMAND sql >> /tmp/results.txt
$COMMAND escape >> /tmp/results.txt
$COMMAND cursor >> /tmp/results.txt
$COMMAND invoke >> /tmp/results.txt

# General Dirty Words
$COMMAND crypt >> /tmp/results.txt
$COMMAND secure >> /tmp/results.txt
$COMMAND auth >> /tmp/results.txt
$COMMAND perm >> /tmp/results.txt
$COMMAND access >> /tmp/results.txt
$COMMAND todo >> /tmp/results.txt
$COMMAND fixme >> /tmp/results.txt
$COMMAND password >> /tmp/results.txt
$COMMAND select >> /tmp/results.txt
$COMMAND update >> /tmp/results.txt
$COMMAND delete >> /tmp/results.txt
$COMMAND backdoor >> /tmp/results.txt
$COMMAND csrf >> /tmp/results.txt
$COMMAND xss >> /tmp/results.txt
sort /tmp/results.txt | uniq | grep -v -F .txt | grep -v -F .git | grep -v -i -F LICENSE | grep -v -i -F .md | grep -v -i -F .png | grep -v -i -F .gif | grep -v -i -F .jpg | grep -v -i -F .css
