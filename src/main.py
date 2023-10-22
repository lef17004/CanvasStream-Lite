import random
from src.canvas import Canvas
from src.event import ServerToClient, Instruction, ClientToServer

class Main:
    """
    Main

    The starting point of the application

    Properties
        session_key: str
            The identifier used to match the client to the application
    """
    def __init__(self):
        """
        Init

        Creates a new Main object
        """
        self.session_key = str(random.randint(1, 100))
        self._width = 700 # Controls width of canvas on client side
        self._height = 700 # Controls height of canvas on client side
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
        ] # List of events to get from the client

    def setup(self, setup_info) -> ServerToClient:
        """
        Setup

        Called only once at when the client connects to the sever. Used to set everything
        to its initial state. 

        Parameters:
            setup_info: ??? Going to change
                Data from the client needed to successfully setup the application

        Returns
            ServerToClient: The message to send to the client
        """
        response = ServerToClient()
        response.add_instructions([
            Instruction("command", "setSessionKey", [self.session_key]),
            Instruction("command", "setWidth", [self._width]),
            Instruction("command", "setHeight", [self._height]),
            Instruction("command", "setListeners", [self._listeners])
        ])

        return response
    
    def loop(self, message: ClientToServer) -> ServerToClient:
        """
        Loop

        Called every frame by the client. Sends a message to the client containing instructions.

        Parameters:
            message: Message from the client containing event data

        Returns:
            ServerToClient: The response to send to the client
        """
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
        """
        Shutdown

        This is called when the client is refreshed or closed.

        Todo: Needs to be made
        """
        ...

    def error(self, client_error):
        """
        Error

        Errors from the client forwared to the server

        Todo: Needs to be made
        """
        response = {}

        return response