import random

class Main:
    def __init__(self):
        self._sessionKey = str(random.randint(1, 100))
        self._width = 500
        self._height = 500

    def setup(self, setup_info):
        print('Setup')
        response = {
            'sessionkey' : self._sessionKey,
            'width': self._width,
            "height": self._height,
            "listeners": [
                "click",
                # "keydown",
                # "dblclick",
                # "mousedown",
                # "mouseup",
                # "mousemove",
                # "touchstart",
                # "touchmove",
                # "touchend",
                # "touchcancel",
                # "keydown",
                # "keyup",
                # "load",
                # "unload",
                # "resize"
            ]
        }

        return response
    
    def loop(self, event):
        time = event['time']
        events = event['events']
        response = []

        print(event)
        

        for e in events:
            print(events)
            response.append({
                'type': 'var',
                'name': 'fillStyle',
                'parameters': ['blue']
                })
            response.append({
                'type': 'func',
                'name': "fillRect",
                'parameters': [e['x'], e['y'], 10, 10]
            })
        

        return response
    
    def error(self, client_error):
        response = {}

        return response