# -*- coding: utf-8 -*-

import bisect
import sys
import copy
sys.setrecursionlimit(10**5)

'''
https://leetcode.com/problems/can-i-win/
'''


def canIWin(maxChoosableInteger, desiredTotal):
    """
    """
    if desiredTotal <= maxChoosableInteger:
        return True

    arr = []
    s = 0

    for n in range(1, maxChoosableInteger+1):
        s += n
        arr.append(n)
    print(arr, desiredTotal)

    if s < desiredTotal:
        return False

    elif s == desiredTotal:
        if maxChoosableInteger % 2:
            return True
        else:
            return False

    dp = {}

    def f(arr, dt):

        k = (tuple(arr), dt)
        cache = dp.get(k)
        if cache:
            print('cached', k, cache)
            return cache

        n = len(arr)
        if n == 1:
            #print('chaching last', k, True)
            dp[k] = (arr[0] >= dt)
            return dp[k]

        # pos = bisect.bisect_left(arr, dt)
        # if pos < len(arr):
        #     # find element >= dt
        #     return True

        # no element >= dt and so recursion
        for i in range(n):
            arrcpy = arr[:i] + arr[i+1:]
            print('pick', arr[i], arrcpy, dt - arr[i])
            win = f(arrcpy, dt - arr[i])
            print(not win)
            if not win:
                #print('chaching', k, True)
                dp[k] = True
                print(k, True)
                return True
        print(k, False)
        dp[k] = False
        return False

    f(arr, desiredTotal)
    k = (tuple(arr), desiredTotal)
    print('final', arr, desiredTotal, dp, dp[k])
    return dp[k]


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
    assert(ret == False)

    maxChoosableInteger = 4
    desiredTotal = 6
    ret = canIWin(maxChoosableInteger, desiredTotal)
    assert(ret == True)
