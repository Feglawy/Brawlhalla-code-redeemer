from screeninfo import get_monitors


def get_screen_resolution():
    monitor = get_monitors()[0]
    width = monitor.width
    height = monitor.height
    return width, height