n = int(input("Enter the number of string : "))
l = []
l1 = []
for i in range(0,n):
    str1 = input("Enter a string : ")
    l.append(str1)
print(l)
for s in l :
    if s.startswith("Hello") and s[-1].isdigit():
        l1.append(s)
print(l1)