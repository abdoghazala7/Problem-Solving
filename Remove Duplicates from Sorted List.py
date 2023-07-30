def calc(list) :
        
   a = []
   for i in list :
     if i not in a :
        a.append(i)
    
   print(a)
    
calc([1,3,6,2,1,1,4,4,2,3])           