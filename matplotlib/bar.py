import matplotlib.pyplot as plt
import random


def bar_random():
    y = random.choices(range(1000), k=7)
    x = ["1", "2", "3", "4", "5", "6", "7"]
    plt.bar(x, y)
    plt.title("Диаграмма с рандомными числами")
    plt.ylabel("числа")
    plt.show()
