# convert time from 12 hour to 24 hour format 

def caluc (a) :
    
    b = a[-2:]
    
    if b == "PM" and a[0:2] != 12 :
        
       a = str((int(a[0:2]) + 12 )) + a[2:]
       
    elif  b == "AM" and a[0:2] == str(12) :   
        
        a = "00" + a[2:] 
       
    print (a[0:-2])
        
    
    
    
caluc ("06:35:50 PM")    