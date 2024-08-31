import re

from .dict import dictnum


def start(num):
    output = ""
    numbackup = num  # 输入数字备份
    needchangenum = []

    class caculate:
        def __init__(self, num, output):
            self.num = num
            self.output = output

        def chufa(self):
            numafter = self.num / 721
            return int(numafter)

        def output1(self):
            if self.num > 721:
                self.output = self.output + "721*"
                return self.output
            else:
                return self.output + f"{changenum(int(self.num))[int(self.num)]}"

    def fenjie(num, output):  # 分解成114514*
        list1 = []
        while 1:
            list1.append(num)
            a = caculate(num, output)
            num = int(a.chufa())
            output = a.output1()
            if num == 0:
                return list1[-1], eval(output), output

    # 分解成****+****的形式
    def addit(num, output):
        nextnum, usednum, output = fenjie(num, output)  # type: ignore
        needchangenum.append(nextnum)
        num = numbackup - usednum
        return num, output, needchangenum

    while 1:
        num, output, needchangenum = addit(num, output)
        if num == 0:
            break
        output = output + "+"
    print(output)
    return output


def changenum(num):
    listkeys = list(dictnum.keys())
    numbackup = num
    data = "("
    while not num == 0:
        for i in listkeys:
            if num - i > 0:
                data = data + dictnum[i] + "+"
                num = num - i
                break
            if num - i == 0:
                data = data + dictnum[i]
                num = 0
                break
    data = data + ")"
    dictover = {numbackup: data}
    return dictover


def yuzu(text):
    try:
        num = int(text)
        if num == 0:
            msg = "0*721"
        elif abs(num) == 721:
            msg = "请看我オナニー吧！"
        elif num > 0:
            msg = start(num)
            pattern_m = r"\*-([0-9]+)"
            pattern_d = r"/-([0-9]+)"
            pattern_q = r"^\((.*)\)$"
            msg = (
                re.sub(
                    r'^721',
                    '0+721',
                    re.sub(
                        pattern_q,
                        r"\1",
                        re.sub(pattern_d, r"/(-\1)", re.sub(pattern_m, r"*(-\1)", msg)),
                    ),
                )
                .replace('+-', '-')
                .replace('*721', '*(0+721)')
            )
        elif num < 0:
            msg = str(start(abs(num)))
            msg = "-" + msg
        return msg
    except:
        return "输整数～(∠·ω< )⌒★"
