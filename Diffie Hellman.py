#secret key
p = 23
g = 5

a = 4
b = 3

x = (g ** a) % p
z = (g ** b) % p

print("a value",x)
print("b value",z)

#shared key

s1 = (z ** a) % p
s2 = (x ** b) % p

print("A's shared ",s1)
print("B's shared ",s2)
