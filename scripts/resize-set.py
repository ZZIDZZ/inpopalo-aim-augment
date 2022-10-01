from PIL import Image
import os

# change workdir 
print(os.getcwd())
os.chdir("./dataset")

def resize(image):
    original = Image.open(image)
    # Get dimensions
    width, height = original.size
    left = width/2.5
    top = height/3
    right = 3 * width/5
    bottom = 2 * height/3
    return original.crop((left, top, right, bottom))

for f in os.listdir():
    if "r" in f:
        continue
    elif os.path.isfile(f):
        resized = resize(f)
        outname = f"{f[:-4]}r.png"
        resized.save(outname)
        print(f)
