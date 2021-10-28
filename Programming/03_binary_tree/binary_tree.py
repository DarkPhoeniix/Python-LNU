
class Node:
    def __init__(self, data: int, height: int = 0):
        self.data = data
        self.height = height
        self.left = None
        self.right = None

    def insert(self, data: int, height: int = 0):
        height += 1
        if self.data > data:
            if self.left is None:
                self.left = Node(data, height)
            else:
                self.left.insert(data, height)
                self.left.height = height
        elif self.data < data:
            if self.right is None:
                self.right = Node(data, height)
            else:
                self.right.insert(data, height)
                self.right.height = height
        else:
            self.data = data
            self.height = height


class BinaryTree:
    def __init__(self):
        self.root: Node = None
        self.height = 0
        self.__tree_by_lines = []

    def insert(self, data: int):
        if self.root is not None:
            self.root.insert(data)
        else:
            self.root = Node(data)

    def tree_by_lines(self):
        self.height = self.__find_height(self.root)
        self.__tree_by_lines = [[] for i in range(self.height)]
        if self.root is not None:
            self.__get_tree_by_lines(self.root)
        return self.__tree_by_lines

    def __get_tree_by_lines(self, node: Node):
        if node is not None:
            self.__get_tree_by_lines(node.left)
            self.__tree_by_lines[node.height].append(node)
            self.__get_tree_by_lines(node.right)

    def get_height(self):
        return self.__find_height(self.root)

    def __find_height(self, node: Node):
        if node is None:
            return 0
        return max(self.__find_height(node.left), self.__find_height(node.right)) + 1

    def get_preorder(self):
        data_list = []
        if self.root is not None:
            self.__get_preorder(self.root, data_list)
        return data_list

    def __get_preorder(self, node: Node, ls):
        if node is not None:
            ls.append(node.data)
            self.__get_preorder(node.left, ls)
            self.__get_preorder(node.right, ls)

    def get_inorder(self):
        data_list = []
        if self.root is not None:
            self.__get_inorder(self.root, data_list)
        return data_list

    def __get_inorder(self, node: Node, ls):
        if node is not None:
            self.__get_inorder(node.left, ls)
            ls.append(node.data)
            self.__get_inorder(node.right, ls)

    def get_postorder(self):
        data_list = []
        if self.root is not None:
            self.__get_postorder(self.root, data_list)
        return data_list

    def __get_postorder(self, node: Node, ls):
        if node is not None:
            self.__get_postorder(node.left, ls)
            self.__get_postorder(node.right, ls)
            ls.append(node.data)
