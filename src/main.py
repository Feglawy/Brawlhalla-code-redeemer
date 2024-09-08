from pynput import keyboard
from threading import Thread
from Brawlhalla.Utils import file
from Brawlhalla.Config import config as conf
from Brawlhalla.CodeRedeemer.OCR import OCR
from Brawlhalla.CodeRedeemer.Logger import logger
from Brawlhalla.CodeRedeemer.Redeemer import CodeRedeemer
from Brawlhalla.CodeRedeemer.Controller import Controller

def main():
    redeemer = CodeRedeemer()
    
    controller = Controller()
    controller.wait_for_key('backspace')

    codes = file.read_codes(conf.CODES_FILE_PATH)

    listener = keyboard.Listener(on_press=controller.on_press)
    listener.start()
    
    redeem_thread = Thread(target=redeemer.redeem_codes, args=(codes,))
    redeem_thread.start()
    

    listener.join()

if __name__ == "__main__":
    main()
