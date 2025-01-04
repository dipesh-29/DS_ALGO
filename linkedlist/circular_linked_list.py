class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None


def list_traversal(head):
    start_ptr = head
    while start_ptr.next != head:
        print(start_ptr.data)
        start_ptr = start_ptr.next
    print(start_ptr.data)


def insert_node_at_beginning(head, node_val):
    n = Node(node_val)
    start_ptr = head
    while start_ptr.next != head :
        start_ptr = start_ptr.next

    start_ptr.next = n
    n.next = head
    head = n
    return head

def insert_node_at_end(head, node_val):
    n = Node(node_val)
    start_ptr = head
    while start_ptr.next != head :
        start_ptr = start_ptr.next
    start_ptr.next = n
    n.next = head
    return head

def insert_after_given_node(head, node_val, search_node):
    n = Node(node_val)
    start_ptr = head
    while start_ptr.data != search_node :
        start_ptr = start_ptr.next

    if start_ptr.next == head :
        #insert after last node
        n.next = head
        start_ptr.next = n
    else:
        n.next = start_ptr.next
        start_ptr.next = n
    return head

def delete_node(head, node_val):
    start_ptr = head
    prev_ptr = start_ptr
    while start_ptr.data != node_val:
        prev_ptr = start_ptr
        start_ptr = start_ptr.next

    if start_ptr == head :
        while prev_ptr.next != head :
            prev_ptr = prev_ptr.next
        head = head.next
        prev_ptr.next = head
        start_ptr = None
    else:
        prev_ptr.next = start_ptr.next
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
    list1 = CircularLinkedList()
    list1.head = n1
    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5
    n5.next = n1

    print("List Traverse.....")
    list_traversal(list1.head)
    print("ADDING NODE AT BEGINNING............")
    list1.head = insert_node_at_beginning(list1.head, 9)
    list_traversal(list1.head)
    print("ADDING NODE AT END............")
    list1.head = insert_node_at_end(list1.head, 4)
    list_traversal(list1.head)
    print("ADDING NODE AFTER GIVEN NODE")
    list1.head = insert_after_given_node(list1.head, 7, 8)
    list_traversal(list1.head)
    print("DELETING NODE.............")
    list1.head = delete_node(list1.head, 4)
    list_traversal(list1.head)
