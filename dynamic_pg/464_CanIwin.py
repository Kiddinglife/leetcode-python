# -*- coding: utf-8 -*-

import bisect
import sys
import copy
sys.setrecursionlimit(10**5)

'''
https://leetcode.com/problems/can-i-win/
'''


def canIWin(self, maxChoosableInteger, desiredTotal):
    """
    1 2 3 4 5   8
    must choose from (1,2) because choose from (3,4,5) must lose
    f(arr, dt) = 
    return first lose and second win if arr[0]+arr[-1] >= dt
    return !if arr[0]+arr[-1] > dt
    """
    if desiredTotal <= maxChoosableInteger:
        return True

    arr = [n for n in range(1, maxChoosableInteger+1)]
    print(sum(arr))
    if sum(arr) < desiredTotal:
        return False
    elif sum(arr) == desiredTotal:
        if maxChoosableInteger % 2:
            return True
        else:
            return False

    def f(arr, dt):
        for i in range(maxChoosableInteger):
            if arr[i] + arr[-1] >= dt:
                if i == 0:
                    return True
                for j in range(1, i):
                    arrr = arr[:(n-i)]
                    dtt = dt - arr[j]
                    return !f(arrr, dtt)
            else:
                for x in range(n):
                    dtt = dt - arr[x]
                    arrr = arr[:]
                    arrr.pop(x)
                    return !f(arrr, dtt)

    return f(arr, desiredTotal)


if __name__ == '__main__':
    pass
