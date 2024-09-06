import os
from dotenv import load_dotenv
from pathlib import Path
from Brawlhalla.CodeRedeemer.Types import Region

ENV_FILE_PATH = Path('/.env')
load_dotenv(ENV_FILE_PATH)

LOG_DIR = Path('./logs')

CODES_FILE_PATH:str = os.getenv("CODES_FILE_PATH")
OWNED_CODES_FILE_PATH:str = os.getenv("OWNED_CODES_FILE_PATH")
TESSERACT_PATH:str = os.getenv("TESSERACT_PATH")


VALIDATING_CODE_REGION = Region(850, 322, 250, 50)
ERROR_HAS_OCCURRED_REGION = Region(778, 224, 367, 45)
ERROR_MESSAGE_REGION = Region(646, 481, 633,114)

