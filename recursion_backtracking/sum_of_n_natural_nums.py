#Functional Recursion
def sum_of_n_numbers(n):
    if n == 1:
        return 1

    return n+sum_of_n_numbers(n-1)


#Parameterised Recursion  -> NOT WORKING
def sum_of_n_numbers_parameter(n,sum):
    if n == 1:
        return 1
    return sum_of_n_numbers_parameter(n-1, sum+n)


if __name__=="__main__":
    n = 3
    result = sum_of_n_numbers(n)
    print(result)
    result = sum_of_n_numbers_parameter(n,0)
    print(result)
