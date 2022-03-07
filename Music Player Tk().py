from tkinter import *
from tkinter import ttk , filedialog
from pygame import mixer
import os
#open Button Function
def open_folder():
    path=filedialog.askdirectory()
    if(path):
        os.chdir(path)
        songs=os.listdir(path)
        for song in songs:
            if song.endswith(".mp3"):
                play_list.insert(END,song)
#Play Command = Paly_song
def play_song():
    mixer.music.load(play_list.get(ACTIVE))
    mixer.music.play()
    #volume function
def set_vol(val):
    mixer.music.set_volume(float(val)/100)



window = Tk()
mixer.init()
window.title("Simple Music Player")
window.geometry("300x180")
window.config(bg="white")
window.resizable(0,0)

#adding Buttons...
ttk.Button(window,text="Play",width=10,command=play_song).place(x=10,y=10)
ttk.Button(window,text="Stop",width=10,command=mixer.music.stop).place(x=10,y=40)
ttk.Button(window,text="Pause",width=10,command=mixer.music.pause).place(x=10,y=70)
ttk.Button(window,text="Un Pause",width=10,command=mixer.music.unpause).place(x=10,y=100)
ttk.Button(window,text="Open",width=10,command=open_folder).place(x=10,y=130)
#Music Frame
music_frame= Frame(window,bd=2,relief= RIDGE)#Border Style
music_frame.place(x=90,y=10,width=200,height=110)
#scroll Bar
scroll_y = ttk.Scrollbar(music_frame)
play_list = Listbox(music_frame,width=29,yscrollcommand=scroll_y.set)
scroll_y.config(command=play_list.yview)
scroll_y.pack(side=RIGHT,fill=Y)
play_list.pack(side=LEFT,fill=BOTH)
#volume Scale...
vol = ttk.Scale(window,from_=0, to = 100, length = 180 , command = None )
vol.set(50)
vol.place(x=100,y=130)




A = ttk.Style(window)
A.theme_use('vista')#alt,clam

window.mainloop()