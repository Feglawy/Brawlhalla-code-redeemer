import os
from dotenv import load_dotenv
from pathlib import Path
from Brawlhalla.CodeRedeemer.Types import Region



PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../'))
dotenv_path = os.path.join(PROJECT_ROOT, '.env')

load_dotenv(dotenv_path)

LOG_DIR = Path('./logs')

CODES_FILE_PATH:str = os.getenv("CODES_FILE_PATH")
OWNED_CODES_FILE_PATH:str = os.getenv("OWNED_CODES_FILE_PATH")
TESSERACT_PATH:str = os.getenv("TESSERACT_PATH")

# ERROR MESSAGE 
VALIDATING_CODE_REGION = Region(850, 322, 250, 50)
ERROR_HAS_OCCURRED_REGION = Region(778, 224, 367, 45)
ERROR_MESSAGE_REGION = Region(646, 481, 633,114)

# When code is redeemed the button says Done
DONE_BUTTON_REGION = Region(863, 775, 189, 37)
REDEEMED_CODE_TYPE = Region(669, 673, 574, 41)



# FHD : 1920*1080
# 2K : 2560*1440
# 4k : 3840*2160