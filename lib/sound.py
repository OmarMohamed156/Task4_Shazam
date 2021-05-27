from librosa.feature.spectral import mfcc
from numpy.lib.arraypad import pad
from scipy import signal
import soundfile as sff
import numpy as np
import winsound
import os
import librosa

class soundfileUtility():
    # read wav file
    # returns sampling rate and sound data 
    @staticmethod
    def fn_ReadFile(file_name):
        data, samplerate = librosa.load(file_name)
        # get first min
        return data[0:(samplerate*60) + 1], samplerate
    
    def get_spectrogram(data,samplerate) : 
        frequancyArr, timeArr, Sxx  = signal.spectrogram(np.array(data),samplerate)
        return frequancyArr,timeArr

    def get_zero_crossing_rate(data):
        data = librosa.zero_crossings(data,pad = False)
        return data
    
    def get_spectral_centroid(data,samplerate) : 
        spectral_centroids = librosa.feature.spectral_centroid(data, sr=samplerate)[0]
        return spectral_centroids
    
    def get_Mel_Frequency(data,samplerate):
        mfccs = librosa.feature.mfcc(data, sr=samplerate)
        return mfcc


    @staticmethod
    def fn_PlaySoundFile(file_name="Tdfgjdli.wav"):
        winsound.PlaySound(file_name, winsound.SND_FILENAME)
        os.remove(file_name)