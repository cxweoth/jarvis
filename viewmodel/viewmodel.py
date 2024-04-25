
from cfg import Config
from model import Model


class ViewModel:
    
    def __init__(self, cfg: Config, model: Model):
        
        self.cfg = cfg
        self.model = model

        self.original_radius = 61
        self.smoothed_radius = 61

    def update_jarvis_radius(self, outer_radius, inner_radius, sensitivity):
        volume = self.model.get_jarvis_volume()        
        if volume is not None:
            target_radius = min(outer_radius, inner_radius + volume / sensitivity)
            self.smoothed_radius = 0.8 * self.smoothed_radius + 0.2 * target_radius
        else:
            self.smoothed_radius = self.original_radius
        return self.smoothed_radius
    
    def update_human_amplitude(self):
        volume = self.model.get_human_volume()
        
        if volume is None:
            amplitude = 0
        elif volume < 50:
            amplitude = 0
        else:
            amplitude = volume
        return amplitude
