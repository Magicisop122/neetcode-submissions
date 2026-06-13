class Solution:
    def findMin(self, nums: List[int]) -> int:

        res = float('inf')

        l, r = 0, len(nums) -1

        while l <= r:
            mid = l + (r - l) // 2

            if nums[mid] >= nums[l]:
                # that means mid is in left sorted half
                # so the nums[l] is the minimum
                res = min(res, nums[l])
                l = mid + 1

            else:
                res = min(res, nums[mid])
                r = mid - 1

        return res