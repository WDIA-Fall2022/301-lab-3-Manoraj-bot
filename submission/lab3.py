import pylightxl as xl

with open('city.xlsx', 'rb') as f:
    db = xl.readxl(f)

l = list(db.ws(ws='Sheet1').col(col=3))

# ask the user for the code of the country and save it into a variable
usrCountryCode = str(input("Please Enter Country Code > ")).upper()

# Scan the list l line by line and add 1 to the counter if the country is the one looked for
counter = 0
for el in l:
    if el.upper() == usrCountryCode:
        print("Found {}".format(el))
        counter = 1
        break
if counter == 0:
    print("{} Not found".format(usrCountryCode))
# Format and print the result


# Ask the user for the population looked for. Use a loop and a try except to validate the input as a valid integer
done = False
while done == False:
    try:
        usrPopulation = int(input("Please Enter Population > "))
        # Store the population values into a list called l1 (see line 6)
        l1 = list(db.ws(ws='Sheet1').col(col=5))
        # Initialize a list lstOfRecords to an empty list
        lstOfRecords = list()
        for i in range(len(l1)):
            # Scan the list l1, if the population is larger than the population looked for, add the list index to lstOfRecords
            if usrPopulation > int(l1[i]):
                lstOfRecords.append(i)
        # Print the list lstOfRecords
        print(lstOfRecords)
        done = True
    except:
        print("Enter Number Only")

l2 = list(db.ws(ws='Sheet1').col(col=2))

for i in range(len(lstOfRecords)):
    # Bonus: Print the name of the cities whose index is in lstOfRecords
    print(l2[lstOfRecords[i]])
