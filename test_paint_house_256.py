import unittest
import sys


class paint_house_256:
    '''
    nosetests paint_house_256:test_paint_house_256.test_4 -s
    https://leetcode.com/problems/paint-house/description/
    '''

    def min_cost(self, costs):
        if not len(costs):
            return 0

        width = 3
        mincosts = [costs[0][0], costs[0][1], costs[0][2]]
        ret = min(mincosts)

        for r, row in enumerate(costs):
            if r == len(costs)-1:
                break
            temp = [sys.maxsize]*3
            mincost = sys.maxsize
            for c, v in enumerate(row):
                print((r, c, v))
                idxl = (c+1) % width
                idxr = (idxl+1) % width

                print(mincosts[c], min(costs[r+1][idxl], costs[r+1][idxr]))
                sum1 = mincosts[c] + min(costs[r+1][idxl], costs[r+1][idxr])
                print(sum1)
                mincost = min(mincost, sum1)
                print(mincost)

                temp[idxl] = min(temp[idxl], v + costs[r+1][idxl])
                temp[idxr] = min(temp[idxr], v + costs[r+1][idxr])

            for i in range(width):
                mincosts[i] = temp[i]
            ret = mincost

            for i, v in enumerate(mincosts):
                print((i, v))
            print('=====')
        return ret


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
        ret = self.inst.min_cost(costs)
        assert(ret == 7)

    def test_1(self):
        '''
        Given:  [[17, 2, 17], [16, 16, 5], [14, 3, 19]]
        Ouput: 2 + 5 + 3 = 10
        '''
        costs = [[17, 2, 17], [16, 16, 5], [14, 3, 19]]
        ret = self.inst.min_cost(costs)
        assert(ret == 10)

    def test_2(self):
        '''
        Given:  []
        Ouput: 0
        '''
        costs = []
        ret = self.inst.min_cost(costs)
        assert(ret == 0)

    def test_3(self):
        '''
        Given:  [[7,6,2]]
        Ouput: 0
        '''
        costs = [[7, 6, 2]]
        ret = self.inst.min_cost(costs)
        assert(ret == 2)

    def test_4(self):
        '''
        Given:  [[3,5,3],[6,17,6],[7,13,18],[9,10,18]]
        Ouput: 26
        '''
        costs = [[3, 5, 3], [6, 17, 6], [7, 13, 18], [9, 10, 18]]
        ret = self.inst.min_cost(costs)
        assert(ret == 26)
