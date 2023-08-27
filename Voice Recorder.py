# importing library functions
import sounddevice as sd
from scipy.io.wavfile import write
import wavio as wv

freq = 44100
duration = int(input("Enter the duration: ")) #giving time duration input

# Recording the audio
print("Start Speaking!")
print("Recording the audio!")
recording = sd.rec(int(duration * freq),samplerate=freq, channels=2) 

# Waiting for the recorded audio to be processed:
sd.wait()
print("Wait!! Your Audio is being processed!")

# Getting the output
wv.write("voice_record.wav", recording, freq, sampwidth=2)
print("Output is out!")
print("Get the Output in the file region")