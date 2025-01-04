class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

def list_traversal_iterative(head):
    start_ptr = head
    while start_ptr is not None:
        print(start_ptr.data)
        start_ptr = start_ptr.next

def insert_node_at_beginning(head, node_val):
    n = Node(node_val)
    n.next = head
    head = n
    return head

def insert_node_at_end(head, node_val):
    start_ptr = head
    n = Node(node_val)
    while start_ptr.next is not None:
        start_ptr = start_ptr.next
    start_ptr.next = n
    return head

def insert_at_given_node(head, node_val, search_node):
    start_ptr = head
    n = Node(node_val)
    while start_ptr.data != search_node :
        start_ptr = start_ptr.next
    n.next = start_ptr.next
    start_ptr.next = n
    return head

def delete_node(head, search_node):
    start_ptr = head
    prev_ptr = start_ptr
    while start_ptr.data != search_node:
        prev_ptr = start_ptr
        start_ptr = start_ptr.next

    if start_ptr == head:
        head = head.next
        start_ptr = None
        return head
    else:
        prev_ptr.next = start_ptr.next
        start_ptr = None
        return head


def get_length(head):
    if head is None:
        return 0
    else:
        start_ptr = head
        length = 0
        while start_ptr is not None :
            start_ptr = start_ptr.next
            length += 1
        return length


def kth_node_from_last(head, k):
    length_of_ll = get_length(head)
    if k > length_of_ll :
        print("Not a valid input")
        return head
    else:
        start_ptr = head
        for index in range(k):
            start_ptr = start_ptr.next
        prev_ptr = head
        while start_ptr is not None:
            start_ptr = start_ptr.next
            prev_ptr = prev_ptr.next
        print(prev_ptr.data)
        return head

def null_terminated_or_cycle_hashing(head):
    d = {}
    start_ptr = head
    while start_ptr is not None:
        if start_ptr.next in d:
            print("Linked list is having cycle")
            return 1
        d[start_ptr.next] = start_ptr.data
        start_ptr = start_ptr.next
    print("Linked list is null terminated.")
    return 0

def null_terminated_or_cycle_racing(head):
    if head is None:
        return None
    elif head.next is None :
        return 0
    else:
        cycle_length = 0
        fast_ptr = head
        slow_ptr = head
        while fast_ptr.next is not None and fast_ptr.next.next is not None:
            fast_ptr = fast_ptr.next.next
            slow_ptr = slow_ptr.next
            if fast_ptr == slow_ptr :
                # Finding length of cycle
                fast_ptr = fast_ptr.next
                cycle_length += 1
                while slow_ptr != fast_ptr:
                    fast_ptr = fast_ptr.next
                    cycle_length += 1

                # Finding starting of cycle
                slow_ptr = head
                while slow_ptr != fast_ptr :
                    slow_ptr = slow_ptr.next
                    fast_ptr = fast_ptr.next
                    cycle_length += 1
                print("Linked list is having cycle of length %d", cycle_length)
                print("Linked list is having cycle starting from Node %d", slow_ptr.data)
                return 1
        print("Linked list is null terminated.")
        return 0


def reverse_iterative(head):
    if head is None :
        return None
    else:
        prev_ptr = None
        curr_ptr = head
        while curr_ptr is not None :
            next_ptr = curr_ptr.next
            curr_ptr.next = prev_ptr
            prev_ptr = curr_ptr
            curr_ptr = next_ptr
        head = prev_ptr
        return head


def reverse_recursive(head):
    if head is None or head.next is None:
        return head

    next_ptr = head.next
    head.next = None

    return_reverse = reverse_recursive(next_ptr)
    next_ptr.next = head
    return return_reverse


# Two singly linked lists intersect at one point and become a single linked list. Find the merging point.
def merging_intersect(head1, head2):
    if head1 is None or head2 is None:
        return None

    l1_length = get_length(head1)
    l2_length = get_length(head2)

    if l1_length > l2_length :
        for index in range(l1_length - l2_length) :
            head1 = head1.next
    else:
        for index in range(l2_length - l1_length) :
            head2 = head2.next

    while head1 is not None and head2 is not None :
        if head1.next == head2.next :
            return head1.next

        head1 = head1.next
        head2 = head2.next

    return None


def middle_of_linked_list(head):
    if head is None:
        return None
    slow_ptr = head
    fast_ptr = head

    while fast_ptr is not None and fast_ptr.next is not None :
        fast_ptr = fast_ptr.next.next
        slow_ptr = slow_ptr.next

    return slow_ptr.data


def print_reverse(head):
    if head is None:
        return head
    print_reverse(head.next)
    print(head.data)
    return head


# ***************** NOT WORKING ********************
#GIven two sorted linked list merge them to single linked list. extra LL
def merge_sorted_linked_list(head1, head2) :
    if head1 is None :
        return head2
    if head2 is None :
        return head1

    result_list = SinglyLinkedList()
    if head1.data <= head2.data :
        result_list.head = head1
    else:
        result_list.head = head2

    while head1 and head2 :
        if head1.data <= head2.data :
            ll_head.next = head1
            head1 = head1.next
        else:
            ll_head.next =  head2
            head2 = head2.next
        ll_head = ll_head.next

    if head1 :
        ll_head.next = head1
    else:
        ll_head.next = head2
    return ll_head.next


def reverse_pairwise(head):
    if head is None :
        return head

    prev_ptr = head
    while prev_ptr is not None and prev_ptr.next is not None :
        next_ptr = prev_ptr.next

        temp = prev_ptr.data
        prev_ptr.data = next_ptr.data
        next_ptr.data = temp

        prev_ptr = next_ptr.next

    return head


def reverse_pairwise_recursive(head):
    if head is None:
        return head

    temp = head



if __name__=="__main__":
    # Creating nodes of Linked List.
    n1 = Node(1)
    n2 = Node(3)
    n3 = Node(5)
    n4 = Node(6)
    n5 = Node(9)
    n6 = Node(13)
    n7 = Node(15)
    n8 = Node(19)
    #n9 = Node(21)

    # Initialising Linked List
    list1 = SinglyLinkedList()
    list1.head = n1
    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5
    n5.next = n6
    n6.next = n7
    n7.next = n8
    #n8.next = n9
    #n9.next = n5

    l1 = Node(2)
    l2 = Node(4)
    l3 = Node(7)
    l4 = Node(11)
    l5 = Node(12)
    l6 = Node(17)
    l7 = Node(20)

    list2 = SinglyLinkedList()
    list2.head = l1
    l1.next = l2
    l2.next = l3
    l3.next = l4
    l4.next = l5
    l5.next = l6
    l6.next = l7


    '''
    list_traversal_iterative(list1.head)
    list1.head = insert_node_at_beginning(list1.head, 9)
    print("After adding node at beginning")
    list_traversal_iterative(list1.head)

    print("After adding node at end")
    insert_node_at_end(list1.head, 4)
    list_traversal_iterative(list1.head)

    print("After adding node after given node")
    insert_at_given_node(list1.head, 7, 8)
    list_traversal_iterative(list1.head)

    print("After deleting node")
    list1.head = delete_node(list1.head, 4)
    list_traversal_iterative(list1.head)

    print("Kth Node from end")
    list1.head = kth_node_from_last(list1.head, 7)


    #null_terminated_or_cycle_hashing(list1.head)
    #null_terminated_or_cycle_racing(list1.head)
    #list1.head = reverse_iterative(list1.head)
    #list_traversal_iterative(list1.head)
    list_traversal_iterative(list1.head)
    print("Reverse Linked List Recursive")
    list1.head = reverse_recursive(list1.head)
    list_traversal_iterative(list1.head)

    print("LIST1 Length : ")
    l1_length = get_length(list1.head)
    print(l1_length)
    print("LIST1 Elements :")
    list_traversal_iterative(list1.head)
    print("LIST2 Length : ")
    l2_length = get_length(list2.head)
    print(l2_length)
    print("LIST2 Elements :")
    list_traversal_iterative(list2.head)

    print("MERGE INTERSACT : ")
    result = merging_intersect(list1.head, list2.head)
    print(result.data)

    list_traversal_iterative(list1.head)
    print("Middle element of linked list.")
    result = middle_of_linked_list(list1.head)
    print(result)

    list_traversal_iterative(list1.head)
    print("Reverse print of linked list.")
    print_reverse(list1.head)

    ll = merge_sorted_linked_list(list1.head, list2.head)
    list_traversal_iterative(ll)
    '''
    list_traversal_iterative(list1.head)
    print("Reverse Pair wise .............")
    ll = reverse_pairwise(list1.head)
    list_traversal_iterative(ll)
