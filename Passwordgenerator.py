import string
import random

s1 = string.ascii_lowercase
#print(s1)
s2 = string.ascii_uppercase
#print(s2) 
s3 = string.digits
#print(s3)
s4 = string.punctuation
#print(s4)
try:
    plen = int(input("Enter passowrd length\n"))
except:
    print("Please enter an integer")
    exit(1)
s = []
s.extend(list(s1))
s.extend(list(s2))
s.extend(list(s3))
s.extend(list(s4))
#print(s)
random.shuffle(s)
#print(s)
print("Generated Password for the user is\n")
print("".join(s[0:plen]))


