from Calculator import *
import collections
import sys
import math


class StatisticCalculator(Calculator):

    #check the list is valid
    # 1. not string
    # 2. not empty
    @staticmethod
    def check(data):
        if not all(isinstance(item,int) for item in data) or len(data)==0:
            print("Your data include string type or is empty,please give valid data")
            sys.exit()

    # calculate mean of the list
    @staticmethod
    def mean(data):
        StatisticCalculator.check(data)
        Calc1=Calculator()
        sum = 0
        for x in data:
            sum= Calc1.addition(x,sum)
        return float(sum/len(data))

    # calculate median of the list

    @staticmethod
    def median(data):
        StatisticCalculator.check(data)
        num_sorted = sorted(data)
        length = len(num_sorted)

        if length % 2 != 0:
            return num_sorted[int(length/2)]
        else:
            return (num_sorted[int(length/2)]+num_sorted[int((length/2)-1)])/2

    # calculate mode of the list
    @staticmethod

    def mode(data):
        StatisticCalculator.check(data)
        num = []
        tuple = collections.Counter(data).most_common()
        num.append(tuple[0][0])
        for i in range(len(tuple) - 1):
            if tuple[i][1] == tuple[i + 1][1]:
                num.append(tuple[i + 1][0])
            else:
                break
        return num

    # calculate variance of the list

    @staticmethod
    def variance(data):
        StatisticCalculator.check(data)
        average=StatisticCalculator.mean(data)
        res = sum((i - average) ** 2 for i in data) / (len(data)-1)
        return res

    # calculate standard variation of the list

    @staticmethod
    def stdvar(data):
        StatisticCalculator.check(data)
        average = StatisticCalculator.mean(data)
        res = sum((i - average) ** 2 for i in data) / (len(data)-1)
        return math.sqrt(res)


