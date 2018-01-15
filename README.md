# CDMasterTool
Tool for Audio CDs, TOC, CUE, CD-Text, CD-Burning, Drive and CD analysis and more.


__Description:__

CDMasterTool is a tool for audio CD creation, TOC and CUE files manipulation, CD burning with CD-TEXT, drive(s) and CD analysis and Commandline launcher. It is mainly based of Cdrdao and libcdio, as well as a couple of other GNU/Linux tools. The main goal is to burn Audio CDs with CD-TEXT, out of a DAW's Red Book export WAV/TOC/CUE combination.

![screenshot](https://github.com/sonejostudios/CDMasterTool/blob/master/CDMasterTool.png "CDMasterTool")


__Main Features:__

* Drive(s) analysis
* Unlock and Eject CD
* CD analysis (CD info, track info, MCN, ISRC, CD-TEXT, CDDB, Medium, etc...)
* Open, edit and save TOC and CUE files
* Replace TOC file path to relative or absolute
* Burning simulation and burning with CD-TEXT
* Adjust driver, device and speed before burning
* Direct link to Flacon to split WAV file according to CUE file and export (WAV, flac, AAC, Ogg, Opus, etc...)
* Direct link to VLC: Play CD (with CD-TEXT) and play CUE file
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
* GNU/Linux (with cp, script, rpl, cdrdao, libcdio)
* Xterm
* Flacon (https://flacon.github.io/)
* VLC (https://www.videolan.org/vlc/)

On Ubuntu/Mint:
```
sudo apt-get install python3 python3-tk libcdio-utils rpl xterm cdrdao vlc flacon
```
You may add first Flacon's ppa to your system (see Flacon's homepage).


__Notes:__

* CDMasterTool was one of my playground for learning Python, I'm sure the code is not the best, but it works! If you have suggestions or you want to help, please contact me. Otherwise, have fun with it, I hope it wilol be helpful for you!
* CDMasterTool is for now a Linux-only Software. It was tested only on LinuxMint MATE, but it should work also on Cinnamon, GNOME and KDE. No OSX and Windows versions are available.


__Tips and Tricks:__

* Export your Audio Master out of your DAW (i.e Ardour). Be sure you filled up the track titles and other metadata.
* Red Book CD Export: At least WAV, 44.100kHz, 16bit, TOC and CUE file with track titles and performer
* Open CDMasterTool and copy/paste the exported WAV file into the WAV-file entry of CDMasterTool
* Cdrdao needs to have the same metadata in the CD title than in the tracks, otherwise, it will not burn. Be sure it is correct.
* Replace the WAV-file path in the TOC-file to a relative path (or somewhere else) (needs rpl). The CUE file path is already relative.
* If you change a metadata in the TOC file, you need to change it in the CUE file as well.
* TOC files are used for burning (Disk-at-Once, via Cdrdao).
* CUE files are used to split with Flacon and play with VLC player (needs Flacon and VLC).
* Cdrdao and libcdio can do much more. Type "cdrdao" or "cd-info/cd-drive --help" and Run it. See also http://cdrdao.sourceforge.net/ and https://www.gnu.org/software/libcdio/
* CDMasterTool was mostly inspired by http://apocalyptech.com/linux/cdtext/. Have a look, there are a lot of good info!
 



__Buttons:__

* cd-drive : Show info and features about the CD drive.
* drive-info : Show drive speed, device, driver, info.
* scanbus : Scan system for drive(s).
* unlock : Unlock drive(s) if locked by mistake.
* eject : Eject drive(s).

* cd-info : Scan CD and show drive info, CD info, track info, MCN, ISRC and CD-TEXT.
* disc id : Scan CD and show tracks (number, start, length) and check CDDB (freedb.org).
* disk-info : Scan CD and show CD info (medium only).

* open toc : Open TOC-file.
* save toc : Overwrite TOC-file. A backup (.toc.bak) will be triggered before saving.
* replace path* : Create a command to replace WAV-file path in TOC-file with relative path. Manually replace OLD_PATH in the command with the old WAV file path present in the TOC file. Press Run to start replacing. A backup (.toc.bak) will be triggered before.

* open cue : Open CUE-file.
* save cue : Overwrite CUE-file. A backup (.cue.bak) will be triggered before saving.

* simulate* : Create command with options for CD Burning simulation (from TOC-file). Press Run to start.
* burn* : Create command with options for CD burning (from TOC-file). Press Run to start.

* flacon split : Split and convert tracks with Flacon/CUE-file. (WAV, Flac, Mp3, Ogg, etc...)
* vlc cue : Open CUE-file with VLC-Player.
* vlc cd : Open CD with VLC-Player.

* ... : Open WAV file with the file chooser dialog. Copy/paste the WAV file into the WAV-file entry will also do the trick, but much faster. :)
* Run : Run command.


Buttons with * will just create the commands (and don't run them). Press Run to do that.




