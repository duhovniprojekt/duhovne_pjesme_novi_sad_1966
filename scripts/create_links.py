#!/usr/bin/env python

import glob
import subprocess

if __name__ == "__main__":
    repos = [repo.split('/')[1] for repo in glob.iglob('songs/*')]
    repos.sort()
    for repo in repos:
        print(repo)
