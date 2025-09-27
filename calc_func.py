import math

# 1. Площадь круга
def circle_area(radius):
    return math.pi * radius**2

# 2. Возведение в куб
def cube(x):
    return x ** 3

# 3. Максимум из трёх чисел
def max_of_three(a, b, c):
    return max(a, b, c)

# 4. Синус
def sin_func(x):
    return math.sin(x)

# 5. Косинус
def cos_func(x):
    return math.cos(x)

if __name__ == "__main__":
    # демо-примеры
    print("Площадь круга (r=3) =", circle_area(3))
    print("Куб 3 =", cube(3))
    print("Максимум из (5, 12, 7):", max_of_three(5, 12, 7))
    print("sin(π/2) =", sin_func(math.pi/2))
    print("cos(0) =", cos_func(0))
