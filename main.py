import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile

def generate_spectrogram(wav_file):
    sample_rate, data = wavfile.read(wav_file)

    if len(data.shape) > 1:
        data = data[:, 0]
    plt.figure(figsize=(12, 6))
    plt.specgram(data, Fs=sample_rate, NFFT=1024, noverlap=512, cmap='inferno')
    plt.title(f'Spectrogram of {wav_file}')
    plt.xlabel('Time (s)')
    plt.ylabel('Frequency (Hz)')
    plt.colorbar(label='Intensity (dB)')
    plt.xlim(0, len(data) / sample_rate)
    plt.ylim(0, sample_rate / 2)  

    plt.grid(True)

    plt.show()
wav_file_path = 'my_file.wav'
generate_spectrogram(wav_file_path)


#kiritigan mattni o'qish
from gtts import gTTS
import os

text = "You are very good student"

language = 'en'
tts = gTTS(text=text, lang=language, slow=False)

audio_file = "output.mp3"
tts.save(audio_file)

from IPython.display import Audio
Audio(audio_file)
