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
                time.sleep(1)
                return # validation ended
            time.sleep(0.5)

    def is_There_an_error_with_code(self):
        CLOSE_BUTTON_TEXT = "close"
        return self.ocr.compare_text_with_region(conf.CLOSE_BUTTON_REGION, CLOSE_BUTTON_TEXT)
    
    def is_code_redeemed(self) -> bool:
        DONE = "done"
        return self.ocr.compare_text_with_region(conf.DONE_BUTTON_REGION, DONE)

    def get_error_message(self) -> str:
        errorMessage = self.ocr.get_region_text(conf.ERROR_MESSAGE_REGION).strip()
        return errorMessage

    def get_redeemed_code_type(self) -> str:
        return self.ocr.get_region_text(conf.REDEEMED_CODE_TYPE).strip()

    def check_code_status(self, code, retries=5):
        is_code_redeemed = self.is_code_redeemed()
        is_there_error = self.is_There_an_error_with_code()
        
        if retries <= 0:
            logger.error(f"{code} - couldn't check code")
            return

        if is_there_error:
            error_message = self.get_error_message()
            logger.info(f"{code} - couldn't be redeemed: {error_message}")

            if error_message == "Code already redeemed":
                file.write_code(conf.OWNED_CODES_FILE_PATH, code + '\n')
        elif is_code_redeemed:
            redeemed_code_type = self.get_redeemed_code_type()
            logger.info(f"{code} is a :{redeemed_code_type}.")
            time.sleep(1)
        else:
            time.sleep(0.5)
            self.check_code_status(code, retries-1)

    def redeem_code(self, code:str):

        self.con.press_enter()
        self.con.select_all_hotkey()
        # self.con.press_key(key=Key.backspace)
        self.con.type_text(code)
        self.con.press_enter()
        
        time.sleep(0.5)
        self.wait_for_validation()

        self.check_code_status(code)

        self.con.press_enter()

    def redeem_codes(self, codes:list[str]):
        try:
            for i in range(len(codes)):
                logger.info(f"redeeming code:{codes[i]} - index: {i}")
                self.redeem_code(codes[i])
            logger.info(f"Finished redeeming {len(codes)} - press 'esc' to exit.")

        except Exception as e: 
            logger.error(f"An error has occured {e}")