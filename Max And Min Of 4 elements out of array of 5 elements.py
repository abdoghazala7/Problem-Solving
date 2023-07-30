# Max And Min Of 4 elements out of array of 5 elements

def calc (listt) :
    
    sum_ = sum(listt)
    max_ = 0
    min_ = 1000000
    
    for i in range(0,5) :
        
        if max_ < listt[i] :
            max_ = listt[i]
            
        if min_ > listt[i] :
            min_ = listt[i]   
            
    print (f"the maximum :{sum_-min_} and the minimum :{sum_-max_} ")         
            
calc([1,2,3,4,5])                
        
        
        
        
        
