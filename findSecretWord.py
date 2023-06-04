class Master:
    def guess(self, word: str) -> int:
        if word not in words:
            return -1
        else:
            # list1 = [word[k] for k in range(6)]
            # list2 = [guss_word[k] for k in range(6)]
            # for i in range(6):
            #     if list1[i] in list2:
            #         list2.remove(list1[i])
            #         cnt += 1
            cnt = sum([guss_word[k] == word[k] for k in range(6)])

            return cnt


def findSecretWord(words, master):
    def jiao(w1, w2):

        cnt = sum([w1[k] == w2[k] for k in range(6)])

        return cnt

    l = len(words)
    if l <= 10:  # 如果单词数量小于等于猜的次数，直接遍历猜即可求解。
        while master.guess(words.pop()) != 6:
            pass
        return True

    w2w = {}
    for i in range(l):
        for j in range(i + 1, l):
            c = jiao(words[i], words[j])  # 匹配次数
            tmp1 = w2w.get(words[i], {})
            tmp2 = tmp1.get(c, [])
            tmp2.append(words[j])
            tmp1[c] = tmp2
            w2w[words[i]] = tmp1

            tmp1 = w2w.get(words[j], {})
            tmp2 = tmp1.get(c, [])
            tmp2.append(words[i])
            tmp1[c] = tmp2
            w2w[words[j]] = tmp1

    m = float("inf")  # 最小的 最大最小值之差
    for i in range(l):
        p = [len(v) for k, v in w2w[words[i]].items()]
        c = max(p) - min(p)
        if c < m:
            m = c
            cur = words[i]  # 最平均的单词索引

    visted = set()
    inter_set = set(words)
    times = 0
    while times < 30:
        c = master.guess(cur)
        times += 1
        visted.add(cur)
        if c == 6:
            print(times)
            break

        tmp = w2w[cur][c]
        flag = False
        inter_set = inter_set & set(tmp)
        if len(inter_set) > 0:
            for w in inter_set:
                if w not in visted:
                    cur = w
                    flag = True
                    break

        if not flag:
            for w in words:
                if w not in visted:
                    cur = w
                    flag = True
                    break


guss_word = 'hbaczn'
words = ["gaxckt", "trlccr", "jxwhkz", "ycbfps", "peayuf", "yiejjw", "ldzccp", "nqsjoa", "qrjasy", "pcldos", "acrtag",
          "buyeia", "ubmtpj", "drtclz", "zqderp", "snywek", "caoztp", "ibpghw", "evtkhl", "bhpfla", "ymqhxk", "qkvipb",
          "tvmued", "rvbass", "axeasm", "qolsjg", "roswcb", "vdjgxx", "bugbyv", "zipjpc", "tamszl", "osdifo", "dvxlxm",
          "iwmyfb", "wmnwhe", "hslnop", "nkrfwn", "puvgve", "rqsqpq", "jwoswl", "tittgf", "evqsqe", "aishiv", "pmwovj",
          "sorbte", "hbaczn", "coifed", "hrctvp", "vkytbw", "dizcxz", "arabol", "uywurk", "ppywdo", "resfls", "tmoliy",
          "etriev", "oanvlx", "wcsnzy", "loufkw", "onnwcy", "novblw", "mtxgwe", "rgrdbt", "ckolob", "kxnflb", "phonmg",
          "egcdab", "cykndr", "lkzobv", "ifwmwp", "jqmbib", "mypnvf", "lnrgnj", "clijwa", "kiioqr", "syzebr", "rqsmhg",
          "sczjmz", "hsdjfp", "mjcgvm", "ajotcx", "olgnfv", "mjyjxj", "wzgbmg", "lpcnbj", "yjjlwn", "blrogv", "bdplzs",
          "oxblph", "twejel", "rupapy", "euwrrz", "apiqzu", "ydcroj", "ldvzgq", "zailgu", "xgqpsr", "wxdyho", "alrplq",
          "brklfk"]
master = Master()
findSecretWord(words, master)
