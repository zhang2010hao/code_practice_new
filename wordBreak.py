
def wordBreak(s, wordDict):
    n = len(s)
    dp = [False] * (n + 1)
    w2idx = {}
    for w in wordDict:
        if w not in w2idx:
            w2idx[w] = len(w2idx)

    dp[0] = True
    for i in range(n + 1):
        for j in range(i):
            if dp[j] and s[j:i] in w2idx:
                dp[i] = True
                break

    return dp[-1]