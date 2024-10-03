from PIL import Image
def PNGtoJPEG():
    inputImg = input("Enter img path: ")
    img = Image.open(inputImg)
    rgb_img = img.convert('RGB')
    rgb_img.save('output_image.jpeg')

def PNGtoGIF():
    inputImg = input("Enter img path: ")
    img = Image.open(inputImg)
    img.save('output_image.gif')

usrInput=input("Enter conversion type: ")

if usrInput=="JPEG":
    PNGtoJPEG()
elif usrInput=="GIF":
    PNGtoGIF()