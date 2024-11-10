class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        output = []

        differences = []
        differences_dict = {}
        for i, num in enumerate(nums):
            difference = target - num

            if num in differences_dict:
                output.append(i)
                output.append(differences_dict[num])
                break

            differences_dict[difference] = i

        return output