#Define a variable weight where the user gives an input of weight.
weight = input('Weight: ')

# Define another variable unit where the user to input the unit of the weight (kg or lbs) inputted
unit= input('(K)g or (L)bs: ')

# Using an if statement, state a condition that if the user gave a value equal to lbs
# And also in any letter case not minding, the return value should continue i
if unit.upper() == 'L':
    conversion = float(weight)*0.45 # Return the output of the first condition given in line 7
    print(f'Weight in Kg: {conversion}')

#Using an else statement, state a second condition that if the user gave another input other than that in line
#The return value should continue in line 15.

else:
    conversion = weight
    # Return the output of the second condition
    print(f'Weight in Lbs: {conversion} ')