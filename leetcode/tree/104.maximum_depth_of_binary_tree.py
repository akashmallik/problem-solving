# https://leetcode.com/problems/maximum-depth-of-binary-tree/
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.top_down(root, 0)

    def top_down(self, root: Optional[TreeNode], depth):
        if root is None:
            return depth

        left_depth = self.top_down(root.left, depth + 1)
        right_depth = self.top_down(root.right, depth + 1)

        return max(left_depth, right_depth)
