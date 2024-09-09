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

# # ERROR MESSAGE 
# VALIDATING_CODE_REGION = Region(854, 329, 232, 37)
# ERROR_HAS_OCCURRED_REGION = Region(778, 224, 367, 45)
# ERROR_MESSAGE_REGION = Region(646, 481, 633,114)

# # When code is redeemed the button says Done
# DONE_BUTTON_REGION = Region(863, 775, 189, 37)
# REDEEMED_CODE_TYPE = Region(669, 673, 574, 41)


# ERROR MESSAGE 
VALIDATING_CODE_REGION = Region().region_percentage(0.4447916667, 0.3046296296, 0.1208333333, 0.0342592593)
ERROR_HAS_OCCURRED_REGION = Region().region_percentage(0.4052083333, 0.2074074074, 0.1911458333, 0.0416666667)
ERROR_MESSAGE_REGION = Region().region_percentage(0.3364583333, 0.4453703704, 0.3296875, 0.1055555556)

# When code is redeemed the button says Done
DONE_BUTTON_REGION = Region().region_percentage(0.4494791667, 0.7175925926, 0.0984375, 0.0342592593)
REDEEMED_CODE_TYPE = Region().region_percentage(0.3484375, 0.6231481481, 0.2989583333, 0.0379629630)
