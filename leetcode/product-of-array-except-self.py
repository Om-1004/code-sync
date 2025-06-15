class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        leftArr = [1] * len(nums)
        rightArr = [1] * len(nums)
        ans = [1] * len(nums)

        holderL = 1
        holderR = 1
        for i in range(len(nums)-1):
            leftArr[i+1] = holderL * nums[i]
            holderL *= nums[i]

            rightArr[len(nums) - i - 2] = nums[len(nums) - i - 1] * holderR
            holderR *= nums[len(nums) - i - 1]


    
        for x in range(len(ans)):
            ans[x] = rightArr[x] * leftArr[x]
        return ans