# CDMasterTool
Tool for Audio CDs, TOC, CUE, CD-Text, CD-Burning, Drive/CD analysis and more.


__Description:__

CDMasterTool is a tool for audio CD creation, TOC and CUE files manipulation, CD burning with CD-TEXT, drive(s) and CD analysis and Commandline launcher. It is mainly based of Cdrdao and libcdio, as well as a couple of other GNU/Linux tools. The main goal is to burn Audio CDs with CD-TEXT, out of a DAW's Red Book export WAV/TOC/CUE combination.

![screenshot](https://github.com/sonejostudios/CDMasterTool/blob/master/CDMasterTool-135.png "CDMasterTool")

CDMasterTool in action: https://youtu.be/A4S1s92GtNU


__Main Features:__

* CD analysis (CD info, track info, MCN, ISRC, CD-TEXT, CDDB, Medium, etc...)
* Open, edit and save TOC and CUE files
* Replace text in TOC and CUE files
* Burning simulation and burning with CD-TEXT
* Adjust driver, device and speed before burning
* Drive(s) analysis
* Unlock and Eject CD
* Direct link to external split application to split WAV file according to CUE file and export
* Direct link to music player: Play CD (with CD-TEXT) and play CUE file
* Show summary of artist, CD title, CD tracks and track lengths for copy/paste
* Commandline launcher for Cdrdao, libcdio and more
* Auto description for buttons and entries
  

__Installation:__

1. copy the whole CDMasterTool folder on your system
```
git clone https://github.com/sonejostudios/CDMasterTool.git
```

2. from this folder start CDMatserTool with: 
```
python3 CDMasterTool.py
```


__Requirements:__

* Python3
* Tkinter
* GNU/Linux (with cp, script, cdrdao, libcdio)
* Cueparser
* Xterm
* Flacon (https://flacon.github.io/)
* VLC (https://www.videolan.org/vlc/)


1. You may add first Flacon's ppa to your system (see Flacon's homepage).
2. On Ubuntu/Mint:
```
sudo apt-get install python3 python3-tk libcdio-utils xterm cdrdao vlc flacon
```
3. Install CueParser via pip3:
```
pip3 install cueparser
```



__Notes:__

* CDMasterTool is a really simple GUI for different GNU/Linux tools, I'm sure the code is not the best, but it works and I really like working with it. If you have suggestions or you want to help, please contact me. Otherwise, have fun with it, I hope it will be helpful for you!
* CDMasterTool is for now a Linux-only Software. It was tested only on LinuxMint 17 MATE, but it should work also on Cinnamon, GNOME and KDE. No OSX and Windows versions are available.


__Tips and Tricks:__

* Export your Audio Master out of your DAW (i.e Ardour). Be sure you filled up the track titles and other metadata.
* Red Book CD Export: WAV / 44.100kHz / 16bit, TOC and CUE file with track titles and performer.
* Open CDMasterTool and copy/paste the exported WAV file into the WAV-file entry of CDMasterTool.
* Cdrdao needs to have the same metadata in the CD title than in the tracks, otherwise, it will not burn. Be sure it is correct.
* Replace the absolute WAV-file path in the TOC-file to a relative path (or somewhere else). The CUE file path is already relative. You can also replace anything in a text.
* If you change a metadata in the TOC file, you need to change it in the CUE file as well.
* Changes in TOC/CUE will not be saved until you press "save toc" or "save cue". If something went wrong, just press "edit toc"/"edit cue" again before saving.
* Saving a TOC/CUE file will trigger an automatic backup (".bak") bevore saving. If you have saved by mistake, just have a look at the ".bak" file.
* TOC files are used for burning (Disk-at-Once, via Cdrdao).
* CUE files are used to split with external split application and play with music player (default are Flacon and VLC).
* Right-click on text entries will delete the content.
* Cdrdao and libcdio can do much more. Type "cdrdao" or "cd-info/cd-drive -?" and Run it. See also http://cdrdao.sourceforge.net/ and https://www.gnu.org/software/libcdio/
* CDMasterTool was mostly inspired by http://apocalyptech.com/linux/cdtext/. Have a look, there are a lot of good info!


__Buttons:__

* cd-drive : Show info and features about the CD drive.
* drive-info : Show drive speed, device, driver, info.
* scanbus : Scan system for drive(s).
* unlock : Unlock drive(s) if locked by mistake.
* eject : Eject drive(s).

* cd-info : Scan CD and show CD info, track info, MCN, ISRC and CD-TEXT.
* disc id : Scan CD and show tracks (number, start, length) and check CDDB (freedb.org).
* disk-info : Scan CD and show CD info (medium only).

* edit toc : Open TOC-file and show the replace text mask instead of the command line.
* save toc : Overwrite TOC-file. A backup (.toc.bak) will be triggered before saving.
* edit cue : Open CUE-file and show the replace text mask instead of the command line.
* save cue : Overwrite CUE-file. A backup (.cue.bak) will be triggered before saving.
* show titles : Show a summary of artist, CD title, CD tracks and track lengths as text. This will also save the titles as .txt file in the working folder.

* simulate* : Create command with options (driver, device and speed) for CD burning simulation (from TOC-file). Press Run to start the simulation.
* burn* : Create command with options (driver, device and speed) for CD burning (from TOC-file). Press Run to start burning.

* open folder : Open the current working folder with the default file browser. This as to be set in the config.json file at "filebrowser".
* external split : Split and convert tracks with external split application and the CUE-file. I recommend "Flacon".
* play cue : Open CUE-file with a music player. I recommend "VLC".
* play cd : Open CD with with a music player. I recommend "VLC".

* ... : Open WAV file with the file chooser dialog. Copy/paste the WAV file into the WAV-file entry will also do the trick, but much faster. :)
* Run : Run command.
* Replace: Replace OLD TEXT with NEW TEXT in the monitor view (but not in the files). You need to save the files (TOC/CUE) manually using the "save toc" and "save cue" buttons.
* Open: Open text file.


Buttons with * will just create the commands (and don't run them). Press Run to do that.


__Help commands:__

* cdrdao
* cd-info -?
* cd-drive -?


__Configuration:__

* You can configure CDMasterTool via the configuration file: config.json
WARNING: Make a backup first before changing anything in the config file!
* You can put a default WAV-file path to open on start
* You can change the driver list, the device list and the speed list (space separated values). The first item in the list will be choosen by default. Change them only if you are really sure you know what you are doing!
* You can hide or show specific buttons (0 = hide, 1 = show)
* You can change the spacer height between button groups (default = 5)
* You can change the terminal application ("terminal"). Some commands are hiding the terminal, put the right command for this in "termhideoption". Default terminal aplication is "xterm" and its hide option is "-iconic". If your terminal emulator doesn't have an hide option, leave it blank: "".
* You can change the music player application ("musicplayer"). Default is "vlc". Put a music player specific play-cd command with "playcdcommand", default for VLC is "cdda://[device][@[track]]".
* You can change the external split application ("splitapp"). Default is "flacon".
* You can change the default file browser ("filebrowser"). Default is "caja".



