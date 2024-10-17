"""
file: file_reader.py
authors:
    - Muhammad Bilal Khan <@Hi-kue>
date: 2024-10-13
description:
    - This file is responsible for reading .txt, .json, and .csv files for the application.
notes:
    - As it can ready various file formats, the format must be altered to match either
      the following:
        - ADMIN_FORMAT
        - CLIENT_FORMAT
    - Note that the file reader is responsible for reading the files and understanding the content.
    - The file reader is also responsible for altering the file to fit the desired format.
    - AI may be used to alter the file to fit the desired format.
questions:
    - *Should we use AI to alter the data from the file to fit the formats?*
"""

ADMIN_FORMAT = """
    id: {id}
    name: {name}
    email: {email}
    password: {password}
    is_active: {is_active}
    is_superuser: {is_superuser}
"""

CLIENT_FORMAT = """
    id: {id}
    name: {name}
    email: {email}
    kwargs: {kwargs}
"""


def read_file(file_path: str, read_type: str) -> None:
    with open(file_path, read_type) as file:
        pass


def conform_to_format(file_path: str, read_type: str, format: str) -> None:
    with open(file_path, read_type) as file:
        pass


def strip_format(file_path: str, read_type: str, format: str) -> None:
    with open(file_path, read_type) as file:
        pass


"""
TODO:
   - Simple Task: Reading files and understanding the content within the file.
      - Every file must have a specific format to follow.
   - AI Task
        - If the file is not of the desired format, but the content is still valid and meaningful,
          get the AI to understand the content and restructure the file in its desired format.
"""
