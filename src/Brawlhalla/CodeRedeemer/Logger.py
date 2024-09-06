import os
import logging
import colorlog
import Brawlhalla.Config.config as conf


LOG_DIR = conf.LOG_DIR

if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

log_file = os.path.join(LOG_DIR, 'app.log')


APP_LOG_FORMAT = "%(asctime)s - %(filename)s:%(lineno)d - %(funcName)s() - %(levelname)s - %(message)s"


color_formatter = colorlog.ColoredFormatter(
    f"%(log_color)s{APP_LOG_FORMAT}",
    datefmt=None,
    reset=True,
    log_colors={
        'DEBUG': 'cyan',
        'INFO': 'green',
        'WARNING': 'yellow',
        'ERROR': 'red',
        'CRITICAL': 'bold_red',
    },
    style='%'
)


# Configure file handlers
file_handler = logging.FileHandler(log_file, encoding="utf-8")
file_handler.setLevel(logging.INFO)  # Log everything at INFO level and above
file_handler.setFormatter(logging.Formatter(APP_LOG_FORMAT))


# Configure console handler
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)  # Show INFO level and above in console
console_handler.setFormatter(color_formatter)

# Set up the root logger
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)  # Root level should be at least as low as the lowest handler level
logger.addHandler(file_handler)
logger.addHandler(console_handler)
# logger.addHandler(fail_file_handler)