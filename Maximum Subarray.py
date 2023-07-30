def calc (arr) :
    max_ = 0
    for i in range (len(arr)) :
        
        s = 0
        for j in range(i,len(arr)) :
            
            s += arr[j]
            max_ = max(max_ , s)
            
    print(max_)   

calc([1])
calc([-2,1,-3,4,-1,2,1,-5,4])         
calc([3,-6,2,4,-1,3,4,6])        
            
            