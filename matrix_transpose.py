import numpy as np

matrix = np.array([[5,4,3],[2,4,6],[4,7,9],[8,1,3]])
matrix_transpose = np.zeros((len(matrix[0]),len(matrix)))

class sol :
    
    def transpose (self, arr) :
        
        for i in range(len(matrix)) :
            for j in range(len(matrix_transpose)) :         
                
                matrix_transpose[j][i] = matrix[i][j]
                
        return matrix_transpose        
                
print(matrix)        
a = sol()
print(a.transpose(matrix))        
