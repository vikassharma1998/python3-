#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.

with open('Input/Names/invited_names.txt') as names_file:
    names = names_file.readlines()
    print(names)

with open('Input/Letters/starting_letter.txt') as names_file:
    info = names_file.read()
    for name in names:
        striping = name.strip()
        complete = info.replace('[name]', striping)
        with open(f'Output/ReadyToSend/its_for_{striping}.txt', 'w') as file:
            file.write(complete)




#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp