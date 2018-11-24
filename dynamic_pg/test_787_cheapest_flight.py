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
    '''
    10%  beats
    dp = [[sys.maxsize]*n]*(K+1)
    # this makes sure the shortest path must start with src 
    # as other paths have maxsize initial length
    dp[0][src] = 0
    for i in range(K+1):
        predp = dp[i][:]
        for (s, d, w) in flights:
            v = predp[s] + w
            dp[i][d] = min(dp[i][d], v)
    v = dp[K][dst]
    return -1 if sys.maxsize == v else v
    '''
    dp = [sys.maxsize]*n
    # this makes sure the shortest path must start with src 
    # as other paths have maxsize initial length
    dp[src] = 0
    for i in range(K+1):
        predp = dp[:]
        for (s, d, w) in flights:
            
            v = predp[s] + w
            dp[d] = min(dp[d], v)
    v = dp[dst]
    return -1 if sys.maxsize == v else v

def findCheapestPrice_v2(n, flights, src, dst, K):
    """
    exactly K stops
    
    """
    dp = [sys.maxsize]*n
    # this makes sure the shortest path must start with src 
    # as other paths have maxsize initial length
    dp[src] = 0
    for i in range(K+1):
        predp = dp[:]
        for (s, d, w) in flights:
            v = predp[s] + w
            dp[d] = min(dp[d], v)
    v = dp[dst]
    return -1 if sys.maxsize == v else v

def findCheapestPrice_v0(n, flights, src, dst, K):
    """
    I refered to this solution to have my own solution v1
    """
    mn = [sys.maxsize]*n
    mn[src] = 0
    for k in range(K+1):
        newmn = mn[:]
        for (a, b, cost) in flights:
            v = mn[a]+cost
            vv = newmn[b]
            newmn[b] = min(vv, v)
        mn = newmn
        print(mn)
    return mn[dst] if mn[dst] != sys.maxsize else -1


def findCheapestPrice_Bellman_Ford(n, flights, src, dst, K):
    graph = {i: set() for i in range(n+1)}
    for s, d, p in flights:
        graph[d].add((s, p))
    k = K + 1
    price = 1e7
    dp = [[1e7 for _ in range(n+1)] for _ in range(k+1)]
    for i in range(n+1):
        if i == src:
            dp[0][i] = 0
        else:
            dp[0][i] = 1e7
    for i in range(1, k+1):
        for j in range(n+1):
            for s, p in graph[j]:
                dp[i][j] = min(dp[i][j], dp[i-1][s] + p)
                if j == dst:
                    price = min(price, dp[i][j])
    return price if price < 1e7 else -1


if __name__ == '__main__':
    n = 4
    flights = [[0, 1, 100], [2, 1, 50], [1, 3, 50]]
    src = 0
    dst = 3
    k = 1
    ret = findCheapestPrice_v1(n, flights, src, dst, k)
    assert(ret == 150)

    n = 3
    flights = [[0, 1, 100], [1, 2, 100], [0, 2, 50]]
    src = 0
    dst = 2
    k = 1
    ret = findCheapestPrice_v1(n, flights, src, dst, k)
    assert(ret == 50)

    n = 3
    flights = [[0,1,100],[1,2,100],[0,2,500]]
    src = 0
    dst = 2
    k = 0
    ret = findCheapestPrice_v0(n, flights, src, dst, k)
    assert(ret == 500)


    # n = 3
    # flights = [[0, 1, 100], [1, 2, 100], [0, 2, 50]]
    # src = 0
    # dst = 2
    # k = 1
    # ret = findCheapestPrice_Bellman_Ford(n, flights, src, dst, k)
    # print(ret)


