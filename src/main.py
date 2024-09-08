import time
from Brawlhalla.CodeRedeemer.OCR import OCR
from Brawlhalla.Config import config as conf
from Brawlhalla.CodeRedeemer.Logger import logger
from Brawlhalla.CodeRedeemer.Redeemer import CodeRedeemer
from Brawlhalla.CodeRedeemer.Controller import Controller
def main():


    redeemer = CodeRedeemer()
    
    con = Controller()
    con.wait_for_key('backspace')

    codes:list[str] = [
        # "code-here"
    ]
    redeemer.redeem_codes(codes)




if __name__ == "__main__":
    main()
