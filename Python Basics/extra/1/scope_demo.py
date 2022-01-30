n = 10
print("global:n:", n) 
print("globals():", globals())

def f1(): 

    n = 100
    print("f1:n:", n)
    print("f1:locals():", locals())
    def f2():

        n = 1000
        print("f2:n:", n) 
        print("f2:locals():", locals())

        def f3(): 

            n = 10000
            print("f3:n:", n)
            print("f3:locals():", locals())

        f3()

    f2()

f1()
