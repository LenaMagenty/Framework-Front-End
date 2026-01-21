import logging
import os


class LoggerConfig:
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    LOGS_DIR_NAME = os.path.join(BASE_DIR, 'logs')
    LOGGER_NAME = 'Logger'
    LOGS_FILE_NAME = os.path.join(LOGS_DIR_NAME, 'test.log')
    LOGS_LEVEL = logging.INFO
    MAX_BYTES = 100000
    BACKUP_COUNT = 10
    FORMAT = '%(asctime)s - %(levelname)s - %(message)s'
    DATETIME_FORMAT = '%Y-%m-%dT%H:%M:%S'
