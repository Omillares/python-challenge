my_first_name = input("What is your name? ")
neigh_first_name = input("What is your neighbors name? ")

months_coding = input("How many months have you been coding? ")
neigh_months_coding = input("How many months has your neighbor been coding? ")

total_months_coded = int(months_coding) + int(neigh_months_coding)

print("I am " + my_first_name + " and my neighboor is " + neigh_months_coding)
print("Together we have been coding for " + str(total_months_coded) + " months!")