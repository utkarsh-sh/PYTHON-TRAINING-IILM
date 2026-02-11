class Solution(object):
    def majorityElement(self, nums):
        dic = {}

        for i in nums:
            if i in dic:
                dic[i]+=1
            else:
                dic[i]=1

        ans = 0
        for key in dic:
            if dic[key] >= len(nums)//2:
                return key
nums = [3, 2, 3]
# nums = [2, 2, 1, 1, 1, 2, 2]
obj = Solution()
s = obj.majorityElement(nums)
print(s)