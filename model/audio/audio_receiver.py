import queue
import numpy as np
import sounddevice as sd
import speech_recognition as sr


from cfg import Config

class AudioReceiver:

    def __init__(self, cfg: Config):
        self.cfg = cfg
        self.audio_queue = queue.Queue()
        self.stream = sd.InputStream(callback=self.audio_callback)
        self.stream.start()

    def audio_callback(self, indata, frames, time, status):
        volume_norm = np.linalg.norm(indata) * 1000
        self.audio_queue.put(volume_norm)

    def get_microphone_volume(self):
        if not self.audio_queue.empty():
            return self.audio_queue.get()
        return None
    
    def get_human_speech_text(self):
        pass
