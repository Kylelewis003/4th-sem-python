def is_prime(num):
    if num<=1 :
        return False
    if num == 2:
        return True
    if num%2 == 0:
        return False
    for i in range(3,int(num*0.5)+1,2):
        if num%i == 0:
            return False
    return True
def unique(n):
    pro = 1
    div = 2
    while n>1 :
        if n % div == 0 and is_prime(div):
            pro*=div
            while n% div == 0:
                n//=div
        div+=1
    return pro

n = int(input("Enter a number :"))
print("Product is  :",unique(n))