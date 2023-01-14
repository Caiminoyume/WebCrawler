# 输入要求：（起始animeID，终止animeID）；作用：将anime的基本信息保存在animeID.xlsx中
from getanimes import getanimesdata
# 输入要求：（animeID）；作用，获得番的主视觉图.ico
from getico import saveanimeimage
from web import animeweb
from web import animegroupweb


def main():
    a = animegroupweb(2822, 48)
    a.getvideosdata()
    print(a.videosdata)


if __name__ == '__main__':
    main()
