from lxml import etree  # 解析HTML


class named:
    def __init__(self, name):
        self.name = name

    def 语言(self):
        zimus = [['简', 'GB', 'CHS'], ['繁', 'BIG5', "CHT"], ['日', 'JP'], ['英']]
        out = ""
        for i in zimus:
            for j in i:
                if j in self.name:
                    out += i[0]
                    break
        if out == '':
            out = '/'
        return out

    def 集数(self):
        yuyans = ['01', '02', '03', '04', '05',
                  '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26']
        for i in yuyans:
            if "["+i in self.name or "- "+i in self.name or "["+str(int(i))+"]" in self.name:
                return i

    def 字幕(self):
        zimus = ['内嵌', '内封', '外挂']
        for i in zimus:
            if i in self.name:
                return i
        return '/'

    def pip(self):
        pips = [['1080p', '1920x1080', '1080P'], [
            '720p', '720P'], ['4K', '3840x2160']]
        for i in pips:
            for j in i:
                if j in self.name:
                    return i[0]
        return '/'

    def rip(self):
        rips = [['网络', 'Web', 'WEB']]
        for i in rips:
            for j in i[1:]:
                if j in self.name:
                    return i[0]
        return '/'

    def 格式(self):
        geshis = [['mp4', 'MP4'], ['mkv', 'MKV']]
        for i in geshis:
            for j in i[1:]:
                if j in self.name:
                    return i[0]
        return '/'


def animevideomegress(inhtml):
    html = etree.HTML(inhtml.text)
    output = []
    cilian = html.xpath(
        '//tbody/tr/td/a[@class="js-magnet magnet-link"]/@data-clipboard-text')
    name = html.xpath('//tbody/tr/td/a[@class="magnet-link-wrap"]/text()')
    size = html.xpath('//tr/td[2]/text()')
    time = html.xpath('//tr/td[3]/text()')
    for i in range(len(name)):
        row = named(name[i])
        output.append([row.集数(),  # 取集数
                       row.语言(),  # 取字幕语言
                       row.字幕(),  # 取字幕封装方法
                       row.pip(),  # 取视频清晰度
                       row.rip(),  # 取视频来源
                       row.格式(),  # 取视频格式
                       time[i], size[i], cilian[i]])
    return output


def animemegress(inhtml):
    html = etree.HTML(inhtml.text)
    listt = html.xpath('//p[@class="bangumi-title"]/text()')  # 获取番名
    if (listt):
        l = html.xpath('//p[@class="bangumi-info"]/text()')
        for i in l:
            if "放送开始：" in i:
                day, mouth, year = i[5:].split("/")
                listt.append("{}/{}/{}".format(year, mouth, day))  # 获得时间
        listt.extend(html.xpath(
            '//p[@class="bangumi-info" and text()="官方网站："]/a/text()'))  # 获取官网链接
        return listt
