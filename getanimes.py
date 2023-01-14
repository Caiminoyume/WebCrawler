from OperateXlsx import animeIDs
from web import animeweb
from web import IDnotExist


def getanimesdata(l, r):  # 总番剧数：2879
    xlsx = animeIDs('.\\file\\animeID.xlsx')
    # xlsx.ws.append(['アニメID', 'アニメ名', '放送时间', '官方网站'])
    for animeID in range(l, r+1):
        listt = [animeID]
        anime = animeweb(animeID)
        try:
            anime.getanimeweb()
        except IDnotExist:
            continue
        listt.append(anime.name)
        listt.append(anime.date)
        listt.append(anime.staffhttp)
        xlsx.ws.append(listt)
        print(listt)
        if animeID % 10 == 0:
            xlsx.wb.save('.\\file\\animeID.xlsx')
            print('保持成功！')
    xlsx.wb.save('.\\file\\animeID.xlsx')
    print('全部完成！')


if __name__ == "__main__":
    pass
    # getanimesdata(1, 1)
