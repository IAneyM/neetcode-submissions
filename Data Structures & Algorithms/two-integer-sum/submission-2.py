class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        ans_arr = []

        for i in range(n):
            for j in range(n):
                if i != j:
                    if target == nums[i]+nums[j]:
                        ans_arr.append(i)
                        ans_arr.append(j)
                        return(ans_arr)
