import re


def debug():
    with open('./file/0.txt', 'r') as f:
        for l in f:
            print(l, end=' ')
            me = dataclear(l)
            print(me.getepisode(), end=' ')
            print(me.zimufengzhuang(), end=' ')
            print(me.zimuyuyan())


class dataclear:
    def __init__(self, txt):
        self.txt = txt

    def rerules(self, rules, mubiao):
        for i in rules:
            e = re.search(i, self.txt, re.I)
            if e:
                ret = re.search(mubiao, e.group()).group()
                return ret
            else:
                return '/'

    def getepisode(self):
        match = re.search(r'(\[| |\[第|\[未删减)([0-9]{2})(\]| |集|v2|话)', self.txt)
        if match:
            return match.group(2)

    def zimuyuyan(self):  # 字幕语言
        sc = re.search(r'(\[| )(简|CHS|GB)', self.txt, re.I)
        tc = re.search(r'(\[| )简?(繁|CHT|BIG5)', self.txt, re.I)
        jp = re.search(r'(\[| )简?繁?(日)', self.txt, re.I)
        eng = re.search(r'(\[| )简?繁?日?(英)', self.txt, re.I)
        r = ''
        if sc:
            r += '简'
        if tc:
            r += '繁'
        if jp:
            r += '日'
        if eng:
            r += '英'
        return r

    def zimufengzhuang(self):  # 字幕封装方式
        match = re.search(r'(内封|内嵌|外挂)(\]|字幕\]| )', self.txt)
        if match:
            return match.group(1)


if __name__ == "__main__":
    debug()
