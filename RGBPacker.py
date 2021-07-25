import tkinter as tk
import tkinter.font as tkFont
from PIL import Image
from PIL.ImageOps import invert
from tkinter import filedialog
import tkinter.messagebox as alert
from os.path import basename

class App:
    def __init__(self, root):
        #setting title
        root.title("RGB Packer")
        #setting window size
        width=710
        height=210
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)
        ft = tkFont.Font(family='Verdana',size=10)

        # red
        labelRed = tk.Label(root)
        labelRed["font"] = ft
        labelRed["fg"] = "#333333"
        labelRed["justify"] = "left"
        labelRed["text"] = "Red"
        labelRed.place(x=10,y=10,width=70,height=25)
        labelRed["anchor"] = "w"

        self.textRed=tk.Entry(root)
        self.textRed["borderwidth"] = "1px"
        self.textRed["font"] = ft
        self.textRed["fg"] = "#333333"
        self.textRed["justify"] = "left"
        self.textRed.place(x=80,y=10,width=320,height=30)

        browseRed=tk.Button(root)
        browseRed["bg"] = "#f0f0f0"
        browseRed["font"] = ft
        browseRed["fg"] = "#000000"
        browseRed["justify"] = "center"
        browseRed["text"] = "Browse"
        browseRed.place(x=410,y=10,width=80,height=30)
        browseRed["command"] = lambda: self.browseFile(self.textRed)

        self.redDef = tk.StringVar(value="black")
        self.redBlack=tk.Radiobutton(root, variable=self.redDef)
        self.redBlack["font"] = ft
        self.redBlack["fg"] = "#333333"
        self.redBlack["justify"] = "left"
        self.redBlack["text"] = "Black"
        self.redBlack.place(x=500,y=10,width=60,height=30)
        self.redBlack["value"] = "black"
        self.redWhite=tk.Radiobutton(root, variable=self.redDef)
        self.redWhite["font"] = ft
        self.redWhite["fg"] = "#333333"
        self.redWhite["justify"] = "left"
        self.redWhite["text"] = "White"
        self.redWhite.place(x=560,y=10,width=60,height=30)
        self.redWhite["value"] = "white"

        self.redInvert = tk.BooleanVar(value=False)
        self.redInvertCheck=tk.Checkbutton(root, variable=self.redInvert)
        self.redInvertCheck["font"] = ft
        self.redInvertCheck["fg"] = "#333333"
        self.redInvertCheck["justify"] = "left"
        self.redInvertCheck["text"] = "Invert"
        self.redInvertCheck.place(x=635,y=10,width=60,height=30)

        # green
        labelGreen = tk.Label(root)
        labelGreen["font"] = ft
        labelGreen["fg"] = "#333333"
        labelGreen["justify"] = "left"
        labelGreen["text"] = "Green"
        labelGreen.place(x=10,y=50,width=70,height=25)
        labelGreen["anchor"] = "w"

        self.textGreen=tk.Entry(root)
        self.textGreen["borderwidth"] = "1px"
        self.textGreen["font"] = ft
        self.textGreen["fg"] = "#333333"
        self.textGreen["justify"] = "left"
        self.textGreen.place(x=80,y=50,width=320,height=30)

        browseGreeen=tk.Button(root)
        browseGreeen["bg"] = "#f0f0f0"
        browseGreeen["font"] = ft
        browseGreeen["fg"] = "#000000"
        browseGreeen["justify"] = "center"
        browseGreeen["text"] = "Browse"
        browseGreeen.place(x=410,y=50,width=80,height=30)
        browseGreeen["command"] = lambda: self.browseFile(self.textGreen)

        self.greenDef = tk.StringVar(value="black")
        self.greenBlack=tk.Radiobutton(root, variable=self.greenDef)
        self.greenBlack["font"] = ft
        self.greenBlack["fg"] = "#333333"
        self.greenBlack["justify"] = "left"
        self.greenBlack["text"] = "Black"
        self.greenBlack.place(x=500,y=50,width=60,height=30)
        self.greenBlack["value"] = "black"
        self.greenWhite=tk.Radiobutton(root, variable=self.greenDef)
        self.greenWhite["font"] = ft
        self.greenWhite["fg"] = "#333333"
        self.greenWhite["justify"] = "left"
        self.greenWhite["text"] = "White"
        self.greenWhite.place(x=560,y=50,width=60,height=30)
        self.greenWhite["value"] = "white"

        self.greenInvert = tk.BooleanVar(value=False)
        self.greenInvertCheck=tk.Checkbutton(root, variable=self.greenInvert)
        self.greenInvertCheck["font"] = ft
        self.greenInvertCheck["fg"] = "#333333"
        self.greenInvertCheck["justify"] = "left"
        self.greenInvertCheck["text"] = "Invert"
        self.greenInvertCheck.place(x=635,y=50,width=60,height=30)

        # blue
        labelBlue = tk.Label(root)
        labelBlue["font"] = ft
        labelBlue["fg"] = "#333333"
        labelBlue["justify"] = "left"
        labelBlue["text"] = "Blue"
        labelBlue.place(x=10,y=90,width=70,height=25)
        labelBlue["anchor"] = "w"

        self.textBlue=tk.Entry(root)
        self.textBlue["borderwidth"] = "1px"
        self.textBlue["font"] = ft
        self.textBlue["fg"] = "#333333"
        self.textBlue["justify"] = "left"
        self.textBlue.place(x=80,y=90,width=320,height=30)

        browseBlue=tk.Button(root)
        browseBlue["bg"] = "#f0f0f0"
        browseBlue["font"] = ft
        browseBlue["fg"] = "#000000"
        browseBlue["justify"] = "center"
        browseBlue["text"] = "Browse"
        browseBlue.place(x=410,y=90,width=80,height=30)
        browseBlue["command"] = lambda: self.browseFile(self.textBlue)

        self.blueDef = tk.StringVar(value="black")
        self.blueBlack=tk.Radiobutton(root, variable=self.blueDef)
        self.blueBlack["font"] = ft
        self.blueBlack["fg"] = "#333333"
        self.blueBlack["justify"] = "left"
        self.blueBlack["text"] = "Black"
        self.blueBlack.place(x=500,y=90,width=60,height=30)
        self.blueBlack["value"] = "black"
        self.blueWhite=tk.Radiobutton(root, variable=self.blueDef)
        self.blueWhite["font"] = ft
        self.blueWhite["fg"] = "#333333"
        self.blueWhite["justify"] = "left"
        self.blueWhite["text"] = "White"
        self.blueWhite.place(x=560,y=90,width=60,height=30)
        self.blueWhite["value"] = "white"

        self.blueInvert = tk.BooleanVar(value=False)
        self.blueInvertCheck=tk.Checkbutton(root, variable=self.blueInvert)
        self.blueInvertCheck["font"] = ft
        self.blueInvertCheck["fg"] = "#333333"
        self.blueInvertCheck["justify"] = "left"
        self.blueInvertCheck["text"] = "Invert"
        self.blueInvertCheck.place(x=635,y=90,width=60,height=30)

        # alpha
        labelAlpha = tk.Label(root)
        labelAlpha["font"] = ft
        labelAlpha["fg"] = "#333333"
        labelAlpha["justify"] = "left"
        labelAlpha["text"] = "Alpha"
        labelAlpha.place(x=10,y=130,width=70,height=25)
        labelAlpha["anchor"] = "w"

        self.textAlpha=tk.Entry(root)
        self.textAlpha["borderwidth"] = "1px"
        self.textAlpha["font"] = ft
        self.textAlpha["fg"] = "#333333"
        self.textAlpha["justify"] = "left"
        self.textAlpha.place(x=80,y=130,width=460,height=30)

        browseAlpha=tk.Button(root)
        browseAlpha["bg"] = "#f0f0f0"
        browseAlpha["font"] = ft
        browseAlpha["fg"] = "#000000"
        browseAlpha["justify"] = "center"
        browseAlpha["text"] = "Browse"
        browseAlpha.place(x=550,y=130,width=80,height=30)
        browseAlpha["command"] = lambda: self.browseFile(self.textAlpha)

        self.alphaInvert = tk.BooleanVar(value=False)
        self.alphaInvertCheck=tk.Checkbutton(root, variable=self.alphaInvert)
        self.alphaInvertCheck["font"] = ft
        self.alphaInvertCheck["fg"] = "#333333"
        self.alphaInvertCheck["justify"] = "left"
        self.alphaInvertCheck["text"] = "Invert"
        self.alphaInvertCheck.place(x=635,y=130,width=60,height=30)

        packButton=tk.Button(root)
        packButton["bg"] = "#f0f0f0"
        packButton["font"] = ft
        packButton["fg"] = "#000000"
        packButton["justify"] = "center"
        packButton["text"] = "Pack"
        packButton.place(x=10,y=170,width=690,height=25)
        packButton["command"] = self.packButton_command
    
    def browseFile(self, textField: tk.Entry):
        file = filedialog.askopenfile(mode="r", filetypes=[
            ("Image files", ".jpg .jpeg .png .tga .gif .tif .tiff .dds .bmp")
        ])

        if file is not None:
            textField.delete(0, tk.END)
            textField.insert(0, file.name)


    def packButton_command(self):
        newImage = self.packImages(self.textRed.get(), self.textGreen.get(), self.textBlue.get(), self.textAlpha.get())
        if newImage:
            file = filedialog.asksaveasfile(filetypes=[
                ("PNG Image", ".png"),
                ("BMP Image", ".bmp"),
                ("TARGA Image", ".tga"),
                ("TIF Image", ".tif"),
                ("JPEG Image", ".jpg"),
            ], defaultextension="*.png")

            if file is not None:
                ext = ""
                if not str(file.name).endswith((".png", ".bmp", ".tga", ".tif", ".jpg")):
                    print(file.filetype)
                    exit()
                newImage.save(file.name)
                alert.showinfo(title="Success!", message=f"{basename(file.name)} has been saved!")

    def packImages(self, red, green, blue, alpha):
        r = Image.open(red) if red != "" else Image.new(mode="RGB", size=(1,1), color=self.redDef.get())
        g = Image.open(green) if green != "" else Image.new(mode="RGB", size=(1,1), color=self.greenDef.get())
        b = Image.open(blue) if blue != "" else Image.new(mode="RGB", size=(1,1), color=self.blueDef.get())

        if r.mode == "I;16":
            r.mode = "I"
            r = r.point(lambda i:i*(1./256))

        if g.mode == "I;16":
            g.mode = "I"
            g = g.point(lambda i:i*(1./256))

        if b.mode == "I;16":
            b.mode = "I"
            b = b.point(lambda i:i*(1./256))

        if alpha != "":
            a = Image.open(alpha)
            if a.mode == "I;16":
                a.mode = "I"
                a = a.point(lambda i:i*(1./256))

        if self.redInvert.get():
            r = invert(r.convert("RGB"))
        if self.greenInvert.get():
            g = invert(g.convert("RGB"))
        if self.blueInvert.get():
            b = invert(b.convert("RGB"))
        if self.alphaInvert.get() and alpha != "":
            a = invert(a.convert("RGB"))

        size = max(r.size, g.size, b.size) if alpha == "" else max(r.size, g.size, b.size, a.size)

        if alpha != "":
            return Image.merge("RGBA", [r.resize(size).convert("L"), g.resize(size).convert("L"), b.resize(size).convert("L"), a.resize(size).convert("L")])
        else:
            return Image.merge("RGB", [r.resize(size).convert("L"), g.resize(size).convert("L"), b.resize(size).convert("L")])

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
