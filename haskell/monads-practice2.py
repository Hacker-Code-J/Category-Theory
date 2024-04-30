def f1(x):
    return (x + 1, str(x) + "+1")

def f2(x):
    return (x + 2, str(x) + "+2")

def f3(x):
    return (x + 3, str(x) + "+3")

def unit(x):
    return (x, "Ops:")

def bind(t, f):
    res = f(t[0])
    return (res[0], t[1] + res[1] + ";")

# Direct calls setup
def direct_calls(x):
    log = "Ops:"
    res, log1 = f1(x)
    log += log1 + ";"
    res, log2 = f2(res)
    log += log2 + ";"
    res, log3 = f3(res)
    log += log3 + ";"
    return res, log

# Functional approach setup
def functional_approach(x):
    return bind(bind(bind(unit(x), f1), f2), f3)

print(direct_calls(10))
print(functional_approach(10))