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
    for the question that has one by one input ysyaly use interative dp
    for the dp formular that need to compare itself usually use itreative dp
    dp[dest][k] = 
        min {dp[dest][k] , dp[src][k-1] + costs[src][dest]) if k > 0
        min { costs[...src][dest] }
    """
    K += 1
    dp = [[sys.maxsize ]  * n for i in range(K)]
    for (s,d,w) in flights:
        dp[0][d] = min(dp[0][d], w)
    print(dp)
    for i in range(1, K):
        for (s,d,w) in flights:
            v = dp[i-1][s] + w
            dp[i][d]= min(dp[i][d], v)
    v =   dp[K-1][dst] 
    if sys.maxsize ==  v:
        return -1
    return v


if __name__ == '__main__':
    n = 3
    flights = [[0,1,100],[1,2,100],[0,2,500]]
    src = 0
    dst = 2
    k = 0
    ret = findCheapestPrice(n, flights, src, dst, k);
    print(ret)
