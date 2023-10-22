import random
from src.canvas import Canvas
from src.event import ServerToClient, Instruction

class Main:
    def __init__(self):
        self.session_key = str(random.randint(1, 100))
        self._width = 700
        self._height = 700
        self._canvas = Canvas()
        self._listeners = [
            "click",
            "keydown",
            "keyup",
            "dblclick",
            "mousedown",
            "mouseup",
            # "mousemove",
            # "touchstart",
            # "touchmove",
            # "touchend",
            # "touchcancel",
            # "load",
            "beforeunload",
            "resize"
        ]

    def setup(self, setup_info):
        print('Setup')
        response = ServerToClient()
        response.add_instructions([
            Instruction("command", "setSessionKey", [self.session_key]),
            Instruction("command", "setWidth", [self._width]),
            Instruction("command", "setHeight", [self._height]),
            Instruction("command", "setListeners", [self._listeners])
        ])

        

        return response
    
    def loop(self, message):
        time = message.time
        events = message.events
        response = ServerToClient()
        
        self._canvas.clear_instructions()
        for e in events:
            print(e.type)
            if e.type == 'click':
                self._canvas.fill_style = "blue"
                self._canvas.fill_rect(e.x, e.y, 10, 10)

                response.add_instructions(self._canvas.get_draw_instructions())

        return response
    
    def shutdown(self):
        ...

    def error(self, client_error):
        response = {}

        return response