def catalan_number(n):
    if n == 0 or n == 1:
        return 1
    res = 0
    for i in range(n):
        res += catalan_number(i) * catalan_number(n-i-1)
    return res


def catalan_number_dp(n):
    cn = []
    cn.append(1)
    cn.append(1)

    while len(cn) != n:
        next_num = 0
        for ind in range(len(cn)):
            next_num += cn[ind] * cn[len(cn) - ind - 1]
        cn.append(next_num)
    return cn[-1]




if __name__=="__main__":
    result = catalan_number_dp(7)
    print(result)
