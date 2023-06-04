

def decodeString(s):
    n = len(s)
    if n == 1:
        return s

    rest = ''
    q = []
    i = 0
    while i < n:
        if s[i] != ']':
            q.append(s[i])

        else:
            tmp_str = ''
            while len(q) > 0:
                c = q.pop(-1)
                if c == '[':
                    break
                else:
                    tmp_str = c + tmp_str
            num = ''
            while len(q) > 0:
                if q[-1].isdigit():
                    num = q.pop(-1) + num
                else:
                    break

            num = int(num)
            tmp_arr = [tmp_str] * num
            tmp_str = ''.join(tmp_arr)
            q.append(tmp_str)

        i += 1

    while len(q) > 0:
        rest = rest + q.pop(0)

    return rest

s = "2[abc]3[cd]ef"
print(decodeString(s))


