from keras.models import load_model
from keras import models
from keras.preprocessing.image import img_to_array
import cv2
import numpy as np
import pickle
import imutils
from tkinter import *
from PIL import Image
import pyttsx3
from gtts import gTTS
from playsound import playsound
import speech_recognition as sr
import os
from tkinter import filedialog
from PIL import ImageTk, Image

root = Tk()
# Set Title as Image Loader
root.title("TRAFFIC SIGN CLASSIFICATION")
  
# Set the resolution of window
root.geometry("550x300")

  
# Allow Window to be resizable
root.resizable(width = True, height = True)
##import button
def load():
     with open("output.img", "r") as f:
          output=f.read()
# Load Model:-
model = load_model("TRAINING_EXPERIENCE.h5")
mlb = pickle.loads(open("mlb.pickle", "rb").read())

# Read an Input image:-
def select_image():
    image1=filedialog.askopenfilename()
    image = cv2.imread(image1)
    
    output = imutils.resize(image,width=400)
    image = cv2.resize(image, (96, 96))
    image = image.astype("float") / 255.0
    image = img_to_array(image)
    image = np.expand_dims(image, axis=0)

    accuracy = model.predict(image)[0]
    
    idxs = np.argsort(accuracy)[::-1][:1]
    #print(idxs)

    for (i, j) in enumerate(idxs):
            label = "{}: {:.2f}%".format(mlb.classes_[j], accuracy[j] * 100)
            print(label)
            cv2.putText(output, label, (10, (i * 30) + 25), 
		cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
    cv2.imshow('Output_image',output)

    if mlb.classes_[j]=='SCHOOLZONE':
         text='goslow'
         resp=text
         language='en'
         myob=gTTS(text=str(resp),lang=language,slow=False)
         myob.save("wel.mp3")
         os.system("mpg321 wel.mp3")
         playsound.playsound("wel.mp3",True)
         os.remove("wel.mp3")
    elif mlb.classes_[j]=='HOSPITAL':
         text='DONT HORN'
         resp=text
         language='en'
         myob=gTTS(text=str(resp),lang=language,slow=False)
         myob.save("wel.mp3")
         os.system("mpg321 wel.mp3")
         playsound.playsound("wel.mp3",True)
         os.remove("wel.mp3")
    elif mlb.classes_[j]=='DANGERTURN':
         playsound('D:/PROJECT_CODE/Alert.wav')
         print('alarm')
         
         
         
btn = Button (root, text="Select a traffic sign  image", command=select_image)
btn.pack(side="bottom", expand="yes", padx="10", pady="10")
# kick off the GUI
root.mainloop()
