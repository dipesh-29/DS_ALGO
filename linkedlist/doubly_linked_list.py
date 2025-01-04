class Node :
    def __init__(self, value):
        self.data = value
        self.prev = None
        self.next = None

class Doubly_linked_list :
    def __init__(self):
        self.head = None


def list_traversal(head):
    start_ptr = head
    prev_ptr = start_ptr
    print("Printing Forward : ")
    while start_ptr is not None:
        print(start_ptr.data)
        prev_ptr = start_ptr
        start_ptr = start_ptr.next

    print("Printing Backward : ")
    while prev_ptr is not None:
        print(prev_ptr.data)
        prev_ptr = prev_ptr.prev


def insert_node_at_beginning(head, node_val) :
    n = Node(node_val)
    n.next = head
    head.prev = n
    head = n
    return head

def insert_node_at_end(head, node_val):
    n = Node(node_val)
    start_ptr = head
    prev_ptr = start_ptr
    while start_ptr is not None:
        prev_ptr = start_ptr
        start_ptr = start_ptr.next
    prev_ptr.next = n
    n.prev = prev_ptr
    return head

def insert_at_given_node(head, node_val, search_node):
    n = Node(node_val)
    start_ptr = head
    while start_ptr.data != search_node:
        start_ptr = start_ptr.next
    n.prev = start_ptr
    n.next = start_ptr.next
    start_ptr.next.prev = n
    start_ptr.next = n
    return head

def delete_node(head, node_val):
    start_ptr = head
    prev_ptr = start_ptr
    while start_ptr.data != node_val:
        prev_ptr = start_ptr
        start_ptr = start_ptr.next

    if start_ptr == head:
        #First node to be deleted
        head = head.next
        head.prev = None
        start_ptr = None
    else:
        if start_ptr.next is None:
            #Last Node to be deleted
            prev_ptr.next = None
            start_ptr = None
        else:
            prev_ptr.next =  start_ptr.next
            start_ptr.next.prev = prev_ptr
            start_ptr = None
    return head


if __name__=="__main__":
    # Creating nodes of Linked List.
    n1 = Node(5)
    n2 = Node(3)
    n3 = Node(8)
    n4 = Node(1)
    n5 = Node(2)

    # Initialising Linked List
    list1 = Doubly_linked_list()
    list1.head = n1
    n1.next = n2
    n2.next = n3
    n2.prev = n1
    n3.next = n4
    n3.prev = n2
    n4.next = n5
    n4.prev = n3
    n5.prev = n4

    list_traversal(list1.head)
    print("ADDING AT BEGINNING......")
    list1.head = insert_node_at_beginning(list1.head, 9)
    list_traversal(list1.head)
    print("ADDING AT END..........")
    list1.head = insert_node_at_end(list1.head, 4)
    list_traversal(list1.head)
    print("ADDING AFTER GIVEN NODE.....")
    list1.head = insert_at_given_node(list1.head, 7, 8)
    list_traversal(list1.head)
    print("DELETING NODE..............")
    list1.head = delete_node(list1.head,4)
    list_traversal(list1.head)
