from cfg import Config
from .audio import AudioModel


class Model:
    
    def __init__(self, cfg: Config) -> None:
        
        self.cfg = cfg

        self.audio_model = AudioModel(cfg)

    def get_human_volume(self):
        return self.audio_model.get_microphone_volume()
    
    def get_jarvis_volume(self):
        import random
        volume = random.randint(70, 500)
        return volume
    
    def stop(self):
        self.audio_model.stop()

