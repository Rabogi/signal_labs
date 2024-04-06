def compMul(C1,C2):
    a = C1.real
    b = C1.imag
    c = C2.real
    d = C2.imag
    
    return complex(a*c-b*d,a*d+b*c)/2

def compSum(C1,C2):
    a = C1.real
    b = C1.imag
    c = C2.real
    d = C2.imag

    return complex(a + c,b + d)

def compSub(C1,C2):
    a = C1.real
    b = C1.imag
    c = C2.real
    d = C2.imag

    return complex(a - c,b - d)

def Bab_2(A,B,W):
    # print(W)
    return [compSum(A,compMul(B,W)),compSub(A,compMul(B,W))]

A = complex(1,7)
B = complex(7,5)
W = complex(2,7)

print(Bab_2(A,B,W))

# 0  0  0  0 | 0  0  0 0 | 0 0 0 0 | 0 0 0 0
# 15 14 13 12  11 10 9 8   7 6 5 4   3 2 1 0