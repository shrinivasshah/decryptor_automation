import pyautogui
import time
# import datetime

pag = pyautogui

# print(pag.position())
pag.moveTo(x=163,y=229, duration=0.7)
pag.click()
pag.hotkey('ctrl','c')
pag.moveTo(x=698, y=449, duration=0.7)
pag.click()
pag.hotkey('ctrl','a')
pag.hotkey('ctrl','v')
pag.moveTo(x=746, y=492, duration=0.7)
pag.click()
pag.moveTo(x=600, y=544,  duration=0.7)
pag.click()
pag.hotkey('ctrl','a')
pag.hotkey('ctrl','c')
pag.moveTo(x=1017, y=254, duration=0.7)
pag.hotkey('ctrl','v')
pag.press('down')








