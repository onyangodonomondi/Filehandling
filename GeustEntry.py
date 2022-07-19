
# Ask customer to Enter  His/Her Name and Store the name in a variable GeustName.

GeustName = input("What is your Name? \n ")
IdNo = input("Id Number ? \n ")
line = (80*"=")


# Write the stored variable into text file.
with open("geust.txt", 'a') as f:

    f.write("Customer Name: " + GeustName + " || ")
    f.write("Customer Id: " + IdNo)
    f.write("\n")
    f.write(line)
# Inserting  New  line After every record
    f.write("\n")
   

