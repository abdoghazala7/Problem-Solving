# absolute diffrence betwean tow digonal in matrix N * N 

import numpy as np

def Diagonal_Difference(arr) :
    
    a = 0
    b = 0
    
    for i in range(0,3) :
        for j in range (0,3) :
            
            if  i == j :
                
                a += arr[i][j]
                
            if  i == 2 - j  :  # i += 1 , j -= 1 
                
                b += arr[i][j]
                
    print( abs(a-b) )            
                
                
Diagonal_Difference(np.array([[1,2,3],[4,5,6],[7,8,5]]))                