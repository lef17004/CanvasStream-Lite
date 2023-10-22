import json

class Event:
    def __init__(self, event_dict):
        self.type = ''
        self.ctrl_key = False
        self.shift_key = False
        self.meta_key = False
        self.key = ''
        self.x = 0
        self.y = 0
        self.width = 0
        self.height = 0
        self.orientation = ''

        if type := event_dict.get('type'):
            self.type = type
        if ctrl := event_dict.get('ctrlKey'):
            self.ctrl_key = bool(ctrl)
        if shift := event_dict.get('shiftKey'):
            self.shift_key = bool(shift)
        if meta := event_dict.get('metaKey'):
            self.meta_key = bool(meta)
        if key := event_dict.get('key'):
            self.key = key
        if x := event_dict.get('x'):
            self.x = x
        if y := event_dict.get('y'):
            self.y = y
        if width := event_dict.get('width'):
            self.width = float(width)
        if height := event_dict.get("height"):
            self.height = float(height)
        if orientation := event_dict.get('orientation'):
            self.orientation = orientation

class Instruction:
    def __init__(self, type, name, parameters):
        self.type = type
        self.name = name
        self.parameters = parameters

    def to_dict(self):
        return {
            "type": self.type,
            "name": self.name,
            "parameters": self.parameters
        }
        

class ClientToServer:
    def __init__(self, dictionary):
        self.time = 0
        self.events = []

        if time := dictionary.get('time'):
            self.time = time
        if events := dictionary.get("events"):
            for e in events:
                self.events.append(Event(e))
        

class ServerToClient: 
    def __init__(self):
        self.instructions = []

    def add_instruction(self, instruction):
        self.instructions.append(instruction.to_dict())

    def add_instructions(self, instructions):
        for instruction in instructions:
            self.add_instruction(instruction)
