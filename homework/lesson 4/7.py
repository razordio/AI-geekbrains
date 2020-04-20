import math


def fibo_gen():
   for el in range(1,15):
       yield el

for el in fibo_gen():
    print(math.factorial(el))