def transformSentence(sentence):
    
    letters = ''
    for i in range(0,len(sentence)) :
        if i == 0 or sentence[i] == ' ':
            letters += sentence[i]
                    
        elif sentence[i-1].lower() < sentence[i].lower() : 
            letters += sentence[i].upper()
         
        elif sentence[i-1].lower() > sentence[i].lower() : 
            letters += sentence[i].lower() 
        
        else :letters += sentence[i]     
            
        
    return letters

    
print(transformSentence('ab cB GG') )  