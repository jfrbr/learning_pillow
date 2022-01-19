from PIL import Image, ImageFilter
import os

def main():

#    cwd = os.getcwd()
#    print(cwd)

    im = Image.open("../assets/images/yellow-italian-car.jpg")
    print(im.format, im.size, im.mode)

    out = im.filter(ImageFilter.DETAIL)
    out.save("../assets/images/yellow-italian-car-filtered.jpg")

    box = (100, 100, 400, 400)
    region = im.crop(box)
    region.save("../assets/images/yellow-italian-car-cropped.jpg")


if __name__ == "__main__":
    main()