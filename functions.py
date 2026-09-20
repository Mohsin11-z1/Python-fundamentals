def student_info(*args , **kwargs):
    print(args)
    print(kwargs)

# student_info('Maths','science', name='John', age='18')

courses=['Maths', 'science']
info={'name': 'John', 'age': 18}

student_info(*courses,**info)