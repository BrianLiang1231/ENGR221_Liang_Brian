"""
Binary Search Tree implementation for Lab 8.
"""


class BinarySearchTree:
    """An unbalanced binary search tree."""

    def __init__(self):
        self.__root = None

    def insert(self, insertKey, insertValue):
        self.__root = self.__insertHelp(self.__root, insertKey, insertValue)

    def __insertHelp(self, node, insertKey, insertValue):
        if node is None:
            return _Node(insertKey, insertValue)

        if insertKey < node.key:
            node.left = self.__insertHelp(node.left, insertKey, insertValue)
        elif insertKey > node.key:
            node.right = self.__insertHelp(node.right, insertKey, insertValue)

        return node

    def isEmpty(self):
        return self.__root is None

    def getRoot(self):
        return self.__root

    def search(self, goalKey):
        return self.__searchHelp(self.__root, goalKey)

    def __searchHelp(self, node, goalKey):
        if node is None:
            return None

        if goalKey == node.key:
            return node
        elif goalKey < node.key:
            return self.__searchHelp(node.left, goalKey)
        else:
            return self.__searchHelp(node.right, goalKey)

    def lookup(self, goal):
        node = self.search(goal)

        if node is None:
            raise Exception("Key not in tree.")

        return node.value

    def findSuccessor(self, subtreeRoot):
        return self.__findSuccessorHelp(subtreeRoot)

    def __findSuccessorHelp(self, node):
        if node is None:
            return None

        if node.left is None:
            return node

        return self.__findSuccessorHelp(node.left)

    def delete(self, deleteKey):
        if self.search(deleteKey):
            self.__root = self.__deleteHelp(self.__root, deleteKey)
            return

        raise Exception("Key not in tree.")

    def __deleteHelp(self, node, deleteKey):
        if node is None:
            return None

        if deleteKey < node.key:
            node.left = self.__deleteHelp(node.left, deleteKey)
        elif deleteKey > node.key:
            node.right = self.__deleteHelp(node.right, deleteKey)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left

            successor = self.__findSuccessorHelp(node.right)
            node.key = successor.key
            node.value = successor.value
            node.right = self.__deleteHelp(node.right, successor.key)

        return node

    def traverse(self) -> None:
        self.__traverseHelp(self.__root)

    def __traverseHelp(self, node) -> None:
        if node is None:
            return

        self.__traverseHelp(node.left)
        print(node)
        self.__traverseHelp(node.right)

    def __str__(self) -> str:
        return self.__strHelp("", self.__root)

    def __strHelp(self, return_string, node) -> str:
        if node is None:
            return "None"

        return "{{{}, {}, {}}}".format(
            node,
            self.__strHelp(return_string, node.left),
            self.__strHelp(return_string, node.right)
        )


class _Node:
    """A node in a binary search tree."""

    def __init__(self, key, value, left=None, right=None):
        self.key = key
        self.value = value
        self.left = left
        self.right = right

    def __str__(self):
        return "({}, {})".format(self.key, self.value)


if __name__ == "__main__":
    pass