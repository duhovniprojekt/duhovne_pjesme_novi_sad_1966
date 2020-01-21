#!/usr/bin/env python3

import github

USER = "yourusername"
PASS = "yourpass"
ORGANISATION = "duhovniprojekt"
REPO_NAME = "test123"
FILE_NAME = "README.md"
FILE_COMMIT = "first commit"
FILE_CONTENT = ""
REPO_NAME_PREFIX = "duhovne_pjesme_novi_sad_1966_"

if __name__ == "__main__":
    g = github.Github(USER, PASS)
    user = g.get_user()
    org = g.get_organization(ORGANISATION)

    while(True):
        REPO_NAME = REPO_NAME_PREFIX + input("song: " + REPO_NAME_PREFIX)
        FILE_CONTENT_SUFIX = input("file content: ")
        FILE_CONTENT = "# " + REPO_NAME + "\n" + FILE_CONTENT_SUFIX
        repo = org.create_repo(REPO_NAME)
        repo.create_file(FILE_NAME, FILE_COMMIT, FILE_CONTENT)
        print()
