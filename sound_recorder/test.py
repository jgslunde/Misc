import numpy as np
import pyaudio
import wave
import sys

format = pyaudio.paInt16
channels = 1
rate = 44100
chunk = 1024
record_seconds = 5
output_file = "file.wav"

audio = pyaudio.PyAudio()

stream = audio.open(format=format, channels=channels, rate=rate, input=True,
					frames_per_buffer=chunk)

intervals = int(rate/chunk * record_seconds)

frames = []

print("Recording...")
for i in range(intervals):
	data = stream.read(chunk)
	frames.append(data)
print("Finished recording")

stream.stop_stream()
stream.close()
audio.terminate()

waveFile = wave.open(output_file, "wb")
waveFile.setnchannels(channels)
waveFile.setsampwidth(audio.get_sample_size(format))
waveFile.setframerate(rate)
waveFile.writeframes(b''.join(frames))
waveFile.close()
