class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:

        if len(nums) == 0:
            return []
        if len(nums) == 1:
            return [str(nums[0])]
        
        l = 0
        r = 1
        runner = nums[0]
        res = []
        

        while r < len(nums):
            if nums[r] - runner == 1:
                runner = nums[r]
            else:
                if runner == nums[l]:
                    res.append(str(nums[l])) 
                else:
                    elem = str(nums[l]) + "->" + str(runner)
                    res.append(elem)
                l = r
                runner = nums[l]

            r += 1
        
        if r - 1 == l:
            res.append(str(nums[l]))
        else:
            elem = str(nums[l]) + "->" + str(nums[-1])
            res.append(elem)
        
        return res