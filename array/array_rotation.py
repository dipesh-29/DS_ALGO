def find_gcd(a,b):
    if b == 0:
        return a
    return find_gcd(b, a%b)


def arr_rotation(arr, k):
    gcd = find_gcd(k, len(arr))
    for index in range(gcd):
        i = index
        j = (i + k) % len(arr)
        t = arr[i]
        while(j != index):
            arr[i] = arr[j]
            i = j
            j = (i + k) % len(arr)
        arr[i] = t
    print(arr)



arr = [3,5,2,7,1,6,0,8,4,9]
print(arr)
arr_rotation(arr, 4)
