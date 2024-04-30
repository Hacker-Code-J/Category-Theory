def add(x):
    def inner_add(y):
        return x + y
    return inner_add

add_five = add(5)  # This holds a function that adds 5 to its argument
result = add_five(3)  # This evaluates to 8

print(result)

# def f1(x):
#     return (x + 1, str(x) + "+1")

def f1(x):
    def with_log(message):
        return (x+1, message)
    return with_log

def f2(x):
    def with_log(message):
        return (x+2, message)
    return with_log

def f3(x):
    def with_log(message):
        return (x+3, message)
    return with_log

# Usage of a curried version
# curried_f1 = f1(1)
# result_cur = curried_f1("+1")

# print(result_cur)

def unit(x):
    return (x, "Ops:")

def bind(t, f):
    res = f(t[0])
    return (res[0], t[1] + res[1] + ";")

print(bind(bind(bind(unit(0), f1), f2), f3))