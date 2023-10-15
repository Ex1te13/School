import matplotlib.pyplot as plt
import math


def graphik():
    x = [i/10 for i in range(-50, 50, 1)]
    y1 = [j**2 for j in x]
    y2 = [math.sin(j) for j in x]
    y3 = [math.cos(j) for j in x]
    y4 = [2 / j if j != 0 else None for j in x]
    plt.figure("Поля с графиками", figsize=(15, 15))
    plt.subplot(2, 2, 1)
    plt.title("x^2")
    plt.ylabel("y1")
    plt.plot(x, y1)
    plt.grid(True)
    plt.subplot(2, 2, 2)
    plt.title("sin(x)")
    plt.ylabel("y2")
    plt.plot(x, y2)
    plt.grid(True)
    plt.subplot(2, 2, 3)
    plt.title("cos(x)")
    plt.ylabel("y3")
    plt.plot(x, y3)
    plt.grid(True)
    plt.subplot(2, 2, 4)
    plt.title("2/x")
    plt.ylabel("y4")
    plt.plot(x, y4)
    plt.grid(True)
    plt.show()
