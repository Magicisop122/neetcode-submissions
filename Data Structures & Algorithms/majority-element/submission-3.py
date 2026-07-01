class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        ele = 0
        cnt = 0

        for n in nums:
            if cnt == 0:
                ele = n
                cnt = 1

            elif n == ele:
                cnt += 1

            else:
                cnt -= 1

        return ele 
        
        