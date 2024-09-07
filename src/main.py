import time
from Brawlhalla.CodeRedeemer.OCR import OCR
from Brawlhalla.Config import config as conf
from Brawlhalla.CodeRedeemer.Logger import logger
from Brawlhalla.CodeRedeemer.Redeemer import CodeRedeemer

def main():

    wait = 5
    for i in range(wait):
        print(wait - i)
        time.sleep(1)

    CR = CodeRedeemer()
    codes:list[str] = [
        # "6____W-BD_1ZA"
    ]
    CR.redeem_codes(codes)



if __name__ == "__main__":
    main()
