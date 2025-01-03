from tkinter import *
from pytube import YouTube

root = Tk()
root.geometry('700x300')
root.resizable(0, 0)
root.title("Download De Vídeos Do YouTube")
root.configure(bg='#1a1a1a') 

title_font = ('Helvetica', 15, 'bold')
label_font = ('Helvetica', 12)
button_font = ('Helvetica', 15, 'bold')

Label(root, text='Copie o link do vídeo que você quer baixar', font=title_font, fg='white', bg='#1a1a1a').pack(pady=(50, 10))

link = StringVar()

Label(root, text='Cole o link aqui:', font=label_font, fg='white', bg='#1a1a1a').pack(pady=5)
Entry(root, width=80, textvariable=link).pack(pady=10)

def Downloader():
    try:
        url = YouTube(str(link.get()))
        video = url.streams.first()
        video.download(r'C:\Users\Usuario\Downloads')
        Label(root, text='Download Completo!', font=title_font, fg='green', bg='#1a1a1a').place(x=270, y=210)
    except Exception as e:
        Label(root, text='ERROR', font=title_font, fg='red', bg='#1a1a1a').place(x=320, y=210)

Button(root, text='DOWNLOAD', font=button_font, bg='white', padx=2, command=Downloader).pack(pady=10)

root.mainloop()
