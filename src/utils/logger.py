import logging

logger = logging.getLogger("sena_test")
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler("sena_test.log")
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

def log_error(msg):
    logger.error(msg)

def log_info(msg):
    logger.info(msg)
