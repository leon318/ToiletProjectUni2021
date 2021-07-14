'''
Test to practice taking the average of the numbers in some arrays. Not important.
'''

from matplotlib import pyplot as plt
import statistics

a = ["/Users/Leon/Documents/ToiletProjectUni2021/Experiment1(Leon_Standing)/Experiment1,T2"]
b = ["/Users/Leon/Documents/ToiletProjectUni2021/Experiment1(Leon_Standing)/Experiment1,T3"]

x = []
file_in = open("/Users/Leon/Documents/ToiletProjectUni2021/Experiment1(Leon_Standing)/Experiment1,T2", 'r')
for y in file_in.read().split('\n'):
    if y.isdigit():
        x.append(float(y))
w = []
file_in2 = open("/Users/Leon/Documents/ToiletProjectUni2021/Experiment1(Leon_Standing)/Experiment1,T3", 'r')
for z in file_in2.read().split('\n'):
    if z.isdigit():
        w.append(float(z))
result = [statistics.mean(k) for k in zip(a, b)]
