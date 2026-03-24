## Leetcode question link
## https://leetcode.com/problems/search-insert-position/

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        output = 0
        while left <= right:
            mid = (left + right) // 2 
            if nums[mid] == target:
                output = mid
                break
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
            output = left
        return output