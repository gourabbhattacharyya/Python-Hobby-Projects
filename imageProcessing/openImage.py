from PIL import Image

img = Image.open("1234.jpg")
print(img.size)
print(img.format)

img.show()