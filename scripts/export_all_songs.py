#!/usr/bin/env python

import glob

def run_bash_cmd(cmd):
    output = None
    try:
        output = subprocess.check_output(cmd, shell=True).decode('UTF-8').strip()
    except:
        print("exit 1")
    return output

def add_dir_pdf(repo):
    cmd = "mkdir -p " + repo + "/pdf"
    if (run_bash_cmd(cmd) == None):
        print("add_dir_pdf failed")

for repo in glob.iglob('songs/*'):
    add_dir_pdf(repo)