from tkinter import *
import requests
from PIL import ImageTk, Image
from pytubefix import YouTube as yt
from functools import cache
from io import BytesIO


def searchVideo(url):
    global img
    v = yt(url)
    print(v.thumbnail_url)
    u = requests.get(v.thumbnail_url)
    img = ImageTk.PhotoImage(Image.open(BytesIO(u.content)).resize((400, 320)))
    generateDLButtons(v)
    Label(root, text=v.title, font=(fontName, 13)).place(x=30, y=380)
    Label(root, image=img).place(x=30,y=50)


def generateDLButtons(v : yt):
    videoStreams = v.streams.filter(adaptive=True, file_extension='mp4').order_by("resolution").desc().all()
    audioStream = v.streams.filter(only_audio=True).first()
    for i in range(3):
        Button(root, text='Download ' + videoStreams[i].resolution, width=15, command=videoStreams[i].download).place(x=500, y=40*i + 120)

    Button(root, text='Download ' + audioStream.abr, width=15,command=audioStream.download).place(x=500, y=280)        

def OpenChangeDestination():
    r = Tk()
    r.geometry("400x80")
    Entry(r, textvariable=destination, font=(fontName, 20)).pack(fill=X)
    Button(r, text='Apply', command=ChangeDestination, font=TupFont).pack(fill=X)
    r.mainloop()

@cache
def ChangeDestination():
    pass

root = Tk()
root.geometry("720x480")
root.title("Youtube Downloader")

fontName = "Roboto"
fontSize = 16
TupFont = (fontName, fontSize)

destination = StringVar()


url = StringVar()
url.set("")

Entry(root, textvariable=url, width=27, font=TupFont).place(x=300,y=5)
Button(root, text="Search", font=(fontName, 16)
       , command=lambda : searchVideo(url.get())).place(x=620,y=5)

menubar = Menu(root)
config = Menu(menubar, tearoff=0)

menubar.add_cascade(label='Config', menu=config, font=(fontName, 12))
config.add_command(label='Change Destination', command=OpenChangeDestination)
config.add_separator()
config.add_command(label='Exit', command=root.destroy)


root.config(menu=menubar)
root.mainloop()