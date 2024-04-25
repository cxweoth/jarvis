import subprocess

class AppleSpeaker:
    def __init__(self):
        self.name = "Apple Speaker"

    def __str__(self):
        return self.name
    
    def speak(self, text: str):
        subprocess.call(["say", "-v", "Alex", text])
        