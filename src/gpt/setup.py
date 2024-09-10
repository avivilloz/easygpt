import logging
from .utils import create_dir


def setup_logging(logs_dir: str = "logs", log_file_name: str = "gpt.log"):
    create_dir(logs_dir)
    log_file_path = f"{logs_dir}/{log_file_name}"

    logging.basicConfig(
        filename=log_file_path,
        filemode="a",
        level=logging.DEBUG,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    )
