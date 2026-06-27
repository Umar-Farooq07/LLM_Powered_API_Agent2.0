import logging
import os

from app.core.config import LOG_DIR






def configure_logging():

    os.makedirs(LOG_DIR, exist_ok=True)
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
        
    formatter = logging.Formatter(
    "%(asctime)s | %(levelname)-8s | %(module)s | %(funcName)s | %(message)s"
    )
    console_handler.setFormatter(formatter)

    file_handler = logging.FileHandler(
        filename=os.path.join(LOG_DIR, "app.log"),   
        mode="a",
        encoding="utf-8"
    )
    file_handler.setLevel(logging.INFO)
    file_handler.setFormatter(formatter)

    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    if not logger.handlers:
        logger.addHandler(console_handler)
        logger.addHandler(file_handler)


