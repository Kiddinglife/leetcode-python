# -*- coding: utf-8 -*-

import bisect
import sys
import copy
sys.setrecursionlimit(10**5)


'''
https://leetcode.com/problems/cheapest-flights-within-k-stops/
'''


def findCheapestPrice_v1(n, flights, src, dst, K):
    """
    for the dp formular that need to compare itself usually use itreative dp
    in the current iterat of recusion, we cannot get the value of ourself.
    so recusion is not possible for the formula that needs to compare with itself.
    initial state:
        each element in dp[dest][k] has a value of INT32_MAX with dp[SRC][0] = 0.
        setup start point to 0 makes sure the shortest path must start with SRC
        because other connected or unconnected paths' initial length is INT32_MAX.
    dp[dest][k] =
        min {dp[dest][k] , dp[src][k-1] + costs[src][dest]) if k > 0
        min {dp[dest][k] , dp[src][k] + costs[src][dest]) if k == 0
    """
    K += 1
    dp = [[sys.maxsize] * n for i in range(K)]
    # this makes sure the shortest path must start with src as other paths have maxsize initial length
    dp[0][src] = 0
    for (s, d, w) in flights:
        dp[0][d] = min(dp[0][d], dp[0][s] + w)
    for i in range(1, K):
        for (s, d, w) in flights:
            v = dp[i-1][s] + w
            dp[i][d] = min(dp[i][d], v)
    v = dp[K-1][dst]
    if sys.maxsize == v:
        return -1
    return v


def findCheapestPrice_v0(n, flights, src, dst, K):
    """
    I refered to this solution to have my own solution v1
    """
    INF = float('inf')
    mn = [INF]*n
    mn[src] = 0
    for k in range(K+1):
        newmn = mn[:]
        for (a, b, cost) in flights:
            v = mn[a]+cost
            vv = newmn[b]
            newmn[b] = min(vv, v)
        mn = newmn
        print(mn)
    return mn[dst] if mn[dst] != INF else -1


if __name__ == '__main__':
    n = 4
    flights = [[0, 1, 100], [2, 1, 50], [1, 3, 50]]
    src = 0
    dst = 3
    k = 1
    ret = findCheapestPrice_v1(n, flights, src, dst, k)
    assert(ret == 150)

    n = 3
    flights = [[0, 1, 100], [1, 2, 100], [0, 2, 500]]
    src = 0
    dst = 2
    k = 0
    ret = findCheapestPrice_v1(n, flights, src, dst, k)
    assert(ret == 500)
