def calc (strr) :
    
    if len(strr) % 2 != 0 :
           
        return False
    
    
    for i in range (len(strr)-1) :
            
        if i % 2 == 0 :
            if (strr[i] == "(" and strr[i+1] == ")" ) or (strr[i] == "[" and strr[i+1] == "]" ) or (strr[i] == "{" and strr[i+1] == "}" ) :
                pass
            
            else :
               
               return False
           
    return True

print(calc("()"))              
print (calc("[](){)")) 
