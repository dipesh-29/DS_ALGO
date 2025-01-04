def ugly_numbers(n):
    un = []
    un.append(1)
    mult2 = 0
    mult3 = 0
    mult5 = 0
    while len(un) != n :
        x2 = un[mult2] * 2
        x3 = un[mult3] * 3
        x5 = un[mult5] * 5
        next_item = min(x2,x3,x5)
        if next_item == x2 :
            mult2 += 1
        if next_item == x3 :
            mult3 += 1
        if next_item == x5 :
            mult5 += 1
        un.append(next_item)
    return un[-1]

if __name__=="__main__":
    n = 190
    result = ugly_numbers(n)
    print(result)
