import time
import threading
import queue
import numpy as np

from ..audio import AudioModel
from ..brain import Brain
from .apple_speaker import AppleSpeaker

class Speaker:

    def __init__(self, speaker_type: str, audio_model: AudioModel, brain: Brain):
        self.name = "Speaker"

        if speaker_type == "apple":
            self.speaker = AppleSpeaker()

        self.brain = brain
        self.audio_model = audio_model
        self.text_queue = queue.Queue()
        self.volume_queue = queue.Queue()

        self.text_to_speech_thread = threading.Thread(target=self._run_text_to_speech)
        self.text_to_speech_thread.start()
        print("init speaker...")

    def __str__(self):
        return self.name
    
    def _run_text_to_speech(self):
        while True:
            text = self.brain.get_reply()
            if text:
                print("speak text: ", text)
                self.speak(text)

            time.sleep(0.01)

    def _get_text(self):
        if not self.text_queue.empty():
            return self.text_queue.get()
        return None

    def speak(self, text: str):
        self.audio_model.start_speaking()
        self.speaker.speak(text)
        self.audio_model.stop_speaking()

