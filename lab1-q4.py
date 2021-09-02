number = int(input("enter a number"))
i = 1
while i <= number:
    if number%i == 0:
        print("The divisors of {} are {}".format(number,i))
    i=i+1