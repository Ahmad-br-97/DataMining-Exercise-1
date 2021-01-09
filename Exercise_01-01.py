text = input("Please enter a text: ")

output = {} #Output Dictionary
uniqueChars = [] #All entered text characters without duplication

for char in text :
    
    if char not in uniqueChars :
        
        numChar = 0 #Num of char
        for value in text :
            if value == char : numChar += 1
             
        uniqueChars += char
        output[char] = numChar
        
print("\nCharacter Frequency:\n", output)  
print("\n***Created By Ahmad Baratian (@ahmad_br_97)***")       