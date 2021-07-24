# Mónica Cordero 
# 05/14/2021
#Homework 2, Part 1


# PART TWO: Lists

# 1) Make a list called "countries" - it should contain seven different countries and NOT be in alphabetical order
# Using a for loop, print each element of the list

countries = ['Croacia', 'Macedonia', 'Montengro', 'Bosnia', 'Polonia','Serbia','Kosovo']
for item in countries:
 print(item)

 #3) Sort the list permanently.

countries =['Croacia', 'Macedonia', 'Montengro', 'Bosnia', 'Polonia','Serbia','Kosovo']
x = sorted (countries) 
print (x)

# Display the first element of the list.

countries =['Croacia', 'Macedonia', 'Montengro', 'Bosnia', 'Polonia','Serbia','Kosovo']
x = sorted (countries) 
print (x[0])

# Display the second-to-last element of the list.
countries =['Croacia', 'Macedonia', 'Montengro', 'Bosnia', 'Polonia','Serbia','Kosovo']
print (countries[5])

#6) Delete one of the countries from the list using its name.

countries =['Croacia', 'Macedonia', 'Montengro', 'Bosnia', 'Polonia','Serbia','Kosovo']
countries.remove ('Polonia')
print (countries)

# Using a for loop, print each country's name in all caps. ////// COME BACK ////
countries =['Croacia', 'Macedonia', 'Montengro', 'Bosnia', 'Polonia','Serbia','Kosovo']
countries2 = [c.upper() for c in countries]
print(countries2)





















