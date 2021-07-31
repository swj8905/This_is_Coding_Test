N = int(input())
price = [500, 100, 50, 10]
count = 0
for i in price:
    count += N // i
    N %= i
print(count)
