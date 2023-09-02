n = int(input("Enter a number : "))

num = n
rev = 0

while n!=0 :
    temp = n%10
    rev = rev*10 + temp
    n = n//10

if rev == num :
    print("Palindrome")
else:
    print("Not Palindrome")
    
    
s = str(num)
d = {}

for i in s :
    if i in d:
        d[i]+=1
    else:
        d[i] = 1
        
print(d)