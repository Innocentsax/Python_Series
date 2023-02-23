import pyautogui
import time
import random


def screenshot():

    name = random.randint(0,100)
    time.sleep(5)

    img = pyautogui.screenshot(f"{name}.png")
    img.show()


screenshot()
