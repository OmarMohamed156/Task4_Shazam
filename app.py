from lib.stringDistance import StringDistance
from lib.sound import soundfileUtility
from lib.hash import Hash
import os
import librosa
# iterate over songs paths
paths = []
for i in range(1,5) :
    p = "Group18_Song"+ str(i) +"_Full.mp3"
    paths.append(os.path.join("songs",p))
    paths.append("Group18_Song"+ str(i) +"_Music.mp3")
    paths.append("Group18_Song"+ str(i) +"_Vocals.mp3")

data,sampleRate =  librosa.load("C:\Task4_Shazam\songs\Group18_Song1_Full.mp3")
print(sampleRate)