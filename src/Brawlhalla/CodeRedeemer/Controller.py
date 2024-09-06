import keyboard
import pyautogui
import win32api
import win32con
import time
from Types import Point


class Controller:
    def __init__(self) -> None:
        pass

    def move_mouse(self, point:Point, duration = 0):
        pyautogui.moveTo(point.x, point.y, duration=duration)
    
    def click_mouse(self, button='left'):
        pyautogui.click(button)

    def __key_down(self, hex_key_code):
        win32api.keybd_event(hex_key_code, 0, 0, 0)

    def __key_up(self, hex_key_code):
        win32api.keybd_event(hex_key_code, 0, win32con.KEYEVENTF_KEYUP, 0)
    
    def press_key(self, hex_key_code):
        self.__key_down(hex_key_code)
        time.sleep(0.05)
        self.__key_up(hex_key_code)
        time.sleep(0.05)

    def press_enter(self):
        self.press_key(0x0D)

    def is_key_pressed(self, key):
        return keyboard.is_pressed(key)
    
    def type_text(self, text, interval=0):
        pyautogui.typewrite(text, interval)
