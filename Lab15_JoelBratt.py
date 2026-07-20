"""Lab15_JoelBratt.py
Joel Bratt
the purpose of the program is to plot a square.
7/20/2026
"""
import matplotlib.pyplot as plt
import math

x_list = []
y_list = []

for i in range(5):
    x = math.pow(-1, math.floor((i + 1) / 2))
    y = math.pow(-1, math.floor(i / 2))

    x_list.append(x)
    y_list.append(y)

