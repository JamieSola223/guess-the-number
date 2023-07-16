import random

x = int(input("What number do you think it is? \n"))

y = random.randint(1, x)
print(y)

if x == y:
    print("Good job!")

else:
    print("Better luck next time!")