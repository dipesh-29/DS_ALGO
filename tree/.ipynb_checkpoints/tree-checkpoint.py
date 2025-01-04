class Node():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.nextsibling = None


def preorder_traversal(root):
    if root is None:
        return root
    print(root.data)
    preorder_traversal(root.left)
    preorder_traversal(root.right)

def preorder_traversal_iterative(root):
    if root is None:
        return root
    stack = []
    while 1:
        while root is not None :
            print(root.data)
            stack.append(root)
            root = root.left

        if not stack:
            break
        root = stack.pop()
        root = root.right
    del(stack)

def inorder_traversal(root):
    if root is None:
        return root
    inorder_traversal(root.left)
    print(root.data)
    inorder_traversal(root.right)

def inorder_traversal_iterative(root):
    if root is None:
        return root
    stack = []
    while 1 :
        while root is not None:
            stack.append(root)
            root = root.left
        if not stack:
            break
        root = stack.pop()
        print(root.data)
        root = root.right
    del(stack)

def postorder_traversal(root):
    if root is None:
        return root
    postorder_traversal(root.left)
    postorder_traversal(root.right)
    print(root.data)

def levelorder_traversal(root):
    if root is None:
        return 0
    queue = []
    queue.append(root)
    while queue :
        root = queue.pop(0)
        print(root.data)
        if root.left :
            queue.append(root.left)
        if root.right :
            queue.append(root.right)
    del(queue)
    return root

def find_max_element(root):
    if root is None:
        return root

    if not root.left and not root.right :
        return root.data

    left_max = find_max_element(root.left)
    right_max = find_max_element(root.right)
    return max(left_max, right_max)


def find_max_element_iterative(root):
    if root is None:
        return root
    queue = []
    queue.append(root)
    max_element = root.data
    while queue:
        root = queue.pop(0)
        if max_element < root.data:
            max_element = root.data
        if root.left:
            queue.append(root.left)
        if root.right:
            queue.append(root.right)
    del(queue)
    return max_element


def search_element(root, x):
    if root is None:
        return root
    if root.data == x :
        return 1
    left_tree = search_element(root.left, x)
    right_tree = search_element(root.right, x)

    if left_tree == 1 or right_tree == 1:
        return 1

def size_of_tree(root):
    if root is None:
        return 0
    return size_of_tree(root.left) + size_of_tree(root.right) + 1

def levelorder_reverse(root):
    if root is None:
        return root
    queue = []
    stack = []
    queue.append(root)
    while queue:
        root = queue.pop(0)
        stack.append(root)
        if root.right:
            queue.append(root.right)
        if root.left:
            queue.append(root.left)
    while stack:
        x = stack.pop()
        print(x.data)
    del(stack)
    del(queue)


#Need to confirm
def height_of_tree(root):
    if root is None:
        return root
    if root.left is None and root.right is None:
        return 0

    left_height = height_of_tree(root.left)
    right_height = height_of_tree(root.right)
    return max(left_height, right_height) + 1


def height_of_tree_iterative(root):
    if root is None:
        return root
    queue = []
    level = 0
    queue.append(root)
    queue.append('$')
    while queue:
        root = queue.pop(0)
        if root == '$':
            if queue :
                queue.append('$')
                level += 1
        else:
            if root.left :
                queue.append(root.left)
            if root.right :
                queue.append(root.right)
    del(queue)
    return level

def number_of_leaves(root):
    if root is None:
        return 0

    if root.left is None and root.right is None:
        return 1

    left_leave_nodes = number_of_leaves(root.left)
    right_leave_nodes = number_of_leaves(root.right)
    return left_leave_nodes + right_leave_nodes

def number_of_full_nodes(root):
    if root is None:
        return 0
    left_leave_nodes = number_of_full_nodes(root.left)
    right_leave_nodes = number_of_full_nodes(root.right)
    if root.left and root.right:
        return 1 + (left_leave_nodes + right_leave_nodes)
    return 0

def diameter_of_tree(root, diameter) :
    if root is None:
        return 0, diameter

    left_height, diameter = diameter_of_tree(root.left, diameter)
    right_height, diameter = diameter_of_tree(root.right, diameter)

    diameter_with_root_node = left_height+right_height+ 1

    diameter = max(diameter, diameter_with_root_node)

    return max(left_height, right_height) + 1, diameter


def level_with_maximum_sum(root):
    if root is None:
        return root
    queue = []
    queue.append(root)
    queue.append('$')
    level = 0
    max_level = 0
    max_sum = root.data
    level_sum = 0
    while queue:
        root = queue.pop(0)
        if root == '$':
            level += 1
            if max_sum < level_sum :
                max_sum = level_sum
                max_level = level
            if queue:
                queue.append('$')
            level_sum = 0
        else:
            level_sum += root.data
            if root.left:
                queue.append(root.left)
            if root.right:
                queue.append(root.right)
    del(queue)
    return (max_level, max_sum)

def print_root_to_leaf_path(root, arr):
    if root is not None:
        arr.append(root)
        left = print_root_to_leaf_path(root.left , arr)
        right = print_root_to_leaf_path(root.right , arr)
        if left == 0 and right == 0:
            for item in arr:
                print(item.data)
            print('-------')
            arr.pop()
        elif arr:
            arr.pop()
        return 1
    return 0


def has_path_sum(root, sum) :
    if root is None:
        return 0
    if root.data == sum :
        return 1
    left = has_path_sum(root.left, sum - root.data)
    right = has_path_sum(root.right, sum - root.data)

    if left or right:
        return 1


def sum_of_all_nodes(root):
    if root is None:
        return 0

    left = sum_of_all_nodes(root.left)
    right = sum_of_all_nodes(root.right)

    return left + right + root.data


def convert_to_mirror(root):
    if root is None:
        return 0

    convert_to_mirror(root.left)
    convert_to_mirror(root.right)

    temp = root.left
    root.left = root.right
    root.right = temp
    return root


# NOT WORKING
def check_mirror(root1, root2):
    if not root1 and not root2:
        return 1
    if not root1 or not root2:
        return 0
    if root1.data != root2.data :
        return 0
    else:
        return check_mirror(root1.left, root2.right) and check_mirror(root1.right, root2.left)


def leaset_common_ancestor(root, node1, node2):
    if root is None:
        return None

    if root.data == node1 or root.data == node2 :
        return root

    left = leaset_common_ancestor(root.left, node1, node2)
    right = leaset_common_ancestor(root.right, node1, node2)

    if left and right :
        return root
    if left :
        return left
    if right :
        return right

def print_all_ancestors(root, node):
    if root is None:
        return 0

    if root.data == node:
        return 1

    left = print_all_ancestors(root.left, node)
    right = print_all_ancestors(root.right, node)

    if left or right:
        print(root.data)
        return 1
    else:
        return 0


# NOT CORRECT
def zigzag_traversal(root) :
    if root is None:
        return None
    level = 0
    queue = []
    queue.append(root)
    queue.append('$')
    while queue:
        root = queue.pop(0)
        if root == '$':
            if queue:
                level += 1
                queue.append('$')
        else:
            print(root.data)
            if level % 2 == 0:
                if root.right:
                    queue.append(root.right)
                if root.left:
                    queue.append(root.left)
            else:
                if root.left:
                    queue.append(root.left)
                if root.right:
                    queue.append(root.right)
    del(queue)
    return 1

def vertical_sum(root, sum_map, column_index):
    if root is None:
        return None
    sum_map[column_index] = sum_map.get(column_index, 0) + root.data
    vertical_sum(root.left, sum_map, column_index-1)
    vertical_sum(root.right, sum_map, column_index+1)
    return sum_map

# ONly for perfect binary tree.
def populate_nextsibling(root):
    if root is None:
        return None

    if root.left :
        root.left.nextsibling = root.right
    if root.right :
        root.right.nextsibling = root.nextsibling.left if root.nextsibling is not None else None

    populate_nextsibling(root.left)
    populate_nextsibling(root.right)


def print_nextsibling(root):
    if root is None:
        return root

    if root.nextsibling is None:
        print("Next sibling of " + str(root.data) + " is : None " )
    else:
        print("Next sibling of " + str(root.data) + " is : " + str(root.nextsibling.data))

    print_nextsibling(root.left)
    print_nextsibling(root.right)

def left_view_of_tree(root):
    if root is None:
        return None
    queue = []
    queue.append(root)
    queue.append('$')
    result = []
    result.append(root.data)
    while queue:
        temp = queue.pop(0)
        if temp == '$':
            if queue:
                queue.append('$')
                result.append(queue[0].data)
        else:
            if temp.left:
                queue.append(temp.left)
            if temp.right:
                queue.append(temp.right)
    del(queue)
    return result

def right_view_of_tree(root):
    if root is None:
        return None
    queue = []
    queue.append(root)
    queue.append('$')
    result = []
    while queue:
        temp = queue.pop(0)
        if temp == '$':
            if queue:
                queue.append('$')
        else:
            if queue[0] == '$':
                result.append(temp.data)
            if temp.left:
                queue.append(temp.left)
            if temp.right:
                queue.append(temp.right)
    del(queue)
    return result

def bottom_view_of_tree(root, bottom_elements):
    #Bottom view of tree is nothing but all the leaf nodes.
    if root is None:
        return None
    if root.left is None and root.right is None:
        bottom_elements.append(root.data)
    bottom_view_of_tree(root.left, bottom_elements)
    bottom_view_of_tree(root.right, bottom_elements)
    return bottom_elements


def top_view_of_tree(root, top_view, column):
    if root is None:
        return None
    if column not in top_view:
        top_view[column] = root.data
    top_view_of_tree(root.left,top_view,column-1)
    top_view_of_tree(root.right,top_view,column+1)

    return top_view


# NOT CORRECT. PLEASE CHECK THE SEQUENCE TO SHOW THE OUTPUT.
def boundry_traversal(root):
    if root is None:
        return None

    result = []
    leftview_result = left_view_of_tree(root)
    bottom_view_result = bottom_view_of_tree(root, [])
    #RIght view result should be in bottom up format. So reverse the output
    right_view_result = right_view_of_tree(root)
    right_view_result.reverse()

    print("---------------------------------------")
    print("Left View : ")
    print(leftview_result)
    print("Bottom View : ")
    print(bottom_view_result)
    print("Right View Reverse: ")
    print(right_view_result)
    print("---------------------------------------")
    result = leftview_result
    for n in bottom_view_result :
        if n not in result :
            result.append(n)

    for n in right_view_result :
        if n not in result :
            result.append(n)
    return result


'''
def constuct_binary_tree_inorder_preorder() :

def print_all_ancestors(root) :

def zigzag_traversal(root) :

def vertical_sum(root) :

def ILILLI(root) :
    #Question number 33

def populate_nextsibling(root) :

def min_depth(root) :

def check_if_complete_binary_tree(root) :


# BINARY SEARCH TREE :

# Searching an element in BST
# Adding an element in BST
# deleting an element in BST

'''



if __name__=="__main__":
    root = Node(1)
    root.left = Node(5)
    root.right = Node(13)
    root.left.left = Node(4)
    root.left.right = Node(8)
    root.right.left = Node(15)
    root.right.right = Node(6)
    root.right.right.left = Node(41)
    root.right.right.right = Node(21)
    root.right.right.right.right = Node(7)
    root.right.left.left = Node(23)
    root.right.left.left.left = Node(21)
    root.right.left.left.left.left = Node(38)

    #Preorder traversal
    '''
    print("Preorder :")
    preorder_traversal(root)
    print("Preorder Iterative : ")
    preorder_traversal_iterative(root)

    print("Inorder :")
    inorder_traversal(root)
    print("Inorder Iterative : ")
    inorder_traversal_iterative(root)

    print("Postorder :")
    postorder_traversal(root)

    print("Level order traversal")
    levelorder_traversal(root)

    print("Maximum Element in tree")
    result = find_max_element(root)
    print(result)
    result = find_max_element_iterative(root)
    print(result)

    result = search_element(root, 17)
    if result:
        print("ELement Found")
    else:
        print("Element Not Found")

    print("Size Of Tree : ")
    result = size_of_tree(root)
    print(result)

    print("Level Order Reverse :")
    levelorder_reverse(root)

    print("Height Of Tree : ")
    result  = height_of_tree(root)
    print(result)

    print("Height Of Tree Iterative : ")
    result = height_of_tree_iterative(root)
    print(result)

    print("Number Of Leave Nodes : ")
    result = number_of_leaves(root)
    print(result)

    print("Number Of Full Nodes : ")
    result = number_of_full_nodes(root)
    print(result)
    '''
    print("Diameter of Tree : ")
    result = diameter_of_tree(root, 0)
    print(result[1])
    '''
    print("Maximum level sum of Tree : ")
    result = level_with_maximum_sum(root)
    print(result)

    print("Root To Leaf Path Of Tree : ")
    print_root_to_leaf_path(root, [])

    print("Check If Path Sum Exist : ")
    result = has_path_sum(root, 21)
    if result :
        print("Path Sum Exist. ")
    else:
        print("Path Sum does not exist")

    print("Sum Of All Nodes Of Tree")
    result = sum_of_all_nodes(root)
    print(result)


    levelorder_traversal(root)
    print("Convert to Mirror : ")
    root1 = convert_to_mirror(root)
    levelorder_traversal(root1)

    result = check_mirror(root, root1)
    if result :
        print("Both Trees are Mirror Of Each Other")
    else:
        print("Both Trees Are Not Mirror of each other")

    print("Least Common Ancester of nodes : ")
    result = leaset_common_ancestor(root, 7, 41)
    print(result.data)

    print("Printing All Ancesters of Node : ")
    print_all_ancestors(root, 41)

    print("Zigzag Traversal : ")
    zigzag_traversal(root)

    print("Vertical Sum : ")
    sum_map = vertical_sum(root, {}, 0)
    for item in sum_map:
        print(item)
        print(sum_map[item])
        print('--------')

    print_nextsibling(root)
    print("Populating NextSibling : ")
    populate_nextsibling(root)
    print_nextsibling(root)

    print("Left View Of Tree : ")
    result = left_view_of_tree(root)
    print(result)

    print("Right View Of Tree : ")
    result = right_view_of_tree(root)
    print(result)

    print("Bottom View Of Tree : ")
    result = bottom_view_of_tree(root,[])
    print(result)

    print("Boundry Traversal : ")
    result = boundry_traversal(root)
    print(result)


    print("Top View Of Tree : ")
    result = top_view_of_tree(root,{},0)
    start = min(result.keys())
    end = max(result.keys())
    for index in range(start, end+1):
        print(result[index])
    '''
