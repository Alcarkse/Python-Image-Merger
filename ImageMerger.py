#   Combines 3-4 grayscale images into a single image, using each input as a R,G,B and Alpha chanel

#   Role: Handle UI and Main logic loop

from Combiner import ImageCombiner
from tkinter import *
from tkinter.filedialog import askopenfilename
import tkinter.messagebox as messagebox
from PIL import Image, ImageTk

root = Tk()


g_blankImage = ImageTk.PhotoImage(Image.new("RGB", [128,128], color="#FFFFFF"))

class App :

    selectedImages = []

    def __init__(self, master) :

        master.winfo_toplevel().title("Image Merger")

        imageSelectionFrame = Frame(master)
        imageSelectionFrame.pack(expand=True, pady=10)

        self.selectedImages.append(ImageSelection(imageSelectionFrame))
        self.selectedImages.append(ImageSelection(imageSelectionFrame))
        self.selectedImages.append(ImageSelection(imageSelectionFrame))

        self.combine_btn = Button(master, text="Combine Images", command=self.ProcessImages)
        self.combine_btn.pack()

        bottomPart = Frame(master)
        bottomPart.pack(pady=10)
        self.outputImageDisplay = ImageDisplay(bottomPart)

        self.save_button = Button(master, text="Save Image As...", command=self.printSelectedImages)
        self.save_button.pack()

    def printSelectedImages(self) :

        files = ""
        for image in self.selectedImages :

            if image.filename == "" :
                messagebox.showwarning("Missing Files","Please select 3 images.")
                break

            files += image.filename + "\n"
            print(image.filename)
        
        if files != "" :
            messagebox.showinfo("Submited Files", "You have submitted the following files:\n" + files)
    
    def ProcessImages(self) :

        if not self.checkSubmittedImages() :
            messagebox.showwarning("Missing Files","Please select 3 valid images.")

        R = self.selectedImages[0].filename
        G = self.selectedImages[1].filename
        B = self.selectedImages[2].filename

        imageCombiner = ImageCombiner(R, G, B)
        result = imageCombiner.Combine()

        self.outputImage = result
        self.outputImageDisplay.DisplayImage(result)

    def checkSubmittedImages(self) :

        for image in self.selectedImages :

            if image.filename == "" :
                return False

        return True


class ImageSelection :

    filename = ""
    
    def __init__(self, master) :

        self.container = Frame(master, relief="flat", bd=3, background="#FFABAB")
        self.container.pack(side="left", ipadx=5, ipady=5, padx=10, pady=10)

        self.header = Frame(self.container)
        self.header.pack(ipady=5)

        self.entry = Entry(self.header)
        self.entry.pack(side="left", fill="x")

        self.browse_button = Button(self.header, text="Browse Files", command=self.BrowseFile)
        self.browse_button.pack(side="right")

        self.imageDisplay = ImageDisplay(self.container)



    def BrowseFile(self) :
        self.filename = askopenfilename()
        self.entry.delete(0, END)
        self.entry.insert(0, self.filename)
        self.imageDisplay.DisplayImage(Image.open(self.filename))

    

class ImageDisplay :

    def __init__(self, master) :
        self.displayElement = Label(master, width=128, height=128, image=g_blankImage)
        self.displayElement.pack()
    
    def DisplayImage(self, imageObject) :
        photo = ImageTk.PhotoImage(imageObject)
        self.displayElement.configure(image=photo)
        self.displayElement.image = photo
        self.displayElement.pack()

app = App(root)

root.mainloop()

