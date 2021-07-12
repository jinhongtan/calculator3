import random


def intGenerator(self):
    data=[]
    for i in range(random.randint(10,50)):
        data.append(random.randint(1,100))
    return data

def floatGenerator(self):
    data=[]
    for i in range(10):
        data.append(random.uniform(1,10))
    return data

