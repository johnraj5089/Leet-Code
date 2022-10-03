class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        ans = [-1,-1]
        def search(self, nums: List[int], target: int) -> int:
            an = -1
            low = 0
            high = len(nums)-1
            while (low <= high):
                mid = (low + high) // 2
                if nums[mid] == target :
                    an = mid
                    if ans[0] == -1 :
                        high = mid -1
                    else:
                        low = mid +1
                elif nums [mid] > target:
                    high = mid -1
                else:
                    low = mid +1
           return an
      ans [0] = search (self,nums,target) 
      if ans [0] != -1:
          ans [1] = search (self, nums,target)
      return ans

