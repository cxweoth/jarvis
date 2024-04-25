import os
import time
import wave
import queue
import pyaudio
import numpy as np
import threading
import struct
from datetime import datetime


from cfg import Config

CHUNK = 256
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
MIC_IDX = 0
SILENCE_THRESHOLD = 500
SILENT_CHUNKS = 2 * RATE / CHUNK  # two seconds of silence marks the end of user voice input
RECORDING_PATH = "recordings"

def compute_rms(data):
    # Assuming data is in 16-bit samples
    format = "<{}h".format(len(data) // 2)
    ints = struct.unpack(format, data)

    # Calculate RMS
    sum_squares = sum(i ** 2 for i in ints)
    rms = (sum_squares / len(ints)) ** 0.5
    return rms

class AudioReceiver:

    def __init__(self, cfg: Config):
        self.cfg = cfg
        self._recording_path = os.path.join(cfg.root_path, RECORDING_PATH)
        self.volume_queue = queue.Queue()
        self.machine_volume_queue = queue.Queue()
        self.audio_path_queue = queue.Queue()
        self.audio_taker = pyaudio.PyAudio()
        self.audio_thread = threading.Thread(target=self.audio_listening)
        self.audio_thread.start()
        self.is_speaking = False

        print("init audio receiver...")

    def audio_listening(self):
        stream = self.audio_taker.open(format=FORMAT, 
                                       channels=CHANNELS, 
                                       rate=RATE, 
                                       input=True, 
                                       input_device_index=MIC_IDX, 
                                       frames_per_buffer=CHUNK)
        silent_chunks = 0
        audio_started = False
        frames = []
        while True:
            
            try:
                data = stream.read(CHUNK)
                rms = compute_rms(data)
                if not self.is_speaking:
                    if rms >= SILENCE_THRESHOLD:   
                        self.volume_queue.put(rms)
                        audio_started = True
                    if audio_started:
                        frames.append(data)
                        if rms < SILENCE_THRESHOLD:
                            silent_chunks += 1
                            if silent_chunks > SILENT_CHUNKS:
                                audio_started = False
                                filename = os.path.join(self._recording_path ,datetime.now().strftime("%Y-%m-%d_%H-%M-%S.wav"))
                                self._save_audio(filename, frames)
                                self.audio_path_queue.put(filename)
                                frames = []
                        else:
                            silent_chunks = 0 
                else:
                    if rms >= SILENCE_THRESHOLD:
                        self.machine_volume_queue.put(rms)
                
            except Exception as e:
                print("get_audio failed:", e)
                break
        
        stream.stop_stream()
        stream.close()
        self.audio_taker.terminate()
    
    def _save_audio(self, filename, frames):
        with wave.open(filename, 'wb') as wf:
            wf.setnchannels(CHANNELS)
            wf.setsampwidth(self.audio_taker.get_sample_size(FORMAT))
            wf.setframerate(RATE)
            wf.writeframes(b''.join(frames))

    def get_microphone_volume(self):
        if not self.volume_queue.empty():
            return self.volume_queue.get()
        return None
    
    def get_machine_volume(self):
        if not self.machine_volume_queue.empty():
            return self.machine_volume_queue.get()
        return None
    
    def get_audio_path(self):
        if not self.audio_path_queue.empty():
            return self.audio_path_queue.get()
        return None

    def start_speaking(self):
        self.is_speaking = True  # stop human recording, start machine recording

    def stop_speaking(self):
        self.is_speaking = False  # start recording, start machine recording
