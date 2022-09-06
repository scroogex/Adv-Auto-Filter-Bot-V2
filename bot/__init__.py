#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) @AlbertEinsteinTG

import os
import logging
import time

from logging.handlers import RotatingFileHandler

from .translation import Translation

# Change Accordingly While Deploying To A VPS
APP_ID = int(os.environ.get(6766195))

API_HASH = os.environ.get("95900e1df408a32d044c1939a2ba4fd9")

BOT_TOKEN = os.environ.get("5486073394:AAFg22KiQh9DZK1kmSBXwUGRf3OQ5K1ggOY")

DB_URI = os.environ.get("mongodb+srv://perera51:perera51@cluster0.2qasku1.mongodb.net/?retryWrites=true&w=majority")

USER_SESSION = os.environ.get("1BVtsOMcBu6uTBV7IXXZHW80STEe02v1t1-HIEZesAO__BG3ZkeqQLglbPNhlk9EyyvMMhYESQfpeSfGoPT4VDJuf9g9oYKA_4he1zlRUTKA7uEv0y9ltya6pW8SWPec2gC51YroSfFiyR67ICYPNgiOAJKW4UckZ3ssRN3A7be7XfKQys_Nhiws5RRlLi-weOPJPpspXwner7f2eWI-L9ciOwYR986kYld7djSjHf3xnwAEKi677kKO67kWmrsy1SY0qQRM73A-9ABXBxbo6XW5ClDdrODWY_4JAJsjQ4x0E5JlXNzWAnNRM_t_UavSuvu3akYCnX6Ghx0jVCK5PPfq_VghfklA=")

VERIFY = {}

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            "autofilterbot.txt",
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

start_uptime = time.time()


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
