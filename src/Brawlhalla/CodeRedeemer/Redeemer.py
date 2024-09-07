import time
from Brawlhalla.CodeRedeemer.OCR import OCR
from Brawlhalla.Config import config as conf
from Brawlhalla.CodeRedeemer.Controller import Controller, Key

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

    def is_There_an_error(self):
        ERROR_HAS_OCCURED_TEXT = "an error has occurred"
        region_text = self.ocr.get_region_text(conf.ERROR_HAS_OCCURRED_REGION)

        if region_text.lower().strip() == ERROR_HAS_OCCURED_TEXT:
            return True
        else:
            return False
    
    def get_error_message(self) -> str:
        return self.ocr.get_region_text(conf.ERROR_MESSAGE_REGION)

    def redeem_code(self, code:str):
        self.con.press_enter()
        self.con.select_all_hotkey()
        # self.con.press_key(key=Key.backspace)
        self.con.type_text(code)
        self.con.press_enter()
        time.sleep(0.2)
        self.wait_for_validation()
        time.sleep(0.3)
        if self.is_There_an_error():
            print(self.get_error_message())
        else:
            print("redeemed succesfully")
        self.con.press_enter()

    def redeem_codes(self, codes:list[str]):
        for code in codes:
            self.redeem_code(code)
