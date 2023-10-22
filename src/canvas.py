from src.event import Instruction

class Canvas:
    """
    Canvas
    Class that mimics the browser's javascript canvas api.

    Citation
        https://developer.mozilla.org/en-US/docs/Web/API/CanvasRenderingContext2D
    """
    def __init__(self):
        """
        Init

        Sets up the class
        """
        self._instructions = []

    def _add_method_call(self, method_name: str, parameters: list[str]):
        """
        Add Method Call

        Creates a valid instruction to call a method of the browser's canvas

        Parameters
            method_name: The name of the method to call
            parameters: The parameters to pass into the called method
        """
        self._instructions.append(
            Instruction(type="func", name=method_name, parameters=parameters)
        )

    def _add_var_set(self, var_name: str, parameter: str):
        """
        Add Var Set

        Creates a valid instruction to set a property of the browser's canvas

        Parameters
            var_name: The name of the propery to set
            parameter: The new value of the property
        """
        self._instructions.append(
            Instruction(type="var", name=var_name, parameters=[parameter])
        )

    def _add_command(self, command_name: str, parameter: str):
        """
        Add Command

        Creates a valid instruction to execute a command in the client

        Parameters
            command_name: The name of the command to execute
            parameter: A value if needed to execute the command
        """
        self._instructions.append(
            Instruction(type="command", name=command_name, parameters=[parameter])
        )

    # Canvas Properties

    def _set_fill_style(self, color: str):
        """
        Set Fill Style

        Specifies the color, gradient, or pattern to use inside shapes
        The default style is #000 (black)

        Parameters:
            color: A color represented as a string

        Citation: 
            https://developer.mozilla.org/en-US/docs/Web/API/CanvasRenderingContext2D/fillStyle
        """
        self._add_var_set("fillStyle", color)


    # Makes it so setters can be accessed as properties
    fill_style = property(fset=_set_fill_style)

    # Canvas Methods

    def fill_rect(self, x: int, y: int, width: int, height: int):
        """
        Fill Rect

        Draws a rectangle that is filled according to the current fillStyle.

        Parameters:
            x: The x-axis coordinate of the rectangle's starting point.
            y: The y-axis coordinate of the rectangle's starting point.
            width: The rectangle's width. Positive values are to the right, and negative to the left.
            height: The rectangle's height. Positive values are down, and negative are up.

        Citation: 
            https://developer.mozilla.org/en-US/docs/Web/API/CanvasRenderingContext2D/fillRect
        """
        self._add_method_call("fillRect", [x, y, width, height])

    def get_draw_instructions(self):
        """
        Get Draw Instructions

        Gets the list of instructions to send to the client.

        Returns:
            List[Instruction]: Send to the client to be drawn on the screen
        """
        return self._instructions
    
    def clear_instructions(self):
        """
        Clear Instructions

        Empties the list of stored instructions. It is recommended that list is
        cleared right after drawing. This does not clear what is on the client's
        screen.
        """
        self._instructions.clear()

    def set_width(self, width: int):
        """
        Set Width

        Changes the width of the canvas

        Parameters:
            width: The new width of the canvas
        """
        self._add_command("setCanvasWidth", width)

    def set_height(self, height: int):
        """
        Set Height

        Changes the height of the canvas

        Parameters:
            height: The new width of the canvas
        """
        self._add_command("setCanvasHeight", height)
    