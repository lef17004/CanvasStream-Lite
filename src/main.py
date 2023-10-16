import random

class CanvasStreamController:
    def __init__(self):
        self.sessionKey = str(random.randint(1, 100))
        self.screen_info = None

    def on_connect(self):
        return self.sessionKey

    def on_setup(self, screen_info):
        self.screen_info = screen_info
        print(screen_info)
        return {
            "width": 1000,
            "height": 1000
        }

    def on_preload(self):
        ...

    def on_event(self):
        ...

    def on_draw(self):
        ...

    def on_disconnect(self):
        ...