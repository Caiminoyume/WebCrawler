import re


def debug():
    with open('./file/0.txt', 'r', encoding='utf-8') as f:
        for l in f:
            print(l, end=' ')
            me = dataclear(l)
            print(me.get(), '\n')


class dataclear:
    def __init__(self, txt):
        self.txt = txt

    def get(self):
        data = []
        data.append(self.getepisode())
        data.append(self.zimuyuyan())
        data.append(self.zimufengzhuang())
        data.append(self.fenbianlv())
        data.append(self.seshen())
        data.append(self.shipinbianmageshi())
        data.append(self.yinpinbianmageshi())
        data.append(self.shipingeshi())
        data.append(self.shipinyuan())
        data.append(self.yuan())
        return data

    def getepisode(self):
        match = re.search(
            r'(\[| |\[第|\[未删减)([0-9]{2}|[0-9]{2}-[0-9]{2})(\]| |集|v2|话)', self.txt)
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

    def fenbianlv(self):
        p720 = re.search(r'(\[| )(720P|1280x720)(\]| |_)', self.txt, re.I)
        p1080 = re.search(r'(\[| )(1080P|1920x1080)(\]| |_)', self.txt, re.I)
        p2160 = re.search(r'(\[| )(4K|3840x2160)(\]| |_)', self.txt, re.I)
        r = ''
        if p720:
            r += '720P'
        if p1080:
            r += '1080P'
        if p2160:
            r += '4K'
        return r

    def seshen(self):
        match = re.search(r'( |\[|-)([0-9]{1,2}bit)(\]| )', self.txt)
        if match:
            return match.group(2)

    def shipinbianmageshi(self):
        hevc = re.search(
            r'( |\[|_)(HEVC|x265|h.265)( |\]|_|-)', self.txt, re.I)
        avc = re.search(
            r'( |\[|_)(AVC|h.264|MPEG-4)( |\]|_|-)', self.txt, re.I)
        av1 = re.search(r'( |\[|_)(AV1)( |\]|_|-)', self.txt, re.I)
        r = ''
        if hevc:
            r += 'HEVC'
        if avc:
            r += 'AVC'
        if av1:
            r += 'AV1'
        return r

    def yinpinbianmageshi(self):
        match = re.search(r'( |\[|_)(AAC|FLAC)( |\]|_)', self.txt, re.I)
        if match:
            return match.group(2)
        # aac = re.search(r'( |\[|_)(AAC)( |\]|_)', self.txt, re.I)
        # flac = re.search(r'( |\[|_)(FLAC)( |\]|_)', self.txt, re.I)

    def shipingeshi(self):
        match = re.search(
            r'( |\[|_)(MKV|MP4)( |\]|_)', self.txt, re.I)
        if match:
            return match.group(2)

    def shipinyuan(self):
        match = re.search(
            r'( |\[|_)(WebRip|BDrip)( |\]|_)', self.txt, re.I)
        if match:
            return match.group(2)

    def yuan(self):
        match = re.search(
            r'( |\[|_)(B-Global|Baha|CR)( |\]|_)', self.txt, re.I)
        if match:
            return match.group(2)


if __name__ == "__main__":
    debug()
