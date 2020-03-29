import logging.config
try:
    logging.config.fileConfig(fname='logging.ini', disable_existing_loggers=False)
except KeyError:
    logging.basicConfig(level=logging.INFO)
