import os
import configparser

class Config:

    def __init__(self, root_path) -> None:
        
        self.root_path = root_path

        # config path
        self.config_path = os.path.join(self.root_path, "config", "config.ini")

        # get config
        self.get_config()

    def get_config(self):
        config = configparser.ConfigParser()
        config.read(self.config_path)
        self.speaker_type = config.get("Setting", "SpeakerType")
        self.ws_host = config.get("WS", "Host")
        self.ws_port = int(config.get("WS", "Port"))
        self.ws_name = config.get("WS", "Name")
        self.web_path = os.path.join(self.root_path, "web")


