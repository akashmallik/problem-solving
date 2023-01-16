# https://leetcode.com/problems/binary-tree-inorder-traversal/description/
from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        inorder_list = []
        self.inorder(root, inorder_list)

        return inorder_list

    def inorder(self,
                root: Optional[TreeNode],
                inorder_list: List[int]):
        if root is None:
            return None

        self.inorder(root.left, inorder_list)
        inorder_list.append(root.val)
        self.inorder(root.right, inorder_list)
