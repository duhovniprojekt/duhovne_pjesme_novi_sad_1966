#!/usr/bin/env python

import glob
import subprocess


def read_lines_from_file(filename):
    lines = []
    with open('./' + filename, 'r') as f:
        lines = f.readlines()
    return lines


def write_lines_to_file(lines, filename):
    print("write_lines_to_file " + filename)
    with open(filename, 'w') as f:
        f.write("".join(lines))


def get_html_start():
    html_list = []
    html_list.append('<!DOCTYPE html>')
    html_list.append('<html>')
    html_list.append('<head>')
    html_list.append('<meta charset="utf-8" />')
    html_list.append('<meta name="viewport" content="width=device-width">')
    html_list.append('</head>')
    html_list.append('<body>')
    html_list.append('<h1>Duhovne Pjesme Novi Sad 1966</h1>')
    html_list.append('<dl>')
    return html_list


def get_html_end():
    html_list = []
    html_list.append('</dl>')
    html_list.append('</body>')
    html_list.append('</html>')
    return html_list


def get_html_list_element(song, lyrics):
    html_list = []
    html_list.append('<dt><h3><a href="' + get_pdf_link(song) + '">' + song + '</a></h3></dt>')
    html_list.append('<dd>' + lyrics + '</dd>')
    return html_list

def get_pdf_link(song):
    return 'https://nbviewer.jupyter.org/github/duhovniprojekt/duhovne_pjesme_novi_sad_1966_' + song + '/blob/master/pdf/' + song + '.pdf'

if __name__ == "__main__":
    html_list = []
    html_list.extend(get_html_start())
    repos = [repo.split('/')[1] for repo in glob.iglob('songs/*')]
    repos.sort()
    for repo in repos:
        file_lines = read_lines_from_file('songs/' + repo + '/README.md')
        html_list.extend(get_html_list_element(repo, file_lines[1].strip()))
    html_list.extend(get_html_end())

    write_lines_to_file(html_list, '/home/schef/index.html')
