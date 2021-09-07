import random

lower ="abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
number = "1234567890"
symbols = "!@#$%^&*()_"

all = lower + upper + number + symbols
length = 12
temp = random.sample(all, length)
password ="".join(temp)
print("Here is Your Generated Password:" + password)
