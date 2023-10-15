import matplotlib.pyplot as plt


def graphics(f1, f2):
    plt.title("Графики f1, f2")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid()
    x = -15
    gr1 = eval(f1)
    gr2 = eval(f2)
    for x in range(-15, 15):
        if eval(f1) == eval(f2):
            break
    gr3 = eval(f1)
    gr4 = eval(f2)
    plt.plot([-15, x], [gr1, gr3], [-15, x], [gr2, gr4])
    plt.legend([f"f1 = {f1}", f"f2 = {f2}"], loc=2)
    plt.show()
