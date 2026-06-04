class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        # hash set: while this is O(n), 
        # the memory complexity needed to create this 
        # solution is also O(n).

        # For optimization of memory complexity,
        # one could sort the list and then iterate through
        # to see if any of the values next to each other are equal. (sliding window)
        # This would be O(1) memory complexity or O(n log n) for the time complexity. 
        

        hashset = set()


        for i in nums:

            if i in hashset:
                return True
            hashset.add(i)
        return False
            
         