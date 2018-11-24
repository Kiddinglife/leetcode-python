# -*- coding: utf-8 -*-

import bisect
import sys
import copy
sys.setrecursionlimit(10**5)


'''
https://leetcode.com/problems/cheapest-flights-within-k-stops/
'''


def findCheapestPrice(n, flights, src, dst, K):
    """
    caution:    up tp K stops
    for the dp formular that need to compare itself usually use itreative dp
    in the current iterat of recusion, we cannot get the value of ourself.
    so recusion is not possible for the formula that needs to compare with itself.
    initial state:
        each element in dp[dest][k] has a value of INT32_MAX with dp[SRC][0] = 0.
        setup start point to 0 makes sure the shortest path must start with SRC
        because other connected or unconnected paths' initial length is INT32_MAX.
    dp[k][dest] = min {dp[k][dest] , dp[k-1][src] + costs[src][dest]) 
    """
    dp = [1e7 for _ in range(n)]
    # this makes sure the shortest path must start with src 
    # as other paths have maxsize initial length
    dp[src] = 0
    for _ in range(K+1):
        predp = dp[:]
        for (s, d, w) in flights:
            v = predp[s] + w
            dp[d] = min(dp[d], v)
    v = dp[dst]
    return -1 if 1e7 == v else v

def findCheapestPrice_v2(n, flights, src, dst, K):
    """
    exactly K stops
    """
    #@TODO
    pass


if __name__ == '__main__':
    n = 4
    flights = [[0, 1, 100], [2, 1, 50], [1, 3, 50]]
    src = 0
    dst = 3
    k = 1
    ret = findCheapestPrice(n, flights, src, dst, k)
    assert(ret == 150)

    n = 3
    flights = [[0, 1, 100], [1, 2, 100], [0, 2, 50]]
    src = 0
    dst = 2
    k = 1
    ret = findCheapestPrice(n, flights, src, dst, k)
    assert(ret == 50)

    n = 3
    flights = [[0,1,100],[1,2,100],[0,2,500]]
    src = 0
    dst = 2
    k = 0
    ret = findCheapestPrice(n, flights, src, dst, k)
    assert(ret == 500)


    n = 4
    flights = [[0,1,1],[0,2,5],[1,2,1],[2,3,1]]
    src = 0
    dst = 3
    k = 1
    ret = findCheapestPrice(n, flights, src, dst, k)
    assert(ret == 6)



