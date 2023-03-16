from tkinter import *
from PIL import ImageTk, Image
import os
import shutil

new_w = 768
new_h = 512

folder_path = f'F:/images/{new_w}x{new_h}/'
index_curr = 0

root = Tk()

image_paths = [x for x in os.listdir(folder_path)]
image_list = [ImageTk.PhotoImage(Image.open(f'{folder_path}{path}')) for path in image_paths]

label = Label(image=image_list[0])
label.grid(row=0, column=1)

def next_image(event):
    global label
    global index_curr
    if index_curr < len(image_list)-1: index_curr += 1
    label = Label(image=image_list[index_curr])
    label.grid(row=0, column=1)


def prev_image(event):
    global label
    global index_curr
    if index_curr > 0: index_curr -= 1
    label = Label(image=image_list[index_curr])
    label.grid(row=0, column=1)
    

def ok_image(e):
    global label
    global index_curr

    folder_in = folder_path
    folder_out = f'F:/images/{new_w}x{new_h}-good/'
    if not os.path.exists(folder_out): os.makedirs(folder_out)
    
    shutil.copy2(f'{folder_in}{image_paths[index_curr]}', f'{folder_out}{image_paths[index_curr]}')
    # os.remove(f'{folder_in}{image_paths[index_curr]}')

    # image_list.pop(index_curr)

    if index_curr < len(image_list)-1: index_curr += 1
    label = Label(image=image_list[index_curr])
    label.grid(row=0, column=1)


button = Button(root, text='<<', command=lambda: prev_image(None))
button.grid(row=1, column=0)
button = Button(root, text='OK', command=lambda: ok_image(None))
button.grid(row=1, column=1)
button = Button(root, text='>>', command=lambda: next_image(None))
button.grid(row=1, column=2)

root.bind('<Right>', next_image)
root.bind('<Left>', prev_image)
root.bind('<space>', ok_image)

root.mainloop()