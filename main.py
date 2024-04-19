import os

from cfg import Config
from view import View
from viewmodel import ViewModel
from model import Model


if __name__ == '__main__':

    root_path = os.path.dirname(os.path.abspath(__file__))
    cfg = Config(root_path)

    try:
        model = Model(cfg)
        view_model = ViewModel(cfg, model)
        app = View(cfg, view_model)
        app.mainloop()
    except KeyboardInterrupt as e:
        print("KeyboardInterrupt", e)
        model.stop()



