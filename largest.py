t1 = int(input("Enter number 1 : "))
t2 = int(input("Enter number 2 : "))
t3 = int(input("Enter number 3 : "))

total = t1+t2+t3

total = total - min(t1,t2,t3)

avg = total/2

print("Avreage of best of two marks : ",avg)
