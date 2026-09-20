def find_index(list1,target):
    for i,value in enumerate(list1):
        if(value==target):
            print(f"{target} found at index {i}")
            break
        else:
            print(f"Target not found at index{i}")
                    



