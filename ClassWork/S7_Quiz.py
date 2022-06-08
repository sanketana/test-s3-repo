from tkinter import *
from PIL import ImageTk, Image


window = Tk()
window.title('Quiz App')
window.geometry('640x360')
#window.iconbitmap('quiz.ico')
img = Image.open('screen1_bg.jpg')
img_tk = ImageTk.PhotoImage(img)
img_lbl = Label(window, image=img_tk)






img_lbl.pack()

window.mainloop()