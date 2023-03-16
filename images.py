import os

from PIL import Image, ImageDraw, ImageFont, ImageEnhance, ImageColor

def image_resize_crop(image, new_w, new_h):
    w, h = image.size
    if w < h: image = image.resize((new_w, int(h * new_w/w)))
    else: image = image.resize((int(w * new_h/h), new_h))
    
    w, h = image.size
    if w < new_w or h < new_h:
        if w > h: image = image.resize((new_w, int(h * new_w/w)))
        else: image = image.resize((int(w * new_h/h), new_h))

    w, h = image.size
    image = image.crop((w//2-new_w//2, h//2-new_h//2, w//2+new_w//2, h//2+new_h//2))
    
    return image


def generate_image(filename, new_w, new_h):
    image = Image.open(f'F:\\images\\original\\{filename}')
    # image = Image.open('01.jpg')

    folder_path = f'F:\\images\\{new_w}x{new_h}\\'
    # folder_path = f'images\\{new_w}x{new_h}\\'
    if not os.path.exists(folder_path): os.makedirs(folder_path)

    image = image_resize_crop(image, new_w, new_h)

    export_name = filename.replace('.', f'-{new_w}x{new_h}.')
    image.save(f'{folder_path}/{export_name}')


def generate_images():
    for filename in os.listdir('F:\\images\\original\\'):
        try: generate_image(filename, 768, 512)
        except: print(filename)
        # try: generate_image(filename, 1000, 1500)
        # except: print(filename)
        # try: generate_image(filename, 1920, 1080)
        # except: print(filename)
        
generate_images()