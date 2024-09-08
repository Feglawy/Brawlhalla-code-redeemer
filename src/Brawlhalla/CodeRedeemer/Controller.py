import pyautogui
import time
import keyboard
from Brawlhalla.CodeRedeemer.Types import Point
from pynput.keyboard import Controller as KeyboardController, Key, KeyCode

class Controller:
    def __init__(self) -> None:
        self.keyboard = KeyboardController()

    def move_mouse(self, point: Point, duration=0):
        """Moves the mouse to the specified point."""
        pyautogui.moveTo(point.x, point.y, duration=duration)
    
    def click_mouse(self, button='left'):
        """Clicks the mouse (left or right)."""
        pyautogui.click(button=button)

    def __key_down(self, key):
        self.keyboard.press(key)

    def __key_up(self, key):
        self.keyboard.release(key)
    
    def press_key(self, key):
        """Presses and releases a key."""
        self.__key_down(key)
        time.sleep(0.05)  # Small delay to simulate key press
        self.__key_up(key)
        time.sleep(0.05)

    def press_enter(self):
        self.press_key(key=Key.enter)
    
    def select_all_hotkey(self):
        """Simulate pressing CTRL+A ."""
        self.__key_down(Key.ctrl)
        self.__key_down('a')
        time.sleep(0.05)
        self.__key_up(Key.ctrl)
        self.__key_up('a')
        time.sleep(0.05)

    def wait_for_key(self, key):
        print(f"waiting for the '{key}' key to proceed with the script...")
        try:
            keyboard.wait(key)
        except KeyboardInterrupt as e:
            print("script stopped Quiting...")
            exit()

        print(f"key pressed.")

    def type_text(self, text, interval=0):
        """Types text using pyautogui with an optional interval."""
        pyautogui.typewrite(text, interval)