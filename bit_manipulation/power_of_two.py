'''
Given a number return true if it is in power of 2. else False.
'''

def power_of_two(n):
    return not n&(n-1)

if __name__ == '__main__':
    n = 32
    result = power_of_two(n)
    print(result)
