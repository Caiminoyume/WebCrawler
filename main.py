# 输入要求：（起始animeID，终止animeID）；作用：将anime的基本信息保存在animeID.xlsx中
from getanimes import getanimesdata
from getIco import getanime_photo


def main():
    #getanimesdata(2882, 3000)
    getanime_photo(2833)


if __name__ == '__main__':
    main()
