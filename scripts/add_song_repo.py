#!/usr/bin/env python

import subprocess
import sys

# git submodule add https://github.com/duhovniprojekt/duhovne_pjesme_novi_sad_1966_019 songs/019
# mkdir -p songs/019/musescore/
# cd songs/019/musescore/
# mv ~/Downloads/19.mscz ./
# git add .
# git commit -m "added unclean version"
# git push
# cd ../../../
# git add .
# git commit -m "added repo 019"
# git push

def run_bash_cmd(cmd):
    output = None
    try:
        output = subprocess.check_output(cmd, shell=True).decode('UTF-8').strip()
    except:
        print("exit 1")
    return output

def get_padded_num(num):
    return str(num).rjust(3, '0')

def get_song_path(num):
    return "songs/" + get_padded_num(num) + "/musescore/"

def add_submodule(num):
    cmd = "git submodule add https://github.com/duhovniprojekt/duhovne_pjesme_novi_sad_1966_" + get_padded_num(num) + " songs/" + get_padded_num(num)
    if (run_bash_cmd(cmd) == None):
        print("add_submodule failed")

def add_dir(num):
    cmd = "mkdir -p songs/" + get_padded_num(num) + "/musescore/"
    if (run_bash_cmd(cmd) == None):
        print("add_dir failed")

def move_file(num, file_name):
    cmd = "mv " + file_name + " songs/" + get_padded_num(num) + "/musescore/"
    if (run_bash_cmd(cmd) == None):
        print("move_file failed")

def git_commit_song(num, message):
    cmd = "git -C " + get_song_path(num) + " add ."
    if (run_bash_cmd(cmd) == None):
        print("git_commit_song add failed")

    cmd = "git -C " + get_song_path(num) + " commit -m " + "\"" + message + "\""
    if (run_bash_cmd(cmd) == None):
        print("git_commit_song commit failed")
        
    cmd = "git -C " + get_song_path(num) + " push"
    if (run_bash_cmd(cmd) == None):
        print("git_commit_song push failed")

def git_commit_repo(message):
    cmd = "git add ."
    if (run_bash_cmd(cmd) == None):
        print("git_commit_repo add failed")

    cmd = "git commit -m " + "\"" + message + "\""
    if (run_bash_cmd(cmd) == None):
        print("git_commit_repo commit failed")
        
    cmd = "git push"
    if (run_bash_cmd(cmd) == None):
        print("git_commit_repo push failed")

if __name__ == "__main__":
    num = sys.argv[1]
    file_name = sys.argv[2]

    print("ACTION: add_submodule")
    print("https://github.com/organizations/duhovniprojekt/repositories/new")
    print("duhovne_pjesme_novi_sad_1966_" + get_padded_num(num))
    input("Press Enter to continue:")
    add_submodule(num)
    
    print("ACTION: add_dir")
    input("Press Enter to continue:")
    add_dir(num)
    
    print("ACTION: move_file")
    input("Press Enter to continue:")
    move_file(num, file_name)
    
    print("ACTION: git_commit_song")
    input("Press Enter to continue:")
    git_commit_song(num, "added unclean version")
    
    print("ACTION: git_commit_repo")
    input("Press Enter to continue:")
    git_commit_repo("added repo " + get_padded_num(num))