#!/usr/bin/python
import os
import typer
import utils
import shutil
import xsdata
from enum import Enum

app = typer.Typer(help="Awesome Cinker CLI.")


class Extensions(Enum):
    MSCZ = ".mscz"
    MSCX = ".mscx"


EXTENSIONS = [Extensions.MSCX.value]


def find_files_with_extensions_is_path(path, extensions):
    files_found = []
    for root, dirs, files in os.walk(utils.get_full_path(path)):
        for file in files:
            for e in extensions:
                if file.endswith(e):
                    files_found.append(os.path.join(root, file))
    return files_found


@app.command()
def ls(path):
    print(find_files_with_extensions_is_path(path, EXTENSIONS))


@app.command()
def cp(path, path_copy_to):
    files = find_files_with_extensions_is_path(path, EXTENSIONS)
    for f in files:
        print(f"cp: {f}")
        shutil.copy(f, path_copy_to)


@app.command()
def create_model(path):
    files = find_files_with_extensions_is_path(path, EXTENSIONS)
    for f in files:
        shutil.move(f, f"{f}.xml")
    utils.run_bash_cmd(f"xsdata --package msmodel {utils.get_full_path(path)}")
    for f in files:
        shutil.move(f"{f}.xml", f)


@app.callback()
def main():
    pass


if __name__ == "__main__":
    app()
