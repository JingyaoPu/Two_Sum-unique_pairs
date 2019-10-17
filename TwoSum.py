class Solution:
    def find(self,nums,target):
        nums.sort()
        l = 0; r = len(nums)-1; res = 0
        while l<r:
            if nums[l]+nums[r] > target:
                r -= 1
            elif nums[l]+nums[r] < target:
                l += 1
            else:
                res += 1
                vr = nums[r]; vl = nums[l]
                while l<r and (nums[r] == vr or nums[l] == vl):
                    r -= 1
                    l += 1
        return res
nums = [1, 1]
target = 2
sol = Solution()
print(sol.find(nums,target))