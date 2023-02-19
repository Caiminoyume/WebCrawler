from qbittorrentapi import Client, LoginFailed


def getqb(config):
    # 获取客户端实例
    qb = Client(host='%s:%s' % (
        config['ip'], config['port']), username=config['user'], password=config['password'])

    # 客户端进行登录
    try:
        qb.auth_log_in()
    except LoginFailed as e:
        print(e)

    # 输出客户端信息
    print(f'qBittorrent: {qb.app.version}')
    print(f'qBittorrent Web API: {qb.app.web_api_version}')
    print()
    return qb


qblogin = {'ip': '192.168.100.1',
           'port': '5080',
           'user': 'admin',
           'password': 'adminadmin'}
getqb(config=qblogin)
