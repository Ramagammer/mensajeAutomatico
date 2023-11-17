import pyautogui as pg
from time import sleep

sleep(3)

for i in range(5):
    pg.write(f'lista.push(obj[{i}].innerText);')
    pg.press("enter")
    sleep(2)



