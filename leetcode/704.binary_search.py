# https://leetcode.com/problems/binary-search/
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                left = mid + 1
            else:
                right = mid - 1

        return -1


if __name__ == "__main__":
    solution = Solution()
    assert solution.search(nums=[-1, 0, 3, 5, 9, 12], target=-2) == -1
    assert solution.search(nums=[-1, 0, 3, 5, 9, 12], target=12) == 5
    assert solution.search(nums=[-1, 0, 3, 5, 9, 12], target=9) == 4
    assert solution.search(nums=[-1, 0, 3, 5, 9, 12], target=5) == 3
    assert solution.search(nums=[-1, 0, 3, 5, 9, 12], target=3) == 2
    assert solution.search(nums=[-1, 0, 3, 5, 9, 12], target=0) == 1
    assert solution.search(nums=[-1, 0, 3, 5, 9, 12], target=-1) == 0
    assert solution.search(nums=[-1, 0, 3, 5, 9, 12], target=13) == -1
