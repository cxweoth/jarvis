import random
import tkinter as tk

from cfg import Config
from viewmodel import ViewModel

class HumanVoiceView(tk.Canvas):

    def __init__(self, cfg: Config, viewmodel: ViewModel) -> None:

        # Humanc Voice canvas
        self._width = 200
        self._height = 100
        bg = 'black'
        padx = (20,0)
        pady = (20, 0)

        super().__init__(width=self._width, height=self._height, bg=bg, highlightthickness=0)

        self.pack(padx=padx, pady=pady)  

        self.cfg = cfg
        self.viewmodel = viewmodel

        # line stting
        self._line_width = 4
        self._num_points = 20
        self._sensitivity = 20
        self._lower_limit = 15
        self._upper_limit = self._height - self._lower_limit
        
        # color setting
        self._tech_blue = self.rgb_to_hex(0, 191, 255)

    def rgb_to_hex(self, r, g, b):
        return f'#{r:02x}{g:02x}{b:02x}'

    def update_human_voice(self):
        self.delete("wave")  
        y_base = self._height//2  
        amplitude = self.viewmodel.update_human_amplitude()//self._sensitivity  

        points = []  
        for i in range(self._num_points):
            x = self._width / self._num_points * i  
            y_variation = random.randint(-amplitude, amplitude)  
            y = y_base + y_variation  
            if y > self._upper_limit:
                y = self._upper_limit
            if y < self._lower_limit:
                y = self._lower_limit
                
            points.append((x, y)) 

        for i in range(1, len(points)):
            x1, y1 = points[i-1]
            x2, y2 = points[i]
            self.create_line(x1, y1, x2, y2, width=self._line_width, fill=self._tech_blue, tag="wave")
