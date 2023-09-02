def merge(a):
    if len(a)>1:
        mid = len(a)//2
        l = a[:mid]
        r = a[mid:]
        
        merge(l)
        merge(r)
        
        i,j,d = 0,0,0
        
        while i<len(l) and j<len(r):
            if l[i] <= r[j] :
                a[d] = l[i]
                i+=1
            else:
                a[d] = r[j]
                j+=1
            
            d+=1
            
        while i<len(l):
            a[d] = l[i]
            i+=1
            d+=1
            
        while j<len(r):
            a[d] = r[j]
            j+=1
            d+=1

a = [8,5,1,3,2]
merge(a)
print(a)
            
        
        
        
            
        
            
        
        
        