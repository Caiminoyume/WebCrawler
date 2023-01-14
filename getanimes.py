from OperateXlsx import animeIds
from web import animeweb
from animedata import animemegress


def getanimesdata(l, r):  # 总番剧数：2879
    xlsx = animeIds('.\\file\\animeID.xlsx')
    # xlsx.ws.append(['アニメID', 'アニメ名', '放送时间', '官方网站'])
    for animeID in range(l, r+1):
        listt = [animeID]
        anime = animeweb(animeID)
        html = anime.getanimeweb()
        l = animemegress(html)
        if (l == None):
            continue
        listt.extend(l)
        xlsx.ws.append(listt)
        print(listt)
        if animeID % 10 == 0:
            xlsx.wb.save('.\\file\\animeID.xlsx')
            print('保持成功！')
    xlsx.wb.save('.\\file\\animeID.xlsx')
    print('全部完成！')