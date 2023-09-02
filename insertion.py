def insertion(a):
    n = len(a)
    for i in range(0,n):
        key = a[i]
        j = i-1
        while j>=0 and a[j]>key:
            a[j+1] = a[j]
            j-=1
            
        a[j+1] = key
        
a = [8,5,1,3,2]
insertion(a)
print(a)