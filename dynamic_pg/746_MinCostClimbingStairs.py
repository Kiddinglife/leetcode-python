# -*- coding: utf-8 -*-

import bisect
import sys
import copy
sys.setrecursionlimit(10**5)


'''
https://leetcode.com/problems/min-cost-climbing-stairs/
'''


def minCostClimbingStairs(cost):
    """
    dp[n] = 
        min { dp[n-1] + cost[n-1], dp[n-2]+cost[n-2] } if n > 1
        0 if n == 1
    """
    n = len(cost)
    c1 = c2 = c = 0
    for i in range(2, n):
        c = min(c1+cost[i-1], c2+cost[i-2])
        c2 = c1
        c1 = c
    retur c
    

if __name__ == '__main__':
    cost =  [0,0,1,1]
    ret = minCostClimbingStairs(cost)
    assert(ret == 0)

    cost =  [0,1,1,1]
    ret = minCostClimbingStairs(cost)
    assert(ret == 1)

    cost =  [0,0,0,1]
    ret = minCostClimbingStairs(cost)
    assert(ret == 0)


    



