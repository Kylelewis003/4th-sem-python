class checkpalin:
    def __init__(self,data):
        self.data=str(data)
        
    def ispalin(self, data):
        y=len(self.data)-1
        palin=True
        for x in range(int(y/2)):
            if self.data[x]!=self.data[y]:
                palin=False
                break
            y-=1
        if palin:
            return True
        else:
            return False
        
data1=int(input("Enter Number : "))
num1=checkpalin(data1)
if num1.ispalin(data1):
    print(data1 , "is a Palindrome")
else:
    print(data1 , "is not a Palindrome")

data2=input("Enter string : ")
str1=checkpalin(data2)
if str1.ispalin(data2):
    print(data2 , "is a Palindrome")
else:
    print(data2 , "is not a Palindrome")
    