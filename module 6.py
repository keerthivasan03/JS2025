from PIL import Image
im = Image.open("example.jpg")
new_im = im.resize((640,480))
new_im.save("example_resized.jpg")
from PIL import Image
im = Image.open("example.jpg")
new_im = im.rotate(90)
new_im.save("example_rotated.jpg")
from PIL import Image
im = Image.open("example.jpg")
im.rotate(180).resize((640,480)).save("flipped_and_resized.jpg")
#!/usr/bin/env python3


import os
from PIL import Image

old_path = os.path.expanduser('~') + '/images/'
new_path = '/opt/icons/'
		
for image in os.listdir(old_path):
    if not image.startswith('.'):  # ✅ Skips hidden files correctly
        img = Image.open(os.path.join(old_path, image))
        
        filename = os.path.splitext(image)[0]  # ✅ Extracts filename correctly
        
        img.rotate(-90).resize((128, 128)).convert("RGB").save(os.path.join(new_path, filename + ".jpeg"), 'JPEG')
        img.close()
