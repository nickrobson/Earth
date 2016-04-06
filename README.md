# Earth

Earth is a simplistic Python application for setting your background picture to a current top post on Reddit's `/r/EarthPorn`.

By default, it fetches 20 images every hour that it is enabled, and changes the background image every five minutes.
These quotas can be changed in [earth/\_\_init\_\_.py](https://raw.githubusercontent.com/nickrobson/Earth/master/earth/__init__.py)

Images are stored in `~/.earth/images`. You can delete them if you wish to, and I do my best to avoid large image downloads.

Currently it supports **Windows** and **Mac OS X**. I'm hoping to support Linux in the near future.

On Mac, there's a tray icon (text for now, but I'll make an icon!) which you can click on to manually change the image or fetch new images.

## Installing

Regardless of your Operating System, you will need [Python](https://python.org) and [Git](https://git-scm.com) installed.

You also need to be able to either:

* use PIP (package manager)
* or install from PyPI (manual)

To install from PyPI, you need to install all packages listed in `requirements.txt`.

### Windows:
* Clone the GitHub repo.
* Run the console command: `pip install -r requirements.txt`
* To run the application, use `python earth.py`

You can use the *Mac OS X / Linux* method if you use a Bash-compatible shell. I'll be making a Batch file when I get around to it.

### Mac OS X / Linux:
* Download the [install.sh](https://raw.githubusercontent.com/nickrobson/Earth/master/install.sh) script.
* If on Linux, install `python-gconf` through your distro's package manager.
* Run this script to launch the program. All necessary files will be downloaded upon first-run.

## Updating

### Windows:
* Pull from the GitHub repo while in the directory.

### Mac OS X / Linux:
* Run the script as `install.sh update`, or `git pull` while inside the `~/.earth/source` directory.

## TODO:
* Windows tray support