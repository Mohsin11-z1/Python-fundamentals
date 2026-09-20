
print(3**2)   #exponent
print(7//2)   #floor division(quotient)
print(3%2)    #modulus

num=1    #increment function for addition(num=num+1)
num += 1
print(num)

num_1=1   #increment function for multiplication(num=num*10)and so on for -,/..
num_1 *=10
print(num_1)

     #built in functions
print(abs(-5))   #absolute value

print(round(5.74))  #round off function
print(round(5.75,1))  #round off function to x decimal places

    #comparisons
num1=3
num2=5
print(num1==num2)   #equal
print(num1!=num2)   #not equal
print(num1<num2)    #greater/less than
print(num1>=num2)   #greater/less equal

   #casting values(converting from one data type to another)
   
num_a='100'       #it looks like int but it is string due to ' '
num_b='200'

#if we print(num_a+num_b)  output--> 100200, to convert it into integers,

num_a=int(num_a)
num_b=int(num_b)
print(num_a+num_b)

