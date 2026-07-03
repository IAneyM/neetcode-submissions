class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        expected = n * (n + 1) // 2
        actual = sum(nums)
        output = 0
    
        if actual != expected:
            output = expected - actual

        return output