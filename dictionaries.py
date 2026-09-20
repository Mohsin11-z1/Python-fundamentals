student={'name':'John', 'age':'25', 'courses':['Maths','CompSci'] }
print(student)
print(student.get('name'))    # OR  print(student['name'])
print(student.get('age'))     # OR  print(student['age'])
print(student.get('courses')) # OR  print(student['courses'])
print(student.get('skills'))  #return none if entry not exist
print(student.get('skills', 'Not found'))  #u can also set ur message for entry that's not in ur dict.

#student['Phone']='12345'    #to add a new entry in dictionary
#print(student.get('Phone'))

#we can also update/add multiple entries in dict. using [.update()] method
student.update({'name':'Johnson', 'age':'30', 'Phone':'12345', 'weight':'60 kg'})
print(student)


del student['age']     #to delete some entry from dict.


weight=student.pop('weight')  #[.pop()] removes value and holds it to get that value we declare some variable
print(weight)
print(student)

print(len(student))   #no of entries/values in dict.

print(student.keys())   #gives all keys in dict.
print(student.values())   #gives all values in dict.
print(student.items())   #gives all items in pair in dict.

for key in student:   #to loop through all keys in dict.
    print(key)

for value in student.values():    #to loop through all values in dict.
    print(value)

for key,value in student.items():    #to loop through all items in dict.
    print(key,value)


