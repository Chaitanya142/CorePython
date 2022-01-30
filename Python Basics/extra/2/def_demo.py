import sys

def find_max(L):
    if type(L) != list:
        print("bad type for input argument")
        sys.exit(-1) 
    if len(L) == 0: 
        return (-1) 
    max_element = L[0] 
    for x in L[1 : ]: 
        if x > max_element: 
            max_element = x 
    print("max_element:", max_element)


print("type(find_max):", type(find_max))

find_max([10, 20, 30, 40])
find_max([100, 400, 300, 200])

X = find_max

print("id(find_max):", id(find_max))
print("id(X):", id(X))

print("type(find_max):", type(find_max))
print("type(X):", type(X))


find_max([1,2,3,4])
X([1.1,2.2,3.3])

def maximum_in_list(L):
    if type(L) != list:
        raise TypeError("Bad type")
    if len(L) == 0: 
        return (-1) 
    max_element = L[0] 
    for x in L[1 : ]: 
        if x > max_element: 
            max_element = x 
    print("max_element:", max_element)

print("id(find_max):", id(find_max))
print("id(maximum_int_list):", id(maximum_in_list))



