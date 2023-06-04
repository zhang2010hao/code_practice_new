def minWindow(s, t):
    def check():
        for k, v in t_c2n.items():
            if s_c2n.get(k, 0) < v:
                return False

        return True

    t_c2n = {}
    for c in t:
        t_c2n[c] = t_c2n.get(c, 0) + 1

    n = len(s)
    left = 0
    right = 0
    best_l = 0
    best_r = n
    s_c2n = {}

    while right < n:
        if s[right] not in t_c2n:
            right += 1
            continue

        s_c2n[s[right]] = s_c2n.get(s[right], 0) + 1

        while check() and left <= right:
            if right - left < best_r - best_l:
                best_r, best_l = right, left

            c = s[left]
            if c not in t_c2n:
                left += 1
                continue

            s_c2n[c] = s_c2n[c] - 1

            if check() and left + 1 <= right:
                if right - left - 1 < best_r - best_l:
                    best_r, best_l = right, left
                left += 1

            else:
                s_c2n[c] = s_c2n.get(c, 0) + 1
                break

        right += 1

    if best_r < n:
        rest = s[best_l: best_r + 1]
    else:
        rest = ''

    return rest


s = "ADOBECODEBANC"
t = "ABC"
print(minWindow(s, t))
