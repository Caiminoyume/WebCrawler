import requests  # 爬虫请求库
from lxml import etree  # 解析HTML
import datetime
import dataclear as dataclear


def debug():  # 测试用
    a = animeweb(2883)
    a.getanimedata()
    with open('./file/data.txt', "w", encoding="utf") as file:
        for group in a.groups:
            animegroup = animegroupweb(2883, group['ID'])
            animegroup.getvideosdata()
            for i in animegroup.videosdata:
                file.write(i['message'])
                file.write('\n')
                print(i['message'])

    pass


class animeweb:
    def __init__(self, animeID):
        self.animeID = animeID
        self.animehttp = "https://mikanani.me/Home/Bangumi/{}".format(
            self.animeID)  # 指定动漫的网页链接
        self.animeweb = None  # 指定动漫的网页（requests实例）
        self.name = ''  # 番名
        self.date = None  # 放送日期（datetime实例）
        self.episodes = 0  # 总集数
        self.staffhttp = ''  # 官网
        self.bangumihttp = ''  # Bangumi计划链接
        self.groups = []  # 各字幕组名称及ID，每个元素都是一个字典，分别有'name''ID'两个键

        # 各种子，每个元素都是一个字典，分别有'groupname''groupID''magnet''information''filesizes''time''data'七个键
        self.animevideos = []
        self.imagehttp = ''  # 主视觉图链接
        self.image = None  # 主视觉图（requests.content实例）

    class IDnotExist(Exception):
        pass

    def getanimeweb(self):
        try:
            self.animeweb = getweb(self.animehttp)
        except URlmoveError:
            raise animeweb.IDnotExist('该ID的动漫不存在')
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
        self.imagehttp = 'https://mikanani.me{}'.format(picture)  # 获取图片
        for item in html.xpath('//ul[@class="list-unstyled"]/li/span/a'):  # 获取字幕组
            groupdata = {}
            groupdata['name'] = item.xpath('text()')[0]
            groupdata['ID'] = item.xpath('@data-anchor')[0][1:]
            self.groups.append(groupdata)

    def getanimevideos(self):
        if self.groups == []:
            self.getanimedata()
        for group in self.groups:
            animegroup = animegroupweb(self.animeID, group['ID'])
            animegroup.getvideosdata()
            for video in animegroup.videosdata:
                self.animevideos.append({**group, **video})

    def getanimeimage(self):
        if self.imagehttp == "":
            self.getanimedata()
        self.image = requests.get(self.imagehttp).content
        return self.image

    def saveweb(self):
        if self.animeweb == None:
            self.getanimeweb()
        savehtml(self.animeweb, self.animeID)

    def saveimage(self):
        imgfile = './file/images/' + str(self.animeID) + '.jpg'
        if self.image == None:
            self.getanimeimage()
        with open(imgfile, "wb") as file:
            file.write(self.image)


class animegroupweb:
    def __init__(self, animeID, groupID):
        self.animeID = animeID
        self.groupID = groupID
        self.animegrouphttp = "https://mikanani.me/Home/ExpandEpisodeTable?bangumiId={}&subtitleGroupId={}&take=200".format(
            self.animeID, self.groupID)  # 指定动漫和指定字幕组的网页链接
        self.animegroupweb = None  # 指定动漫和指定字幕组的网页（requests实例）

        # 存放一系列视频的信息，其中每个元素都是一个字典，分别有'magnet''filesizes''time''information''data'五个键
        self.videosdata = []

    def getanimegroupweb(self):
        self.animegroupweb = getweb(self.animegrouphttp)
        return self.animegroupweb

    def getvideosdata(self):
        if self.animegroupweb == None:
            self.getanimegroupweb()
        html = etree.HTML(self.animegroupweb.text)
        for item in html.xpath('//tbody/tr'):
            data = {}
            data['magnet'] = item.xpath(
                'td/a[@class="js-magnet magnet-link"]/@data-clipboard-text')[0]
            data['information'] = item.xpath(
                'td/a[@class="magnet-link-wrap"]/text()')[0]
            data['data'] = dataclear.dataclear(data['information'])
            data['filesizes'] = item.xpath('td[2]/text()')[0]
            date, time = item.xpath('td[3]/text()')[0].split()
            year, month, day = map(int, date.split("/"))
            hour, minute = map(int, time.split(":"))
            data['time'] = datetime.datetime(year, month, day, hour, minute)
            self.videosdata.append(data)

    def saveweb(self):
        if self.animegroupweb == None:
            self.getanimegroupweb()
        savehtml(self.animegroupweb, self.animeID)


class URlmoveError(Exception):
    pass


def getweb(http):
    print('正在访问：%s' % http)
    f = requests.get(http)
    if str(f.url) != http:
        raise URlmoveError('服务器将原地址定位到别处')
    return f


def savehtml(html, filename):
    htmlpath = './file/htmls/'
    with open(htmlpath + "%s.html" % filename, "w", encoding="utf") as file:
        file.write(html.text)


if __name__ == "__main__":
    debug()
