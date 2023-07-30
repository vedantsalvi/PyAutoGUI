import pyautogui as pe
import time
import os
import subprocess

## for teams users!

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


# below code is for meet users! uncomment and use it but dont forget to comment the above code
#time.sleep(1)
#pe.press('win')

#time.sleep(0.1)
#pe.typewrite(" microsoft teams",0.2)

#time.sleep(4)
#pe.typewrite("https://meet.google.com/qwx-euet-wnm",0.005)
#pe.press('enter')

#time.sleep(4)
#pe.click(x=1142, y=689)

#time.sleep(2)
#https://meet.google.com/qwx-euet-wnm
