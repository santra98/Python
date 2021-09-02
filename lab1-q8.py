import random
a = random.randint(1,9)
b = int(input("Guess the number"))
if a == b:
    print("correct")
elif b > a:
    print("too high")
else:
    print("too low")
print(a)