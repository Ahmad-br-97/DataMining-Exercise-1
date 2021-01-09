sentence = input("Please enter a sentence: ")

output = {} #Output Dictionary
allWords_array = sentence.split(' ') #Add all words to this array
uniqueWords_array = [] #All entered sentence words without duplication

for word in allWords_array : 
    
    if word not in uniqueWords_array :
        
        numWord = 0 #Num of word
        for value in allWords_array :
            if value == word : numWord += 1
            
        uniqueWords_array += word
        
        if numWord > 1 : output[word] = numWord
            
print("\nIn the entered sentence:")

for value in output :               
    print("The word \"{0}\" is repeated {1} times.".format(value, output[value])) 
    
print("\n***Created By Ahmad Baratian (@ahmad_br_97)***")       