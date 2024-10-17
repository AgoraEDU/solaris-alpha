"""
file: main.py
author: Muhammad Bilal Khan <@Hi-kue>
date: 2024-10-13
description: Logging module for logging messages to the console effectively.
notes:
    - This module requires the `rich` library to be installed for it to work.
    - Use extensively throughout the app to perform logging and understand program flow better.
        - Often times, we use `logger.info("message")` to log messages at info level.
        - We also use `logger.debug("message")` to log messages at debug level.
        - If there is an issue, we ensure to use `logger.error("message")` to log error messages.
"""


import time
import logging
from rich.logging import RichHandler

start_time = time.time()  # time::now
logging.basicConfig(
    format="{asctime} - {levelname}: {message}",
    style="{",
    datefmt="%Y-%m-%d %H:%M",
    level=logging.INFO,
    handlers=[RichHandler()]
)
logger = logging.getLogger("rich")
