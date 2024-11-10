class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        output = []

        differences = []
        for i, num in enumerate(nums):
            differences.append(target - num)

            if target - num in nums:
                j = nums.index(target - num)

                if i == j:
                    continue

                output.append(i)
                output.append(j)

                break
        
        print(differences)

        return output