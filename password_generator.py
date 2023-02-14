import random


print("\n")
print('hello, Welcome to Random Password generator!')
length = int(input('\nEnter the length of password: '))
lower_alpha = "abcdefghijklmnopqrstuvwxyz"
upper_alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
number = "1234567890"
symbols = "!@#$%^&*"
all_itmes = lower_alpha + upper_alpha + number + symbols
temp = random.sample(all_itmes,length)
password = "".join(temp)
print("----------------------------------")
print("Your PassWord is : ",password)
print("----------------------------------")