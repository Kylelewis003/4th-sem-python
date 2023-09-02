import re

def find_phonenumbers_and_emails(a):
    with open(a ,'r') as file:
        text = file.read()
        
    phone_pattern = r'\+\d{12}'
    email_pattern = r'[A-Za-z0-9]+@[A-Za-z]+\.[A-Za-z]{2,}'
    
    phone_numbers = re.findall(phone_pattern , text)
    email_address = re.findall(email_pattern , text)
    
    return phone_numbers , email_address

a = "sample.txt"
phone_numbers , email_address = find_phonenumbers_and_emails(a)

print("Phone Numbers found are : ")
for i in phone_numbers:
    print(i)

print("Email addresses found are : ")
for j in email_address:
    print(j)