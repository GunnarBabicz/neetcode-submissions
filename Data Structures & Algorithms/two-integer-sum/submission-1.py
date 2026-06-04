class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}

        for i, j in enumerate(nums):
            difference = target - j
            if difference in hashMap:
                return [hashMap[difference], i]
            else:
                hashMap[j] = i
        return
            