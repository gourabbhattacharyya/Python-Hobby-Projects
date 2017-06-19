from PIL import Image

img = Image.open("1234.jpg")
area = (10,50,800,950)
cropped_img = img.crop(area)

img.show()
cropped_img.show()