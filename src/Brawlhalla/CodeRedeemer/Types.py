from Brawlhalla.Utils.screen import get_screen_resolution
import math

class Region:
    def __init__(self, x:int=0, y:int=0, width:int=0, height:int=0):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def region_percentage(self, x_per:float, y_per:float, width_per:float, height_per:float):
        width, height = get_screen_resolution()
        self.x = math.ceil(x_per * width)
        self.y = math.ceil(y_per * height)
        self.width = math.ceil(width_per * width)
        self.height = math.ceil(height_per * height)
        return self

    def to_tuple(self):
        return (self.x, self.y,self.width, self.height)

class Point:
    def __init__(self, x:int, y:int):
        self.x = x
        self.y = y
    
    def point_percentage(self, x_per:float, y_per:float):
        width, height = get_screen_resolution()
        self.x = int(x_per * width)
        self.y = int(y_per * height)

    def to_tuple(self):
        return (self.x, self.y)