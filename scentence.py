str = input("Enter a scentence :")

w = u = l = d = 0

for i in str.split():
    w+=1
    for j in i: 
        if j.isupper():
            u+=1
        if j.islower():
            l+=1
        if j.isdigit():
            d+=1

print(f"Words:{w}\t\tUppercase:{u}\tLowercase:{l}\tDigits:{d}")