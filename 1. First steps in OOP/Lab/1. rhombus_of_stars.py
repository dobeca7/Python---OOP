n = int(input())

for num in range(1, n+1):
    print(f"{' '*(n-num)}{'* ' * num}")

for num in range(1, n):
    print(f"{' ' * num}{'* ' * (n - num)}")
