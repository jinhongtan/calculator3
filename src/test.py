import StatisticsCalc
import unittest
import math
import statistics
import randomNum


class test(unittest.TestCase):

    data=[]
    x = StatisticsCalc.StatisticCalc()

    def setUp(self) -> None:
        self.data=randomNum.intGenerator(self)

    def test_mean(self):
        self.assertEqual(self.x.mean(self.data),sum(self.data)/len(self.data))

    def test_median(self):
        self.assertEqual(self.x.median(self.data),statistics.median(self.data))

    def test_mode(self):
        self.assertEqual(self.x.mode(self.data),statistics.mode(self.data))

    def test_variance(self):
        self.assertAlmostEqual(self.x.variance(self.data),statistics.variance(self.data))

    def test_stdvar(self):
        self.assertAlmostEqual(self.x.stdvar(self.data), statistics.stdev(self.data))


if __name__ == '__main__':
    unittest.main()
