#### 내 정답 ####
n, m = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(sorted(list(map(int, input().split()))))

result = arr[0][0]
for i in arr:
    if result < i[0]:
        result = i[0]
print(result)

#### 책 정답 - min 함수 이용 ####
n, m = map(int, input().split())
result = 0
for i in range(n):
    arr = list(map(int, input().split()))
    min_value = min(arr)
    result = max(result, min_value)
print(result)