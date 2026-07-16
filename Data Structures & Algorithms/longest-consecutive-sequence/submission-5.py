class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        collection = set(nums)
        empty = set()
        upperBound = len(collection)

        for num in collection:
            if num not in empty:
                empty.add(num)
                continue
            
        # for each num in nums, if it is consecutive then there must be another num that is plu sor minus that if thats tru we cna add oen
        consecutive = 0
        for num in collection:
            if (num + 1) in collection or (num - 1) in collection:
                consecutive += 1
                empty.add(num)
                # [2,20,4,10,3,4,5] -> [2,20,4,10,3,5] -> [2, 4, 3, 5]
                # [0,3,2,5,4,6,1,1] -> [0,3,2,5,4,6,1] -> [0, 3, 2, 5, 4, 6, 1]
    
        if len(collection) == 1:
            return 1
        if empty == collection:
            return consecutive

        
        for i in range(len(empty)):
            target = len(empty)
            smallest = min(empty)
            counter = 0
            while (smallest + 1) in empty:
                counter += 1
                smallest = smallest + 1
            if counter == len(empty):
                return counter
            empty.remove(smallest)
        """
        nums = set(nums)
        if not nums:
            return 0
        if len(nums) == 1:
            return 1
        newSet = set()
        # [2,20,4,10,3,5]
        for num in nums:
            if (num - 1) not in nums:
                newSet.add(num)
        
        globalLongest = 1
        for num in newSet:
            travel = num
            longest = 1
            while (travel + 1) in nums:
                longest += 1
                travel = travel + 1
            if longest > globalLongest:
                globalLongest = longest
        
        return globalLongest


        

        
        

        