import pyaudio
import wave
import sys
import time

class AudioFile:
    chunk = 1024

    def __init__(self, file):
        """ Init audio stream """ 
        self.wf = wave.open(file, 'rb')
        self.p = pyaudio.PyAudio()
        self.stream = self.p.open(
            format = self.p.get_format_from_width(self.wf.getsampwidth()),
            channels = self.wf.getnchannels(),
            rate = self.wf.getframerate(),
            output = True,
            output_device_index =  6 ## use `python -m sounddevice` to find index of speaker: Speakers (Realtek(R) Audio), MME (0 in, 2 out)
        )

    def play(self):
        """ Play entire file """
        data = self.wf.readframes(self.chunk)
        while len(data) > 0:
            self.stream.write(data)
            data = self.wf.readframes(self.chunk)

    def close(self):
        """ Graceful shutdown """ 
        self.stream.close()
        self.p.terminate()

# Usage example for pyaudio
# a = AudioFile("a_match_has_been_found.wav")
# a.play()
# a.close()