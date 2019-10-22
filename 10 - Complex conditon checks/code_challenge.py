# When you join a hockey team you get your name on the back of the jersey
# but the jersey may not be big enough to hold all the letters
# Ask the user for their first name
naam= input("Wat is je naam? ")

# Ask the user for their last name
Achternaam = input("Wat is jouw achternaam? ")
# if first name is < 10 characters and last name is < 10 characters 
#       print first and last name on the jersey
if len(naam) < 10 and len(Achternaam) <10:
    print('%s  %s'%(naam,Achternaam))
# if first name >= 10 characters long and last name is < 10 characters
#       print first initial of first name and the entire last name
elif len(naam) >= 10 and len(Achternaam) <10:
    eerste_voornaam = naam[0:1]
    print('%s. %s'%(eerste_voornaam,Achternaam))
# if first name < 10 characters long and last name is >= 10 characters
#       print entire first name and first initial of last name
elif len(naam) <10 and len(Achternaam) >= 10:
    eerste_achternaam = Achternaam[0:1]
    print('%s %s.'%(naam,eerste_achternaam))

# if first name >= 10 characters long and last name is >= 10 characters
#       print last name only
else:
    print(Achternaam)

# Test with the following values
# first name: Susan  last name: Ibach
# output: Susan Ibach
# first name: Susan  last name: ReallyLongLastName
# output: Susan R.
# first name: ReallyLongFirstName  last name: Ibach
# output: R. Ibach
# first name: ReallyLongFirstName  last name: ReallyLongLastName
# output: ReallyLongLastName