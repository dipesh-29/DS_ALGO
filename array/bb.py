a = [2,4,8,5,1,3,9,0]
b = 0

hash_map = {}
result = []
for num in a:
    if b == 0:
        if b != num:
            result.append([num, b]) 
    elif hash_map.get((b/num)) and ((b % num) == 0) and (num != 0):
        result.append([num, hash_map.get((b/num))])
    else:
        hash_map[num] = num

print(result)
