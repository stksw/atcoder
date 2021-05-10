N = int(input())
arr = [[None]] * N
result = 0

for i in range(N):
    arr[i] = [int(j) for j in input().split(' ')] 

mod = [0] * N
counter = 0

for i in range(N-1, -1, -1):
    # forの二重ループにしないよう、ボタン回数を加算して判定
    arr[i][0] += counter
    mod = arr[i][0] % arr[i][1]
    if mod != 0:
        # 倍数でない場合は余りを差し引き、counterに加算しておく
        arr[i][0] += arr[i][1] - mod
        counter += arr[i][1] - mod
print(counter)