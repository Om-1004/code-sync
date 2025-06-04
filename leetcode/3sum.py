class Solution:
    def threeSum(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        l = 0
        r = len(arr) - 1
        triplets = set()

        while l < r:
            mover = l + 1
            while mover < r:
                if arr[l] + arr[mover] + arr[r] == 0:
                    arrayToAdd = [arr[l], arr[mover], arr[r]]
                    triplets.add(tuple(arrayToAdd))
                    mover += 1
                elif arr[l] + arr[mover] + arr[r] > 0:
                    r -= 1
                else:
                    mover += 1
            r = len(arr) - 1
            l += 1
      
        list_of_list = [list(item) for item in triplets]
        return list_of_list