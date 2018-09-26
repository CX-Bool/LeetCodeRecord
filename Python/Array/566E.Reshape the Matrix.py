# Accepted
class Solution:
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        flatten = [x for raw in nums for x in raw]
        # flatten = []
        # for raw in nums:
        #     for x in raw:
        #         flatten.append(x)
        if r*c != len(flatten):
            return nums
        else:
            return [flatten[i*c:i*c+c] for i in range(r)]

if __name__ == '__main__':
    nums = [[1,2],[3,4]]
    s = Solution()
    s.matrixReshape(nums,1,4)