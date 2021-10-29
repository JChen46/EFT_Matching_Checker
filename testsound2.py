import pyaudio
import wave
import time
filename = 'SlowMotionEnd.wav'
 
# Defines a chunk size of 1024 samples per data frame.
chunk = 1024 
# Open sound file  in read binary form.
file = wave.open(filename, 'rb')
 
# Initialize PyAudio
p = pyaudio.PyAudio()
 
# Creates a Stream to which the wav file is written to.
# Setting output to "True" makes the sound be "played" rather than recorded
stream = p.open(format = p.get_format_from_width(file.getsampwidth()),
                channels = file.getnchannels(),
                rate = file.getframerate(),
                output = True)
 
# Read data in chunks
data = file.readframes(chunk)
 
print('2')
# Play the sound by writing the audio data to the stream
while len(data) > 0:
    stream.write(data)
    data = file.readframes(chunk)
time.sleep(2)
print('here')
# Creates a Stream to which the wav file is written to.
# Setting output to "True" makes the sound be "played" rather than recorded
stream2 = p.open(format = p.get_format_from_width(file.getsampwidth()),
                channels = file.getnchannels(),
                rate = file.getframerate(),
                output = True)
 
# Read data in chunks
data = file.readframes(chunk)
 
# Play the sound by writing the audio data to the stream
while len(data) > 0:
    stream2.write(data)
    data = file.readframes(chunk)
 
# Stop, Close and terminate the stream
stream.stop_stream()
stream.close()
p.terminate()