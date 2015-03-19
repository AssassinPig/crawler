import logging
import sys

def get_logger(name='mylogger', file_name="log.log"):
    logger = logging.getLogger(name)
    formatter = logging.Formatter('%(name)-12s %(asctime)s %(levelname)-8s %(message)s', '%a, %d %b %Y %H:%M:%S',)
    file_handler = logging.FileHandler(file_name)
    file_handler.setFormatter(formatter)
    stream_handler = logging.StreamHandler(sys.stderr)

    logger.setLevel(logging.DEBUG)

    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)

    return logger
