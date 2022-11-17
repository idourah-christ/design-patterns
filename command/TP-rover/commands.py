from rover import WaterRover

class Command:

    def __init__(self, rover):
        self.rover:WaterRover = rover 


    def execute(self):
        pass 


class StartCommand(Command):

    def execute(self):
        self.rover.start()

class StopCommand(Command):

    def execute(self):
        self.rover.stop()


class LightUpCommand(Command):

    def execute(self):
        self.rover.turn_up_light()

class LightOffCommand(Command):

    def execute(self):
        self.rover.turn_off_light()

class TranslateXCommand(Command):

    def __init__(self, rover, value):
        super().__init__(rover)
        self.value = value 

    def execute(self):
        self.rover.translate_x(self.value)

    
class TranslateYCommand(Command):

    def __init__(self, rover, value):
        super().__init__(rover)
        self.value = value

    def execute(self):
        self.rover.translate_y(self.value)


class PrintCoordinateCommand(Command):

    def execute(self):
        self.rover.get_coordinates()