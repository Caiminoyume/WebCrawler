import qbittorrentapi as qba


def main():
    qb = getqb('192.168.100.1', '5080', 'admin', 'adminadmin')
    # 实例磁链
    magnets = ['magnet:?xt=urn:btih:812a72f0a70c48455ea772d179d1350c03139e93&tr=http%3a%2f%2ft.nyaatracker.com%2fannounce&tr=http%3a%2f%2ftracker.kamigami.org%3a2710%2fannounce&tr=http%3a%2f%2fshare.camoe.cn%3a8080%2fannounce&tr=http%3a%2f%2fopentracker.acgnx.se%2fannounce&tr=http%3a%2f%2fanidex.moe%3a6969%2fannounce&tr=http%3a%2f%2ft.acg.rip%3a6699%2fannounce&tr=https%3a%2f%2ftr.bangumi.moe%3a9696%2fannounce&tr=udp%3a%2f%2ftr.bangumi.moe%3a6969%2fannounce&tr=http%3a%2f%2fopen.acgtracker.com%3a1096%2fannounce&tr=udp%3a%2f%2ftracker.opentrackr.org%3a1337%2fannounce']
    qb.torrents_add(urls=magnets, category="追い付くアニメ")  # 将该磁链加入qb中


def getqb(ip, port, user, pwd):
    # 获取客户端实例
    qb = qba.Client(host='%s:%s' % (ip, port), username=user, password=pwd)

    # 客户端进行登录
    try:
        qb.auth_log_in()
    except qba.LoginFailed as e:
        print(e)

    # 输出客户端信息
    print(f'qBittorrent: {qb.app.version}')
    print(f'qBittorrent Web API: {qb.app.web_api_version}')
    return qb


if __name__ == "__main__":
    main()
