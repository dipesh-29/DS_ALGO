#NOT WORKING CODE

def subset_sum(A,sum,i):
    if i >= len(A):
        return 0
    if sum == 0 :
        return True
    x = subset_sum(A,sum-A[i],i+1)
    if x :
        return True
    return False

if __name__ == '__main__':
    A = [3, 34, 4, 12, 5, 2]
    sum = 9
    i = 0
    result = subset_sum(A,sum,i)
    print(result)
