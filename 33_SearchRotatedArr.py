from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            # print("left: "+str(left)+", right: "+str(right))
            mid = left + (right - left)//2
            # print("mid: "+str(mid))
            if nums[mid] == target:
                return mid
            if nums[mid] < nums[right]:
                if nums[mid] < target and nums[right] >= target:
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                if nums[left]<=target and nums[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1

        return -1

x = Solution()
data1 = [4,5,6,7,0,1,2]
print(x.search(data1, 0))
print(x.search(data1, 4))
print(x.search([], 0))