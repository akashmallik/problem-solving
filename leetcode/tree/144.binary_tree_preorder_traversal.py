# https://leetcode.com/problems/binary-tree-preorder-traversal/description/
from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        preorder_list = []

        self.preorder(preorder_list, root)

        return preorder_list

    def preorder(self,
                 preorder_list: List[int],
                 root: Optional[TreeNode]) -> Optional[int]:
        if root is None:
            return None

        preorder_list.append(root.val)
        self.preorder(preorder_list, root.left)
        self.preorder(preorder_list, root.right)
