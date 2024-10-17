"""
file: main.py
author: Muhammad Bilal Khan <@Hi-kue>
date: 2024-10-13
description: Main runnable file for the application.
notes:
    - ...
"""

from typer import Typer
from lib.logger import logger as log

app = Typer()


@app.command()
def main():
    pass


@app.command()
@app.info("Exports the data from a file to an excel file in the proper format.")
def export_to_excel(file_path: str) -> None:
    pass


if __name__ == "__main__":
    log.info("Starting Solaris-Alpha...")
    app()


    # py main.py --help
    # py main.py --m --ete --f --g --h
