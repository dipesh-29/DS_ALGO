'''
Given number n count the number of set bits in binary representation of number.
'''

def count_set_bits(n,count,num):
    if num > n :
        return count

    count += 1 if (n & num) else 0
    num = num << 1
    print(count)
    count_set_bits(n, count, num)
    return count



def count(n):
    cnt = 0
    cnt = count_set_bits(n,cnt,1)
    return cnt



if __name__ == '__main__':
    n = 26
    result = count(n)
    print(result)
