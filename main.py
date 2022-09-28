import os
import shutil
import matplotlib.pyplot as plt
import cv2
import pathlib
import tkinter as tk
from tkinter import *
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk

file = []
target_dir = r"C:\Users\kolan\PycharmProjects\sliding_windows\bears"


def clicked_open():
    text = selected.get()
    global file
    if text == 0:
        messagebox.showinfo('ERROR', "Ошибка, формат не выбран")
    if text == 1:
        file = filedialog.askopenfilename(filetypes=(("ZIP", "*.zip"), ("all files", "*.*")))
    if text == 2:
        file = filedialog.askdirectory()


def clicked_load():
    if len(file) == 0:
        messagebox.showinfo('ERROR',"Ошибка, файл не выбран")

    i = 0
    for images in os.listdir(file):
        if (images.endswith(".png") or images.endswith(".jpg") or images.endswith(".JPG") or images.endswith(".jpeg")):
            shutil.copy(os.path.join(file, images), target_dir)

    listOfFiles = os.listdir(target_dir)
    countOfFiles = len(listOfFiles)
    os.chdir(target_dir)
    for i in range(0, countOfFiles):
        os.rename(target_dir + "/" + listOfFiles[i], str(i) + '.jpg')

    messagebox.showinfo("Фотографии обработаны")

    # j = 0
    # for images in os.listdir("Bears"):
    #     if (images.endswith(".png") or images.endswith(".jpg") or images.endswith(".jpeg")):
    #         picture = cv2.imread("Bears/"+images)
    #         picture = cv2.cvtColor(picture, cv2.COLOR_BGR2RGB)
    #         pic_box.add_subplot(30, 5, j + 1)
    #         j+=1
    #         plt.imshow(picture)
    #         plt.axis('off')
    # plt.show()

def clicked_save():
    text = save.get()
    global file
    if text == 0:
        messagebox.showinfo('ERROR', "Ошибка, формат не выбран")
    if text == 1:
        print(text)
        text_file = open("result.txt", "w")
        for images in os.listdir(target_dir):
            if (images.endswith(".png") or images.endswith(".jpg") or images.endswith(".jpeg")):
                text_file.write(images)
                text_file.write(" ")

    if text == 2:
        text_file = open("result.csv", "w")
        for images in os.listdir(target_dir):
            if (images.endswith(".png") or images.endswith(".jpg") or images.endswith(".jpeg")):
                text_file.write(images)
                text_file.write(" ")


window = Tk()
window.title("In search of bears...")

canvas = tk.Canvas(window, height=250, width=200)
image = Image.open("МИНПРИРОДЫ.jpg")
photo = ImageTk.PhotoImage(image)
image = canvas.create_image(0, 0, anchor='nw',image=photo)
canvas.place(x=10, y=20)

pic_box = plt.figure(figsize=(16,4))


lbl = Label(window, text="Выберите формат загрузки данных:", font=("Times New Roman", 15), bg='#6fb3f2', fg="white")
lbl.place(x=10, y=200)


selected = IntVar()
rad1 = Radiobutton(window,text='ZIP ФАЙЛ', font=("Times New Roman", 12), value=1, variable=selected)
rad2 = Radiobutton(window,text='ПАПКА С ФОТО',  font=("Times New Roman", 12), value=2, variable=selected)
btn_open = Button(window, text="ВЫБРАТЬ",  font=("Times New Roman", 12), command=clicked_open, width = 20, height = 3 )
rad1.place(x=10, y=240)
rad2.place(x=10, y=260)
btn_open.place(x=10, y=310)
btn_load = Button(window,text='Отправить на проверку', font=("Times New Roman", 12), bg='#6fb3f2', fg="white", command = clicked_load, width = 20, height = 3 )
btn_load.place(x=220, y=310)

# canvas_result = tk.Canvas(window, height=250, width=200)
# canvas_result.place(x=600, y=500)


lbl = Label(window, text="Сохранить результат в:", font=("Times New Roman", 15), bg='#6fb3f2', fg="white")
lbl.place(x=10, y=450)
save = IntVar()
rad3 = Radiobutton(window,text='ТЕКСТОВЙ ФАЙЛ', font=("Times New Roman", 12), value=1, variable=save)
rad4 = Radiobutton(window,text='CSV ФАЙЛ',  font=("Times New Roman", 12), value=2, variable=save)
rad5 = Radiobutton(window,text='ПАПКУ',  font=("Times New Roman", 12), value=3, variable=save)
btn_save = Button(window, text="СОХРАНИТЬ",  font=("Times New Roman", 12), command=clicked_save, width = 20, height = 3 )
rad3.place(x=10, y=490)
rad4.place(x=10, y=520)
rad5.place(x=10, y=550)
btn_save.place(x=10, y=600)

window.geometry('1000x2000')
window.mainloop()
