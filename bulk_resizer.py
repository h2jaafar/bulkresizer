from resize_v3 import resize_single_img
import os 

def main():
    path_main = './30_maps/'
    counter = 0
    for filename in os.listdir(path_main):
        path = './png/' + filename
        img = resize_single_img.black_background_thumbnail(path,(100,100))
        img.save('./resized/' + str(counter) + '.png')
        counter +=1
        print("Saved : " + str(counter) + '.png')

main()
