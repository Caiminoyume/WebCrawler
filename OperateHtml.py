import requests  # 爬虫请求库
from lxml import etree  # 解析HTML


def gethtml(http):
    f = requests.get(http)
    f.encoding = "utf-8"
    print(f.status_code)
    return f


def savehtml(f):
    with open("anime.html", "w", encoding="utf") as file:
        file.write(f.text)


def openfilehtml(inhtml):
    return etree.parse(inhtml, etree.HTMLParser())  # 读取文件解析


def getsubanime(animeID, subtitleGroupID):
    Ahttp = "https://mikanani.me/Home/ExpandEpisodeTable?bangumiId={aID}&subtitleGroupId={sID}&take=200".format(
        aID=animeID, sID=subtitleGroupID)  # take：最大条目
    return gethtml(Ahttp)


def getanime(animeID):
    Ahttp = "https://mikanani.me/Home/Bangumi/{aID}".format(aID=animeID)
    return gethtml(Ahttp)


def getphoto(inhtml):
    html = etree.HTML(inhtml.text)
    photo = html.xpath(
        '//div[@class="bangumi-poster"]/@style')[0].split("'")[1]
    http_photo = 'https://mikanani.me{}'.format(photo)
    img = requests.get(http_photo).content
    return img
