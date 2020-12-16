# Read in the price using the function input and then use the
# function float to convert the string to a floating-point value. 

price = float(input("Enter a price: "))

# Convert the price to an integer using the function int
# and store the integer in the variable dollars
print("price: ", price)
 
dollars = int(price)
print("dollars: ", dollars)

 # Create a variable CENTS_IN_A_DOLLAR and assign it the value 100
 
CENTS_IN_A_DOLLAR = 100
 
#Add a Python statement to create and initialise the variable CENTS_IN_A_DOLLAR

# Multiply the difference(price – dollars) by CENTS_IN_A_DOLLAR

simple_difference = price - dollars
print("price minus dollars is: ", simple_difference)

difference = (price - dollars)*CENTS_IN_A_DOLLAR + 0.5
print("price - dollars)*CENTS_IN_A_DOLLAR + 0.5: ", difference)
cents = int(difference)
print("cents: ", cents)

# and add 0.5; and then store the answer in a new variable result
#Add a Python statement to do the calculation as described in above comment # Convert the ‘result’ to an integer using the function int
# and store the integer in the variable cents.
#Add a Python statement to do the conversion as described in above comment # Print the dollars and cents.
#Call the function print to display the dollars and cents
