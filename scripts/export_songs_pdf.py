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

if __name__ == "__main__":
    repos = [repo for repo in glob.iglob('songs/*')]
    repos.sort()
    for e,repo in enumerate(repos):
        print(str(e).rjust(3, ' ') + ": " "[" + repo + "]")
    selection = input("select with , or -: ").strip().replace(" ", "")
    selected_repo = []
    for sel in selection.split(","):
        if "-" in sel:
            start, end = sel.split("-")
            for i in range(int(start), int(end) + 1):
                selected_repo.append(repos[i])

        else:
            selected_repo.append(repos[int(sel)])
    selected_repo.sort()
    print(selected_repo)
    for repo in selected_repo:
        print(repo)
        add_dir_pdf(repo)
        rm_pdf(repo)
        generate_pdf(repo)
        add_changes(repo)
        if (commit_changes(repo)):
            push_changes(repo)