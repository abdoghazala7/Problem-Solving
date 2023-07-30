def reverse_words_order_and_swap_cases(sentence):
     
     list_ = sentence.split()
     letters = ''
     for i in range(1,len(list_)+1) :
         letters = letters + list_[-i].swapcase() + ' '
         
     print(letters)
    
reverse_words_order_and_swap_cases('Abdo Mohamed Ghazala')    


