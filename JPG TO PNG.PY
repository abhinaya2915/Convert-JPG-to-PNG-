from PIL import Image

img = Image.open("dog.jpg")
img.save("dog1.png")
print("Successfully Converted (JPG --> PNG)")
