courses=['AI&ML','DataScience','Cybersecurity','BioEngineering']
print(courses)  #print the list

print(len(courses))  #length of list

   #slicing
print(courses[0])    #to know value of list at specific index no.
print(courses[-1])   #-1 is always the index no of last value in list
print(courses[0:3])  #second value is exclusive

courses.append('Electronics')  #[.append] add value to last of list
print(courses)



courses.insert(0,'Mechanical')   #[.insert] value in list to a specific index no
print(courses)

courses_2=['Civil','Gaming']   #[.extend] to add list in a list
courses.extend(courses_2)
print(courses)             

courses.remove('BioEngineering')  #[.remove] to remove a value from list
print(courses)

popped=courses.pop()  #[.pop] remoeves out last value from list [pop returns the value it removes so we ca n grab that value using variable]
print(popped)      
print(courses) 

courses.reverse()   #to reverse the list order
print(courses)

     #SORTING

sorted_courses=sorted(courses)    #to get the sorted list without altering the original list
print(sorted_courses)

courses.sort()      #to sort the list in alphabetical order
print(courses)

courses.sort(reverse=True)      #to sort the list in reverse alphabetical order
print(courses)


num=[1,5,7,3,4,11,2]   #sort numbers in ascending order
num.sort()
print(num)

num.sort(reverse=True)     #sort numbers in descending order
print(num)

print(min(num))   # to print min value in list

print(max(num))   #to print max value in list

print(sum(num))   #to print sum of all values in list

print(courses.index('Civil'))   #to find index no of value in list

print('Art' in courses)     #to see whether some value in list or not

for course in courses:     #print all the values in the list (line by line or we can say loop)
    print(course)          

for index, course in enumerate(courses):   #print values along with index number
    print(index, course)                   #we can use [enumerate(courses,start=1)] to start with index no 1


course_str ='- '.join(courses)    #to join values or make string of values in list using '-'
print(course_str)

new_list=course_str.split('-')     # to convert string into lists
print(new_list)

     #How to create an Empty List
empty_list=[]
empty_list=list()



                                                 