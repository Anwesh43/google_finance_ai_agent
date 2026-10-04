from terminaltexteffects.effects import Rain
import time 

class PrinterService:
    def __init__(self, bucket : int = 100):
        self.textParts = []
        self.bucket = bucket 

    def addText(self, token : str):
        self.textParts.append(token)
        if len(self.textParts) == 3:
            self.display()
       
    def display(self):
        effect = Rain("".join(self.textParts))
        with effect.terminal_output() as terminal:
            for frame in effect:
                terminal.print(frame)
        time.sleep(1)
        self.textParts = []
    
