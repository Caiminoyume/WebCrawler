from PIL import Image
from web import animeweb


def main():  # 测试用
    aimg = animeimage(2833)
    aimg.getico()


class animeimage:
    def __init__(self, animeID):
        self.animeID = animeID
        self.imgfile = '.\\file\\images\\' + str(self.animeID) + '.jpg'
        self.icopath = '.\\file\\icos\\'

    def getimage(self):
        anime = animeweb(self.animeID)
        img = anime.getanimeimage()
        with open(self.imgfile, "wb") as file:
            file.write(img)

    def getico(self):
        try:
            im = Image.open(self.imgfile)
        except FileNotFoundError:
            self.getimage()
        width, height = im.size  # 获取图片宽和高
        max_edge = max(width, height)  # 计算最大边长
        canvas = Image.new('RGBA', (max_edge, max_edge),
                           (0, 0, 0, 0))  # 创建一个透明画布
        canvas.paste(im, ((max_edge - width) // 2,
                          (max_edge - height) // 2))  # 将图片粘贴到画布上
        im_512 = canvas.resize((256, 256))  # 将图片转换为256*256
        im_512.save(self.icopath + '主视觉图.ico')  # 保存ico图标


if __name__ == "__main__":
    main()
