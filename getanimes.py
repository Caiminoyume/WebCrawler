from OperateXlsx import animeId
from OperateHtml import getanime
from animedata import animemegress


def getanimesdata(l, r):  # 总番剧数：2879
    xlsx = animeId('.\\file\\animeID.xlsx')
    # xlsx.ws.append(['アニメID', 'アニメ名', '放送时间', '官方网站'])
    for animeID in range(l, r+1):
        listt = [animeID]
        html = getanime(animeID)
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
