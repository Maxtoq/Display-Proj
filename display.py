import os
import time
import random
import tkinter as tk
from PIL import ImageTk, Image 


def blend(imLabel, imgs, last_img, next_i):
    new_img = ImageTk.PhotoImage(last_img)
    imLabel.config(image=new_img)
    alpha = 0.0
    while alpha < 1:
        alpha += 0.01
        print("blend ", alpha, i, next_i)
        new_img = ImageTk.PhotoImage(Image.blend(last_img, imgs[next_i],alpha))
        imLabel.config(image=new_img)

        window.update_idletasks()
        window.update()
        time.sleep(0.01)

def robot(imLabel, ph_imgs):
    i = 0
    while i < 8:
        imLabel.config(image=ph_imgs[i])
        t = random.uniform(0.05, 0.5)
        time.sleep(t)
        r = random.random()
        if r < 0.6:
            i += 1
        else:
            if i > 0:
                i -= 1
        window.update_idletasks()
        window.update()
    time.sleep(3.0)

# def flicker(imLabel):
#     print(imLabel.place_info(), imLabel.winfo_x(), imLabel.winfo_y())

def get_num(text):
    return int(text[:-4])

def load_imgs(path):
    imgs = []
    ph_imgs = []
    files = os.listdir(path)

    # Sort if only numbers
    names = [f[:-4] for f in files]
    if names[0].isdigit():
        files.sort(key=get_num)

    for file in files:
        if file[-4:] == ".png":
            imgs.append(Image.open(os.path.join(path, file)))
            ph_imgs.append(ImageTk.PhotoImage(imgs[-1]))
    return imgs, ph_imgs


if __name__ == "__main__":
    window = tk.Tk()

    window.attributes('-fullscreen', True)
    window.configure(background="black")

    width= window.winfo_screenwidth()               
    height= window.winfo_screenheight() 

    # imgs = [Image.open(f"vis{i + 1}.png") for i in range(4)]
    # ph_imgs = [ImageTk.PhotoImage(imgs[i]) for i in range(4)]

    vis, ph_vis = load_imgs("vis/")
    rob, ph_rob = load_imgs("robot/")

    imLabel = tk.Label(window, image=ph_vis[0])
    imLabel.pack()

    i = 0
    while True:
        if i < 3:
            last_img = vis[i]
            next_i = i + 1
        else:
            robot(imLabel, ph_rob)
            next_i =  0
        blend(imLabel, vis, last_img, next_i)
        time.sleep(3.0)
        i = next_i