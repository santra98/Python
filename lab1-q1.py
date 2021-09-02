from datetime import date
name = input("enter your name")
age = int(input("enter your age"))
cur_date = date.today()
year = int(cur_date.year) + (100-age)
print("Hello {}. You will turn 100 years old in {} ".format(name,year))

