class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        results = []
        seenPivots = set()
        for i in range(len(nums)):
            pivot = nums[i]
            if pivot in seenPivots:
                continue
            else:
                seenPivots.add(pivot)
            l = i + 1
            r = len(nums) - 1
            if pivot > 0:
                break
            while l < r:
                if nums[l] + nums[r] == -1 * pivot:
                    results.append((nums[i], nums[l], nums[r]))
                    l += 1
                    r -= 1
                elif nums[l] + nums[r] > -1 * pivot:
                    r -= 1
                else:
                    l += 1
        return [list(x) for x in set(results)]



            
        