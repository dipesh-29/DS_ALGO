import heapq

#NOT WORKING
def merge_m_sorted_list(m_list):
    result = []
    m = len(m_list)
    heap = []
    for index in range(m):
        heapq.heappush(heap,[m_list[index][0],index])

    while heap :
        item, index = heapq.heappop(heap)
        result.append(item)
        if m_list[index]:
            m_list[index].pop(0)
        print(m_list)
        if m_list[index]:
            heapq.heappush(heap,[m_list[index][0],index])
    return result


if __name__ == '__main__':
    m_list = [[10, 20, 30, 40], [15, 25, 35], [27, 29, 37, 48, 93], [32, 33]]
    result = merge_m_sorted_list(m_list)
    print(result)
