from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


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


if __name__ == "__main__":
    _root = [1, None, 2, 3]
    t = tree(_root, 0)
    print(t)
