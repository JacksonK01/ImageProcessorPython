from PIL import Image
import random

image = Image.open( "ImagesFolder/csbsju-logo.jpg")
width = image.width
height = image.height
pixels = image.load()
image.show()

'''
Solve the following exercises; the expected output images are shown in document
ExpectedOutputImages.docx in this exercise subfolder ImagesFolder

Here is how to loop over the pixels of an image
for c in range(width):
    for r in range(height):
        colors = list(pixels[????,????])

'''



'''
1. Uncomment below to make newImage_1 a negative-color-scale copy of old image
     This is done by converting each color to its negative:
     
         new color intensity = 255 - old color intensity for R,G
         and B in each pixel check this out for more details
         https://en.wikipedia.org/wiki/Negative_(photography)

 The following creates a new empty image (all black)
'''
newImage_1 =Image.new("RGB", (width, height))
newPixels_1 = newImage_1.load()

#replace ?? and complete rest of loop body
for c in range(width):
    for r in range(height):
        colors = list(pixels[c,r])
        red = colors[0]
        green = colors[1]
        blue = colors[2]
        colors[0] = 255 - red
        colors[1] = 255 - green
        colors[2] = 255 - blue
        
        
        newPixels_1[c, r] = (tuple(colors))
newImage_1.show()


'''
2. UNCOMMENT CODE BELOW AND make newImage_2 an image of randomly generated RGB pixels
'''
newImage_2 =Image.new("RGB", (width, height))
newPixels_2 = newImage_2.load()

for c in range(width):
    for r in range(height):
        colors[0] = random.randint(0,255)
        colors[1] = random.randint(0,255)
        colors[2] = random.randint(0,255)
        
        newPixels_2[c, r] = (tuple(colors))
newImage_2.show()


'''
3. UNCOMMENT CODE BELOW AND make newImage_3 an image of randomly generated GRAY pixels
'''
newImage_3 =Image.new("RGB", (width, height))
newPixels_3 = newImage_3.load()
#complete rest of loop body
for c in range(width):
    for r in range(height):
        greyScale = random.randint(0,255)
        colors[0] = greyScale
        colors[1] = greyScale
        colors[2] = greyScale
        newPixels_3[c, r] = (tuple(colors))

newImage_3.show()


'''
4. UNCOMMENT CODE BELOW AND make newImage_4 a copy of old image with AS MUCH white converted
   to black. Experitment with thresholds to eliminate as much of the white as possible
'''
newImage_4 =Image.new("RGB", (width, height))
newPixels_4 = newImage_4.load()

for c in range(width):
    for r in range(height):
        colors = list(pixels[c,r])
        red = colors[0]
        green = colors[1]
        blue = colors[2]
        #ONLY replace ?? below
        if(red > 200 and blue > 200 and green > 200):
            newPixels_4[c, r] = (0, 0, 0)
        else:
            newPixels_4[c, r] = (red, green, blue)

newImage_4.show()


'''
5. UNCOMMENT CODE BELOW AND flip image vertically: make newImage_5 a VERTICAL mirror
    image of old image.
'''
newImage_5 =Image.new("RGB", (width, height))
newPixels_5 = newImage_5.load()

for c in range(width):
    for r in range(height):
        #ONLY replace ?? below
        vertical = height - 1 - c
        newPixels_5[c, r] = pixels[vertical, r]
        
newImage_5.show()



'''
6.  UNCOMMENT CODE BELOW AND flip image diagonally: make newImage_6 a VERTICAL & HORIZONTAL
    mirror image of old image
'''
newImage_6 =Image.new("RGB", (width, height))
newPixels_6 = newImage_6.load()
for c in range(width):
    for r in range(height):
        #ONLY replace ?? below
        vertical = height - 1 - c
        horizontal = width - 1 - r
        newPixels_6[c, r] = pixels[vertical, horizontal]

newImage_6.show()
