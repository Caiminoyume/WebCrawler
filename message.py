import re


def debug():
    me = dataclear(
        '[织梦字幕组][别当欧尼酱了 お兄ちゃんはおしまい][04集][1080P][AVC][繁日双语]')
    a = me.getepisode()
    print(a)


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

    def getepisode(self):  # 取集数
        rules = [
            '\[[0-9]{2}\]',
            ' [0-9]{2} ',
            '\[[0-9]{2}集\]',
            '\[[0-9]{2}v2\]',
            ' [0-9]{2}v2 ',
            '\[第[0-9]{2}话\]'
        ]
        return self.rerules(rules, '[0-9]{2}')

    def zimuyuyan(self):  # 字幕语言
        rules = [
            '\[[简繁日英]{1,3}',
            '\[CH[ST]\]',
            '\[GB\]',
            '\[BIG5\]'
        ]
        return self.rerules(rules)

    def zimufengzhuang(self):  # 字幕封装方式
        rules = [
            '内[封嵌]\]',
            '内[封嵌]字幕\]',
            '内[封嵌] ',
            '外挂\]',
            '外挂 ',
            '外挂\]',
        ]


if __name__ == "__main__":
    debug()
