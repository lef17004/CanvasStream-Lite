from src.event import Instruction

class Canvas:
    def __init__(self):
        self._instructions = []

    def _add_method_call(self, method_name, parameters):
        self._instructions.append(
            Instruction(type="func", name=method_name, parameters=parameters)
        )

    def _add_var_set(self, var_name, parameter):
        self._instructions.append(
            Instruction(type="var", name=var_name, parameters=[parameter])
        )

    def _add_command(self, command_name, parameter):
        self._instructions.append(
            Instruction(type="command", name=command_name, parameters=[parameter])
        )

    def _set_fill_style(self, color):
        self._add_var_set("fillStyle", color)

    fill_style = property(fset=_set_fill_style)

    def fill_rect(self, x, y, width, height):
        self._add_method_call("fillRect", [x, y, width, height])

    def get_draw_instructions(self):
        return self._instructions
    
    def clear_instructions(self):
        self._instructions.clear()

    def set_width(self, width):
        self._add_command("setCanvasWidth", width)

    def set_height(self, height):
        self._add_command("setCanvasHeight", height)
    