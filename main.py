# 100 Days of Code: The Complete Python Pro Bootcamp by Dr. Angela Yu
# Day 25 - Intermediate - Files, Directories and Paths

#TODO: Create a letter using starting_letter.txt
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

#Import all the names as a list
with open("Input/Names/invited_names.txt") as invited_names:
    names = invited_names.readlines()
    #Loop through names to remove \n (new line), strip() can also remove extra blank spaces
    i = 0
    for name in names:
        name = name.strip()
        names[i] = name
        i +=1

#Import the starting letter
with open("Input/Letters/starting_letter.txt") as starting_letter:
    letter_template = starting_letter.read()

#Replace name from names list in letter_template and save the new letter
for name in names:
    new_letter_name = f"letter_to_{name.lower()}.txt"
    with open(f"Output/ReadyToSend/{new_letter_name}", mode="w") as letter:
        letter.write(letter_template.replace("[name]", name))
