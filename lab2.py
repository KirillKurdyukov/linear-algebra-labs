import math
import cmath
def cur(fin):
    A1 = list(map(float, fin.readline().split()))
    A = []
    for i in range(3):
        A.append(A1[i])
    return A
def Write(A, ff):
    for i in range(3):
        ff.write(str(A[i]) + " ")
    ff.write("\n")
def VecDiff(A, B):
    C = []
    for i in range(3):
        C.append(A[i] - B[i])
    return C
def VecMulti(A, B):
    C = []
    C.append(A[1] * B[2] - B[1] * A[2])
    C.append((-1) * (A[0] * B[2] - B[0] * A[2]))
    C.append(A[0] * B[1] - B[0] * A[1])
    return C
def VecAngle(A, B):
    return ((A[0] * B[0] + A[1] * B[1] + A[2] * B[2]) / (math.sqrt(A[0] * A[0] + A[1] * A[1] + A[2] * A[2]) * math.sqrt(B[0] * B[0] + B[1] * B[1] + B[2] * B[2])))
def main():
    fin = open("input.txt", "r")
    ff = open("output.txt", "w")
    V = cur(fin)
    A = cur(fin)
    M = cur(fin)
    W = cur(fin)
    C = VecDiff(W, V)
    N = []
    N.append(0)
    N.append(0)
    N.append(1)
    FR = VecMulti(A, N)
    FL = VecMulti(N, A)
    CosMandN = VecAngle(M, N)
    CosCandA = VecAngle(C, A)
    if(math.fabs(CosMandN) < 0.5):
        ff.write(str(0))
        return 0
    if (math.fabs(CosCandA) > math.sqrt(3) / 2):
        ff.write(str(0))
        return 0
    if (VecAngle(FR, C) >= 0.5):
        if (CosCandA < 0):
            temp = -1
        else:
            temp = 1
        ff.write(str(-1) + "\n")
        ff.write(str(math.acos(math.fabs(VecAngle(FR, C))) * (180 / math.pi) * temp) + "\n")
    if (VecAngle(FL, C) >= 0.5):
        if (CosCandA < 0):
            temp = -1
        else:
            temp = 1
        ff.write(str(1) + "\n")
        ff.write(str(math.acos(VecAngle(FL, C)) * (180 / math.pi) * temp) + "\n")
    if (VecAngle(FL, M) > 0):
        temp = 1
    else:
        temp = -1
    ff.write(str(math.acos(math.fabs(CosMandN)) * (180 / math.pi) * temp) + "\n")
    ff.write(str("Na zlo vragam, na radost mame") + "\n")
    fin.close()
    ff.close()
if __name__ == '__main__':
    main()