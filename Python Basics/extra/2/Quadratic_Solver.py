import sys

def are_roots_real(P, Q, R):
    if type(P) != float or type(Q) != float :
        print("Bad type for arguments")
        sys.exit(-1)

    delta = Q**2 - 4 * P * R

    if delta >= 0:
        return True
    else:
        return False

def get_roots(L, M, N):
    root1 = (-M + (M**2 - 4 * L * N) ** 0.5)/ (2 * L)
    root2 = (-M - (M**2 - 4 * L * N) ** 0.5)/ (2 * L)
    T = (root1, root2)
    return (T)

def main():

    A = float(input("Enter the C.F. of power 2:"))
    if A == 0.0:
        print("Bad C.F. of power 2")
        sys.exit(-1)
    B = float(input("Enter the C.F. of power 1:"))
    C = float(input("Enter the constant:"))

    if are_roots_real(A, B, C) == True:
        T = get_roots(A, B, C)
        print("Root1:%.4f Root2:%.4f" % (T[0], T[1]))
    else:
        print("No real roots found")
        sys.exit(-1)
        
    sys.exit(0)
    
main()

    
