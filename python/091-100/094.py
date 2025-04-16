# 별 찍기


N = int(input())

for k in range(1, 2*N):
    abs_k = abs(N-k)
    print(abs_k*' '+((N-abs_k)*2-1)*'*')
