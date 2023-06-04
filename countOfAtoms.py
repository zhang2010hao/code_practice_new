def countOfAtoms(formula):
    def findnum(idx):
        if idx >= n:
            return '1'
        elif formula[idx] in n_ch:
            r = idx + 1
            while r < n and formula[r] in n_ch:
                r += 1

            num = formula[idx:r]
            return num

        else:
            return '1'

    def findatom(idx):
        if idx < n - 1:
            if formula[idx:idx+2] in atom:
                return formula[idx:idx+2]
            else:
                return formula[idx]
        else:
            return formula[idx]


    n = len(formula)


    l_ch = ['a', 'b', 'c', 'd', 'e', 'f', 'g',
                'h', 'i', 'j', 'k', 'l', 'm', 'n',
                'o', 'p', 'q', 'r', 's', 't', 'u',
                'v', 'w', 'x', 'y', 'z']

    g_ch = ['A', 'B', 'C', 'D', 'E', 'F', 'G',
                'H', 'I', 'J', 'K', 'L', 'M', 'N',
                'O', 'P', 'Q', 'R', 'S', 'T', 'U',
                'V', 'W', 'X', 'Y', 'Z']

    atom = set()
    for c1 in g_ch:
        atom.add(c1)
        for c2 in l_ch:
            atom.add(c1+c2)

    n_ch = set(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'])

    stack = [{}]
    i = 0
    while i < n:
        if formula[i] == '(':
            stack.append({})
            i += 1

        elif formula[i] == ')':
            i += 1
            num_str = findnum(i)
            if int(num_str) > 1:
                i = i + len(num_str)
            num = int(num_str)

            top_dict = stack.pop(-1)
            second_dict = stack.pop(-1)
            for k, v in top_dict.items():
                second_dict[k] = second_dict.get(k, 0) + v * num
            stack.append(second_dict)
        else:
            atom_str = findatom(i)
            i = i + len(atom_str)
            num_str = findnum(i)
            if int(num_str) > 1:
                i = i + len(num_str)
            num = int(num_str)
            top_dict = stack.pop(-1)
            tmp = top_dict.get(atom_str, 0) + num
            top_dict[atom_str] = tmp

            stack.append(top_dict)

    rst_dict = {}
    for d in stack:
        for k, v in d.items():
            tmp = rst_dict.get(k, 0) + v
            rst_dict[k] = tmp

    sorted_dict = sorted(rst_dict.items(), key=lambda x: x[0])
    rst = ''
    for k, v in sorted_dict:
        if v > 1:
            rst = rst + k + str(v)
        else:
            rst = rst + k

    return rst


formula = "(Cr36At29)10(KrHs9Fm20Y)28(Md4Sc19I36)2"
rst = countOfAtoms(formula)
print(rst)


