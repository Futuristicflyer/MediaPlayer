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


#<--- Setting up images for buttons --->
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

#<------------------------------------->


directory = askdirectory() #Prompts user to choose a directory from which they want their music
os.chdir(directory)
songList = os.listdir()

playList = tkr.Listbox(musicPlayer, font="Helvetica 12 bold", bg="black", fg="white", selectmode=tkr.SINGLE) #Creates a list box with the songs included in the directory chosen by the user.


artworkPresent = False
for item in songList:
    pos=0
    if ((item[(len(item)-3):(len(item))]) == 'mp3'): #Checks for only mp3 files as to skip over any other non-audio files
        playList.insert(pos, item) #If file is audio file, it will be addeed onto the list box
        pos+=1
        pygame.init()
        pygame.mixer.init()
    if ((item[(len(item)-3):(len(item))]) == ('png' or 'jpg')): #Checks folder to see if there is any artwork to be displayed while user listens to music
        artworkPresent = True
        artworkPic = Image.open(item)
        resizePhoto = artworkPic.resize((500,500))
        artworkPic = ImageTk.PhotoImage(resizePhoto)
        artwork = tkr.Label(musicPlayer, bg="black", image=artworkPic)

if artworkPresent == False: #If users directory does not contain artwork, use the default image provided
    artworkPresent == True
    directory_path = os.path.join(os.environ['USERPROFILE'],'Documents','Project','Pictures')
    os.chdir(directory_path)
    pictures = os.listdir()
    artworkPic = Image.open("musicPic.jpg")
    resizePhoto = artworkPic.resize((500,500))
    artworkPic = ImageTk.PhotoImage(resizePhoto)
    artwork = tkr.Label(musicPlayer, bg="black", image=artworkPic)
    os.chdir(directory)


def play(): #Defines the play command which begins to play music/audio
    pygame.mixer.music.load(playList.get(tkr.ACTIVE))
    var.set(playList.get(tkr.ACTIVE))
    pygame.mixer.music.play()

def stop(): #Defines stop command which completely stops music, and returns to the beginning
    pygame.mixer.music.stop()

def pause(): #Defines pause command which pauses music at the timestamp the command is issued
    pygame.mixer.music.pause()

def unpause(): #Defines unpause command which resumes music at the timestamp provided by the pause command
    pygame.mixer.music.unpause()


#<---Setting up buttons and the commands and pictures to issue --->
playButton = tkr.Button(musicPlayer, width=100, height=100, image=playPic, command=play, bg="white")

stopButton = tkr.Button(musicPlayer, width=100, height=100, image=stopPic, command=stop, bg="white")

pauseButton = tkr.Button(musicPlayer, width=100, height=100, image=pausePic, command=pause, bg="white")

unpauseButton = tkr.Button(musicPlayer, width=100, height=100, image=unpausePic, command=unpause, bg="white")
#<---------------------------------------------------------------->


var = tkr.StringVar()
songTitle = tkr.Label(musicPlayer, font="Helvetica 12 bold", textvariable=var) #Sets the name of the song currently playing to the top of the GUI

songTitle.pack()
artwork.pack()
playList.pack(fill="both", expand="yes")
playButton.pack(anchor="s", side="left", fill="y")
stopButton.pack(anchor="s", side="left", fill="y")
pauseButton.pack(anchor="s", side="left", fill="y")
unpauseButton.pack(anchor="s", side="left", fill="y")

musicPlayer.mainloop()
