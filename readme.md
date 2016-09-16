Automagic Image Resizing Tool
=============================

This is a simple tool for automatic image resizing:

* once started it is watching folder(s) for any new jpeg or png files
* if a new file is discovered it does its best to resize and crop it into multiple sizes
* and stores them in the same folder
* folders and sizes are predefined in the config file
* ... and that is all.

How To Get It Running
---------------------
Preinstall all dependencies:

    pip install -r requirements.txt

*For Windows computers you might want to manually download and install Pillow library [from here](https://pypi.python.org/pypi/Pillow/3.3.1).*

and run the tool:

    python watch.py

Now you can drop your jpegs into the folders and get them resized straight away. Simple as that.

