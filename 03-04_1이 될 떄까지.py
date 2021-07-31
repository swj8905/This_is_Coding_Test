#### 내 정답 ####
n, k = map(int, input().split())
cnt = 0
while True:
    if n % k == 0:
        n = n/k
    else:
        n -= 1
    cnt += 1
    if n == 1:
        break
print(cnt)


#### 책 정답 - 연산을 더 줄이는 방법 ####
n, k = map(int, input().split())
cnt = 0
while True:
    target = (n // k) * k
    cnt += (n-target)
    if n < k:
        break
    n //= k
    cnt += 1

cnt += (n-1)
