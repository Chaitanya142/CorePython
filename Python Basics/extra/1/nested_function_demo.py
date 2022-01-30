def f(): 
    print("In f") 
    def g():
        print("In g") 
    n = 10
    print(n) 
    g()
    print(n * 2)
f()
