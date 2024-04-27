# Reference:
# https://nikgrozev.com/2013/12/10/monads-in-15-minutes/

#=======================
# Logging
#=======================

# def f1(x):
#     return (x + 1, str(x) + "+1")
# def f2(x):
#     return (x + 2, str(x) + "+2")
# def f3(x):
#     return (x + 3, str(x) + "+3")

# log = "Ops:"

# x = 0
# res, log1 = f1(x)
# log += log1 + ";"

# res, log2 = f2(res)
# log += log2 + ";"

# res, log3 = f3(res)
# log += log3 + ";"

# print(res, log)

# #--

# def unit(x):
#     return (x, "Ops:")

# def bind(t, f):
#     res = f(t[0])
#     return (res[0], t[1] + res[1] + ";")

# print( bind(bind(bind(unit(x), f1), f2), f3) )

#=======================
# List of Interim Values
#=======================

# def f1(x): return x + 1
# def f2(x): return x + 2
# def f3(x): return x + 3

# x = 0
# lst = [x]

# res = f1(x)
# lst.append(res)

# res = f2(res)
# lst.append(res)

# res = f3(res)
# lst.append(res)

# print(res, lst)

# def unit(x):
#     return (x, [x])

# def bind(t, f):
#     res = f(t[0])
#     return (res, t[1] + [res])

# print( bind(bind(bind(unit(x), f1), f2), f3) )

#=======================
# Nulls/Nones
#=======================