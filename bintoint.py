def bin(n):
    p = 1
    d = 0
    while n!= 0 :
        rem = n%10
        d = d + (p*rem)
        p = p*2
        n = n//10
    return d

num = int(input("Enter a binary value : "))
print("Decaimal value is : ",bin(num))