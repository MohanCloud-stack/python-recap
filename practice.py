from typing import List


def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
    for i in range(0, len(nums)):
        for j in range(0, len(nums)):
            if (nums[i] == nums[j]):
                if (abs(i - j) <= k):
                    break
                    return True
                else:
                    break
                    return False


print(containsNearbyDuplicate([1, 2, 3, 1], 3))
