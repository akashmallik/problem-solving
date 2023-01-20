from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return self.prettyPrintTree()

    def prettyPrintTree(self, prefix="", isLeft=True):
        # if not self:
        #     print("Empty Tree")
        #     return

        if self.right:
            self.prettyPrintTree(self.right, prefix + ("│   " if isLeft else "    "), False)

        print(prefix + ("└── " if isLeft else "┌── ") + str(self.val))

        if self.left:
            self.prettyPrintTree(self.left, prefix + ("    " if isLeft else "│   "), True)


def tree(values: list, root_index: int) -> Optional[TreeNode]:
    if not values or root_index >= len(values):
        return None

    root = TreeNode(values[root_index])

    left_index = root_index + 1
    if left_index < len(values) and values[left_index]:
        root.left = tree(values, left_index)

    right_index = root_index + 2
    if right_index < len(values) and values[right_index]:
        root.right = tree(values, right_index)

    return root


def fromlist(values):
    def create(it):
        value = next(it)
        return None if value is None else TreeNode(value)

    if not values:
        return None
    it = iter(values)
    root = TreeNode(next(it))
    nextlevel = [root]
    try:
        while nextlevel:
            level = nextlevel
            nextlevel = []
            for node in level:
                if node:
                    node.left = create(it)
                    node.right = create(it)
                    nextlevel += [node.left, node.right]

    except StopIteration:
        return root
    raise ValueError("Invalid list")


def stringToTreeNode(input):
    input = input[1:-1]
    if not input:
        return None

    inputValues = [s.strip() for s in input.split(',')]
    root = TreeNode(int(inputValues[0]))
    nodeQueue = [root]
    front = 0
    index = 1
    while index < len(inputValues):
        node = nodeQueue[front]
        front = front + 1

        item = inputValues[index]
        index = index + 1
        if item != "null":
            leftNumber = int(item)
            node.left = TreeNode(leftNumber)
            nodeQueue.append(node.left)

        if index >= len(inputValues):
            break

        item = inputValues[index]
        index = index + 1
        if item != "null":
            rightNumber = int(item)
            node.right = TreeNode(rightNumber)
            nodeQueue.append(node.right)
    return root

if __name__ == "__main__":
    # _root = [1, None, 2, 3]
    _root = [1, 2, 2, 3, 4, 4, 3]
    t = fromlist(_root)
    print(t)
