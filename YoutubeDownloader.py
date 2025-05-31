from tkinter import *
import requests
from PIL import ImageTk, Image
from pytubefix import YouTube as yt
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
    videoStreams = v.streams.filter(adaptive=True)
    audioStreams = v.streams.filter(only_audio=True)
    print(videoStreams)
    print(audioStreams)

root = Tk()
root.geometry("720x480")
root.title("Youtube Downloader")

fontName = "Roboto"
fontSize = 16
TupFont = (fontName, fontSize)

url = StringVar()
url.set("")

Entry(root, textvariable=url, width=27, font=TupFont).place(x=300,y=5)
Button(root, text="Search", font=(fontName, 16)
       , command=lambda : searchVideo(url.get())).place(x=620,y=5)


root.mainloop()