#Creating a nested tuple
Students = (("Faria", 3, 21), "Faiza", "Oni")
print(Students)
#Accessing Values in Tuples
print(Students[1])

# Update a tuple
y = list(Students)
y[1] = "Farida"
Students = tuple(y)
print(Students)

# Delete a tuple

Students = Students[:2] + Students[3:]

print(Students)

#join tuples

Students1 = ("Mahi","Nishi")

Students2 = Students+Students1

print(Students2)