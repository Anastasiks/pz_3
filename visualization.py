import math
import matplotlib.pyplot as plt

def plot_xy(x, y, a=None, b=None, title="График X-Y"):
    if a is not None and b is not None:
        x2, y2 = [], []
        for xi, yi in zip(x, y):
            if a <= xi <= b:
                x2.append(xi)
                y2.append(yi)
    else:
        x2, y2 = x, y

    plt.plot(x2, y2) #строит линию по точкам
    plt.xlabel("X") #подпись оси
    plt.ylabel("Y")
    plt.title(title)
    plt.grid(True) #сетка на графике
    plt.show() #показывает окнос графиком


def print_table_xy(x, y):
    width = max(len(f"{val:.3f}") for val in x + y)
    row_x = " ".join(f"{val:{width}.3f}" for val in x)
    row_y = " ".join(f"{val:{width}.3f}" for val in y)

    print("X:", row_x)
    print("Y:", row_y)

if __name__ == "__main__":
    x = [i * 0.5 for i in range(-10, 11)]   # от -5 до 5 с шагом 0.5
    y = [math.sin(val) for val in x]
    plot_xy(x, y, a=-3, b=3, title="gr")
    print_table_xy(x, y)
