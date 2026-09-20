                          #DIFFERENCE BETWEEN LISTS AND TUPLES 
#Lists are mutable (can be changed after creation) || Tuples are immutable (cannot be modified once created)
#Syntax: lists- Square bracket[....]               || Tuples- parenthesis(...)
# lists can grow or shrink                         || Tuples are fixed
#METHODS:  Many (append, remove, pop etc.)         ||  Few (count, index)

tuple_1=('History', 'Math', 'Physics', 'Chemistry' )

print (tuple_1)

# tuple_1[0]=('Art')
# print(tuple_1)   # it will give error as tuples are immutable

#How to create an Empty List
empty_tuple=()   

empty_tuple=tuple()
for i in tuple_1:
    print(i)