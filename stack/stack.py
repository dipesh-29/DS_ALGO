'''
Stack has following operations :
1. push
2. pop
3. top
4. size
5. empty
'''

class Stack :
    def __init__(self):
        self.s = []
        self.top = -1
        self.empty = True

    def stack_push(self, data):
        #print("Pushing data : ")
        self.top += 1
        self.s.append(data)
        self.empty = False

    def stack_pop(self) :
        #print("Popping data : ")
        if self.empty:
            print("Stack is Empty")
            return []
        self.s.pop()
        self.top -= 1
        if self.top == -1 :
            self.empty = True

    def size(self):
        return self.top+1

    def empty(self):
        return self.empty

    def stack_print(self):
        for index in range(self.top, -1, -1):
            print(self.s[self.top])


if __name__=="__main__":
    print("-------")
    S1 = Stack()
    S1.stack_push(3)
    S1.stack_push(4)
    S1.stack_print()
    S1.stack_pop()
    S1.stack_print()
    S1.stack_push(1)
    S1.stack_print()
    S1.stack_pop()
    S1.stack_print()
    S1.stack_push(9)
    S1.stack_print()
