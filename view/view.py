import tkinter as tk

from cfg import Config
from viewmodel import ViewModel
from .jarvis_view import JarvisView
from .human_voice_view import HumanVoiceView


class View(tk.Tk):


    def __init__(self, cfg: Config, view_model: ViewModel):
        
        super().__init__()

        self.cfg = cfg
        self.viewmodel = view_model

        self.jarvis_view = JarvisView(cfg, self.viewmodel)
        self.huamn_voice_view = HumanVoiceView(cfg, self.viewmodel)

        self.configure(bg='black')
        self.geometry('800x800')
        self.title('Jarvis')

        self.update_frame()
        self.check_interrupt()

    def update_frame(self):

        self.jarvis_view.update_jarvis()
        self.huamn_voice_view.update_human_voice()

        self.after(1, self.update_frame)

    def check_interrupt(self):
        try:
            pass
        except KeyboardInterrupt:
            self.quit()
        finally:
            self.after(500, self.check_interrupt)



