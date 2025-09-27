# ФУНКЦИЯ № 1
def subst(a,b):
    print("a-b = ", a-b)
def summ(x,y):
    print("x+y = ", x+y)
def decore(func):
    def wrapper(t,z):
        print("Run function")
        func(t,z)
        print("Stop function")
    return wrapper
subst_wrapped = decore(subst)
summ_wrapped = decore(summ)
subst(88,77)
summ(88, 77)
subst_wrapped(88, 77)
summ_wrapped(88, 77)


# ФУНКЦИЯ № 2

def uppercase(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.upper()
    return wrapper

@uppercase
def greet(name):
    return f"Привет, {name}"

print(greet("Аня"))

# ФУНКЦИЯ № 3

def smile(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return str(result) + " 🙂"
    return wrapper

@smile
def say_hello(name):
    return f"Привет, {name}"

print(say_hello("Алексей"))

