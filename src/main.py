from PIL import Image, ImageFilter, ImageDraw, ImageFont
import os

def main():

    im = Image.open("../assets/images/yellow-italian-car.jpg")
    
    print(im.format, im.size, im.mode)

    out = im.filter(ImageFilter.DETAIL)
    out.save("../assets/images/yellow-italian-car-filtered.jpg")

    box = (100, 100, 400, 400)
    region = im.crop(box)
    region.save("../assets/images/yellow-italian-car-cropped.jpg")

    blurred = im.filter(ImageFilter.BLUR)
    blurred.save("../assets/images/yellow-italian-car-blurred.jpg")

    idraw = ImageDraw.Draw(im)
    text = "Put your text here"

    #font = ImageFont.truetype("arial.ttf", size=18)
    idraw.text((im.size[0]/2,im.size[1]/2), text)

    im.save("../assets/images/yellow-italian-car-watermark.jpg")


    grayscale = im.convert('L')
    grayscale.save("../assets/images/yellow-italian-car-grayscale.jpg")




if __name__ == "__main__":
    main()