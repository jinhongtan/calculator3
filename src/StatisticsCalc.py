from Calculator import *
from collections import Counter
import sys
import math


class StatisticCalc(Calculator):

    #check the list is valid
    # 1. not string
    # 2. not empty
    def check(self,data):
        if not all(isinstance(item,int) for item in data) or len(data)==0:
            print("Your data include string type or is empty,please give valid data")
            sys.exit()

    # calculate mean of the list

    def mean(self,data):
        self.check(data)
        Calc1=Calculator()
        sum = 0
        for x in data:
            sum= Calc1.addition(x,sum)
        return float(sum/len(data))

    # calculate median of the list

    def median(self,data):
        self.check(data)
        num_sorted = sorted(data)
        length = len(num_sorted)

        if length % 2 != 0:
            return num_sorted[int(length/2)]
        else:
            return (num_sorted[int(length/2)]+num_sorted[int((length/2)-1)])/2

    # calculate mode of the list

    def mode(self,data):
        self.check(data)
        return Counter(data).most_common(1)[0][0]

    # calculate variance of the list

    def variance(self,data):
        self.check(data)
        average=self.mean(data)
        res = sum((i - average) ** 2 for i in data) / (len(data)-1)
        return res

    # calculate standard variation of the list

    def stdvar(self,data):
        self.check(data)
        average = self.mean(data)
        res = sum((i - average) ** 2 for i in data) / (len(data)-1)
        return math.sqrt(res)


