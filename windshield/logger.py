import logging
import pathlib
from datetime import datetime


import logging
import pathlib
from datetime import datetime


LOGGER_NAME = "main_logger"

root = pathlib.Path(__file__).parent
logs_path = root.joinpath("logs/logs3")
log_filename = datetime.now().strftime("%d%m%Y_%H%M%S.log")
log_abs_path = logs_path.joinpath(log_filename)

def configure_logger():
    try:
        logs_path.mkdir(exist_ok=True, parents=True)
    except OSError as err:
        print(err)

   
    message_only = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s")
    verbose_fmt = logging.Formatter("<%(asctime)s> <%(msecs)d> - [%(levelname)s] - %(filename)s - %(levelno)s - %(message)s")

    
    cli_handler = logging.StreamHandler() 
    cli_handler.formatter = message_only
    cli_handler.setLevel(logging.INFO)


    file_handler = logging.FileHandler(log_abs_path)
    file_handler.formatter = verbose_fmt
    file_handler.setLevel(logging.ERROR)

    
    logger = logging.getLogger(LOGGER_NAME)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(cli_handler)
    logger.addHandler(file_handler)
