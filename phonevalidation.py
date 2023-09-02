import re

ph = input("Enter a Phone number  :")

phonenumber = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')

if phonenumber.match(ph):
    print("Valid Phone number ")
else:
    print("Invalid Phone number ")