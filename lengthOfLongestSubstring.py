
def lengthOfLongestSubstring(s):
    # cset = set()
    # rst = 0
    # rk = -1
    # n = len(s)
    # for i in range(n):
    #     if i > 0:
    #         cset.remove(s[i - 1])
    #
    #     while rk + 1 < n and s[rk + 1] not in cset:
    #         cset.add(s[rk + 1])
    #         rk += 1
    #
    #     rst = max(rst, rk + 1 - i)
    #
    # return rst

    c2idx = {}
    left = 0
    right = 0
    rst = 0
    n = len(s)
    while left < n and right < n and left <= right:
        if s[right] in c2idx and c2idx[s[right]] >= left:
            left = c2idx[s[right]] + 1

        c2idx[s[right]] = right
        right += 1

        rst = max(right - left, rst)

    return rst



s = "abba"
print(lengthOfLongestSubstring(s))
