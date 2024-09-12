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
VALIDATING_CODE_REGION = Region().region_percentage(0.4447916667, 0.3046296296, 0.1208333333, 0.0342592593)
CLOSE_BUTTON_REGION = Region().region_percentage(0.4703125, 0.5611111111, 0.0473958333, 0.0296296296)
ERROR_MESSAGE_REGION = Region().region_percentage(0.3364583333, 0.4453703704, 0.3296875, 0.1055555556)

# When code is redeemed the button says Done
DONE_BUTTON_REGION = Region().region_percentage(0.4494791667, 0.7175925926, 0.0984375, 0.0342592593)
REDEEMED_CODE_TYPE = Region().region_percentage(0.3484375, 0.6231481481, 0.2989583333, 0.0379629630)
