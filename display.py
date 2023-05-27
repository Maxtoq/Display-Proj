
import time
import tkinter as tk
from PIL import ImageTk, Image 


def blend(imLabel, imgs, i, next_i):
    new_img = ImageTk.PhotoImage(imgs[i])
    imLabel.config(image=new_img)
    alpha = 0.0
    while alpha < 1:
        alpha += 0.01
        print("blend ", alpha, i, next_i)
        new_img = ImageTk.PhotoImage(Image.blend(imgs[i],imgs[next_i],alpha))
        imLabel.config(image=new_img)

        window.update_idletasks()
        window.update()
        time.sleep(0.01)

if __name__ == "__main__":
    window = tk.Tk()

    window.attributes('-fullscreen', True)
    window.configure(background="black")

    width= window.winfo_screenwidth()               
    height= window.winfo_screenheight() 

    imgs = [Image.open(f"vis{i + 1}.png") for i in range(4)]
    ph_imgs = [ImageTk.PhotoImage(imgs[i]) for i in range(4)]
    imLabel = tk.Label(window, image=ph_imgs[0])
    imLabel.pack()

    i = 0
    while True:
        # Position image
        print(i, ph_imgs[i])
        imLabel.config(image=ph_imgs[i])

        window.update_idletasks()
        window.update()
        time.sleep(30)

        next_i = i + 1 if i < 3 else 0

        blend(imLabel, imgs, i, next_i)
        i = next_i