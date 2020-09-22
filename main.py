import pyautogui
import time
# import datetime

pag = pyautogui

# print(pag.position())
pag.moveTo(x=163,y=229, duration=0.7)
pag.click()
pag.hotkey('ctrl','c')
pag.moveTo(x=491, y=452, duration=0.7)
pag.click()
pag.keyDown('delete')

pag.keyUp('delete')
pag.hotkey('ctrl','v')
pag.moveTo(x=746, y=508, duration=0.7)
pag.click()
pag.moveTo(x=493, y=545,  duration=0.7)
pag.click()
pag.drag(300,0)
pag.hotkey('ctrl','c')
pag.moveTo(x=1017, y=254, duration=0.7)
pag.hotkey('ctrl','v')
pag.press('down')








