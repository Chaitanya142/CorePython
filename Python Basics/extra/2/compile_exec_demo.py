s = "n = 10" 
print("s:", s)
print("type(s):", type(s))

#print(n) # NameError exception because 'n' is not created yet

C = compile(s, mode='single', filename='fakename')
print("type(C):", type(C))

#print(n) # NameError exception because 'n' is not created yet

exec(C)

print(n)
