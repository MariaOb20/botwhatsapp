import pyautogui
import webbrowser
from time import sleep

webbrowser.open("https://web.whatsapp.com/send?phone=+5218442128264")
sleep(10)

for i in range(25):
    pyautogui.typewrite('prueba')
    pyautogui.press('enter')
    sleep(1)  # Puedes ajustar el tiempo de espera entre cada iteración si es necesario
