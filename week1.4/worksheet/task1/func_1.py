
def func_1(lst_value): 
    ''' 
    write your docstring to explain the function 
    gets the mean of a list of number values
    ''' 

    sum = 0 
    num_of_value = len(lst_value) 
    for value in lst_value: 
        sum = sum + value 
    return sum/num_of_value 