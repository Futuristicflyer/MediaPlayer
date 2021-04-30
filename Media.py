import pygame
import tkinter as tkr
from tkinter.filedialog import askdirectory
from PIL import ImageTk, Image
import os

if os.environ.get ('DISPLAY', '') == '':
    print('no display found. Using :0.0')
    os.environ.__setitem__('DISPLAY', ':0.0')

musicPlayer = tkr.Tk()
musicPlayer.title("Music Player")
musicPlayer.geometry("500x1000")


directory_path = os.path.join(os.environ['USERPROFILE'],'Documents','Project','Pictures')
if not os.path.isdir(directory_path): os.mkdir(directory_path)
os.chdir(directory_path)
pictures = os.listdir()

playPic = Image.open("playButton2.jpg")
resizePhoto = playPic.resize((100,100))
playPic = ImageTk.PhotoImage(resizePhoto)

stopPic = Image.open("stopButton2.jpg")
resizePhoto = stopPic.resize((100,100))
stopPic = ImageTk.PhotoImage(resizePhoto)

pausePic = Image.open("pauseButton2.jpg")
resizePhoto = pausePic.resize((100,100))
pausePic = ImageTk.PhotoImage(resizePhoto)

unpausePic = Image.open("unpauseButton2.jpg")
resizePhoto = unpausePic.resize((100,100))
unpausePic = ImageTk.PhotoImage(resizePhoto)

directory = askdirectory()
os.chdir(directory)
songList = os.listdir()

playList = tkr.Listbox(musicPlayer, font="Helvetica 12 bold", bg="black", fg="white", selectmode=tkr.SINGLE)

artworkPresent = False
for item in songList:
    pos=0
    if ((item[(len(item)-3):(len(item))]) == 'mp3'):
        playList.insert(pos, item)
        pos+=1
        pygame.init()
        pygame.mixer.init()
    if ((item[(len(item)-3):(len(item))]) == ('png' or 'jpg')):
        artworkPresent = True
        artworkPic = Image.open(item)
        resizePhoto = artworkPic.resize((500,500))
        artworkPic = ImageTk.PhotoImage(resizePhoto)
        artwork = tkr.Label(musicPlayer, bg="black", image=artworkPic)

if artworkPresent == False:
    artworkPresent == True
    directory_path = os.path.join(os.environ['USERPROFILE'],'Documents','Project','Pictures')
    os.chdir(directory_path)
    pictures = os.listdir()
    artworkPic = Image.open("musicPic.jpg")
    resizePhoto = artworkPic.resize((500,500))
    artworkPic = ImageTk.PhotoImage(resizePhoto)
    artwork = tkr.Label(musicPlayer, bg="black", image=artworkPic)
    os.chdir(directory)


def play():
    pygame.mixer.music.load(playList.get(tkr.ACTIVE))


def play():
    pygame.mixer.music.load(playList.get(tkr.ACTIVE))
    var.set(playList.get(tkr.ACTIVE))
    pygame.mixer.music.play()

def stop():
    pygame.mixer.music.stop()

def pause():
    pygame.mixer.music.pause()

def unpause():
    pygame.mixer.music.unpause()

playButton = tkr.Button(musicPlayer, width=100, height=100, image=playPic, command=play, bg="white")

stopButton = tkr.Button(musicPlayer, width=100, height=100, image=stopPic, command=stop, bg="white")

pauseButton = tkr.Button(musicPlayer, width=100, height=100, image=pausePic, command=pause, bg="white")

unpauseButton = tkr.Button(musicPlayer, width=100, height=100, image=unpausePic, command=unpause, bg="white")

var = tkr.StringVar()
songTitle = tkr.Label(musicPlayer, font="Helvetica 12 bold", textvariable=var)
playing = False

songTitle.pack()
artwork.pack()
playList.pack(fill="both", expand="yes")
playButton.pack(anchor="s", side="left", fill="y")
stopButton.pack(anchor="s", side="left", fill="y")
pauseButton.pack(anchor="s", side="left", fill="y")
unpauseButton.pack(anchor="s", side="left", fill="y")

musicPlayer.mainloop()
