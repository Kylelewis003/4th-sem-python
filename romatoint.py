def rtoint(s):
    preval = 0
    total = 0
    roman = {'I':1 , 'V':5 , 'X':10 , 'L':50 , 'C':100 , 'D':150 , 'M':1000}
    
    for i in s[::-1]:
        curval = roman[i]
        
        if curval>=preval:
            total+=curval
        else:
            total-=curval
            
        preval = curval
    
    return total

str = input("Enter a roman numeral : ")
print("Its corresponding integer value is : ",rtoint(str))