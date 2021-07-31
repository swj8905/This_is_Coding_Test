# n: 배열의 크기
# m: 더해지는 숫자 개수
# k: 연속 인덱스 허용 개수

#### 내 정답 ####
n, m, k = map(int, input().split())
arr = sorted(list(map(int, input().split())), reverse=True)

cnt = 0
cnt_continuous = 0
sum = 0
while cnt < m:
    if cnt_continuous >= k:
        cnt_continuous = 0
        sum += arr[1]
    else:
        sum += arr[0]
    cnt += 1
    cnt_continuous += 1
print(sum)


#### 책 정답1 ####
n, m, k = map(int, input().split())
data = list(map(int, input().split()))
data.sort()
first = data[n-1]
second = data[n-2]

result = 0

while True:
    for i in range(k):
        result += first
        m -= 1
        if m == 0:
            break
    if m == 0:
        break
    result += second
    m -= 1
print(result)


#### 책 정답 2 - 수학적 아이디어 ####
n, m, k = map(int, input().split())
data = list(map(int, input().split()))
data.sort()
first = data[n-1]
second = data[n-2]

# 큰 수가 더해지는 횟수 계산
count = m // (k+1) * k + m % (k+1)

result = count * first + (m-count) * second
print(result)