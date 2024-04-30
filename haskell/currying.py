# def add(x):
#     def inner_add(y):
#         return x + y
#     return inner_add

# add_five = add(5)  # This holds a function that adds 5 to its argument
# result = add_five(3)  # This evaluates to 8

# print(result)

# # def f1(x):
# #     return (x + 1, str(x) + "+1")

# def f1(x):
#     def with_log(message):
#         return (x+1, message)
#     return with_log

# def f2(x):
#     def with_log(message):
#         return (x+2, message)
#     return with_log

# def f3(x):
#     def with_log(message):
#         return (x+3, message)
#     return with_log

# # Usage of a curried version
# # curried_f1 = f1(1)
# # result_cur = curried_f1("+1")

# # print(result_cur)

# def unit(x):
#     return (x, "Ops:")

# def bind(t, f):
#     res = f(t[0])
#     return (res[0], t[1] + res[1] + ";")

# print(bind(bind(bind(unit(0), f1), f2), f3))

# def f(x, y):
# 	return x**2 + y**2

# result = f(3, 4)
# print("Direct result:", result)  # Outputs 25

# #===========================================================

# def g(x):
# 	def g_x(y):
# 		return x**2 + y**2
# 	return g_x

# # This holds a function that 
# # adds 3^2 to its argument squared
# curried = g(3)  
# result = curried(4)
# print("Curried result:", result)  # Outputs 25

# def f(x, y, z):
# 	return x**2 + y**2 + z**2

# result = f(2, 3, 4)
# print(result)  # Outputs 29

# def g(x):
# 	def g_x(y):
# 		def g_xy(z):
# 			return x**2 + y**2 + z**2
# 		return g_xy
# 	return g_x

# # First function, taking x
# curried_g = g(2)
# # Second function, taking y
# curried_gx = curried_g(3)
# # Final function, taking z and calculating the result
# result = curried_gx(4)
# # Outputs 29, since (2^2 + 3^2 + 4^2 = 4 + 9 + 16 = 29)
# print(result)  


pt = [0x48, 0x65, 0x6c, 0x6c, 0x6f]
key = [0x1f, 0x1b, 0x1a, 0x17, 0x10]

def xor_encrypt(key, pt):
    return [hex(p ^ k) for p, k in zip(pt, key)]

ct = xor_encrypt(key, pt)
print("Direct result:", ct)

def xor_cipher(key):
    def encrypt(pt):
        return [hex(p ^ k) for p, k in zip(pt, key)]
    return encrypt

enc_k = xor_cipher(key)
ct = enc_k(pt)
print("Curried result:", ct)