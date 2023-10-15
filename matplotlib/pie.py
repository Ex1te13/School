import matplotlib.pyplot as plt


def pie(n):
    plt.title("Круговая диаграмма")
    labels = [i+1 for i in range(n)]
    values = [100/n for j in range(n)]
    plt.pie(values, labels=labels)
    plt.show()
