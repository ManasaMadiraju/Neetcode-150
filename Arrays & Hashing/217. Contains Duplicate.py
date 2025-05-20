class Solution:
    def contains_duplicate(self, nums):
        hashset = set()

        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False
    

if __name__ == '__main__':
    nums = [2,3,4,3,1,6]
    print(Solution().contains_duplicate(nums))
   
   

