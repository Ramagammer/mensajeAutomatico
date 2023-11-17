import pyautogui as pg
from time import sleep


i = 0
while i < 1:
   #sleep(5)
   pg.typewrite("Hola esto es un mensaje!")
   pg.press("enter")
   i += 1
