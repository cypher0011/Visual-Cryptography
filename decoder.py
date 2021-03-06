from PIL import Image
#photo one
img1 = Image.open("first_ph.png")
pixels1 = img1.load()
#photo two
img2 = Image.open("second_ph.png")
pixels2 = img2.load()

flag = Image.new("RGB",img1.size)
flagpix = flag.load()

for row in range(img1.size[1]):
    for col in range(img1.size[0]):
        flagpix[col,row]=(
            (pixels1[col,row][0]+pixels2[col,row][0])%256,
            (pixels1[col,row][1]+pixels2[col,row][1])%256,
            (pixels1[col,row][2]+pixels2[col,row][2])%256)
#out_put
flag.save("output.png")
