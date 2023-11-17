import pyautogui as pg
from time import sleep
import random


personas = []

archivo = open('C:\\Users\\ramih\\Desktop\\Python\\lista.txt')

num = 3

nlinea = 1

for linea in archivo:
    word = linea.split()
    if(len(word)) == 0: continue
    if nlinea == num:
        donde = word[0].find('\"')
        new = word[0]
        palabra = new[donde + 1:]
        palabra = palabra[:len(palabra) - 1]
        print(palabra)
        personas.append(palabra)
        num = num + 3
    nlinea = nlinea + 1

sleep(3)

for i in range(50):
    pg.write(f'lista.push(obj[{i}].innerText);')
    pg.press("enter")
    sleep(2)

archivo.close()