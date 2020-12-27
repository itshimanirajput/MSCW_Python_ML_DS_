import gtts
import os
MyText = "Heyyyy, What's up "

MyValue = gtts.gTTS(text = MyText,lang= 'en', slow = True)

MyValue.save("MySpeech1.mp3")
os.system("MySpeech1.mp3")