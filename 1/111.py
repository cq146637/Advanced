__author__ = 'Cq'
from collections import deque
import pickle
from random import randint
import os
result = randint(1,100)

print("result is ",result)
deque1 = deque([],5)

if os.path.isfile("save.data"):
    deque1 = pickle.load(open("save.data"))


while True:
    k = input("\nplease input your guess number: ")

    if k.isdigit():
       k = int(k)
    elif k == 'h' or k == 'H':
        print("your input history is ",list(deque1))

    else:
        continue

    if k != result:
        if k > result:
            print("your number is greater than result\n")
        else:
            print("your number is less than result\n")
        deque1.append(k)

    else:
        print("It was good result...")
        deque1.append(k)
        break

    if k == 100:
        break


f = open("save.data",'w')

pickle.dump(deque1, f)