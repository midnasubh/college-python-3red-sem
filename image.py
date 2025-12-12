from PIL import Image
image=Image.open("mm.jpg")
filp_H=image.transpose(Image.FLIP_LEFT_RIGHT)
filp_H.save("filpmm.jpg")
image.show()
filp_H.show()

# from PIL import Image
# image=Image.open("mm.jpg")
# filp_v=image.transpose(Image.FLIP_TOP_BOTTOM)
# filp_v.save("filpmm1.jpg")
# image.show()
# filp_v.show()