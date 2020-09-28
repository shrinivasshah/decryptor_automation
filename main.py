import pyautogui
import time
import pyperclip
# import datetime

pag = pyautogui
count = 0


def copy_clipboard():
    pag.hotkey('ctrl','c')
    time.sleep(0.1)
    
    return str(pyperclip.paste())



time.sleep(9)
pag.moveTo(x=1033, y=242, duration=0.5)
pag.click()
for i in range(29021):
    pag.hotkey('ctrl','c')
    time.sleep(0.1)
    x = str(pyperclip.paste())
    if x != '':      
        pag.hotkey('alt','tab')
        time.sleep(.3)
        pag.hotkey('ctrl','a')
        pag.hotkey('ctrl','v')
        pag.press('tab', presses=3)
        time.sleep(.3)
        pag.press('enter')
        time.sleep(.3)
        pag.press('tab', presses=2)
        pag.hotkey('ctrl','a')
        pag.hotkey('ctrl','c')
        pag.press('tab',presses=3)
        pag.sleep(.3)
        pag.hotkey('alt','tab')
        time.sleep(.3)
        pag.press('right')
        pag.hotkey('ctrl','v')
        pag.press('left')
        pag.press('down')
    else:
        pag.press('down')
# print(pag.posit ion())
# pag.moveTo(x=1045, y=224, duration=0.7)
# pag.click()
# pag.hotkey('ctrl','c')
# pag.moveTo(x=487, y=98, duration=0.7)
# pag.click()
# pag.hotkey('ctrl','a')
# pag.hotkey('ctrl','v')
# pag.moveTo(x=732, y=137, duration=0.7)
# pag.click()
# pag.moveTo(x=595, y=186,  duration=0.7)
# pag.click()
# pag.hotkey('ctrl','a')
# pag.hotkey('ctrl','c')
# pag.moveTo(x=1299, y=227, duration=0.7)
# pag.click()
# pag.hotkey('ctrl','v')
# pag.press('down')




# for i in range(29021):
    
#     pag.moveTo(x=1045, y=224, duration=0.7)
#     pag.click()
#     pag.press('down', presses=count)
#     pag.hotkey('ctrl','c')
#     pag.moveTo(x=487, y=98, duration=0.7)
#     pag.click()
#     pag.hotkey('ctrl','a')
#     pag.hotkey('ctrl','v')
#     pag.moveTo(x=732, y=137, duration=0.7)
#     pag.click()
#     pag.moveTo(x=595, y=186,  duration=0.7)
#     pag.click()
#     pag.hotkey('ctrl','a')
#     pag.hotkey('ctrl','c')
#     pag.moveTo(x=1299, y=227, duration=0.7)
#     pag.click()
#     pag.press('down',presses=count)
#     pag.hotkey('ctrl','v')
#     pag.press('down')
#     count += 1





print('')

