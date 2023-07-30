import numpy as np 
inverted_matrix = np.empty((3,3))

def calc (arr) :
    
    
    for i in range(0,3) :
        
        for j in range(0,3) :
             
            if j == 1 :
                 inverted_matrix[i][j] = arr[i][j]
                
            elif j == 0 :
                inverted_matrix[i][j] = arr[i][j+2]
            
            elif j == 2 :
                inverted_matrix[i][j] = arr[i][j-2]  
                
    print(arr)            
    return inverted_matrix           
  
print(calc(np.array([[1,2,3],[4,5,6],[7,8,5]])))
