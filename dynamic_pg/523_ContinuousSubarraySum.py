# -*- coding: utf-8 -*-

import bisect
import sys
import copy
sys.setrecursionlimit(10**5)

'''
Example 1:
Input: [23, 2, 4, 6, 7],  k=6
Output: True
Explanation: Because [2, 4] is a continuous subarray of size 2 and sums up to 6.

Example 2:
Input: [23, 2, 6, 4, 7],  k=6
Output: True
Explanation: Because [23, 2, 6, 4, 7] is an continuous subarray of size 5 and sums up to 42.
'''


def checkSubarraySum(nums, k):
    """
    """
    n = len(nums)
    if n < 2:
        return False

    if k == 0:
        for i in range(1, n):
            if nums[i] == 0 and nums[i-1] == nums[i]:
                return True
        return False

    s = nums[0] + nums[1]
    if not (s % k):
        return True

    dp = {(nums[0] % k): set([0]), (s % k): set([1])}
    for i in range(2, n):
        s += nums[i]
        r = s % k
        if not r:
            return True
        elif r in dp:
            if i -1 ==  dp[r][-1] and len(dp[r]) == 1:
                return False
            return True
        else:
            dp[r] = {i}

    return False


if __name__ == '__main__':
    nums = [23, 2, 3, 6, 7]
    k = 6
    ret = checkSubarraySum(nums, k)
    assert(ret == False)

    nums = [23, 2, 4, 6, 7]
    k = 6
    ret = checkSubarraySum(nums, k)
    assert(ret == True)

    nums = [23, 2, 4, 6, 7]
    k = 0
    ret = checkSubarraySum(nums, k)
    assert(ret == False)

    nums = [0, 0]
    k = 0
    ret = checkSubarraySum(nums, k)
    assert(ret == True)
