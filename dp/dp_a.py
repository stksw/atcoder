N = int(input())
score = [int(i) for i in input().split(' ')]
total = sum(score)

dp = [[0] * (total+1) for _ in range(N+1)]


def compare_max(a, b):
    return a if a > b else b

for i in range(N):
    for j in range(total+1):
        if j >= score[i]:
            # score[i]を選ぶ
            dp[i+1][j] = dp[i][j - score[i]] + score[i]
        # score[i]を選ばない
        dp[i+1][j] = compare_max(dp[i][j], dp[i+1][j])

result = []
for i in range(int(N+1)):
    result.extend(dp[i])
print(len(list(set(result))))