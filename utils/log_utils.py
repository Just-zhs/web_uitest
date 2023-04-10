import logging

logger = logging.getLogger("log")
ch1 = logging.FileHandler("../mylog.log", encoding='utf-8')
ch1.setLevel(logging.DEBUG)
# create formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# add formatter to ch
ch1.setFormatter(formatter)

# add ch to logger
logger.addHandler(ch1)