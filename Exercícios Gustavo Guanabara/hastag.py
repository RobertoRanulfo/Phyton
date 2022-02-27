import pyautogui
import time
import pyperclip

pyautogui.PAUSE = 1
pyautogui.press('winleft')
pyautogui.write('Chrome')
pyautogui.press('enter')
pyautogui.alert('Vai começar, aperte OK e não mexa em nada.')
pyautogui.hotkey('ctrl', 't')

link = 'https://drive.google.com/drive/folders/149xknr9JvrlEnhNWO49zPcw0PW5icxga'
pyperclip.copy(link)
pyautogui.hotkey('ctrl','v')
#time.sleep(1)
pyautogui.press('enter')
time.sleep(2)
pyautogui.click(855,298)
