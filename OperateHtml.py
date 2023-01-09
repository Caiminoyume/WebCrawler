import requests  # 爬虫请求库
from lxml import etree  # 解析HTML


class animeweb:
    def __init__(self, animeID, groupID=None) -> None:
        self.animeID = animeID
        self.groupID = groupID
        self.Ahttp = "https://mikanani.me/Home/Bangumi/{}".format(self.animeID)
        self.AGhttp = "https://mikanani.me/Home/ExpandEpisodeTable?bangumiId={}&subtitleGroupId={}&take=200".format(
            self.animeID, self.groupID)  # take：最大条目

    def getanimeweb(self):
        return gethtml(self.Ahttp)

    def getanimegroupweb(self):
        return gethtml(self.AGhttp)

    def getanimephoto(self):
        html = etree.HTML(self.getanimeweb().text)
        photo = html.xpath(
            '//div[@class="bangumi-poster"]/@style')[0].split("'")[1]
        http_photo = 'https://mikanani.me{}'.format(photo)
        img = requests.get(http_photo).content
        return img


def gethtml(http):
    f = requests.get(http)
    f.encoding = "utf-8"
    print(f.status_code)
    return f


def savehtml(f):
    with open("anime.html", "w", encoding="utf") as file:
        file.write(f.text)


def openfilehtml(inhtmlfile):
    return etree.parse(inhtmlfile, etree.HTMLParser())  # 读取文件解析
