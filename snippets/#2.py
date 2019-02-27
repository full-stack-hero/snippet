# In our last example for today, we will show how you can apply the "contour"
# filter to your image. The code below will take our image and apply
from PIL import Image, ImageFilter

im = Image.open("image.png")
im = im.filter(ImageFilter.CONTOUR)

im.save("image.jpg")
