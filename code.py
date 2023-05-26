def fff():
    from PIL import Image, ImageOps, ImageFilter, ImageDraw, ImageFont

    s = Image.open('тузик.jpg')
    s.show()

    print(s.format, s.size, s.palette)

    hor = ImageOps.mirror(s)
    hor.save('гор.jpg')
    ver = ImageOps.flip(s)
    ver.save('вер.jpg')
    hor.show()
    ver.show()

def f():
    from PIL import Image, ImageOps, ImageFilter, ImageDraw, ImageFont
    image1 = Image.open('1.jpeg')
    image2 = Image.open('2.jpeg')
    image3 = Image.open('3.jpg')
    image4 = Image.open('4.jpg')
    image5 = Image.open('5.jpeg')

    e1 = image1.filter(ImageFilter.FIND_EDGES)
    e2 = image2.filter(ImageFilter.FIND_EDGES)
    e3 = image3.filter(ImageFilter.FIND_EDGES)
    e4 = image4.filter(ImageFilter.FIND_EDGES)
    e5 = image5.filter(ImageFilter.FIND_EDGES)

    e1.save('_1.jpg')
    e1.show()
    e2.save('_2.jpg')
    e2.show()
    e3.save('_3.jpg')
    e3.show()
    e4.save('_4.jpg')
    e4.show()
    e5.save('_5.jpg')
    e5.show()
def ff():
    from PIL import Image
    img_path = '1.jpeg'
    watermark_path = 'ii.png'
    img = Image.open(img_path).convert('RGB')
    watermark = Image.open(watermark_path).convert('RGBA')
    watermark = watermark.resize((1200, 800))
    img.paste(watermark, (1, 10), watermark)
    img.save('iii.jpg')
    img.show()
ff()
