
import time
import tkinter as tk
from PIL import ImageTk, Image 


if __name__ == "__main__":
    window = tk.Tk()

    window.attributes('-fullscreen', True)
    window.configure(background="white")

    width= window.winfo_screenwidth()               
    height= window.winfo_screenheight() 

    imgs = [ImageTk.PhotoImage(Image.open(f"vis{i + 1}.png")) for i in range(4)]
    imLabel = tk.Label(window, image=imgs[0])
    imLabel.pack()

    i = 0
    while True:
        # Position image
        print(i, imgs[i])
        imLabel.config(image=imgs[i])
        i = i + 1 if i < 3 else 0

        window.update_idletasks()
        window.update()
        time.sleep(1)