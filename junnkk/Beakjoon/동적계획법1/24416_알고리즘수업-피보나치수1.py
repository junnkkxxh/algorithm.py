# pypy3으로 제출
def fib(n):
    global cnt1
    if n == 1 or n == 2:
        return 1
    else:
        cnt1 += 1
        return fib(n-1)+fib(n-2)


# 한 번 계산된 결과를 메모이제이션하기 위한 리스트 초기화
d = [0]*100

# 피보나치 함수(Fibonacci Function)를 재귀함수로 구현(탑다운 다이나믹 프로그래밍)


def fibo(x):
    global cnt2
    # 종료 조건(1 혹은 2일때 1을 반환)
    if x == 1 or x == 2:
        return 1
    # 이미 계산한 적 있는 문제라면 그대로 반환
    if d[x] != 0:
        cnt2 += 1
        return d[x]
    # 아직 계산하지 않은 문제라면 점화식에 따라서 피보나치 결과 반환

    d[x] = fibo(x-1)+fibo(x-2)

    return d[x]


n = int(input())
cnt1 = 0
cnt2 = 0

fib(n)
fibo(n)
print(cnt1+1, cnt2+2)
