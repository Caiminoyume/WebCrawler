import re


def debug():
    with open('./file/0.txt', 'r', encoding='utf-8') as f:
        for l in f:
            print(l, end=' ')
            me = dataclear(l)
            # print(me.get(), '\n')
            print('剧集：', me.episode,
                  '字幕语言：', me.subtitle_language,
                  '字幕封装：', me.subtitle_encapsulation,
                  '清晰度：', me.definition,
                  '位深：', me.bit_depth,
                  '视频编码格式：', me.video_encoding,
                  '音频编码格式：', me.audio_encoding,
                  '视频文件格式：', me.video_format,
                  '视频源：', me.video_source,
                  '网络源：', me.video_net_source,
                  '\n'
                  )


class dataclear:
    def __init__(self, video_information):
        self.video_inf = video_information
        self.get_episode()  # 剧集
        self.get_subtitle_language()  # 字幕语言
        self.get_subtitle_encapsulation()  # 字幕封装
        self.get_definition()  # 清晰度
        self.get_bit_depth()  # 位深
        self.get_video_encoding()  # 视频编码格式
        self.get_audio_encoding()  # 音频编码格式
        self.get_video_format()  # 视频文件格式
        self.get_video_source()  # 视频源
        self.get_video_net_source()  # 网络源

    def get_episode(self):  # 剧集
        self.episode = '/'
        episode = re.search(
            r'( |\[第?未?删?减?)([0-9]{2}|[0-9]{2}-[0-9]{2})(\]| |集|v2|话)', self.video_inf)
        if episode:
            self.episode = episode.group(2)

    def get_subtitle_language(self):  # 字幕语言
        self.subtitle_language = '/'
        sc = re.search(r'(\[| )(简|CHS|GB)', self.video_inf, re.I)
        tc = re.search(r'(\[| )简?(繁|CHT|BIG5)', self.video_inf, re.I)
        jp = re.search(r'(\[| )简?繁?(日)', self.video_inf, re.I)
        eng = re.search(r'(\[| )简?繁?日?(英)', self.video_inf, re.I)
        r = ''
        if sc:
            r += '简'
        if tc:
            r += '繁'
        if jp:
            r += '日'
        if eng:
            r += '英'
        if r:
            self.subtitle_language = r

    def get_subtitle_encapsulation(self):  # 字幕封装方式
        self.subtitle_encapsulation = '/'
        subtitle_encapsulation = re.search(
            r'(内封|内嵌|外挂)(\]|字幕\]| )', self.video_inf)
        if subtitle_encapsulation:
            self.subtitle_encapsulation = subtitle_encapsulation.group(1)

    def get_definition(self):  # 清晰度
        self.definition = '/'
        _720p = re.search(r'(\[| )(720P|1280x720)(\]| |_)',
                          self.video_inf, re.I)
        _1080p = re.search(
            r'(\[| )(1080P|1920x1080)(\]| |_)', self.video_inf, re.I)
        _4k = re.search(r'(\[| )(4K|3840x2160)(\]| |_)',
                        self.video_inf, re.I)
        r = ''
        if _720p:
            r += '720P'
        if _1080p:
            r += '1080P'
        if _4k:
            r += '4K'
        if r:
            self.definition = r

    def get_bit_depth(self):  # 位深
        self.bit_depth = '/'
        bit_depth = re.search(r'( |\[|-)([0-9]{1,2}bit)(\]| )', self.video_inf)
        if bit_depth:
            self.bit_depth = bit_depth.group(2)

    def get_video_encoding(self):  # 视频编码格式
        self.video_encoding = '/'
        hevc = re.search(
            r'( |\[|_)(HEVC|x265|h.265)( |\]|_|-)', self.video_inf, re.I)
        avc = re.search(
            r'( |\[|_)(AVC|h.264|MPEG-4)( |\]|_|-)', self.video_inf, re.I)
        av1 = re.search(r'( |\[|_)(AV1)( |\]|_|-)', self.video_inf, re.I)
        r = ''
        if hevc:
            r += 'HEVC'
        if avc:
            r += 'AVC'
        if av1:
            r += 'AV1'
        if r:
            self.video_encoding = r

    def get_audio_encoding(self):  # 音频编码格式
        self.audio_encoding = '/'
        audio_encoding = re.search(
            r'( |\[|_)(AAC|FLAC)( |\]|_)', self.video_inf, re.I)
        if audio_encoding:
            self.audio_encoding = audio_encoding.group(2)

    def get_video_format(self):  # 视频文件格式
        self.video_format = '/'
        video_format = re.search(
            r'( |\[|_)(MKV|MP4)( |\]|_)', self.video_inf, re.I)
        if video_format:
            self.video_format = video_format.group(2)

    def get_video_source(self):  # 视频源
        self.video_source = '/'
        video_source = re.search(
            r'( |\[|_)(WebRip|BDrip)( |\]|_)', self.video_inf, re.I)
        if video_source:
            self.video_source = video_source.group(2)

    def get_video_net_source(self):  # 网络源
        self.video_net_source = '/'
        video_net_source = re.search(
            r'( |\[|_)(B-Global|Baha|CR)( |\]|_)', self.video_inf, re.I)
        if video_net_source:
            self.video_net_source = video_net_source.group(2)
            self.video_source = 'WebRip'


if __name__ == "__main__":
    debug()
