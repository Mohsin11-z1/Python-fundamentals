m='Hello, World!'
print(m)

print(len(m)) #to print length of string

print(m[10])  #slicing i.e. printing specific parts of string
print(m[0:5])
print(m[:5])
print(m[7:])

print(m.lower())  # convert string to lowercase
print(m.upper())  # convert string to uppercase

print(m.count('Hello'))  #count no. of words or letters
print(m.count('l'))

print(m.find('World') )    #find index of the string

new_m=m.replace('World!','Universe!')   #to replace a word in string(declare new var.(new_m) or use same var.(m) only)
print(new_m)

word1="Hello"
word2="python"
print(word1+' ' +word2)