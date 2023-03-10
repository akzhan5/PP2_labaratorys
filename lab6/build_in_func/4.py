from time import sleep
import math


n = int(input())
t = int(input())

def delay(fn, ms, *args):
  sleep(ms / 1000)
  return fn(*args)
print("Square root after specific miliseconds:")

print(delay(lambda x: math.sqrt(n),t))



