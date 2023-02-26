'''
2 имитирование работы с помощью стрелочек
3 обрезание фото
4 перевод изображение в другой формат
5 распознование опасности
6 распозноваие расположения каратиста

'''
# Program for partial screenshot

import pyautogui
import time
import keyboard

t = False
while True:

    print(keyboard.read_key())
    if keyboard.read_key() == "right shift":
        t = True

    while t:
        time.sleep(3)
        screen = pyautogui.screenshot('screenshot.png',region=(655,211, 607, 808))
        if keyboard.read_key() == "shift":
            t = False
    if keyboard.read_key() == "ctrl":
        break




