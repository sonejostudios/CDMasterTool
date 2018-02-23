#!/usr/bin/env python3

from tkinter import *
from tkinter import ttk

from tkinter.filedialog import askopenfilename

import os
import subprocess
import json

from threading import Thread


version = "1.3.5"


# read config file
configfile = open('config.json', 'r')
config = json.loads(configfile.read())
configfile.close()

driver_presets = config["driver"]
device_presets = config["device"]
speed_presets = config["speed"]
spacerheight = config["spacerheight"]

terminal = config["terminal"]
term_hide_option = config["termhideoption"]

music_player = config["musicplayer"]
playcd_command = config["playcdcommand"]

split_app = config["splitapp"]

file_browser = config["filebrowser"]



white = "#ffffff"
black = "#000000"


speed = ""
speedcom = ""
burnsim = "simulate"



def doNothing():
    print("do nothing")


def cd_info():
    print("cd-info")
    command_entry.delete(0.0,END)
    command_entry.insert(0.0, "cd-info --no-device-info")
    run_command("term")


def cd_drive():
    print("cd-drive")
    command_entry.delete(0.0,END)
    command_entry.insert(0.0, "cd-drive")
    run_command("noterm")


# speed work, but some speed not depending of the drive
def set_speed():
    global speedcom

    if speed_entry.get() != "max":
        speed = speed_entry.get()
        speedcom = "--speed " + speed
    else:
        speedcom = ""

    print(speedcom)



def simulate():
    global burnsim
    burnsim = "simulate"
    print(burnsim)
    burn_simulate()

    monitor.delete(0.0, END)
    monitor.insert(0.0, "*Press Run to start the simulation, using :\n\nDriver : " + driver_entry.get() + "\nDevice : " + device_entry.get() + "\nSpeed : " + speed_entry.get())


def burn():
    global burnsim
    burnsim = "write"
    print(burnsim)
    burn_simulate()

    monitor.delete(0.0, END)
    monitor.insert(0.0, "* Press Run to start burning, using :\n\nDriver : " + driver_entry.get() + "\nDevice : " + device_entry.get() + "\nSpeed : " + speed_entry.get())


def burn_simulate():
    tocfile = wavfile_entry.get() + ".toc"
    drive = device_entry.get()
    set_speed()
    command_entry.delete(0.0, END)
    command_entry.insert(0.0, "cdrdao " + burnsim + " --device " + drive + " --driver " + driver_entry.get() + " " + speedcom + " -v 2 -n --eject " + tocfile)
    # run_command()

    # disable saves
    disable_saves()

    # show command entries
    show_commandentry()


def open_toc():
    print("open toc")
    showcuefile = open(wavfile_entry.get() + ".toc", "r")
    toc = showcuefile.read()
    monitor.config(wrap=NONE)
    monitor.delete(0.0, END)
    monitor.insert(0.0, toc)
    showcuefile.close()

    command_entry.delete(0.0, END)
    command_entry.insert(0.0, wavfile_entry.get() + ".toc")

    # enable save toc
    savetoc_button.config(state="normal")

    # disable save cue
    savecue_button.config(state="disable")

    # replace view
    replace_view()


def save_toc():
    print("save toc")
    tocfile = wavfile_entry.get() + ".toc"

    #auto backup
    os.system("cp " + tocfile + " " + tocfile + ".bak")

    savetocfile = open(tocfile, "w")
    savetocfile.write(monitor.get(0.0, END))
    savetocfile.close()

    command_entry.delete(0.0, END)

    # disable saves
    disable_saves()

    # show command entries
    show_commandentry()


def open_cue():
    print("open cue")
    showtocfile = open(wavfile_entry.get() + ".cue", "r")
    toc = showtocfile.read()
    monitor.config(wrap=NONE)
    monitor.delete(0.0, END)
    monitor.insert(0.0, toc)
    showtocfile.close()

    command_entry.delete(0.0, END)
    command_entry.insert(0.0, wavfile_entry.get() + ".cue")

    # enable save cue
    savecue_button.config(state="normal")

    # disable save toc
    savetoc_button.config(state="disable")

    # replace view
    replace_view()


def save_cue():
    print("save cue")
    tocfile = wavfile_entry.get() + ".cue"

    #auto backup
    os.system("cp " + tocfile + " " + tocfile + ".bak")

    savetocfile = open(tocfile, "w")
    savetocfile.write(monitor.get(0.0, END))
    savetocfile.close()

    command_entry.delete(0.0, END)

    # disable saves
    disable_saves()

    # show command entries
    show_commandentry()


# disables save toc and save cue and replace
def disable_saves():
    savetoc_button.config(state="disable")
    savecue_button.config(state="disable")




def eject():
    print("eject")
    show_commandentry()
    command_entry.delete(0.0, END)
    command_entry.insert(0.0, "eject")
    os.system("eject")



def driveinfo():
    print("drive-info")
    command_entry.delete(0.0, END)
    command_entry.insert(0.0, "cdrdao drive-info")
    run_command("noterm")


def diskinfo():
    print("disk-info")
    command_entry.delete(0.0, END)
    command_entry.insert(0.0, "cdrdao disk-info")
    run_command("term")

def diskid():
    print("disk id")
    command_entry.delete(0.0, END)
    command_entry.insert(0.0, "cdrdao discid")
    run_command("term")


def scanbus():
    print("scanbus")
    command_entry.delete(0.0,END)
    command_entry.insert(0.0, "cdrdao scanbus")
    run_command("noterm")



def unlock():
    print("unlock")
    command_entry.delete(0.0,END)
    command_entry.insert(0.0, "cdrdao unlock")
    run_command("noterm")



def openfolder():
    print("open folder")

    dirpath = os.path.dirname(wavfile_entry.get())

    command = file_browser + " " + dirpath

    command_entry.delete(0.0, END)
    command_entry.insert(0.0, command)
    #run_command("noterm")
    subprocess.Popen(command, shell=True)


def splitfile():
    print("split and convert with " + split_app)
    show_commandentry()
    command_entry.delete(0.0,END)
    #monitor.delete(0.0, END)

    wavfile = wavfile_entry.get()
    cuefile = wavfile + ".cue"

    print(cuefile)

    command = split_app + " " + cuefile

    command_entry.insert(0.0, command)
    subprocess.Popen(command, shell=True)

    # disable saves
    disable_saves()


def playcue():
    print("play cue with " + music_player)
    show_commandentry()
    command_entry.delete(0.0,END)

    command = music_player + " " + wavfile_entry.get() + ".cue"

    command_entry.insert(0.0, command)
    subprocess.Popen(command, shell=True)


    # disable saves
    disable_saves()


def playcd():
    print("play cd with with " + music_player)
    show_commandentry()
    command_entry.delete(0.0,END)

    command = music_player + " " + playcd_command

    command_entry.insert(0.0, command)
    subprocess.Popen(command, shell=True)

    # disable saves
    disable_saves()


def replace_view():
    basename = os.path.basename(wavfile_entry.get())
    #newstring_entry.insert(0, basename)

    command_entry.grid_remove()
    oldstring_entry.grid()
    newstring_entry.grid()

    runreplace_button.grid()

    command_label.config(text="Text :")



# Command Replace string in monitor
def on_replace_string(event):
    replace_string()

def replace_string():
    print("replace strings")

    oldstring = oldstring_entry.get()
    newstring = newstring_entry.get()

    mytext = monitor.get(0.0, END)
    mytext = mytext.replace(oldstring, newstring)
    monitor.delete(0.0, END)
    monitor.insert(0.0, mytext)





# --------------RUN COMMAND---------------
def on_run_command():
    run_command("term")

def on_run_command2(event):
    run_command("term")

def run_command(x):
    command = command_entry.get(0.0, END)
    print("run : " + command)

    # create command with text dump
    comtermout = 'script -c "' + command + '" -q stdout.txt'

    if x == "term":
        t1 = Thread(target=run_command_thread,name ="RunCommandThread")
        t1.start()

    else:
        # run command
        os.system(terminal + " " + term_hide_option + " -e ' " + comtermout + " ' ")

        # read stdout file
        read_stdout()


    # disable saves
    disable_saves()

    # show command entries
    show_commandentry()



def run_command_thread():
    monitor.delete(0.0, END)
    monitor.insert(0.0, "Please wait...")

    command = command_entry.get(0.0, END)
    print("run : " + command)

    # create command with text dump
    comtermout = 'script -c "' + command + '" -q stdout.txt'

    #run command
    os.system(terminal + " -e ' " + comtermout + " ' ")

    # read stdout file
    read_stdout()





def show_commandentry():
    # hide replace entries
    oldstring_entry.grid_remove()
    newstring_entry.grid_remove()

    command_entry.grid()

    runreplace_button.grid_remove()

    command_label.config(text="Command :")



# read stdout file and insert text in monitor
def read_stdout():
    outputfile = open("stdout.txt", "r")
    stdout = outputfile.read()
    monitor.delete(0.0, END)
    monitor.insert(0.0, stdout)
    outputfile.close()



# clear entry with mouse button3
def entry_clear(event):
    try:
        event.widget.delete(0, END)
        event.widget.focus_set()
    except:
        event.widget.delete(0.0, END)
        event.widget.focus_set()


# file chooser
def open_file():
    FILEOPENOPTIONS = dict(defaultextension='.wav',
                           filetypes=[('WAV-files', '*.wav'), ('All files', '*.*')])
    filename = askopenfilename(**FILEOPENOPTIONS)
    if filename != "":
        wavfile_entry.delete(0, END)
        wavfile_entry.insert(0, filename)
    else:
        pass


# welcome and read me
def readme():
    command_entry.insert(0.0, "Welcome to CDMasterTool!")
    readmefile = open("README.md", "r")
    readmetext = readmefile.read()
    monitor.config(wrap=WORD)
    monitor.delete(0.0, END)
    monitor.insert(0.0, readmetext)
    readmefile.close()



# show titles etc
def show_titles():
    print("show titles")
    monitor.delete(0.0,END)

    # get cd titale and artist
    cuefile = wavfile_entry.get() + ".cue"
    with open(cuefile, "r") as f:

        cdtitle = ""
        artist = ""
        for l in f:
            if "PERFORMER" in l and artist == "":
                title2 = l[11:-2]
                artist = title2

            if "TITLE" in l and cdtitle == "":
                title = l[7:-2]
                cdtitle = title

        monitor.insert(END, artist + " - " + cdtitle + "\n")


    # read artist + titles from toc
    tocfile = wavfile_entry.get() + ".toc"
    titlelist = []
    with open(tocfile, "r") as f:

        for l in f:
            if "     TITLE" in l :
                title = l[12:-2]
                titlelist.append(title)

        monitor.insert(END, "\n\n")
        # insert track title with numbers
        for c, value in enumerate(titlelist, 1):
            finalnames = str(c) + " " + artist + " - "+ value + "\n"
            monitor.insert(END, finalnames)


    # read titles from toc
    tocfile = wavfile_entry.get() + ".toc"
    titlelist = []
    with open(tocfile, "r") as f:

        for l in f:
            if "     TITLE" in l :
                title = l[12:-2]
                titlelist.append(title)

        monitor.insert(END, "\n\n")
        # insert track title with numbers
        for c, value in enumerate(titlelist, 1):
            finalnames = str(c) + " " + value + "\n"
            monitor.insert(END, finalnames)

        monitor.insert(END, "\n\n")


    # track lengths
    tocfile = wavfile_entry.get() + ".toc"
    with open(tocfile, "r") as f:

        for line in f:

            if "FILE" in line:
                time = line[-9:]
                finaltime = time[:-4]
                # print(finaltime)
                monitor.insert(END, finaltime + "\n")


    # show command entry
    show_commandentry()
    command_entry.delete(0.0, END)




#---------INFO-----------

def noinfo(event):
    info_label.config(text="")

def runinfo(event):
    info_label.config(text="Run command (Enter).")

def cddriveinfo(event):
    info_label.config(text="Show info and features about the CD drive.")

def driveinfoinfo(event):
    info_label.config(text="Show drive speed, device, driver, info.")

def scanbusinfo(event):
    info_label.config(text="Scan system for drive(s).")
def unlockinfo(event):
    info_label.config(text="Unlock drive(s) if locked by mistake.")

def ejectinfo(event):
    info_label.config(text="Eject drive(s).")

def cdinfoinfo(event):
    info_label.config(text="Scan CD and show CD info, track info, MCN, ISRC and CD-TEXT.")

def discidinfo(event):
    info_label.config(text="Scan CD and show tracks (number, start, length) and check CDDB (freedb.org).")

def diskinfoinfo(event):
    info_label.config(text="Scan CD and show CD info (medium only).")

def showtocinfo(event):
    info_label.config(text="Edit TOC-file.")

def savetocinfo(event):
    info_label.config(text="Overwrite TOC-file. A backup (.toc.bak) will be triggered before saving.")

def showcueinfo(event):
    info_label.config(text="Edit CUE-file.")

def savecueinfo(event):
    info_label.config(text="Overwrite CUE-file. A backup (.cue.bak) will be triggered before saving.")

def showtitlesinfo(event):
    info_label.config(text="Show a summary of artist, CD title, CD tracks and track lengths as text.")

def simulateinfo(event):
    info_label.config(text="Create command with options for CD Burning simulation (from TOC-file). Press Run to start.")

def burninfo(event):
    info_label.config(text="Create command with options for CD burning (from TOC-file). Press Run to start.")

def openfolderinfo(event):
    info_label.config(text="Open working folder with " + file_browser + ".")

def splitinfo(event):
    info_label.config(text="Split and convert tracks with " + split_app + " & CUE-file.")

def playcueinfo(event):
    info_label.config(text="Open CUE-file with " + music_player + ".")

def playcdinfo(event):
    info_label.config(text="Open CD with " + music_player + ".")

def wavfileinfo(event):
    info_label.config(text="Full path to WAV-file.")

def filechooserinfo(event):
    info_label.config(text="Open WAV-file with file chooser dialog.")

def driverlistinfo(event):
    info_label.config(text="Choose a driver for simulation and burning. Recommended : generic-mmc:0x10")

def devicelistinfo(event):
    info_label.config(text="Choose a device for simulation and burning.")

def speedlistinfo(event):
    info_label.config(text="Choose drive speed for simulation and burning.")

def commandinfo(event):
    info_label.config(text="Write command. Type 'cdrdao' or 'cd-info -?' for help.")

def replacebuttoninfo(event):
    info_label.config(text="Replace OLD TEXT with NEW TEXT.")

def oldstringinfo(event):
    info_label.config(text="OLD TEXT (text to be replaced). i.e absolute path to WAV-file.")

def newstringinfo(event):
    info_label.config(text="NEW TEXT (replace with this text). i.e relative path to WAV-file.")




# --------------GUI------------------
root = Tk()
root.title("CDMasterTool " + version)

#root.geometry("704x718+300+30")
window_w = 704 # width for the Tk root
window_h = 718 # height for the Tk root

# get screen width and height
window_ws = root.winfo_screenwidth() # width of the screen
windwo_hs = root.winfo_screenheight() # height of the screen

# calculate x and y coordinates for the Tk root window
window_x = (window_ws / 2) - (window_w / 2)
window_y = (windwo_hs / 2) - (window_h / 2)

# set the dimensions of the screen and where it is placed
root.geometry('%dx%d+%d+%d' % (window_w, window_h, window_x, window_y))

root.resizable(False, False)



# Entry WAV file
wavfile_frame = Frame(root)
wavfile_label = Label(wavfile_frame, text="WAV-file :", justify=LEFT)
wavfile_label.grid(row=0, column=0)

wavfile_entry = Entry(wavfile_frame, width=61, background=white)
wavfile_entry.bind("<Button-3>", entry_clear)
wavfile_entry.bind("<Enter>", wavfileinfo)
wavfile_entry.bind("<Leave>", noinfo)
wavfile_entry.grid(row=0, column=1, padx=5)

filechooser_button = ttk.Button(wavfile_frame, text="...", width=2, state="normal", command= open_file)
filechooser_button.bind("<Enter>", filechooserinfo)
filechooser_button.bind("<Leave>", noinfo)
filechooser_button.grid(row=0, column=2)

wavfile_frame.grid(row=0, column=1, padx=0, sticky=W)


#Logo
bitmap2 = PhotoImage(file="logo.png")
w = Canvas(root, width=100, height=100, bd=0, highlightthickness=0, relief="ridge")
w.create_image(50,50, image=bitmap2)
w.grid(row=0, column=0, rowspan=3)

#Button frame
button_frame = Frame(root)
button_frame.grid(row=3, column=0, pady=5, padx=5, sticky=W+N, rowspan=2)


# Button cd-drive
if config["cd-drive"] == 1:
    cddrive_button = ttk.Button(button_frame, text="cd-drive", width=11, state="normal", command= cd_drive)
    cddrive_button.bind("<Enter>", cddriveinfo)
    cddrive_button.bind("<Leave>", noinfo)
    cddrive_button.pack()

# Button Drive-info
if config["drive-info"] == 1:
    driveinfo_button = ttk.Button(button_frame, text="drive-info", width=11, state="normal", command=driveinfo)
    driveinfo_button.bind("<Enter>", driveinfoinfo)
    driveinfo_button.bind("<Leave>", noinfo)
    driveinfo_button.pack()


# Button Scanbus
if config["scanbus"] == 1:
    scanbus_button = ttk.Button(button_frame, text="scanbus", width=11, state="normal", command= scanbus)
    scanbus_button.bind("<Enter>", scanbusinfo)
    scanbus_button.bind("<Leave>", noinfo)
    scanbus_button.pack()


# Button Unlock
if config["unlock"] == 1:
    unlock_button = ttk.Button(button_frame, text="unlock", width=11, state="normal", command= unlock)
    unlock_button.bind("<Enter>", unlockinfo)
    unlock_button.bind("<Leave>", noinfo)
    unlock_button.pack()

# Button Eject
if config["eject"] == 1:
    eject_button = ttk.Button(button_frame, text="eject", width=11, state="normal", command= eject)
    eject_button.bind("<Enter>", ejectinfo)
    eject_button.bind("<Leave>", noinfo)
    eject_button.pack()


#Spacer
spacer_label = Label(button_frame, text="", font=("Helvetica", spacerheight), justify=LEFT)
spacer_label.pack()


# Button cd-info
if config["cd-info"] == 1:
    cdinfo_button = ttk.Button(button_frame, text="cd-info", width=11, state="normal", command= cd_info)
    cdinfo_button.bind("<Enter>", cdinfoinfo)
    cdinfo_button.bind("<Leave>", noinfo)
    cdinfo_button.pack()

# Button discid
if config["discid"] == 1:
    diskinfo_button = ttk.Button(button_frame, text="disc id", width=11, state="normal", command= diskid)
    diskinfo_button.bind("<Enter>", discidinfo)
    diskinfo_button.bind("<Leave>", noinfo)
    diskinfo_button.pack()

# Button Disk-info
if config["disk-info"] == 1:
    diskinfo_button = ttk.Button(button_frame, text="disk-info", width=11, state="normal", command= diskinfo)
    diskinfo_button.bind("<Enter>", diskinfoinfo)
    diskinfo_button.bind("<Leave>", noinfo)
    diskinfo_button.pack()

#Spacer
spacer_label = Label(button_frame, text="", font=("Helvetica", spacerheight), justify=LEFT)
spacer_label.pack()


# Button open toc
if config["edittoc"] == 1:
    opentoc_button = ttk.Button(button_frame, text="edit toc", width=11, state="normal", command= open_toc)
    opentoc_button.bind("<Enter>", showtocinfo)
    opentoc_button.bind("<Leave>", noinfo)
    opentoc_button.pack()

# Button save toc
if config["savetoc"] == 1:
    savetoc_button = ttk.Button(button_frame, text="save toc", width=11, state="disable", command= save_toc)
    savetoc_button.bind("<Enter>", savetocinfo)
    savetoc_button.bind("<Leave>", noinfo)
    savetoc_button.pack()

# Button open cue
if config["editcue"] == 1:
    opencue_button = ttk.Button(button_frame, text="edit cue", width=11, state="normal", command= open_cue)
    opencue_button.bind("<Enter>", showcueinfo)
    opencue_button.bind("<Leave>", noinfo)
    opencue_button.pack()

# Button save cue
if config["savecue"] == 1:
    savecue_button = ttk.Button(button_frame, text="save cue", width=11, state="disable", command= save_cue)
    savecue_button.bind("<Enter>", savecueinfo)
    savecue_button.bind("<Leave>", noinfo)
    savecue_button.pack()

# Button show titles
if config["showtitles"] == 1:
    showtitles_button = ttk.Button(button_frame, text="show titles", width=11, state="normal", command=show_titles)
    showtitles_button.bind("<Enter>", showtitlesinfo)
    showtitles_button.bind("<Leave>", noinfo)
    showtitles_button.pack()

#Spacer
spacer_label = Label(button_frame, text="", font=("Helvetica", spacerheight), justify=LEFT)
spacer_label.pack()


# Button Simulate
if config["simulate"] == 1:
    simulate_button = ttk.Button(button_frame, text="simulate*", width=11, state="normal", command= simulate)
    simulate_button.bind("<Enter>", simulateinfo)
    simulate_button.bind("<Leave>", noinfo)
    simulate_button.pack()

# Button Burn
if config["burn"] == 1:
    burn_button = ttk.Button(button_frame, text="burn*", width=11, state="normal", command= burn)
    burn_button.bind("<Enter>", burninfo)
    burn_button.bind("<Leave>", noinfo)
    burn_button.pack()

#Spacer
spacer_label = Label(button_frame, text="", font=("Helvetica", spacerheight), justify=LEFT)
spacer_label.pack()

# Button open folder
if config["openfolder"] == 1:
    split_button = ttk.Button(button_frame, text="open folder", width=11, state="normal", command= openfolder)
    split_button.bind("<Enter>", openfolderinfo)
    split_button.bind("<Leave>", noinfo)
    split_button.pack()


# Button external spit
if config["externalsplit"] == 1:
    split_button = ttk.Button(button_frame, text="external split", width=11, state="normal", command= splitfile)
    split_button.bind("<Enter>", splitinfo)
    split_button.bind("<Leave>", noinfo)
    split_button.pack()

# Button play cue
if config["playcue"] == 1:
    playcue_button = ttk.Button(button_frame, text="play cue", width=11, state="normal", command= playcue)
    playcue_button.bind("<Enter>", playcueinfo)
    playcue_button.bind("<Leave>", noinfo)
    playcue_button.pack()

# Button vlc cd
if config["playcd"] == 1:
    playcd_button = ttk.Button(button_frame, text="play cd", width=11, state="normal", command= playcd)
    playcd_button.bind("<Enter>", playcdinfo)
    playcd_button.bind("<Leave>", noinfo)
    playcd_button.pack()




#Driver
driver_frame = Frame(root)
driver_label = Label(driver_frame, text="Driver :", justify=LEFT)
driver_label.grid(row=0, column=0, padx=0)

driver_entry = ttk.Combobox(driver_frame, width=21)
#driver_entry.bind("<<ComboboxSelected>>", doNothing)
driver_entry["values"] = driver_presets
driver_entry.current(0) # set init preset
driver_entry.bind("<Enter>", driverlistinfo)
driver_entry.bind("<Leave>", noinfo)
driver_entry.grid(row=0, column=1, padx=5, pady=5)

device_label = Label(driver_frame, text="Device :", justify=LEFT)
device_label.grid(row=0, column=2, padx=0)

device_entry = ttk.Combobox(driver_frame, width=15)
device_entry["values"] = device_presets
device_entry.current(0) # set init preset
device_entry.bind("<Enter>", devicelistinfo)
device_entry.bind("<Leave>", noinfo)
device_entry.grid(row=0, column=3, padx=5, pady=5)

speed_label = Label(driver_frame, text="Speed :", justify=LEFT)
speed_label.grid(row=0, column=4, padx=0)

speed_entry = ttk.Combobox(driver_frame, width=10)
speed_entry["values"] = speed_presets
speed_entry.current(0) # set init preset
speed_entry.bind("<Enter>", speedlistinfo)
speed_entry.bind("<Leave>", noinfo)
speed_entry.grid(row=0, column=5, padx=5, pady=5)


driver_frame.grid(row=1, column=1, pady=5, sticky=W)



# Entry Command
command_frame = Frame(root)
command_label = Label(command_frame, text="Command :", justify=RIGHT)
command_label.grid(row=0, column=0, sticky=N+E)

    #run entry
command_entry = Text(command_frame, width=73, height=4, background=white)
command_entry.bind("<Button-3>", entry_clear)
command_entry.bind("<Return>", on_run_command2)
command_entry.bind("<Enter>", commandinfo)
command_entry.bind("<Leave>", noinfo)
command_entry.grid(row=0, column=1, rowspan=2, pady=3)

    #replace entries
oldstring_entry = Entry(command_frame, width=64, background=white)
oldstring_entry.bind("<Button-3>", entry_clear)
oldstring_entry.bind("<Return>", on_replace_string)
oldstring_entry.bind("<Enter>", oldstringinfo)
oldstring_entry.bind("<Leave>", noinfo)
oldstring_entry.grid(row=0, column=1, pady=3)
oldstring_entry.grid_remove()

newstring_entry = Entry(command_frame, width=64, background=white)
newstring_entry.bind("<Button-3>", entry_clear)
newstring_entry.bind("<Return>", on_replace_string)
newstring_entry.bind("<Enter>", newstringinfo)
newstring_entry.bind("<Leave>", noinfo)
newstring_entry.grid(row=1, column=1, pady=12)
newstring_entry.grid_remove()

    #buttons
runcom_button = ttk.Button(command_frame, text="Run", width=7, state="normal", command= on_run_command)
runcom_button.bind("<Enter>", runinfo)
runcom_button.bind("<Leave>", noinfo)
runcom_button.grid(row=1, column=0, padx=5, pady=4, sticky=S+E)

runreplace_button = ttk.Button(command_frame, text="Replace", width=7, state="normal", command= replace_string)
runreplace_button.bind("<Enter>", replacebuttoninfo)
runreplace_button.bind("<Leave>", noinfo)
runreplace_button.grid(row=1, column=0, padx=5, pady=4, sticky=S+E)
runreplace_button.grid_remove()

command_frame.grid(row=2, column=1, pady=5, sticky=W)




#monitor
monitorframe = Frame(root)
monitorframe.grid(row=3, column=1, columnspan=2, rowspan=1, sticky=N+W+E, padx=5, pady=0)

xscrollbar = ttk.Scrollbar(monitorframe, orient=HORIZONTAL)
xscrollbar.pack(side=BOTTOM, fill=X)
yscrollbar = ttk.Scrollbar(monitorframe)
yscrollbar.pack(side=RIGHT, fill=Y)

monitor = Text(monitorframe, wrap=NONE, xscrollcommand=xscrollbar.set, yscrollcommand=yscrollbar.set, height=35,padx=5, pady=5)
monitor.bind("<Button-3>", entry_clear)
monitor.pack(fill=X)
xscrollbar.config(command=monitor.xview)
yscrollbar.config(command=monitor.yview)


# info label
info_label = Label(root, text="", justify=LEFT)
info_label.grid(row=4, column=1, columnspan=1, rowspan=1, sticky=W, padx=2, pady=0)



#insert default wav file if needed
wavfile_entry.insert(0, config["wavfile"])

# show readme on start
readme()

# mainloop
#root.protocol('WM_DELETE_WINDOW', on_quit)
root.mainloop()

