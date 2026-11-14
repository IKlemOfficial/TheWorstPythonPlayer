import tkinter
from tkinter import ttk
import vlc

root = tkinter.Tk()

root.title("JMusic")
root.geometry("400x600")
#root.maxsize(400, 600)

# ["TitleOfThisFile", AllLengthOfThisSong, LengthOfThisSongNow]
Info = ["", 0, 0]

def PlaySound(PathToFile):
    global player
    player = vlc.MediaPlayer(PathToFile)
    
    player.play()

    # Removing path to the file (idk how to get it from VLC)
    # /path/to/file/music.mp3 > music.mp3
    try: Info[0] = PathToFile[PathToFile.rindex("/") + 1:]
    except ValueError: Info[0] = PathToFile

    # if FileName is more than 30 char; then split it
    Counter = 0
    FinalTitleName = ""

    for a in Info[0]:
        if Counter > 30:
            Counter = 0
            FinalTitleName += "\n"

        FinalTitleName += a
        Counter += 1

    Info[0] = FinalTitleName
    TitleText["text"] = FinalTitleName
    PauseButton["text"] = "⏸️"

    UpdateSecTime()

def UpdateSecTime():
    Info[2] = player.get_time() / 1000 // 1
    root.after(1000, UpdateSecTime)

def Pause():
    try: 
        if player.get_state() == vlc.State.Paused: PauseButton["text"] = "⏸️"
        elif player.get_state() == vlc.State.Playing: PauseButton["text"] = "▶️"

        player.pause()
    except NameError: print("Music not playing! (Or player did not created?)")

FileToPlayEntry = ttk.Entry(root)
PlayButton = ttk.Button(root, text="Play", command=lambda: PlaySound(FileToPlayEntry.get()))
PauseButton = ttk.Button(root, text="▶️", command=lambda: Pause())
TitleText = ttk.Label(root, text="Nothing")

FileToPlayEntry.pack(anchor='ne', side='left')
PlayButton.pack(anchor='ne', side='left')
PauseButton.place(relx=0.4, rely=0.95)
TitleText.place(relx=0.5, rely=0.5, anchor="center")

root.mainloop()
