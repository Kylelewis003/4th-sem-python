def fib(n):
    if n<0:
        print("Invalid")
    elif n==1 or n == 0:
        return n
    else:
        return fib(n-1) + fib(n-2)
        
n = int(input("Enter a number : "))
print("The Fibonacci series until ",n," is : ")
for i in range (0,n):
    print(fib(i))