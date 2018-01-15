from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter.font import Font

from tkinter import filedialog
from tkinter.filedialog import askopenfilename

import os


version = "1.0"

devmode = 0

white = "#ffffff"
black = "#000000"

spacerheight = 5

drivers = ["generic-mmc:0x10", "generic-mmc", "generic-mmc-raw",
           "cdd2600", "plextor", "plextor-scan", "ricoh-mp6200", "sony-cdu920", "sony-cdu948", "taiyo-yuden", "teac-cdr55", "toshiba", "yamaha-cdr10x"]

speed_presets = ["max", "4", "8", "16", "24"]

drive_presets = ["/dev/sr0", "/dev/sr1"]

speed = ""
speedcom = ""
burnsim = "simulate"


def doNothing():
    print("do nothing")


def cd_info():
    print("cd-info")
    command_entry.delete(0.0,END)
    command_entry.insert(0.0, "cd-info")
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


def open_toc():
    print("open toc")
    showcuefile = open(wavfile_entry.get() + ".toc", "r")
    toc = showcuefile.read()
    monitor.delete(0.0, END)
    monitor.insert(0.0, toc)
    showcuefile.close()

    command_entry.delete(0.0, END)
    command_entry.insert(0.0, wavfile_entry.get() + ".toc")

    # enable save toc
    savetoc_button.config(state="normal")

    # disable save cue
    savecue_button.config(state="disable")


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


def open_cue():
    print("open cue")
    showtocfile = open(wavfile_entry.get() + ".cue", "r")
    toc = showtocfile.read()
    monitor.delete(0.0, END)
    monitor.insert(0.0, toc)
    showtocfile.close()

    command_entry.delete(0.0, END)
    command_entry.insert(0.0, wavfile_entry.get() + ".cue")

    # enable save cue
    savecue_button.config(state="normal")

    # disable save toc
    savetoc_button.config(state="disable")


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


# disables save toc and save cue
def disable_saves():
    savetoc_button.config(state="disable")
    savecue_button.config(state="disable")


def eject():
    print("eject")
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


def driverlist():
    print("driverlist")
    command_entry.delete(0.0, END)
    command_entry.insert(0.0, "cdrdao simulate --driver none " + wavfile_entry.get() + ".toc")
    run_command("noterm")

def unlock():
    print("unlock")
    command_entry.delete(0.0,END)
    command_entry.insert(0.0, "cdrdao unlock")
    run_command("noterm")


def flacon():
    print("split and convert with flacon")
    command_entry.delete(0.0,END)
    #monitor.delete(0.0, END)

    wavfile = wavfile_entry.get()
    cuefile = wavfile + ".cue"

    print(cuefile)

    os.system("flacon " + cuefile)
    command_entry.insert(0.0, "flacon " + cuefile)
    #run_command("noterm")

    # disable saves
    disable_saves()


def vlccue():
    print("play cue with vlc player")
    command_entry.delete(0.0,END)
    #monitor.delete(0.0, END)

    command = "vlc " + wavfile_entry.get() + ".cue"

    os.system(command)
    command_entry.insert(0.0, command)
    #run_command("noterm")

    # disable saves
    disable_saves()


def vlccd():
    print("play cd with vlc player")
    command_entry.delete(0.0,END)
    #monitor.delete(0.0, END)

    os.system("vlc cdda://[device][@[track]]")
    command_entry.insert(0.0, "vlc cdda://[device][@[track]]")
    #run_command("noterm")

    # disable saves
    disable_saves()






def replace_path():
    print("replace path")
    tocfile = wavfile_entry.get() + ".toc"

    basename = os.path.basename(wavfile_entry.get())

    # auto backup
    os.system("cp " + tocfile + " " + tocfile + ".bak")

    # rpl command
    command = "rpl OLD_PATH " + basename + " " + tocfile

    command_entry.delete(0.0, END)
    command_entry.insert(0.0, command)





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

    # run command and pipe stdout to text file
    #os.system(command + " | tee stdout.txt")
    #os.system(command + " > stdout.txt" )

    if x == "term":
        os.system("xterm -e ' " + comtermout + " ' ")
    else:
        #os.system(comtermout)
        os.system("xterm -iconic -e ' " + comtermout + " ' ")




    # read stoutfile
    read_stdout()

    # disable saves
    disable_saves()


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



#---------INFOS-----------

def noinfo(event):
    info_label.config(text="")

def runinfo(event):
    info_label.config(text="Run command.")

def cddriveinfo(event):
    info_label.config(text="Show info and features about the CD drive.")

def driveinfoinfo(event):
    info_label.config(text="Show drive speed, device, driver, info.")

def scanbusinfo(event):
    info_label.config(text="Scan system for drive(s).")

#def driversinfo(event):
#    info_label.config(text="Show available drivers.")

def unlockinfo(event):
    info_label.config(text="Unlock drive(s) if locked by mistake.")

def ejectinfo(event):
    info_label.config(text="Eject drive(s).")

def cdinfoinfo(event):
    info_label.config(text="Scan CD and show drive info, CD info, track info, MCN, ISRC and CD-TEXT.")

def discidinfo(event):
    info_label.config(text="Scan CD and show tracks (number, start, length) and check CDDB (freedb.org).")

def diskinfoinfo(event):
    info_label.config(text="Scan CD and show CD info (medium only).")

def showtocinfo(event):
    info_label.config(text="Open TOC-file.")

def savetocinfo(event):
    info_label.config(text="Overwrite TOC-file. A backup (.toc.bak) will be triggered before saving.")

def replacepathinfo(event):
    info_label.config(text="Replace WAV-file path in TOC-file with relative path. Replace OLD_PATH and press Run to start.")

def showcueinfo(event):
    info_label.config(text="Open CUE-file.")

def savecueinfo(event):
    info_label.config(text="Overwrite CUE-file. A backup (.cue.bak) will be triggered before saving.")

def simulateinfo(event):
    info_label.config(text="Create command with options for CD Burning simulation (from TOC-file). Press Run to start.")

def burninfo(event):
    info_label.config(text="Create command with options for CD burning (from TOC-file). Press Run to start.")

def flaconinfo(event):
    info_label.config(text="Split and convert tracks with Flacon/CUE-file. (WAV, Flac, Mp3, Ogg, etc...)")

def vlccueinfo(event):
    info_label.config(text="Open CUE-file with VLC-Player.")

def vlccdinfo(event):
    info_label.config(text="Open CD with VLC-Player.")

def wavfileinfo(event):
    info_label.config(text="Full path to WAV-file. Copy/paste the WAV-file to this entry also does the trick.")

def filechooserinfo(event):
    info_label.config(text="Open WAV-file with file chooser dialog.")

def driverlistinfo(event):
    info_label.config(text="Choose a driver for simulation and burning. Recommended : generic-mmc:0x10")

def devicelistinfo(event):
    info_label.config(text="Choose a device for simulation and burning.")

def speedlistinfo(event):
    info_label.config(text="Choose drive speed for simulation and burning.")

def commandinfo(event):
    info_label.config(text="Write command. Type 'cdrdao' or 'cd-info --help' for help.")




# --------------GUI------------------
root = Tk()
root.title("CDMasterTool " + version)
root.geometry("704x712+300+30")
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
cddrive_button = ttk.Button(button_frame, text="cd-drive", width=11, state="normal", command= cd_drive)
cddrive_button.bind("<Enter>", cddriveinfo)
cddrive_button.bind("<Leave>", noinfo)
cddrive_button.pack()

# Button Drive-info
driveinfo_button = ttk.Button(button_frame, text="drive-info", width=11, state="normal", command=driveinfo)
driveinfo_button.bind("<Enter>", driveinfoinfo)
driveinfo_button.bind("<Leave>", noinfo)
driveinfo_button.pack()


# Button Scanbus
scanbus_button = ttk.Button(button_frame, text="scanbus", width=11, state="normal", command= scanbus)
scanbus_button.bind("<Enter>", scanbusinfo)
scanbus_button.bind("<Leave>", noinfo)
scanbus_button.pack()

# Button drivers - needed?
#driverlist_button = ttk.Button(button_frame, text="drivers", width=11, state="normal", command= driverlist)
#driverlist_button.bind("<Enter>", driversinfo)
#driverlist_button.bind("<Leave>", noinfo)
#driverlist_button.pack()


# Button Unlock
unlock_button = ttk.Button(button_frame, text="unlock", width=11, state="normal", command= unlock)
unlock_button.bind("<Enter>", unlockinfo)
unlock_button.bind("<Leave>", noinfo)
unlock_button.pack()

# Button Eject
eject_button = ttk.Button(button_frame, text="eject", width=11, state="normal", command= eject)
eject_button.bind("<Enter>", ejectinfo)
eject_button.bind("<Leave>", noinfo)
eject_button.pack()


#Spacer
spacer_label = Label(button_frame, text="", font=("Helvetica", spacerheight), justify=LEFT)
spacer_label.pack()


# Button cd-info
cdinfo_button = ttk.Button(button_frame, text="cd-info", width=11, state="normal", command= cd_info)
cdinfo_button.bind("<Enter>", cdinfoinfo)
cdinfo_button.bind("<Leave>", noinfo)
cdinfo_button.pack()

# Button discid
diskinfo_button = ttk.Button(button_frame, text="disc id", width=11, state="normal", command= diskid)
diskinfo_button.bind("<Enter>", discidinfo)
diskinfo_button.bind("<Leave>", noinfo)
diskinfo_button.pack()

# Button Disk-info
diskinfo_button = ttk.Button(button_frame, text="disk-info", width=11, state="normal", command= diskinfo)
diskinfo_button.bind("<Enter>", diskinfoinfo)
diskinfo_button.bind("<Leave>", noinfo)
diskinfo_button.pack()

#Spacer
spacer_label = Label(button_frame, text="", font=("Helvetica", spacerheight), justify=LEFT)
spacer_label.pack()


# Button open toc
opentoc_button = ttk.Button(button_frame, text="open toc", width=11, state="normal", command= open_toc)
opentoc_button.bind("<Enter>", showtocinfo)
opentoc_button.bind("<Leave>", noinfo)
opentoc_button.pack()

# Button save toc
savetoc_button = ttk.Button(button_frame, text="save toc", width=11, state="disable", command= save_toc)
savetoc_button.bind("<Enter>", savetocinfo)
savetoc_button.bind("<Leave>", noinfo)
savetoc_button.pack()

# Button path replace
opentoc_button = ttk.Button(button_frame, text="replace path*", width=11, state="normal", command= replace_path)
opentoc_button.bind("<Enter>", replacepathinfo)
opentoc_button.bind("<Leave>", noinfo)
opentoc_button.pack()

#Spacer
spacer_label = Label(button_frame, text="", font=("Helvetica", spacerheight), justify=LEFT)
spacer_label.pack()


# Button open cue
opencue_button = ttk.Button(button_frame, text="open cue", width=11, state="normal", command= open_cue)
opencue_button.bind("<Enter>", showcueinfo)
opencue_button.bind("<Leave>", noinfo)
opencue_button.pack()

# Button save cue
savecue_button = ttk.Button(button_frame, text="save cue", width=11, state="disable", command= save_cue)
savecue_button.bind("<Enter>", savecueinfo)
savecue_button.bind("<Leave>", noinfo)
savecue_button.pack()

#Spacer
spacer_label = Label(button_frame, text="", font=("Helvetica", spacerheight), justify=LEFT)
spacer_label.pack()


# Button Simulate
simulate_button = ttk.Button(button_frame, text="simulate*", width=11, state="normal", command= simulate)
simulate_button.bind("<Enter>", simulateinfo)
simulate_button.bind("<Leave>", noinfo)
simulate_button.pack()

# Button Burn
burn_button = ttk.Button(button_frame, text="burn*", width=11, state="normal", command= burn)
burn_button.bind("<Enter>", burninfo)
burn_button.bind("<Leave>", noinfo)
burn_button.pack()

#Spacer
spacer_label = Label(button_frame, text="", font=("Helvetica", spacerheight), justify=LEFT)
spacer_label.pack()


# Button flacon
flacon_button = ttk.Button(button_frame, text="flacon split", width=11, state="normal", command= flacon)
flacon_button.bind("<Enter>", flaconinfo)
flacon_button.bind("<Leave>", noinfo)
flacon_button.pack()

# Button vlc cue
vlccue_button = ttk.Button(button_frame, text="vlc cue", width=11, state="normal", command= vlccue)
vlccue_button.bind("<Enter>", vlccueinfo)
vlccue_button.bind("<Leave>", noinfo)
vlccue_button.pack()

# Button vlc cd
vlccd_button = ttk.Button(button_frame, text="vlc cd", width=11, state="normal", command= vlccd)
vlccd_button.bind("<Enter>", vlccdinfo)
vlccd_button.bind("<Leave>", noinfo)
vlccd_button.pack()




#Driver
driver_frame = Frame(root)
driver_label = Label(driver_frame, text="Driver :", justify=LEFT)
driver_label.grid(row=0, column=0, padx=0)

driver_entry = ttk.Combobox(driver_frame, width=21)
#driver_entry.bind("<<ComboboxSelected>>", doNothing)
driver_entry["values"] = drivers
driver_entry.current(0) # set init preset
driver_entry.bind("<Enter>", driverlistinfo)
driver_entry.bind("<Leave>", noinfo)
driver_entry.grid(row=0, column=1, padx=5, pady=5)

device_label = Label(driver_frame, text="Device :", justify=LEFT)
device_label.grid(row=0, column=2, padx=0)

device_entry = ttk.Combobox(driver_frame, width=15)
device_entry["values"] = drive_presets
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
command_label = Label(command_frame, text="Command : ", justify=LEFT)
command_label.grid(row=0, column=0, sticky=N)
command_entry = Text(command_frame, width=73, height=4, background=white)
command_entry.bind("<Button-3>", entry_clear)
command_entry.bind("<Return>", on_run_command2)
command_entry.bind("<Enter>", commandinfo)
command_entry.bind("<Leave>", noinfo)
command_entry.grid(row=0, column=1, rowspan=2)
runcom_button = ttk.Button(command_frame, text="Run", width=7, state="normal", command= on_run_command)
runcom_button.bind("<Enter>", runinfo)
runcom_button.bind("<Leave>", noinfo)
runcom_button.grid(row=1, column=0, padx=5, sticky=N)
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



#dev mode auto insert toc
if devmode == 1:
    wavfile_entry.insert(0, "/media/sda7/StudioSession3/CD-TEXT/ardour/cdtext/export/cdtext_superdirtvince.wav")

# mainloop
#root.protocol('WM_DELETE_WINDOW', on_quit)
root.mainloop()

