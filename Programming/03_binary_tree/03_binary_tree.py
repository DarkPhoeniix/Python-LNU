
from binary_tree import BinaryTree, Node


def pretty_print(tree: BinaryTree):
    positions = {}
    for line in tree.tree_by_lines():
        for node in line:
            positions[node] = 0
    tree_by_lines = tree.tree_by_lines()
    find_node_position(tree.root, positions)
    shift = 0
    for i in range(tree.get_height()):
        shift -= coef(i) + 2

    for line in tree_by_lines:
        pos = 0
        slashes = []
        for node in line:
            print(" " * (positions[node] - shift - pos - coef(tree.height - node.height - 1)), end="")
            if node.left is None:
                print(" " * coef(tree.height - node.height - 1), end="")
            else:
                print("_" * coef(tree.height - node.height - 1), end="")
            print(node.data, end="")
            if node.right is None:
                print(" " * coef(tree.height - node.height - 1), end="")
            else:
                print("_" * coef(tree.height - node.height - 1), end="")
            pos = positions[node] - shift + len(str(node.data)) + coef(tree.height - node.height - 1)
            if node.left is not None:
                slashes.append([positions[node] - shift - coef(tree.height - node.height - 1) - 1, "/"])
            if node.right is not None:
                slashes.append([positions[node] - shift + len(str(node.data)) + coef(tree.height - node.height - 1), "\\"])

        print("\n", end="")
        pos = 0
        for slash in slashes:
            print((slash[0] - pos) * ' ', end="")
            print(slash[1], end='')
            pos = slash[0] + 1
        print("\n", end="")


def coef(height):
    return (2 ** height) - 1


def find_node_position(node: Node, positions):
    if node.left is not None:
        positions[node.left] = positions[node] - coef(tree.height - node.height - 1) - 2
        find_node_position(node.left, positions)
    if node.right is not None:
        positions[node.right] = positions[node] + len(str(node.data)) + coef(tree.height - node.height - 1) + 1
        find_node_position(node.right, positions)


inp = input("Input elements (print 'stop' to print tree)\n")
tree = BinaryTree()

while inp != 'stop':
    tree.insert(int(inp))
    inp = input()


pretty_print(tree)
