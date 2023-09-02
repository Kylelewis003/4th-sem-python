s = input("Enter a Sting : ")
s1 = ""
l = ['a','e','i','o','u']
for i in s:
    if i not in l:
        s1 = s1+i
print(s1)