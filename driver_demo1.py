from driver import create_driver
import pyautogui
import time


def open_cmd():
    path = 'cd C:\\Program Files (x86)\\Google\\Chrome\\Application'
    path2 = 'chrome.exe --remote-debugging-port=9222 --user-data-dir=“D:\auto”'
    pyautogui.hotkey('win', 'r')
    time.sleep(0.5)
    pyautogui.hotkey('backspace')
    pyautogui.typewrite('cmd')
    pyautogui.hotkey('enter')
    pyautogui.hotkey('enter')
    time.sleep(1)
    pyautogui.hotkey('shift')
    time.sleep(1)
    pyautogui.typewrite(path)
    pyautogui.hotkey('enter')
    time.sleep(1)
    pyautogui.typewrite(path2)
    pyautogui.hotkey('enter')
    time.sleep(2)


open_cmd()
driver = create_driver('chrome')

driver.get('https://www.jd.com/')

time.sleep(10)
driver.quit()
