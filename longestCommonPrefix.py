def longestCommonPrefix (listt) :
    
    prefix = ""
    if len(listt) == 0 :
        return prefix
    
    for i in range(len(min(listt))) :
            
        c = listt[0][i] 
        if all (a[i]== c for a in listt) :
            
            prefix += c
        
        else :
            break
       
    return prefix    
            
    
print(longestCommonPrefix(["flower","flow","flight"]))
print(longestCommonPrefix(["dog","racecar","car"]))

