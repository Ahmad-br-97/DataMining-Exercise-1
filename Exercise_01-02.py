text = input("Please enter a string: ")

output_string = ''

i = 0
for char in text :
    
    if i%2 == 0 : output_string += char
    i += 1
    
print("\nRemove Odd Index Values:", output_string)
print("\n***Created By Ahmad Baratian (@ahmad_br_97)***")       
