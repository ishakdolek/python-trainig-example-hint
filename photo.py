from PIL import Image

image=Image.open("t.jpg")

image.convert(mode="L").save()

image.show()