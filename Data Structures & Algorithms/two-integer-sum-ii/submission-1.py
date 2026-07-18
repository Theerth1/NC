class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1

        leftNum = numbers[l]
        rightNum = numbers[r]
        
        if (leftNum + rightNum) == target:
            return [l + 1, r + 1]
        elif (leftNum + rightNum) < target:
            l += 1
        elif (leftNum + rightNum) > target:
            r -= 1
        
        while True:
            leftNum = numbers[l]
            rightNum = numbers[r]
            if (leftNum + rightNum) == target:
                return [l + 1, r + 1]
            elif (leftNum + rightNum) < target:
                l += 1
            elif (leftNum + rightNum) > target:
                r -= 1
        