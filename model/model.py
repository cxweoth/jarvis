from cfg import Config
from .audio import AudioModel
from .ai_agents import SpeechToTextAgent
from .speaker import Speaker


class Model:
    
    def __init__(self, cfg: Config) -> None:
        
        self.cfg = cfg
        self.audio_model = AudioModel(cfg)
        self.speech_to_text_agent = SpeechToTextAgent(self.audio_model)
        self.speaker = Speaker(cfg.speaker_type, self.audio_model, self.speech_to_text_agent)

    def get_human_volume(self):
        return self.audio_model.get_microphone_volume()
    
    def get_jarvis_volume(self):
        return self.audio_model.get_machine_volume()
    
    def stop(self):
        self.audio_model.stop()

