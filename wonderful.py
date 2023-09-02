s = input("Enter a String: ")
a = ""
for i in s:
    if i not in a:
        a+=i
n = len(a)

if n>3:
    print("-1")
else:
    print("Wonderful")