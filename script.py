import pyautogui
from time import sleep

pyautogui.PAUSE = 0.5
pyautogui.press("win")
pyautogui.write("opera")
pyautogui.press("enter")
sleep(1)
pyautogui.hotkey('ctrl', 't')
pyautogui.write("https://mail.google.com/mail/u/0/#inbox")
pyautogui.press("enter")

sleep(5)
pyautogui.click(x=628, y=257)
pyautogui.click(x=278, y=210)

sleep(5)
print(pyautogui.position())