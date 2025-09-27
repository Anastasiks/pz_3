# main.py
from visualization import plot_xy, print_table_xy
from calc_func import circle_area, cube, sin_func, cos_func

def frange(a, b, step):
    x = a
    out = []
    while (step > 0 and x <= b) or (step < 0 and x >= b):
        out.append(x)
        x += step
    return out

def choose_func():
    print("1) cube(x)")
    print("2) circle_area(x)")
    print("3) sin(x)")
    print("4) cos(x)")
    ch = input("Твой выбор: ").strip()
    return {
        "1": (cube, "cube(x)"),
        "2": (circle_area, "π*x^2"),
        "3": (sin_func, "sin(x)"),
        "4": (cos_func, "cos(x)"),
    }.get(ch, (cube, "cube(x)"))

if __name__ == "__main__":
    a = float(input("Введите a: "))
    b = float(input("Введите b: "))
    step = float(input("Введите шаг: "))

    f, fname = choose_func()

    X = frange(a, b, step)
    Y = [f(x) for x in X]

    print_table_xy(X, Y)
    plot_xy(X, Y, a=min(a, b), b=max(a, b))
