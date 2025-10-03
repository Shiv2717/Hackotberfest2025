	class Solution:

	    def canJump(self, nums: List[int]) -> bool:

		      # Recursive Solution

		      # Time: O(Max(nums) ^ n)

		      # Space: O(n)

	        n = len(nums)

	        

	        def can_reach(i):

	            if i == n-1:

	                return True

	            

	            for jump in range(1, nums[i]+1):

	                if can_reach(i+jump):

	                    return True

	            

	            return False

	        

	        return can_reach(0)
