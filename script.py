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

# foi pra aba promoções
for i in range(0, 22):
    pyautogui.press("tab")

# clicou
pyautogui.press("enter")

# foi pro icone de selecionar os emails
for i in range(0, 5):
    pyautogui.hotkey("shift", "tab")

# selecionou os emails
pyautogui.press("enter")
pyautogui.press("down")
pyautogui.press("enter")

# foi pro icone de deletar
for i in range(0, 3):
    pyautogui.press("tab")

# deletou
pyautogui.press("enter")

# foi pra aba social
for i in range(0, 5):
    pyautogui.press("tab")

pyautogui.press("enter")

for i in range(0, 6):
    pyautogui.hotkey("shift", "tab")

pyautogui.press("enter")
pyautogui.press("down")
pyautogui.press("enter")

for i in range(0, 3):
    pyautogui.press("tab")

pyautogui.press("enter")