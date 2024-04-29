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
        
        self.audio_path_queue = queue.Queue()
        self._speaking_volume_queue = queue.Queue()
        self._listening_volume_queue = queue.Queue()
        self.audio_taker = pyaudio.PyAudio()
        
        self._is_listening = False
        self._is_speaking = False
        self._is_outside_speaking = False

        self._is_recording = False

        self.audio_thread = threading.Thread(target=self.audio_listening)
        self.audio_thread.start()

        print("init audio receiver...")

        self.start_listening()

    def start_listening(self):
        self._is_listening = True

    def stop_listening(self):
        self._set_stop_listening_params()

    def start_speaking(self):
        self._is_outside_speaking = True

    def stop_speaking(self):
        self._is_outside_speaking = False
        
    def _set_start_listening_params(self):
        self._listen_stream = self.audio_taker.open(format=FORMAT, 
                                                    channels=CHANNELS, 
                                                    rate=RATE, 
                                                    input=True, 
                                                    input_device_index=MIC_IDX, 
                                                    frames_per_buffer=CHUNK)
        self._listen_silent_chunks = 0
        self._listen_audio_started = False
        self._listen_frames = []
        self._is_listening = True
        self._is_recording = True

    def _set_stop_listening_params(self):
        self._listen_stream.stop_stream()
        self._listen_stream.close()
        self._listen_silent_chunks = 0
        self._listen_audio_started = False
        self._listen_frames = []
        self._is_listening = False
        self._is_recording = False

    def _set_start_speaking_params(self):
        
        self._speak_stream = self.audio_taker.open(format=FORMAT, 
                                                    channels=CHANNELS, 
                                                    rate=RATE, 
                                                    input=True, 
                                                    input_device_index=MIC_IDX, 
                                                    frames_per_buffer=CHUNK)
        self._is_speaking = True
        self._is_recording = True
        
    def _set_stop_speaking_params(self):
        
        self._speak_stream.stop_stream()
        self._speak_stream.close()
        self._is_speaking = False
        self._is_recording = False
        self._is_listening = True

    def audio_listening(self):
        
        while True:
            try:
                if self._is_listening:
                    if not self._is_recording:
                        self._set_start_listening_params()
                    data = self._listen_stream.read(CHUNK)
                    rms = compute_rms(data)
                    if rms >= SILENCE_THRESHOLD:   
                        self._listening_volume_queue.put(rms)
                        self._listen_audio_started = True
                    if self._listen_audio_started:
                        self._listen_frames.append(data)
                        if rms < SILENCE_THRESHOLD:
                            self._listen_silent_chunks += 1
                            if self._listen_silent_chunks > SILENT_CHUNKS:
                                self._listen_audio_started = False
                                filename = os.path.join(self._recording_path ,datetime.now().strftime("%Y-%m-%d_%H-%M-%S.wav"))
                                self._save_audio(filename, self._listen_frames)
                                self.audio_path_queue.put(filename)
                                self._set_stop_listening_params()
                        else:
                            self._listen_silent_chunks = 0 
                
                if self._is_outside_speaking:
                    self._set_start_speaking_params()

                if self._is_speaking:
                    data = self._speak_stream.read(CHUNK)
                    rms = compute_rms(data)
                    if rms >= SILENCE_THRESHOLD:
                        self._speaking_volume_queue.put(rms)
                    if not self._is_outside_speaking:
                        self._set_stop_speaking_params()
                
            except Exception as e:
                print("get_audio failed:", e)
                break
        
        self.audio_taker.terminate()
    
    def _save_audio(self, filename, frames):
        with wave.open(filename, 'wb') as wf:
            wf.setnchannels(CHANNELS)
            wf.setsampwidth(self.audio_taker.get_sample_size(FORMAT))
            wf.setframerate(RATE)
            wf.writeframes(b''.join(frames))

    def get_microphone_volume(self):
        if not self._listening_volume_queue.empty():
            return self._listening_volume_queue.get()
        return None
    
    def get_machine_volume(self):
        if not self._speaking_volume_queue.empty():
            return self._speaking_volume_queue.get()
        return None
    
    def get_audio_path(self):
        if not self.audio_path_queue.empty():
            return self.audio_path_queue.get()
        return None
    
    
