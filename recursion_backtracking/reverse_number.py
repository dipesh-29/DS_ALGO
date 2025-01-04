'''
Write a program to revere the number.
'''

def reverse_num(n):
    result = 0
    while n > 0 :
        result = (result * 10) + n % 10
        n = n / 10
    return result

def reverse_num_recursion(n,r):
    if n == 0 :
        return r
    r = (r * 10) + n % 10
    return reverse_num_recursion(n/10,r)




if __name__ == '__main__':
    n = 26738
    #result = reverse_num(n)
    result = reverse_num_recursion(n,0)
    print(result)
