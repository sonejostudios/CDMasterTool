# CDMasterTool
Tool for Audio CDs, TOC, CUE, CD-Text, CD-Burning, Drive and CD analysis and more.


__Description:__

CDMastertool is a Tool for Audio CD creation, TOC and CUE files manipulation, CD burning with CD-TEXT, drive(s) and CD analysis and Commandline launcher. It is mainly based of Cdrdao and libcdio, as well as a couple of other GNU/Linux tools. The main goal is to burn Audio CDs with CD-TEXT, out of a DAW's Red Book export WAV/TOC/CUE combination.

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


__Notes:__

* CDMasterTool was one of my playground for learning Python, I'm sure the code is not the best, but it works!. If you have suggestions or you want to help, please contact me. Otherwise, have fun with it, I hope it wilol be helpful for you!
* CDMasterTool is for now a Linux-only Software. It was tested only on LinuxMint MATE, but it should work also on Cinnamon, GNOME and KDE. No OSX and Windows versions are available.


__Tips and Tricks:__

* coming..




__Buttons:__


* cd-drive
* drive-info
* scanbus
* unlock
* eject

* cd-info
* disc id
* disk-info

* open toc
* save toc
* replace path*

* open cue
* save cue

* simulate*
* burn*

* flacon split
* vlc cue
* vlc cd






