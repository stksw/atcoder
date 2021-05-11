a = [int(i) for i in input().split(' ')]
b = [int(i) for i in input().split(' ')]

result = max(a) - min(b)
print(result)