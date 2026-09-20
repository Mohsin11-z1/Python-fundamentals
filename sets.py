#SETS are unordered,also used to test if value is part of set?,  Duplicates are not allowed(only unique characters),
set_1={'History', 'Math', 'Physics', 'Chemistry'}
print (set_1)
set_2={'History', 'Math', 'Art', 'Commerce','Math'}
print(set_2)    #SET removes duplicate value

print(set_1.intersection(set_2))   #common value in both sets

print(set_1.difference(set_2))    #value in set_1 but not in set_2
print(set_2.difference(set_1))    #value in set_2 but not in set_1

print(set_1.union(set_2))        #combine both sets unique values in one set

#How to create an Empty Set
empty_set={}   #this isnt right; it's a dictionary
empty_set=set()
