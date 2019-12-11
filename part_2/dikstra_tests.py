import unittest
from part_2.dijkstra import dijkstra
graph = [[],
         [[2,10],[3,40]],
         [[3,20],[4,70]],
         [[4,30]],
         [[2,10]]]

class MyTestCase(unittest.TestCase):
    def test_something(self):
        costs = dijkstra(graph)
        self.assertEqual(costs[1], 0)
        self.assertEqual(costs[2], 10)
        self.assertEqual(costs[3], 30)
        self.assertEqual(costs[4], 60)



if __name__ == '__main__':
    unittest.main()
