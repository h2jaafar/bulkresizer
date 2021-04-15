from PIL import Image

class resize_single_img: 
    def black_background_thumbnail(path_to_image, thumbnail_size=(300,300)):
        background = Image.new('RGBA', thumbnail_size, "black")    
        source_image = Image.open(path_to_image).convert("RGBA")
        source_image.thumbnail(thumbnail_size)
        (w, h) = source_image.size
        background.paste(source_image, (int((thumbnail_size[0] - w) / 2), int((thumbnail_size[1] - h) / 2 )))
        return background

if __name__ == '__main__':
    path = '/home/hussein/Pictures/HouseExpo_PNGs/final/house_expo_0.png'
    img = black_background_thumbnail(path)
    img.save('tmp.png')
    img.show()
