import sys
import os
from logger import get_root_logger

LOG = get_root_logger("default", filename="logs")

LOG.info("Hello world!")
LOG.info(f"LOG.infoing current os.environ values - including any set in DOckefile/compose file etc.")
envars = os.environ
for var, value in envars.items():
    LOG.info(f"{var}: {value}")
LOG.info(f"Current working directory: {os.getcwd()}")

LOG.info(f"Listing all files & folder in working directory:")
for file_folder in os.listdir():
    LOG.info(f"{file_folder}")
