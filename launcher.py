import alpha
from playsound import playsound
import time

playsound('ready.wav')
print('Ready')
while True:
    alpha.listen()
