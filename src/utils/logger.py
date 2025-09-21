import logging 
import os
from datetime import datetime

LOGS_DIR = "logs"
os.makedirs(LOGS_DIR, exist_ok=True)

LOG_FILE_NAME = f"log_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"


logging.basicConfig(
    filename=os.path.join(LOGS_DIR, LOG_FILE_NAME),
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def get_logger(name: str=__name__) -> logging.Logger:
    """Get a logger instance."""
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    return logger
