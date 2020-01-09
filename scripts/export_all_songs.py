#!/usr/bin/env python

import glob
import subprocess

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
        exit(1)

def rm_pdf(repo):
    cmd = "rm -rvf " + repo + "/pdf/*"
    if (run_bash_cmd(cmd) == None):
        print("rm_pdf failed")
        exit(1)

def generate_pdf(repo):
    cmd = "musescore " + repo + "/musescore/* -o " + repo + "/pdf/" + repo.split('/')[1] + ".pdf"
    if (run_bash_cmd(cmd) == None):
        print("generate_pdf failed")
        exit(1)

def add_changes(repo):
    cmd = "git -C " + repo + " add ."
    if (run_bash_cmd(cmd) == None):
        print("add_changes failed")
        exit(1)

def commit_changes(repo):
    cmd = "git -C " + repo + " commit -m \"auto generated pdf\""
    if (run_bash_cmd(cmd) == None):
        print("commit_changes failed")
        return False
    return True

def push_changes(repo):
    cmd = "git -C " + repo + " push"
    if (run_bash_cmd(cmd) == None):
        print("push_changes failed")
        exit(1)

for repo in glob.iglob('songs/*'):
    print(repo)
    # add_dir_pdf(repo)
    # rm_pdf(repo)
    # generate_pdf(repo)
    add_changes(repo)
    if (commit_changes(repo)):
        push_changes(repo)
