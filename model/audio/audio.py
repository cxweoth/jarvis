from cfg import Config
from .audio_receiver import AudioReceiver


class AudioModel:

    def __init__(self, cfg: Config):    
        self.cfg = cfg
        self.audio_receiver = AudioReceiver(cfg)

    def get_microphone_volume(self):
        return self.audio_receiver.get_microphone_volume()
    
    def stop(self):
        self.audio_receiver.stop()
        

