import io,sys
with open("/Users/shunyonai/Documents/GitHub/atcoder/input.txt") as TxtOpen:
    INPUT=TxtOpen.read()
sys.stdin=io.StringIO(INPUT)
# --------------------------------------------------------

N, M = map(int, input().split())
X = sum(N ** i for i in range(M+1))
print(X) if X <= 10 ** 9 else print('inf')
