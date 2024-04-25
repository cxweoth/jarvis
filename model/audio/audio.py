from cfg import Config
from .audio_receiver import AudioReceiver


class AudioModel:

    def __init__(self, cfg: Config):    
        self.cfg = cfg
        self.audio_receiver = AudioReceiver(cfg)

        print("init audio model...")

    def get_microphone_volume(self):
        return self.audio_receiver.get_microphone_volume()
    
    def get_machine_volume(self):
        return self.audio_receiver.get_machine_volume()
    
    def get_audio_path(self):
        return self.audio_receiver.get_audio_path()
    
    def start_speaking(self):
        self.audio_receiver.start_speaking()

    def stop_speaking(self):
        self.audio_receiver.stop_speaking()
    
    def stop(self):
        pass
        

