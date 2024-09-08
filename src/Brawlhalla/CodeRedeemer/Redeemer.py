import time
from Brawlhalla.CodeRedeemer.OCR import OCR
from Brawlhalla.Config import config as conf
from Brawlhalla.CodeRedeemer.Controller import Controller, Key
from Brawlhalla.Utils import file
from Brawlhalla.CodeRedeemer.Logger import logger

class CodeRedeemer:
    def __init__(self):
        self.ocr = OCR()
        self.con = Controller()

    def wait_for_validation(self):
        """Waits until the validation message is no longer on the screen."""
        VALIDATING_CODE_TEXT = "validating code..."
        while True:
            region_text:str = self.ocr.get_region_text(conf.VALIDATING_CODE_REGION)
            if region_text.lower().strip() != VALIDATING_CODE_TEXT:
                break
            time.sleep(0.5)

    def is_There_an_error_with_code(self):
        ERROR_HAS_OCCURED_TEXT = "an error has occurred"
        return self.ocr.compare_text_with_region(conf.ERROR_HAS_OCCURRED_REGION, ERROR_HAS_OCCURED_TEXT)
    
    def get_error_message(self) -> str:
        return self.ocr.get_region_text(conf.ERROR_MESSAGE_REGION).strip()

    def is_code_redeemed(self) -> bool:
        DONE = "done"
        return self.ocr.compare_text_with_region(conf.DONE_BUTTON_REGION, DONE)

    def get_redeemed_code_type(self) -> str:
        return self.ocr.get_region_text(conf.REDEEMED_CODE_TYPE).strip()

    def redeem_code(self, code:str):
        logger.info(f"redeeming code:{code}")

        self.con.press_enter()
        self.con.select_all_hotkey()
        # self.con.press_key(key=Key.backspace)
        self.con.type_text(code)
        self.con.press_enter()
        
        time.sleep(0.2)
        self.wait_for_validation()
        time.sleep(0.3)

        if self.is_There_an_error_with_code():
            error_message = self.get_error_message()
            logger.info(f"{code} - couldn't be redeemed: {error_message}")
            
            if error_message == "Code already redeemed":
                file.write_code(conf.OWNED_CODES_FILE_PATH, code + '\n')
        
        else:
            redeemed_code_type = self.get_redeemed_code_type()
            logger.info(f"{code} is a :{redeemed_code_type}.")
            time.sleep(1)
        
        self.con.press_enter()

    def redeem_codes(self, codes:list[str]):
        try:
            for i in range(len(codes)):
                self.redeem_code(codes[i])
            logger.info(f"Finished redeeming {len(codes)} - press 'esc' to exit.")

        except Exception as e: 
            logger.error(f"an error has occured {e}")