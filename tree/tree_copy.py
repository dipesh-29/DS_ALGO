from collections import deque

class Node():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def preorder(root):
    if root is not None:
        print(root.data)
        preorder(root.left)
        preorder(root.right)
    return 0

def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.data)
        inorder(root.right)
    return 0

def postorder(root):
    if root is not None:
        postorder(root.left)
        postorder(root.right)
        print(root.data)
    return 0

def levelorder(root):
    if root is not None:
        queue = deque()
        queue.append(root)
        while queue:
            temp = queue.popleft()
            print(temp.data)
            if temp.left:
                queue.append(temp.left)
            if temp.right:
                queue.append(temp.right)
    return 0

def levelorder_reverse(root):
    if root is not None:
        queue = deque()
        stack = []
        queue.append(root)
        while queue:
            temp = queue.popleft()
            if temp.right:
                queue.append(temp.right)
            if temp.left:
                queue.append(temp.left)

            stack.append(temp)
        while stack:
            t = stack.pop()
            print(t.data)
    return 0


def max_in_tree(root):
    if root is not None:
        max = 0
        root_val = root.data
        left = max_in_tree(root.left)
        right = max_in_tree(root.right)
        if max < root_val:
            max = root_val
        if max < left:
            max = left
        if max < right:
            max = right
        return max
    return 0


def max_in_tree_iterative(root):
    if root is not None:
        queue = deque()
        max = -1
        queue.append(root)
        while queue:
            temp = queue.popleft()
            if temp.data > max:
                max = temp.data
            if temp.left:
                queue.append(temp.left)
            if temp.right:
                queue.append(temp.right)

        return max
    return 0

def search_in_tree(root, n):
    if root is not None:
        if root.data == n:
            return 1
        left = search_in_tree(root.left, n)
        right = search_in_tree(root.right, n)

        if left == 1 or right == 1:
            return 1
        return 0
    return 0


def size_of_tree(root):
    if root is not None:
        return size_of_tree(root.left) + size_of_tree(root.right) + 1
    return 0

def height_of_tree(root):
    if root is not None:
        left = height_of_tree(root.left)
        right = height_of_tree(root.right)
        return max(left, right) + 1
    return 0

def height_of_tree_iterative(root):
    if root is not None:
        queue = deque()
        queue.append(root)
        queue.append('$')
        height = 0
        while queue:
            temp = queue.popleft()
            if temp == '$':
                height += 1
                if queue:
                    queue.append('$')
            else:
                if temp.left:
                    queue.append(temp.left)
                if temp.right:
                    queue.append(temp.right)
        return height
    return 0


def number_of_leaves(root):
    if root is not None:
        left = number_of_leaves(root.left)
        right = number_of_leaves(root.right)
        if left == 0 and right == 0:
            return 1
        else:
            return left + right
    return 0


def number_of_leaves_iterative(root):
    if root is not None:
        queue = deque()
        queue.append(root)
        leaves_count = 0
        while queue:
            temp = queue.popleft()
            if(not temp.left and not temp.right):
                leaves_count += 1
            if temp.left:
                queue.append(temp.left)
            if temp.right:
                queue.append(temp.right)
        return leaves_count
    return 0

def number_of_full_nodes_iterative(root):
    if root is not None:
        queue = deque()
        queue.append(root)
        full_count = 0
        while queue:
            temp = queue.popleft()
            if(temp.left and temp.right):
                full_count += 1
            if temp.left:
                queue.append(temp.left)
            if temp.right:
                queue.append(temp.right)
        return full_count
    return 0


def number_of_half_nodes_iterative(root):
    if root is not None:
        queue = deque()
        queue.append(root)
        half_count = 0
        while queue:
            temp = queue.popleft()
            if((temp.left and not temp.right) or (temp.right and not temp.left)):
                half_count += 1
            if temp.left:
                queue.append(temp.left)
            if temp.right:
                queue.append(temp.right)
        return half_count
    return 0

# def number_of_full_nodes(root):
#     if root is not None:
#         res = 0
#         if root.left and root.right:
#             res += 1
#         res += (number_of_leaves(root.left) + number_of_leaves(root.right))
#         return res
#     return 0


# def diameter_of_tree(root, ans):
#     if root is not None:
#         left = diameter_of_tree(root.left, ans)
#         right = diameter_of_tree(root.right, ans)
#
#         ans = max(ans, left+right+1)
#
#         return 1 + left + right
#     return 0


def diameter_of_tree(root, diameter):
    if root is not None:
        left = diameter_of_tree(root.left, diameter)
        right = diameter_of_tree(root.right, diameter)
        if diameter[0] < (left + right + 1):
            diameter[0] = left + right + 1
        return max(left, right) + 1
    return 0


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


def has_path_sum(root, sum):
    if root is not None:
        if (sum - root.data) == 0:
            return 1
        if (sum - root.data) > 0:
            left = has_path_sum(root.left, sum - root.data)
            right = has_path_sum(root.right, sum - root.data)
            if left == 1 or right == 1:
                return 1
        return 0
    return 0


def least_common_ancester(root, num1, num2):
    if root is not None:
        if root.data == num1 or root.data == num2:
            return root
        left = least_common_ancester(root.left, num1, num2)
        right = least_common_ancester(root.right, num1, num2)

        if left and right:
            return root
        if left :
            return root.left
        if right:
            return root.right
    return 0

def print_all_ancestors(root, num, arr):
    if root is not None:
        arr.append(root)
        if root.data == num:
            for item in arr:
                print(item.data)
            return 1

        left = print_all_ancestors(root.left, num, arr)
        right = print_all_ancestors(root.right, num, arr)
        if not left and not right:
            arr.pop()
        return 0
    return 0


def least_common_ancester_binary_tree(root, num1, num2):
    if root is not None:
        if root.data == num1 or root.data == num2:
            return root
        if root.data >= num1 and root.data <= num2:
            return root
        left = least_common_ancester_binary_tree(root.left, num1, num2)
        right = least_common_ancester_binary_tree(root.right, num1, num2)
        if left:
            return left
        if right:
            return right
        return 0
    return 0

def is_binary_search_tree_wrong(root):
    if root is not None:
        l = root.left
        r = root.right
        if l and r:
            if (root.data >= l.data) and (root.data <= r.data):
                return 1
        elif l :
            if (root.data >= l.data):
                return 1
        elif r:
            if (root.data <= r.data):
                return 1
        else:
            return 0

        left = is_binary_search_tree(root.left)
        right = is_binary_search_tree(root.right)

        if left == 0 or right == 0:
            return 0
        return 1
    return 1


def bottom_view_of_tree(root, d, width):
    if root is not None:
        d[width] = root.data
        bottom_view_of_tree(root.left, d, width-1)
        bottom_view_of_tree(root.right, d, width+1)
    return 0


def vertical_sum(root, d, width):
    if root is not None:
        d[width] = d.get(width, 0) + root.data
        vertical_sum(root.left, d,  width-1)
        vertical_sum(root.right, d,  width+1)
    return 0


root = Node(1)
root.left = Node(5)
root.right = Node(2)
root.left.left = Node(4)
root.left.right = Node(8)
root.right.left = Node(7)
root.right.right = Node(6)

# BINARY TREE
root1 = Node(5)
root1.left = Node(3)
root1.right = Node(7)
root1.left.left = Node(1)
root1.left.right = Node(4)
root1.right.left = Node(6)
root1.right.right = Node(8)

# print('------PREORDER-------')
# preorder(root)
# print('------INORDER-------')
#inorder(root1)
# print('------POSTORDER-------')
# postorder(root)
#m = max_in_tree(root)

# m = search_in_tree(root, 0)
# if m == 1:
#     print('FOUND')
# else:
#     print('NOT FOUND')

# m = size_of_tree(root)
# print(m)

# m = height_of_tree(root)
# print(m)

# m = number_of_leaves(root)
# print(m)

#m = number_of_full_nodes(root)
# print(m)

#m = diameter_of_tree(root, 0)

#levelorder(root)
#print(m)
# m = max_in_tree_iterative(root)
# print(m)


#levelorder_reverse(root)

# m = height_of_tree_iterative(root)
# print(m )

# m = number_of_leaves_iterative(root)
# print(m)


# m = number_of_full_nodes_iterative(root)
# print(m)


# m = number_of_half_nodes_iterative(root)
# print(m)

# diameter = [0]
# diameter_of_tree(root,diameter)
# print(diameter)

#print_root_to_leaf_path(root, [])

# m = has_path_sum(root, 9)
# print(m)

# m = least_common_ancester(root, 4,8)
# print(m.data)


#print_all_ancestors(root, 5, [])

# m = least_common_ancester_binary_tree(root1, 4,7)
# if m:
#     print(m.data)
# else:
#     print(0)


# m = is_binary_search_tree_wrong(root1)
# if m:
#     print('TREE IS BINARY TREE')
# else:
#     print('TREE IS NOT BINARY TREE')

d = {}
vertical_sum(root, d, 0)
print(d)




# d = {}
# bottom_view_of_tree(root, d, 0)
# d = sorted(d.items(), key = lambda x:x[0])
#
# for item in d:
#     print(item[1])
