from cfg import Config
from .audio import AudioModel
from .ai_agents import SpeechToTextAgent
from .speaker import Speaker
from .brain import Brain


class Model:
    
    def __init__(self, cfg: Config) -> None:
        
        self.cfg = cfg
        self.audio_model = AudioModel(cfg)
        self.speech_to_text_agent = SpeechToTextAgent(self.audio_model)
        self.brain = Brain(self.speech_to_text_agent)
        self.speaker = Speaker(cfg.speaker_type, self.audio_model, self.brain)

    def get_human_volume(self):
        return self.audio_model.get_microphone_volume()
    
    def get_jarvis_volume(self):
        return self.audio_model.get_machine_volume()
    
    def stop(self):
        self.audio_model.stop()

