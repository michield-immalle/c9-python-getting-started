# Ask a user their name
# If their first name starts with A or B 
# tell them they go to room AB
# IF their first name starts with C
# tell them to go to room CD
# If their first name starts with another letter, ask for their last name
# IF their last name starts with Z, tell them to go to room Z
# if their last name starts with any other letter, tell them to go to room OTHER
# When you are done
# Anna should be in room AB
# Bob should be in room AB
# Charlie should be in room C
# Khalid Haque should be in room OTHER
# Xin Zhao should be in room Z

naam= input("wat is uw naam: ")
eerste_letter= naam[0:1]

if eerste_letter.upper() in ('B','A'):
    kamer= 'AB'

elif eerste_letter.upper() == 'C':
    kamer= 'C'

else:

    achternaam = input("Wat is je achternaam? ")
    achternaam_letter = achternaam[0:1]

    if achternaam_letter.upper() == "Z":

        kamer= 'Z'
    else:

        kamer= 'OTHER'
print('ga naar kamer ' + kamer) 
