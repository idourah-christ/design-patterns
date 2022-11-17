from state import StopState, State

class Position:

    def __init__(self, x=0, y=0):
        self.x = x 
        self.y = y 

    def __str__(self):
        return f'({self.x}, {self.y})'

class WaterRover:

    def __init__(self, name):
        self.name = name
        self.position:Position = Position()
        self.light = False 
        self.state: State = StopState(self)

    def translate_x(self, value):
        self.state.translate_x(value)

    def translate_y(self, value):
        self.state.translate_y(value)

    def turn_up_light(self):
        self.state.turn_up_light()

    def turn_off_light(self):
        self.state.turn_off_light()

    def start(self):
        self.state.start()

    def stop(self):
        self.state.stop()

    def print(self):
        print(self.state) 

    def get_coordinates(self):
        print(self.position)