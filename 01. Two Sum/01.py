class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        output = []

        for i, first_num in enumerate(nums):
            j = i + 1
            for second_num in nums[i + 1:]:
                if first_num + second_num == target:
                    output.append(i)
                    output.append(j)

                j += 1

        return output