from terminaltexteffects.effects import Rain, Burn, Smoke, Bubbles, Fireworks
import time 

effectMap = {
    "smoke": lambda t:  Smoke(t),
    "rain": lambda t:   Rain(t),
    "burn": lambda t:   Burn(t),
    "bubbles": lambda t:    Bubbles(t),
    "fireworks": lambda t:  Fireworks(t)
}

class PrinterService:
    def __init__(self, bucket : int = 100, typeOfEffect : str = 'smoke'):
        self.textParts = []
        self.bucket = bucket 
        self.typeOfEffect = typeOfEffect

    def addText(self, token : str):
        self.textParts.append(token)
        if len(self.textParts) == 3:
            self.display()
       
    def display(self):
        effect = effectMap[self.typeOfEffect]("".join(self.textParts))
        with effect.terminal_output() as terminal:
            for frame in effect:
                terminal.print(frame)
        time.sleep(1)
        self.textParts = []
    
