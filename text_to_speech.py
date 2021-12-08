from gtts import gTTS # we have imported this module for text to speech conversion
import os
# if you want text from your file
# abc = open("sample.txt")
# text = abc.read()
text = "I am Kshaunish I am a computer science student"
language = 'en'  # en is for english language

obj = gTTS(text = text, lang = language , slow =  False)
# we have used slow = False because our converted video will have a high speed

obj.save("sample.mp3")

# to open the video file automatically we have to import os

os.system("sample.mp3")
