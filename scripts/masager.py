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


EXTENSIONS = [Extensions.MSCZ.value, Extensions.MSCX.value]


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
def convert(path):
    files = find_files_with_extensions_is_path(path, EXTENSIONS)
    for f in files:
        print(f"convert: {f}")
        if f.endswith(Extensions.MSCX.value):
            shutil.move(f, f"{f}.xml")
        elif f.endswith(Extensions.MSCZ.value):
            utils.run_bash_cmd(f"musescore {f} -o {f}.mscx")
            shutil.move(f"{f}.mscx", f"{f}.xml")
            os.remove(f)


@app.command()
def create_model(path):
    utils.run_bash_cmd(f"xsdata --package msmodel {utils.get_full_path(path)}")


@app.callback()
def main():
    pass


if __name__ == "__main__":
    app()
