darkBlue = (0, 51, 76)
red = (217, 26, 33)
lightBlue = (112, 150, 158)
yellow = (252, 227, 166)

from PIL import Image # importing image from file

im = Image.open("selfie.png") # defining new image name


new_image = Image.new(im.mode, im.size) # creating a copy of the Image
new_image.save("output.jpg", "jpeg") #saves the new image

colorpixels = list(im.getdata()) #compiles data into a list
list_length = len(colorpixels)#returns sequence length in a string

for i in range(list_length):
    red1 = colorpixels[i][0]
    blue2 = colorpixels[i][1]
    green3 = colorpixels[i][2]
    sum = red1 + blue2 + green3 #takes each individual pixel color and adds them together

    print(sum) #prints out the cum of each pixel in the list and prints out color based on what the sum is
    if sum < 182:
        colorpixels[i] = darkBlue
    elif sum >= 182 and sum < 360:
        colorpixels[i] = red
    elif sum >= 360 and sum < 546:
        colorpixels[i] = lightBlue
    else:
        colorpixels[i] = yellow
im.putdata(colorpixels)

im.show()
