def getMinCost(crew_id, job_id): 
    
   result = 0
   
   if len(crew_id) < len(job_id) :
       crew_id = crew_id.sort()
       job_id = job_id.sort()
       for i in range(0,len(crew_id)) :
           result += abs(crew_id[i]-job_id[i])
   else :
        
        for i in range(0,len(crew_id)) :
               result += abs(crew_id[i]-job_id[i])
               
   return result     

print(getMinCost([1,3,5],[3,5,7]))    
        
            