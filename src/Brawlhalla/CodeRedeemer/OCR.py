import pyautogui
import pytesseract
from PIL import Image
from Brawlhalla.Config import config as conf
from Brawlhalla.CodeRedeemer.Types import Region
from Brawlhalla.CodeRedeemer.Logger import logger

class OCR:
    def __init__(self) -> None:
        try:
            pytesseract.pytesseract.tesseract_cmd = conf.TESSERACT_PATH
        except Exception as e:
            logger.critical("You need to add the path of Tesseract")

    def __capture_screen_region(self, region:Region=None):
        screenshot = pyautogui.screenshot(region=region.to_tuple())
        # Convert screenshot to grayscale for better OCR results
        return screenshot.convert('L') 

    def __extract_text_from_image(self, image):
        # Use pytesseract to extract text from the image
        return pytesseract.image_to_string(image)

    def __compare_text(extracted_text:str, reference_text:str):
        return extracted_text.strip().lower() == reference_text.strip().lower()

    def get_region_text(self, region:Region=None):
        image = self.__capture_screen_region(region)
        return self.__extract_text_from_image(image)