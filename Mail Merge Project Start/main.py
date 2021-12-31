# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
with open(".\\Input\\Names\\invited_names.txt") as namelist:
    name_list = []
    for name in namelist.readlines():
        new_name = name.strip('\n')
        name_list.append(new_name)
    print(name_list)
for name in name_list:
    with open(".\\Input\\Letters\\starting_letter.txt") as starting_letter:
        contents = starting_letter.read()
        with open(f"./Output/ReadyToSend/{name}.txt", 'w') as invite:
            personalised_content = contents.replace("[name]", name)
            invite.write(personalised_content)

''' Replit to Pycharm'''
''' Test Test Test'''