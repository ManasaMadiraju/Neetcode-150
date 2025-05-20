class Solution():
    def two_sum(self, nums, target):
        hashmap = {}

        for i,n in enumerate(nums):
            diff = target - n
            if diff in hashmap:
                return [hashmap[diff], i]
            hashmap[n] = i
            

if __name__ == '__main__':
    nums = [3,6,2,1,5]
    target = 3
    print(Solution().two_sum(nums,target))