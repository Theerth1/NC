class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zero_indices = []
        aggregate = 1
        fList = []

        for i in range(len(nums)):
            if nums[i] == 0:
                zero_indices.append(i)
                continue
            aggregate *= nums[i]
        
        if len(zero_indices) >= 2:
            return [0] * len(nums)
        elif len(zero_indices) == 1:
            fList = [0] * len(nums)
            fList[zero_indices[0]] = aggregate
            return fList
        else:
            for i in range(len(nums)):
                fList.append(aggregate//nums[i])
            return fList

            
        

        

        