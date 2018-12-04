# -*- coding: utf-8 -*-

import bisect
import sys
import copy
sys.setrecursionlimit(10**5)

'''
https://leetcode.com/problems/can-i-win/
'''


def canIWin(maxChoosableInteger, desiredTotal):
    if desiredTotal <= maxChoosableInteger:
        return True

    arr = []
    s = 0

    for n in range(1, maxChoosableInteger+1):
        s += n
        arr.append(n)

    if s < desiredTotal:
        return False

    if s == desiredTotal:
        if maxChoosableInteger % 2:
            return True
        else:
            return False

    dp = {}

    def f(arr, dt):
        # if arr[-1] >= dt
        # must use arr[-1] largest one eg arr [2,4] dt 3
        # arr[-1] >= dt gives false but it should be true
        if arr[-1] >= dt:
            return True

        k = tuple(arr)
        cache = dp.get(k)
        if cache:
            return cache

        # no element >= dt and so recursion
        for i in range(len(arr)):
            # print('pick', arr[i], arrcpy, dt - arr[i])
            if not f(arr[:i] + arr[i+1:], dt - arr[i]):
                dp[k] = True
                return True
        dp[k] = False
        return False

    return f(arr, desiredTotal)


# def canIWin(maxChoosableInteger, desiredTotal):
#     def helper(nums, desiredTotal):
#         hash = str(nums)
#         if hash in memo:
#             return memo[hash]

#         if nums[-1] >= desiredTotal:
#             return True

#         for i in range(len(nums)):
#             if not helper(nums[:i] + nums[i+1:], desiredTotal - nums[i]):
#                 memo[hash]= True
#                 return True
#         memo[hash] = False
#         return False

#     if (1 + maxChoosableInteger) * maxChoosableInteger/2 < desiredTotal:
#         return False
#     memo = {}
#     return helper([n for n in range(1, maxChoosableInteger+1)], desiredTotal)

if __name__ == '__main__':
    maxChoosableInteger = 3
    desiredTotal = 5
    ret = canIWin(maxChoosableInteger, desiredTotal)
    assert(ret == True)

    maxChoosableInteger = 10
    desiredTotal = 11
    ret = canIWin(maxChoosableInteger, desiredTotal)
    assert(ret == False)

    maxChoosableInteger = 18
    desiredTotal = 79
    ret = canIWin(maxChoosableInteger, desiredTotal)
    assert(ret == True)

    maxChoosableInteger = 4
    desiredTotal = 6
    ret = canIWin(maxChoosableInteger, desiredTotal)
    assert(ret == True)
