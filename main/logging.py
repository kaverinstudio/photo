import logging
import logging.config

logging.config.dictConfig({
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'long': {
            'format': "%(asctime)s | %(levelname)8s | %(name)10s | %(filename)s.%(funcName)s:%(lineno)s - %(message)s",
        },
        'short': {
            'format': "%(asctime)s|%(levelname)s|%(name)s - %(message)s",
        },
    },
    'handlers': {
        'default': {
            'formatter': 'long',
            'class': 'logging.StreamHandler',
        },
        'file': {
            'formatter': 'short',
            'class': 'logging.FileHandler',
            'filename': 'log.log',
            'encoding': 'utf-8',
        },
    },
    'loggers': {

        '': {
            'handlers': ['default', 'file'],
            'level': 'WARNING',
            'propagate': True,
        }}})

logger = logging.getLogger(__name__)
