
from binary_tree import BinaryTree
import unittest


class TestBinaryTreeMethods(unittest.TestCase):
    def test_insert(self):
        tree = BinaryTree()
        tree.insert(10)
        tree.insert(5)
        tree.insert(15)
        tree.insert(0)
        tree.insert(7)
        tree.insert(20)
        tree.insert(13)
        correct_array = [[10],
                         [5, 15],
                         [0, 7, 13, 20]]
        given_array = tree.tree_by_lines()
        for line in range(len(given_array)):
            for item in range(len(given_array[line])):
                self.assertEqual(correct_array[line][item], given_array[line][item].data)

    def test_height(self):
        tree = BinaryTree()
        tree.insert(10)
        self.assertEqual(tree.get_height(), 1)
        tree.insert(5)
        self.assertEqual(tree.get_height(), 2)
        tree.insert(15)
        self.assertEqual(tree.get_height(), 2)
        tree.insert(0)
        self.assertEqual(tree.get_height(), 3)
        tree.insert(7)
        self.assertEqual(tree.get_height(), 3)
        tree.insert(20)
        self.assertEqual(tree.get_height(), 3)
        tree.insert(13)
        self.assertEqual(tree.get_height(), 3)
        tree.insert(-10)
        self.assertEqual(tree.get_height(), 4)

    def test_preorder(self):
        tree = BinaryTree()
        tree.insert(10)
        tree.insert(5)
        tree.insert(15)
        tree.insert(0)
        tree.insert(7)
        tree.insert(20)
        tree.insert(13)
        self.assertEqual(tree.get_preorder(), [10, 5, 0, 7, 15, 13, 20])

    def test_inorder(self):
        tree = BinaryTree()
        tree.insert(10)
        tree.insert(5)
        tree.insert(15)
        tree.insert(0)
        tree.insert(7)
        tree.insert(20)
        tree.insert(13)
        self.assertEqual(tree.get_inorder(), [0, 5, 7, 10, 13, 15, 20])

    def test_postorder(self):
        tree = BinaryTree()
        tree.insert(10)
        tree.insert(5)
        tree.insert(15)
        tree.insert(0)
        tree.insert(7)
        tree.insert(20)
        tree.insert(13)
        self.assertEqual(tree.get_postorder(), [0, 7, 5, 13, 20, 15, 10])
