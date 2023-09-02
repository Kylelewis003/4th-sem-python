t1 = int(input("Enter number 1 : "))
t2 = int(input("Enter number 2 : "))
t3 = int(input("Enter number 3 : "))

total = t1+t2+t3

if t1<t2 and t1<t3 :
    min = t1
elif t2<t3 and t2<t1:
    min = t2
else:
    min = t3
    
total = total-min

avg = total/2

print("Average of best of two marks : ",avg)
