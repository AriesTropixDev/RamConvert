import tkinter
from tkinter import ttk
from tkinter import messagebox
from tkinter import *
from pytube import YouTube
options = ['144p','240p','360p','480p','720p','1080p']
root = Tk()
clicked =tkinter.StringVar(root)
clicked.set(options[0])
qual = '144p'
def extract(s):
    global qual
    qual = s
def Downloader():
    try:
     quality = qual
     url =YouTube(str(link.get()))

     video = url.streams.filter( res=f'{quality}').first()

     video.download()
     Label(root, text = 'DOWNLOADED', font = 'arial 15').grid(row=6,column=2,pady=15)
    except:
        messagebox.showerror(title='ERROR!',message='SOMETHING WENT WRONG\n\nTRY AGAIN')


root.geometry('500x300')
root.resizable(0,0)
root.config(padx=30,pady=30)
root.title("youtube video downloader")
Label(root,text = 'Youtube Video Downloader', font ='arial 20 bold').grid(row=0,column=2)
link = StringVar()

Label(root, text = 'Paste Link Here:', font = 'arial 15 bold').grid(row=1,column=2)
link_enter = Entry(root, width = 70,textvariable = link).grid(row=2,column=2,pady=10)
Label(root,text='Choose the quality',font='arial 15 bold').grid(row=3,column=2)
quality =ttk.OptionMenu(root,clicked,*options,command=extract).grid(row=4,column=2,pady=10)
Button(root,text = 'DOWNLOAD', font = 'arial 15 bold' ,bg = 'pale violet red', padx = 2,
       command = Downloader).grid(row=5,column=2)



root.mainloop()
