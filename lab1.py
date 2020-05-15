def cur(Na, Ma, fin):
    A1 = list(map(float, fin.readline().split()))
    A = []
    l = 0
    r = Ma
    for i in range(Na):
        A.append([])
        for p in range(l, r):
            A[i].append(A1[p])
        l = l + Ma
        r = r + Ma
    return A
def SumMatrix(A, B, Na, Ma, Nb, Mb):
    if (Na!=Nb or Ma != Mb):
        return 0
    C = []
    for i in range(Na):
        C.append([])
        for j in range(Ma):
            C[i].append(A[i][j] + B[i][j])
    return C
def AntiSumMatrix(A, B, Na, Ma, Nb, Mb):
    if (Na!=Nb or Ma != Mb):
        return 0
    C = []
    for i in range(Na):
        C.append([])
        for j in range(Ma):
            C[i].append(A[i][j] - B[i][j])
    return C
def MultiConst(A, a):
    C = []
    for i in range(Na):
        C.append([])
        for j in range(Ma):
            C[i].append(A[i][j]*a)
    return C
def MultiMatrix(A, B, Na, Ma, Nb, Mb):
    if (Ma != Nb):
        return 0
    C = []
    for i in range(Na):
        C.append([])
        for j in range(Mb):
            a = 0
            for k in range(Ma):
                a = a + A[i][k] * B[k][j]
            C[i].append(a)
    return C
def Tran(A, Na, Ma):
    C = []
    for i in range(Ma):
        C.append([])
        for j in range(Na):
            C[i].append(A[j][i])
    return C
def X(A, B, C, D, F, a, b, Na, Ma, Nb, Mb, Nc, Mc, Nd, Md, Nf, Mf, ff):
    aA = MultiConst(A, a)
    BT = Tran(B, Nb, Mb)
    bBT = MultiConst(BT, b)
    SUM = SumMatrix(aA, bBT, Na, Ma, Nb, Mb)
    if (SUM == 0):
        ff.write(str(0))
        return 0
    Tsum = Tran(SUM, Na, Ma)
    MULTI = MultiMatrix(C, Tsum, Nc, Mc, Na, Ma)
    if (MULTI == 0):
        ff.write(str(0))
        return 0
    multi = MultiMatrix(MULTI, D, Nc, Ma, Nd, Md)
    if (multi == 0):
        ff.write(str(0))
        return 0
    XX = AntiSumMatrix(multi, F, Nc, Md, Nf, Mf)
    if (XX == 0):
        ff.write(str(0))
        return 0
    ff.write(str(1))
    ff.write('\n')
    ff.write(str(Nf) + " " +  str(Mf) + '\n')
    for i in range(Nf):
        for j in range(Mf):
            ff.write(str(XX[i][j]) + " ")
        ff.write('\n')
    ff.close()
    return 0
fin = open("input.txt", "r")
ff = open("output.txt", "w")
a, b = map(float, fin.readline().split())
Na, Ma = map(int, fin.readline().split())
A = cur(Na, Ma, fin)
Nb, Mb = map(int, fin.readline().split())
B = cur(Nb, Mb, fin )
Nc, Mc = map(int, fin.readline().split())
C = cur(Nc, Mc, fin)
Nd, Md = map(int, fin.readline().split())
D = cur(Nd, Md, fin)
Nf, Mf = map(int, fin.readline().split())
F = cur(Nf, Mf, fin)
X(A, B, C, D, F, a, b, Na, Ma, Nb, Mb, Nc, Mc, Nd, Md, Nf, Mf, ff)
fin.close()
ff.close()
