import librosa
import numpy as np
from scipy.spatial.distance import euclidean

audio1, sr = librosa.load("ref.wav", sr=None)
audio2, sr = librosa.load("test.wav", sr=None)

mfcc1 = librosa.feature.mfcc(y=audio1, sr=sr).flatten()
mfcc2 = librosa.feature.mfcc(y=audio2, sr=sr).flatten()

distance = euclidean(mfcc1, mfcc2)

print("Distance:", distance)

if distance < 50:
    print("Similar voice")
else:
    print("Different voice")
    