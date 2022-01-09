import os
from time import sleep
import winsound

try:
    timer = int(input('Enter a timer in seconds: '))
    os.system('cls')
except ValueError:
    print('Non-numerical value entered')
    exit()

while timer:
    print(timer)
    timer -= 1

    sleep(1)
    os.system('cls')

while True:
    print('TIME UP!!!')
    winsound.Beep(600, 1000)
    os.system('cls')
    sleep(0.7)