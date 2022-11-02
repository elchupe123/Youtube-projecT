from tkinter import *
from tkinter import filedialog
from moviepy import *
from moviepy.editor import VideoFileClip
from pytube import  YouTube

import shutil


def select_path():
    path = filedialog.askdirectory()
    path_label.config(text=path)

def download_file():
    get_link = link_field.get()
    user_path = path_label.cget("text")
    screen.title('Descargando...')
    mp4_video = YouTube(get_link).streams.get_highest_resolution().download()
    vid_clip = VideoFileClip(mp4_video)
    vid_clip.close()
    shutil.move(mp4_video, user_path)
    screen.title('Descarga Completada! ')




screen = Tk()
title = screen.title("Descargador de Videos")
canvas = Canvas(screen, width=500, height=500)
canvas.pack()

logo_img = PhotoImage(file='yt.png')
logo_img = logo_img.subsample(8,8)
canvas.create_image(250, 80, image=logo_img)

dw_img = PhotoImage(file='dw.png')
dw_img = dw_img.subsample(2,2)

path = PhotoImage(file='path.png')
path = path.subsample(7,7)




link_field = Entry(screen, width=50)
link_label = Label(screen, text="Ingresa el link del video: ", font=("Arial", 15))

path_label = Label(screen, text="Selecciona la ruta de descarga: ", font=("Arial", 15))
select_btn = Button(screen, image=path, command=select_path)

canvas.create_window(230, 280, window=path_label)
canvas.create_window(400, 280, window=select_btn)




canvas.create_window(250, 170, window=link_label)
canvas.create_window(250, 200, window=link_field)


download_btn = Button(screen, image=dw_img, command=download_file)
canvas.create_window(250, 390, window=download_btn)



screen.mainloop()