def lcs_length(X, Y):
    m = len(X)
    n = len(Y)


    dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

    # Fill DP table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[m][n], dp


def build_lcs(X, Y, dp):
    i = len(X)
    j = len(Y)
    result = []

    while i > 0 and j > 0:

        if X[i - 1] == Y[j - 1]:
            result.append(X[i - 1])
            i -= 1
            j -= 1


        elif dp[i - 1][j] >= dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

    result.reverse()

    return "".join(result)


X = "APPLE"
Y = "APP"

length, dp = lcs_length(X, Y)
subsequence = build_lcs(X, Y, dp)

print("First string :", X)
print("Second string:", Y)
print("Length of LCS:", length)
print("LCS         :", subsequence)