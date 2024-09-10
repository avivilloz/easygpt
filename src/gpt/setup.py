import logging
from .utils import create_dir

LOGS_DIR = "logs"
LOG_FILE = f"{LOGS_DIR}/gpt.log"

create_dir(LOGS_DIR)

logging.basicConfig(
    filename=LOG_FILE,
    filemode="a",
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
