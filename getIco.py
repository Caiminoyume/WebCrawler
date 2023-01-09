from PIL import Image
from OperateHtml import animeweb


def toico(infile):
    im = Image.open(infile)
    width, height = im.size  # 获取图片宽和高
    max_edge = max(width, height)  # 计算最大边长
    canvas = Image.new('RGBA', (max_edge, max_edge), (0, 0, 0, 0))  # 创建一个透明画布
    canvas.paste(im, ((max_edge - width) // 2,
                      (max_edge - height) // 2))  # 将图片粘贴到画布上
    im_512 = canvas.resize((256, 256))  # 将图片转换为256*256
    im_512.save('主视觉图.ico')  # 保存ico图标


def getanime_photo(animeID):
    imgpath = '.\\file\\images\\'
    anime = animeweb(animeID)
    img = anime.getanimephoto()
    with open(imgpath + str(animeID) + '.jpg', "wb") as file:
        file.write(img)
    toico(imgpath + str(animeID) + '.jpg')
