import requests  # 爬虫请求库
from lxml import etree  # 解析HTML
import ToIco as ico


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
    return "https://mikanani.me/Home/ExpandEpisodeTable?bangumiId={aID}&subtitleGroupId={sID}&take=200".format(
        aID=animeID, sID=subtitleGroupID)  # take：最大条目


def getanime_photo(animeID):
    imgpath = '.\\爬虫\\file\\images\\'
    http = 'https://mikanani.me/Home/Bangumi/{}'.format(animeID)
    anime = gethtml(http)
    html = etree.HTML(anime.text)
    photo = html.xpath(
        '//div[@class="bangumi-poster"]/@style')[0].split("'")[1]
    http_photo = 'https://mikanani.me{}'.format(photo)
    img = requests.get(http_photo).content
    with open(imgpath + photo[-12:], "wb") as file:
        file.write(img)
    ico.start(imgpath+photo[-12:])
