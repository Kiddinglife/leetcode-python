# -*- coding: utf-8 -*-

import sys
import copy

'''
    https://leetcode.com/problems/longest-increasing-subsequence/description/
'''


def lengthOfLIS_v0(nums):
    """
    O(n^2)

    dp[i] =
        max{dp[0,i-1] and a[0,i-1] < a[i]} + 1 if i > 1;
        1 if i = 0;
    maxx = max{dp[i], maxx}
    """
    n = len(nums)
    dp = [1] * n
    maxx = 1
    for i in range(1, n):
        maxv = 0
        for x in range(i):
            if nums[x] < nums[i] and dp[x] > maxv:
                maxv = dp[x]
                print(maxv)
        dp[i] += maxv
        maxx = max(maxx, dp[i])
        print(nums[i], dp[i])
        print(maxx)
        print('\n')
    return maxx


def lengthOfLIS_v1(nums):
    """
    lis(i,j) =
        0                                           if i = 0 or j = 0;
        lis(i-1, j-1) + 1                      if x[i] = y[j];
        max(list[(i, j-1), lis(i-1, j)     if x[i] != y[j]
    """
    if not nums:
        return 0
    
    x = nums
    y = copy.deepcopy(x)
    y.sort()
    a = b = len(x)

    dp = []
    for n in range(a):
        arr = [0]*b
        dp.append(arr)

    def lis(i, j):
        if i < 0 or j < 0:
                return 0

        if not dp[i][j]:
            if x[i] == y[j]:
                v = lis(i - 1, j-1) + 1
                dp[i][j] = v 
            else:
                v1 = lis(i - 1, j)
                v2 = lis(i,  j-1)
                dp[i][j] = max(v1, v2)

        return dp[i][j]

    lis(a-1, b-1)
    v = dp[a-1][b-1]
    # print(dp)
    return v
    # def lis(i, j):
    #     if i == 0 or j ==  0:
    #         return 0
    #     elif x[i] == y[j]:
    #         return lis(i-1, j-1) + 1
    #     else:
    #         return max(lis(i-1, j),  lis(i, j-1))

    # v = lis(i-1, j-1)
    # return v


if __name__ == '__main__':
    nums = [10, 9, 2, 5, 3, 7, 101, 18]
    ret = lengthOfLIS_v0(nums)
    print(ret)
    assert(ret == 4)

    nums = [1, 3, 6, 7, 9, 4, 10, 5, 6]
    ret = lengthOfLIS_v0(nums)
    assert(ret == 6)

    nums = [3, 1, 2]
    ret = lengthOfLIS_v1(nums)
    print(ret)
    assert(ret == 2)

    nums = [2, 2, 2]
    ret = lengthOfLIS_v1(nums) # 3 should be 1due to incre
    assert(ret == 1)
