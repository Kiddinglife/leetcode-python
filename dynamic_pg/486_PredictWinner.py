# -*- coding: utf-8 -*-

import collections
import bisect
import sys
import copy
sys.setrecursionlimit(10**5)

'''
https://leetcode.com/problems/predict-the-winner/
'''


def PredictTheWinner(nums):
    n = len(nums)
    if n < 3:
        return True
    sums = [0, 0, ]

    def canwin(start, end, sumidx):
        if end == start:
            sums[sumidx] += nums[start]
            f = sums[0] >= sums[1]
            # print('end', f, sumidx, sums[sumidx] - nums[start],'+', nums[start], '=', sums[sumidx], sums)
            sums[sumidx] -= nums[start]
            return f

        diff1 = max(nums[end], nums[start+1]) - nums[start]
        diff2 = max(nums[end-1],  nums[start]) - nums[end]
        idx = (sumidx + 1) % 2

        if diff1 <= 0 or diff1 <= diff2:
            sums[sumidx] += nums[start]
            ret = canwin(start + 1, end,  idx)
            # print('left ', ret , sumidx,  sums[sumidx] - nums[start] , '+', nums[start], '=',  sums[sumidx])
            sums[sumidx] -= nums[start]
            if (not ret and sumidx == 0) or (ret and sumidx == 1):
                sums[sumidx] += nums[end]
                ret = canwin(start, end - 1,  idx)
                # print('right', ret, sumidx,  sums[sumidx] - nums[end] , '+', nums[end], '=',  sums[sumidx])
                sums[sumidx] -= nums[end]
        elif diff2 <= 0 or diff1 >= diff2:
            sums[sumidx] += nums[end]
            ret = canwin(start, end - 1,  idx)
            # print('right', ret,  sumidx, sums[sumidx] - nums[end], '+', nums[end], '=', sums[sumidx])
            sums[sumidx] -= nums[end]
            if (not ret and sumidx == 0) or (ret and sumidx == 1):
                sums[sumidx] += nums[start]
                ret = canwin(start + 1, end,  idx)
                # print('left ', ret , sumidx,  sums[sumidx] - nums[start], '+', nums[start], '=',  sums[sumidx])
                sums[sumidx] -= nums[start]
        return ret
    ret = canwin(0, n - 1, 0)
    return ret


def PredictTheWinnerCached(nums):
    n = len(nums)
    if n < 3:
        return True
    sums = [0, 0]
    dp = {}

    def canwin(start, end, sumidx):
        print(start, end, sumidx)
        if end == start:
            sums[sumidx] += nums[start]
            f = sums[0] >= sums[1]
            # print('end', f, sumidx, sums[sumidx] - nums[start],'+', nums[start], '=', sums[sumidx], sums)
            sums[sumidx] -= nums[start]
            return f

        cache = dp.get((start, end, sumidx))
        if cache:
            print('use chaches')
            return cache

        diff1 = max(nums[end], nums[start+1]) - nums[start]
        diff2 = max(nums[end-1],  nums[start]) - nums[end]
        idx = (sumidx + 1) % 2

        if diff1 <= 0 or diff1 <= diff2:
            sums[sumidx] += nums[start]
            ret = canwin(start + 1, end,  idx)
            # print('left ', ret , sumidx,  sums[sumidx] - nums[start] , '+', nums[start], '=',  sums[sumidx])
            sums[sumidx] -= nums[start]
            if (not ret and sumidx == 0) or (ret and sumidx == 1):
                sums[sumidx] += nums[end]
                ret = canwin(start, end - 1,  idx)
                # print('right', ret, sumidx,  sums[sumidx] - nums[end] , '+', nums[end], '=',  sums[sumidx])
                sums[sumidx] -= nums[end]
        elif diff2 <= 0 or diff1 >= diff2:
            sums[sumidx] += nums[end]
            ret = canwin(start, end - 1,  idx)
            # print('right', ret,  sumidx, sums[sumidx] - nums[end], '+', nums[end], '=', sums[sumidx])
            sums[sumidx] -= nums[end]
            if (not ret and sumidx == 0) or (ret and sumidx == 1):
                sums[sumidx] += nums[start]
                ret = canwin(start + 1, end,  idx)
                # print('left ', ret , sumidx,  sums[sumidx] - nums[start], '+', nums[start], '=',  sums[sumidx])
                sums[sumidx] -= nums[start]
        dp[(start, end, sumidx)] = ret
        return ret
    ret = canwin(0, n - 1, 0)
    print(dp)
    return ret


if __name__ == '__main__':
    nums = [1, 5, 2]
    ret = PredictTheWinner(nums)
    assert(ret == False)
    print('---')
    nums = [1, 5, 233, 7]
    ret = PredictTheWinner(nums)
    assert(ret == True)
    print('---')
    nums = [1, 2, 3, 4, 5, 6, 7]
    ret = PredictTheWinner(nums)
    assert(ret == True)
    print('---')
    nums = [1, 2, 3, 2, 1]
    ret = PredictTheWinner(nums)
    assert(ret == True)
    print('---')
    nums = [2, 4, 55, 6, 8]
    ret = PredictTheWinner(nums)
    assert(ret == False)
    print('---')
    nums = [0, 0, 7, 6, 5, 6, 1]
    ret = PredictTheWinner(nums)
    assert(ret == False)

    nums = [1, 5, 2]
    ret = PredictTheWinnerCached(nums)
    assert(ret == False)
    print('---')
    nums = [1, 5, 233, 7]
    ret = PredictTheWinnerCached(nums)
    assert(ret == True)
    print('---')
    nums = [1, 2, 3, 4, 5, 6, 7]
    ret = PredictTheWinnerCached(nums)
    assert(ret == True)
    print('---')
    nums = [1, 2, 3, 2, 1]
    ret = PredictTheWinnerCached(nums)
    assert(ret == True)
    print('---')
    nums = [2, 4, 55, 6, 8]
    ret = PredictTheWinnerCached(nums)
    assert(ret == False)
    print('---')
    nums = [0, 0, 7, 6, 5, 6, 1]
    ret = PredictTheWinnerCached(nums)
    assert(ret == False)
