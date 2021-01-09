text = input("Please enter a comma separated string of words: ")

split_text = text.split(',')
output_set = set()
output_list = []

for word in split_text : output_set.add(word) #Add words to a Set for remove duplicate words
 
for word in output_set : output_list.append(word) #convert Set To List

output_list.sort() #Sort List
 
print("\nSort Unique Words Alphabetically:")

for word in output_list : print(word)

print("\n***Created By Ahmad Baratian (@ahmad_br_97)***") 

   
