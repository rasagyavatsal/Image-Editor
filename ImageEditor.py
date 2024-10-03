from PIL import Image
inputImg = input("Enter img path: ")
img = Image.open(inputImg)

def convert_to_JPEG():
    format=img.format  
    if format=="PNG":
        rgb_img = img.convert('RGB')
        rgb_img.save('output_image.jpeg')
    elif format=="GIF":
        img.save('output_image.gif')
    elif format=="WEBP":
        img.save("output_image.webp")

def convert_from_JPEG():
    format_to_convert=input("Enter which format to convert(PNG/GIF): ")
    if format_to_convert=="PNG":
        img.save("output_image.png")
    if format_to_convert=="GIF":
        img.save("output_image.GIF")