n = int(input("Enter a number : "))
count = 0
for i in range(1,n+1):
    factors = 0
    for j in range (1,i+1):
        if i%j == 0:
            factors+=1
    
    if factors %2 != 0:
        count+=1
    
print(f"Number of elements with odd factors in range 1 to {n} is : ",count)