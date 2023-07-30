import pyautogui as pe
import time
import os
import subprocess

query = input("What you wanna search? \n")
#while True:
#    x , y =pe.position()
#    print(x , y)

time.sleep(1)

pe.press('win')
time.sleep(2)
pe.typewrite("chrome")

time.sleep(1)
pe.press('enter')

time.sleep(1)
pe.getWindowsWithTitle('New Tab')[0].maximize()

time.sleep(2)
pe.typewrite("https://www.youtube.com/",0.005)



time.sleep(1)
pe.press('enter')
time.sleep(4)
pe.press('tab')
pe.press('tab')
pe.press('tab')
pe.press('tab')

time.sleep(1)

pe.typewrite(query,0.005)
time.sleep(1)
pe.press('enter')
