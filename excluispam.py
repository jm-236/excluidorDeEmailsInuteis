import pyautogui
from time import sleep

pyautogui.PAUSE = 0.5
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
sleep(2)

for i in range(0, 7):
    pyautogui.press("tab")


pyautogui.press("enter")
pyautogui.hotkey('ctrl', 't')
pyautogui.write("https://mail.google.com/mail/u/0/#inbox")
pyautogui.press("enter")

sleep(5)

# foi pra aba "mais"
for i in range(0, 14):
    pyautogui.press("tab")

pyautogui.press("enter")

for i in range(0, 5):
    pyautogui.press("down")

pyautogui.press("enter")

for i in range(0, 10):
    pyautogui.press("tab")

pyautogui.press("enter")
pyautogui.press("down")
pyautogui.press("enter")
pyautogui.press("tab")
pyautogui.press("enter")