# Earth

Earth is a simplistic Python application for setting your background picture to a current top post on Reddit's `/r/EarthPorn`.

By default, it fetches 20 images every hour that it is enabled, and changes the background image every five minutes.
These quotas can be changed in [earth/\_\_init\_\_.py](https://raw.githubusercontent.com/nickrobson/Earth/master/earth/__init__.py)

Currently it supports **Windows** and **Mac OS X**. I'm hoping to support Linux in the near future.

On Mac, there's a tray icon (text for now, but I'll make an icon!) which you can click on to manually change the image or fetch new images.

## Installing

### Windows:
* Clone the GitHub repo.
* Run the console command: `pip install -r requirements.txt`
* To run the application, use `python earth.py`

You can use the *Mac OS X* method if you use a Bash-compatible shell. I'll be making a Batch file when I get around to it.

### Mac OS X:
* Download the [install.sh](https://raw.githubusercontent.com/nickrobson/Earth/master/install.sh) script.
* Run this script to launch the program. All necessary files will be downloaded upon first-run.

## Updating

### Windows:
* Pull from the GitHub repo while in the directory.

### Mac OS X:
* Run the script as `install.sh update`, or `git pull` while inside the `~/.earth/source` directory.