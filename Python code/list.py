Subjects = ['C', 'C++', 'Python', 'Software','TOC']

#print all subjects
print(Subjects)

#print first subject
print(Subjects[0])

#print middle to end subject
print(Subjects[2:])

#print last subject
print(Subjects[-1])

#Check the Subject yes or no
print("Python" in Subjects)
print("Python" not in Subjects)

#Add the subjects
print(Subjects + ["OS",6])

#Multiply the subjects
print(Subjects * 3)

#Length of subjects
print(len(Subjects))

# Subjects to the end of the list.
Subjects.append("Java")
print(Subjects)

# Adds subject at the specified position
Subjects.insert(3,'Algo')
print(Subjects)

# Removes the subject at the specified position
Subjects.pop(1)
print(Subjects)

# Removes the first subject with the specified value
Subjects.remove('C')
print(Subjects)

# Reverses the order of the list
Subjects.reverse()
print(Subjects)

# Sorts the list
Subjects.sort()
print(Subjects)