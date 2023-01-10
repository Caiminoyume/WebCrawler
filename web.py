import requests  # 爬虫请求库
from lxml import etree  # 解析HTML
import datetime


class animeweb:
    def __init__(self, animeID):
        self.animeID = animeID
        self.animehttp = "https://mikanani.me/Home/Bangumi/{}".format(
            self.animeID)  # 指定动漫的网页链接
        self.animeweb = None  # 指定动漫的网页
        self.name = None  # 番名
        self.date = None  # 放送日期
        self.episodes = None  # 总集数
        self.staffhttp = None  # 官网
        self.bangumihttp = None  # Bangumi计划链接
        self.groups = None  # 各字幕组ID
        self.imagehttp = None  # 主视觉图链接
        self.image = None  # 主视觉图

    def getanimeweb(self):
        self.animeweb = getweb(self.animehttp)
        return self.animeweb

    def getanimedata(self):
        if self.animeweb == None:
            self.getanimeweb()
        html = etree.HTML(self.animeweb.text)
        self.name = html.xpath('//p[@class="bangumi-title"]/text()')  # 获取番名
        for i in html.xpath('//p[@class="bangumi-info"]/text()'):
            if "放送开始：" in i:
                month, day, year = map(int, i[5:].split("/"))
                self.date = datetime.date(year, month, day)  # 获取时间
            if "总集数：" in i:
                self.episodes = int(i[4:])  # 获取总集数
        self.staffhttp = html.xpath(
            '//p[@class="bangumi-info" and text()="官方网站："]/a/text()')  # 获取官网链接
        self.bangumihttp = html.xpath(
            '//p[@class="bangumi-info" and text()="Bangumi番组计划链接："]/a/text()')  # 获取Bangumi计划链接
        picture = html.xpath(
            '//div[@class="bangumi-poster"]/@style')[0].split("'")[1]
        self.imagehttp = 'https://mikanani.me{}'.format(picture)

    def getanimeimage(self):
        if self.imagehttp == None:
            self.getanimedata()
        self.image = requests.get(self.imagehttp).content
        return self.image

    def saveweb(self):
        savehtml(self.animeweb, self.animeID)


class animegroupweb:
    def __init__(self, animeID, groupID) -> None:
        self.animeID = animeID
        self.groupID = groupID
        self.animegrouphttp = "https://mikanani.me/Home/ExpandEpisodeTable?bangumiId={}&subtitleGroupId={}&take=200".format(
            self.animeID, self.groupID)  # 指定动漫和指定字幕组的网页链接
        self.animegroupweb = None  # 指定动漫和指定字幕组的网页

    def getanimegroupweb(self):
        self.animegroupweb = getweb(self.animegrouphttp)
        return self.animegroupweb


def getweb(http):
    print('正在访问服务器...(目标：%s)' % http)
    f = requests.get(http)
    f.encoding = "utf-8"
    if f.status_code == 200:
        print('已连接')
    else:
        print(f.status_code)
    return f


def savehtml(html, filename):
    htmlpath = '.\\file\\htmls\\'
    with open(htmlpath + "%s.html" % filename, "w", encoding="utf") as file:
        file.write(html.text)
