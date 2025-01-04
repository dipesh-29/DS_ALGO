'''
Questions : 
1. Given an array of n numbers, write program for checking if any duplicate element or not? 
2. Given an array of n numbers, write program to fine the element which appears maximum number of time in array?
'''

class ArrayQuestions:
    def __init__(self, arr):
        self.arr = arr

    # 1.1
    def check_if_duplicate_number(self):
        for index in range(len(self.arr)-1):
            for index1 in range(index+1, len(self.arr)-1):
                if self.arr[index] == self.arr[index1]:
                    return True
        return False
    
    # 1.2
    def check_if_duplicate_number_improved(self):
        self.arr.sort()
        for index in range(1,len(self.arr)-1):
            if self.arr[index-1] == self.arr[index]:
                return True
        return False

    #1.3
    def check_if_duplicate_number_optimised(self):
        hash_table = {}
        for item in self.arr:
            if hash_table.get(item):
                return True
            else:
                hash_table[item] = 1
        return False

    '''
    1.4 : ????? (How to handle 0??)
    - Array is not read only. 
    - All the elements are in range of 1 to n-1
    '''
    def check_if_duplicate_number_condition(self):
        for item in self.arr:
            if self.arr[abs(item)] < 0:
                print(self.arr)
                return True
            else:
                self.arr[item] = self.arr[item] * -1
        else:
            print(self.arr)
            return False
        


    

if __name__=='__main__':
    arr = [1,3,5,7,6,8,4,9,2]
    aq = ArrayQuestions(arr)
    #result = aq.check_if_duplicate_number()
    #result = aq.check_if_duplicate_number_improved()
    #result = aq.check_if_duplicate_number_optimised()
    result = aq.check_if_duplicate_number_condition()
    if result:
        print("There is duplicate element in array.")
    else:
        print("There is no duplicate element in array.")
