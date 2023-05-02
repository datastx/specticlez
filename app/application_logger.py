from typing import Optional
import logging
import sys
import json


class JSONFormatter(logging.Formatter):
    def format(self, record: logging.LogRecord) -> str:
        log_dict = {
            'timestamp': self.formatTime(record, self.datefmt),
            'name': record.name,
            'level': record.levelname,
            'message': record.getMessage(),
        }
        return json.dumps(log_dict)

def setup_logger(log_format: Optional[str] = None) -> logging.Logger:
    # ANSI escape code for red text
    red = "\033[31m"
    reset = "\033[0m"

    logger = logging.getLogger('file_processor')
    logger.setLevel(logging.INFO)

    handler = logging.StreamHandler(sys.stdout)

    if log_format == 'json':
        formatter = JSONFormatter()
    else:
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s')
        handler.addFilter(ColorizeErrorFilter(red, reset))

    handler.setFormatter(formatter)
    logger.addHandler(handler)

    logger.info("Logger created and configured.")
    if log_format == 'json':
        logger.info("Using JSON log format.")

    return logger

class ColorizeErrorFilter(logging.Filter):
    def __init__(self, red: str, reset: str):
        super().__init__()
        self.red = red
        self.reset = reset

    def filter(self, record: logging.LogRecord) -> bool:
        if record.levelno >= logging.ERROR:
            record.msg = f"{self.red}{record.msg}{self.reset}"
        return True

