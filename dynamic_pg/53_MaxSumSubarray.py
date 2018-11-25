# -*- coding: utf-8 -*-

import bisect
import sys
import copy
sys.setrecursionlimit(10**5)

'''
https://leetcode.com/problems/maximum-subarray/
'''


def maxSubArray(nums):
    """
    initial states:
        dp = []*len(nums)
        dp[0] = maxsum = nums[0]
    formula:
        dp[n] =
            max { dp[n-1] + nums[i], nums[i] }
            nums[0] if n == 0
        maxsum =
            max{maxsum, dp[n]} if n > 0
            nums[0] if n == 0

    """
    # l = len(nums)
    # if not l:
    #     return 0
    # dp = [-sys.maxsize-1]*l
    # dp[0] = maxsum = nums[0]
    # print(maxsum)
    # for n in range(1, l):
    #     dp[n] = max(dp[n-1] + nums[n], nums[n])
    #     print(maxsum)
    #     maxsum = max(maxsum, dp[n])
    # return maxsum
    # fater vwrsion 44ms beats 98%
    l = len(nums)
    if not l:
        return 0
    pre = curr = maxsum = nums[0]
    for n in range(1, l):
        if pre > 0:
            curr = pre + nums[n]
        else:
            curr = nums[n]
        pre = curr
        maxsum = max(maxsum, curr)
    return maxsum


if __name__ == '__main__':
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    ret = maxSubArray(nums)
    assert(ret == 6)
