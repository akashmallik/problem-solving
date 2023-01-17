# https://leetcode.com/problems/binary-tree-level-order-traversal/description/
from collections import deque
from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        level_order = []

        queue= deque()
        queue.append(root)

        while queue:
            level = []
            for i in range(len(queue)):
                node = queue.popleft()
                if node:
                    queue.append(node.left)
                    queue.append(node.right)
                    level.append(node.val)

            if level:
                level_order.append(level)

        return level_order
