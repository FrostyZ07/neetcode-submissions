class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        hash={}
        for n in nums:
            hash[n]=0
        if len(hash)!= len(nums):
            return True
        return False
        