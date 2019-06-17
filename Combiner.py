#   Role: Alogirthm that combines the images
from __future__ import print_function
from PIL import Image
import os, sys

class ImageCombiner :

    sourceImages = []
    outputAvailable = False

    def __init__(self, img_R, img_G, img_B) :
        self.sourceImages.append(Image.open(img_R))
        self.sourceImages.append(Image.open(img_G))
        self.sourceImages.append(Image.open(img_B))


    def Combine(self) :
       
        combinedChannels = []

        for i in range(len(self.sourceImages)) :
            inputImage = self.sourceImages[i]
            combinedChannels.append(inputImage.getchannel(i))

        self.combinedImage = Image.merge(self.sourceImages[0].mode, combinedChannels)
        self.outputAvailable = True

        return self.combinedImage

    def SaveToDir(self, path) :

        if not self.outputAvailable :
            print("No images to save")
            return False

        self.combinedImage.image.save(path)
