# gunicorn_logconfig.py

import logging
import sys

class FilterWinch(logging.Filter):
    def filter(self, record):
        return "winch" not in record.getMessage()

loglevel = "info"
errorlog = "-"
accesslog = "-"
logconfig_dict = {
    "version": 1,
    "disable_existing_loggers": False,
    "filters": {
        "no_winch": {
            "()": FilterWinch,
        }
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "stream": sys.stdout,
            "filters": ["no_winch"],
            "formatter": "generic"
        }
    },
    "formatters": {
        "generic": {
            "format": "%(asctime)s [%(process)d] [%(levelname)s] %(message)s",
            "datefmt": "%Y-%m-%d %H:%M:%S",
        }
    },
    "root": {
        "level": "INFO",
        "handlers": ["console"]
    }
}
