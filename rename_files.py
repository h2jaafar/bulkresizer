import os 


def main():
   i = 0
   path="/home/ADD_PATH_HERE"

   for filename in os.listdir(path):
      my_dest =str(i) + ".png"
      my_source =path + filename
      my_dest =path + my_dest
      # rename() function will
      # rename all the files
      os.rename(my_source, my_dest)
      i += 1


if __name__ == '__main__':
   # Calling main() function
   main()
