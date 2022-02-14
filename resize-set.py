from PIL import Image
import os

# change workdir 
print(os.getcwd())
os.chdir("./dataset")

test_image = "0.png"
original = Image.open(test_image)

# Get dimensions
width, height = original.size
left = width/4
top = height/4
right = 3 * width/4
bottom = 3 * height/4
cropped_example = original.crop((left, top, right, bottom))

outname = f"{test_image[:-4]}a.png"
cropped_example.save(outname)
print(outname)