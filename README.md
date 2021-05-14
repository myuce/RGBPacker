# RGB Packer
A simple image packer that combines grayscale images into a single image.

# Installing & running
The only dependency needed to run RGB Packer is Pillow, which can be installed using the following command.
```
python3 -m pip install --upgrade pip
python3 -m pip install --upgrade Pillow
```

Afterwards, you can simply run `RGBPacker.py`. Optionally, you can also install PyInstaller and run `build.bat` to build an exe file if you want to build it yourself. Otherwise, you can get the prebuilt executables from [here](https://github.com/myuce/RGBPacker/releases).

You can then simply choose the images you want to pack and then press the pack button. If you are going to leave a channel empty, you can decide if the said channel will be filled with black or white. If you leave the alpha channel empty, the result will not have an alpha channel.

Icon file source: http://www.fatcow.com/free-icons