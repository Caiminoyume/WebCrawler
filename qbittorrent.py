import qbittorrentapi as qba
import web as animeweb
from configparser import ConfigParser
import dataclear

cfg = ConfigParser()
cfg.read('./config/qbittorrent.ini')


def debug():
    # qb = getqb(**dict(cfg.items('server')))
    # # 实例磁链
    # magnets = ['magnet:?xt=urn:btih:812a72f0a70c48455ea772d179d1350c03139e93&tr=http%3a%2f%2ft.nyaatracker.com%2fannounce&tr=http%3a%2f%2ftracker.kamigami.org%3a2710%2fannounce&tr=http%3a%2f%2fshare.camoe.cn%3a8080%2fannounce&tr=http%3a%2f%2fopentracker.acgnx.se%2fannounce&tr=http%3a%2f%2fanidex.moe%3a6969%2fannounce&tr=http%3a%2f%2ft.acg.rip%3a6699%2fannounce&tr=https%3a%2f%2ftr.bangumi.moe%3a9696%2fannounce&tr=udp%3a%2f%2ftr.bangumi.moe%3a6969%2fannounce&tr=http%3a%2f%2fopen.acgtracker.com%3a1096%2fannounce&tr=udp%3a%2f%2ftracker.opentrackr.org%3a1337%2fannounce']
    # qb.torrents_add(urls=magnets, category="追い付くアニメ")  # 将该磁链加入qb中
    anime = oitsukeanime(2883)
    magnets = anime.get_anime_episode('09')
    print(*magnets, sep='\n')
    # anime.add_magnet(magnets)


def get_qb(host, port, username, password):
    # 获取客户端实例
    qb = qba.Client('%s:%s' % (host, port), username, password)

    # 客户端进行登录
    try:
        qb.auth_log_in()
    except qba.LoginFailed as e:
        print(e)

    # 输出客户端信息
    print(f'qBittorrent: {qb.app.version}')
    print(f'qBittorrent Web API: {qb.app.web_api_version}')
    return qb


class oitsukeanime:
    def __init__(self, animeID):
        self.qb = get_qb(**dict(cfg.items('server')))
        self.animeID = animeID
        self.anime = animeweb.animeweb(animeID)
        self.anime.getanimevideos()

    def get_anime_episode(self, episode):
        magnets = []
        for video in self.anime.animevideos:
            if video['data'].episode == episode:
                magnets.append(video['magnet'])
        return magnets

    def add_magnet(self, magnets):
        self.qb.torrents_add(urls=magnets, category="追い付くアニメ")


if __name__ == "__main__":
    debug()
