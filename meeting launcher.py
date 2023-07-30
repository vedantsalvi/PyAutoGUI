import pyautogui as pe
import time
import os
import subprocess

#query = input("What you wanna search?")
#while True:
#    x , y =pe.position()
#    print(x , y)

time.sleep(1)
pe.press('win')

time.sleep(0.1)
pe.typewrite(" microsoft teams",0.2)

time.sleep(0.5)
pe.press('enter')


time.sleep(1)
pe.getWindowsWithTitle('Microsoft Teams')[0].maximize()

time.sleep(1)
pe.click(x=38,y=191)

time.sleep(1)
pe.click(x=1167,y=258)

time.sleep(1)
pe.click(x=1824, y=129)


#time.sleep(1)
#pe.typewrite("https://meet.google.com/qwx-euet-wnm",0.005)
#pe.press('enter')

#time.sleep(4)
#pe.click(x=1142, y=689)

#time.sleep(2)
#https://meet.google.com/qwx-euet-wnm
