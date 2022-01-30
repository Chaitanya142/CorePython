L = [10, 20, 30]
for x in L:
    print(x)
def f(): 
    D = {"a" : 10, "b" : 20, "c" : 30} 

    for k in sorted(D.keys()):
        print(k, D[k]) 
    def g(): 
        S = {100, 200, 300} 
        for y in sorted(S):
            print(y, type(y)) 
        def h(): 
            L = [100, 200, 300, 400, 3, 2, 1]
            def find_min(L): 
                if len(L) == 0: 
                    return (None) 
                min_element = L[0] 
                for i in range(1, len(L)): 
                    if L[i] < min_element: 
                        min_element = L[i]
                return min_element
            x = find_min(L) 
            print(x)
        print("Hello") 
        h()
        print("World") 
    g()
    print("Bye") 

print("where will this be?") 
f()
print("Good-Bye!") 



