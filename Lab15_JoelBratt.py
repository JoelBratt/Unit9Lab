"""Lab15_JoelBratt.py
Joel Bratt
the purpose of the program is to plot a square.
7/20/2026
"""
import matplotlib.pyplot as plot
import math

x_list = []
y_list = []

for i in range(5):
    x = math.pow(-1, math.floor((i + 1) / 2))
    y = math.pow(-1, math.floor(i / 2))

    x_list.append(x)
    y_list.append(y)

plot.plot(x_list, y_list, color="darkcyan", linestyle ="-", linewidth = 3 )

plot.title("Making a Square")
plot.xlabel('X-axis')
plot.ylabel('Y-axis')

plot.grid(True)
plot.axis('equal')

plot.savefig('Square.png')
print("Square generated check the folder!")
