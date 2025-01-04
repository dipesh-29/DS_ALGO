'''
Steps for Recursion :
1. Find the base case. Boundry conditions.
   - Think about the conditions whose answer you know. Mainly focus on the conditions where you should dtop the recursive calls.
2. Find the relationship between problem and subproblem.
   - Dont think much about the subproblem. Consider you have got output from subproblem and you have to compute the result of main problem. Thats how you can find relationship between problem and subproblem.
3. Generalize the relation.
   - Once you find the relation between problem and subproblems we just need to generalize using some equation.


Example : Find sum of n natural numbers.
1. Base case : [I want to stop Recursion call when n==1 and I know the the sum of one natural number is 1.] so my base condition would be :
    if n == 1:
        return 1

2. Relationship between problem and subproblem :
    sum(4) = sum(3) + 4 , Now here dont think much about hwo we are going to get sum(3). Just focus on how you get sum(4) given that sum(3) is already present.

3. Generalize the relation :
    sum(n) = sum(n-1) + n , Once you generalize the relation return this value from your recursion call.
'''

def sum_of_natural_numbers(n):
    if n==1:
        return 1
    return sum_of_natural_numbers(n-1) + n

# Calculate a**b using recursion
def power_of(a,b):
    if b == 0:
        return 1
    return (a ** (b-1)) * a

def palindrom_string(s, l, r):
    if l >= r :
        return True
    if s[l] != s[r]:
        return False
    return palindrom_string(s, l+1, r-1)


if __name__ == '__main__':
    #result = sum_of_natural_numbers(7)
    #result = power_of(2,3)
    s = 'racsdecar'
    result = palindrom_string(s,0,len(s)-1)
    print(result)
