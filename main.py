import pyautogui
# import datetime

pag = pyautogui

print(pag.position())
pag.moveTo(x=193,y=223)
pag.click()
pag.hotkey('ctrl','c')
pag.moveTo(x=596,y=339)
pag.hotkey('ctrl','a')
pag.hotkey('ctrl','v')
pag.moveTo(x=618, y=407)
pag.click()
pag.moveTo(x=485, y=438)
pag.press('down')







