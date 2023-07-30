import logging
import sys
from datetime import datetime
from pathlib import Path
from typing import Literal
from tqdm.asyncio import tqdm

from loguru import logger


LoggingLevel = Literal["CRITICAL", "ERROR", "WARNING", "INFO", "DEBUG", "SUCCESS"]
LOG_FORMAT = "<white>{time:HH:mm:ss}</white> | <level>{level: <8}</level> | <white>{message}</white>"


def setup_logger(level: LoggingLevel = "DEBUG"):
    logger.remove()
    logger.add(
        lambda msg: tqdm.write(msg, end=''),
        colorize=True,
        format=LOG_FORMAT,
        level=level,
    )
