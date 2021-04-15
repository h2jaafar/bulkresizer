from PIL import Image

def make_square(im, base_width, fill_color=(0, 0, 0, 0)):
    x, y = im.size
    print("Image size =", x,y)
    wpercent = float(base_width)/float(max(x,y))
    hsize = int(float(y)*wpercent)
    x,y = base_width,hsize
    print("new image size with aspect ratio = ", x, y)
    im = im.resize((x,y),Image.ANTIALIAS)
    print(im.size)
    #size = max(min_size, x, y)
    size = base_width
    new_im = Image.new('RGBA', (size, size), fill_color)
    print(new_im.size)
    new_im.paste(im, ((int((size - x) / 2), int((size - y) / 2))))
    return new_im
    
 
img = Image.open('/home/hussein/Pictures/HouseExpo_PNGs/100/house_expo_0.png')
image_resized = make_square(img,300)

img.save('house_expo_52_resized2.png') 
