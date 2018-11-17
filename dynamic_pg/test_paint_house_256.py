# -*- coding: utf-8 -*-

import unittest
import sys
import copy


class paint_house_256:
    '''
    cd dynamic_pg
    nosetests test_paint_house_256:test_paint_house_256.test_0 -s
    https://leetcode.com/problems/paint-house/description/
    think of steps:
    currmins[col] = costs[row][col] + min(premins[idxl], premins[idxr]) 
    mincost = min(currmins)
    '''

    def min_cost_v1(self, costs):
        '''
        created by myself but  only beats 37%
        reason is the copy of mins and tempmins
        '''
        if not len(costs):
            return 0
        mins = [costs[0][0], costs[0][1], costs[0][2]]
        tempmins = [0]*3
        mincost = min(mins)
        for row in range(1, len(costs)):
            for col in range(3):
                print(costs[row][col])
                idxl = (col + 1) % 3
                idxr = (idxl+1) % 3
                smaller = min(mins[idxl],  mins[idxr])
                print(smaller)
                tempmins[col] = costs[row][col] + smaller
                print(tempmins[col])
            mincost = min(tempmins)
            # ucan only pdate mins after each row
            for i in range(3):
                mins[i] = tempmins[i]
        return mincost

    def min_cost_v2(self, costs):
        '''
        created by  valeriy2
        https://leetcode.com/problems/paint-house/discuss/162876/Simple-Python-beats-100
        faster because removal of copy of mins
        '''
        if not costs:
            return 0
        for index in range(1, len(costs)):
            costs[index][0] += min(costs[index-1][1], costs[index-1][2])
            costs[index][1] += min(costs[index-1][0], costs[index-1][2])
            costs[index][2] += min(costs[index-1][0], costs[index-1][1])
        return min(costs[-1])


class test_paint_house_256(unittest.TestCase):
    def setUp(self):
        self.inst = paint_house_256()

    def test_0(self):
        '''
        Given: [[17,2,17],[16,16,5]]
        Ouput: 2 + 5  = 7.
        '''
        #costs = [[17, 2, 17], [16, 16, 5], [14, 3, 19]]
        costs = [[17, 2, 17], [16, 16, 5]]
        ret = self.inst.min_cost_v1(costs)
        assert(ret == 7)

    def test_1(self):
        '''
        Given:  [[17, 2, 17], [16, 16, 5], [14, 3, 19]]
        Ouput: 2 + 5 + 3 = 10
        '''
        costs = [[17, 2, 17], [16, 16, 5], [14, 3, 19]]
        ret = self.inst.min_cost_v1(costs)
        assert(ret == 10)

    def test_2(self):
        '''
        Given:  []
        Ouput: 0
        '''
        costs = []
        ret = self.inst.min_cost_v1(costs)
        assert(ret == 0)

    def test_3(self):
        '''
        Given:  [[7,6,2]]
        Ouput: 0
        '''
        costs = [[7, 6, 2]]
        ret = self.inst.min_cost_v1(costs)
        assert(ret == 2)

    def test_4(self):
        '''
        Given:  [[3,5,3],[6,17,6],[7,13,18],[9,10,18]]
        Ouput: 26
        '''
        costs = [[3, 5, 3], [6, 17, 6], [7, 13, 18], [9, 10, 18]]
        ret = self.inst.min_cost_v1(costs)
        assert(ret == 26)
