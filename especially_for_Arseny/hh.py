from PIL import Image

im = Image.open('lampa.jpg')
im = im.crop((600, 300, 800, 420)).rotate(180)
im.save('hh.jpg')
im.show()
