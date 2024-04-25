import os
import whisper
import queue
import threading
import time
from ..audio import AudioModel


class SpeechToTextAgent:
    
    def __init__(self, audio_model: AudioModel, model_path: str = "models/whisper-base.en"):
        self.model_path = model_path
        self.audio_model = audio_model
        self.user_text_input_queue = queue.Queue()

        self.transcribe_thread = threading.Thread(target=self.transforming_audio_to_text)
        self.transcribe_thread.start()

        print("init speech to text agent...")

    def transforming_audio_to_text(self):
        while True:
            audio_path = self.audio_model.get_audio_path()
            if audio_path:
                text = self.transcribe(audio_path)
                self.user_text_input_queue.put(text)
                # remove the audio file
                os.remove(audio_path)

            time.sleep(0.01)

    def transcribe(self, audio_path: str) -> str:
        return whisper.transcribe(audio_path, path_or_hf_repo=self.model_path)["text"]
    
    def get_user_text_input(self):
        if not self.user_text_input_queue.empty():
            return self.user_text_input_queue.get()
        return None




