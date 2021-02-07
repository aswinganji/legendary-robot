from tkinter import*
from PIL import ImageTk,Image
import os 
from tkinter import filedialog
root = Tk()
root.geometry("1000x1000")
lab = Label(root)


def fun():
    global pointy
    pointy =  filedialog.askopenfilename(title = "Open Image File",filetypes = [("Image Files","*.jpg *.png *.jpeg *.gif")])
    img = Image.open(pointy)
    img2 = ImageTk.PhotoImage(img)
    lab['image'] = img2
    img2.close()

B2 = Button(root,text = "Work",command = fun)



B2.pack()
lab.pack()

root.mainloop()