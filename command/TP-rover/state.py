class State:

    def __init__(self, rover):
        self.rover = rover

    def translate_x(self, value):
        pass 

    def translate_y(self,value):
        pass 

    def turn_up_light(self):
        self.rover.light = True 

    def turn_off_light(self):
        self.rover.light = False 

    def stop(self):
        pass 

    def start(self):
        pass 


class WorkingState(State):

    def translate_x(self, value):
        self.rover.position.x = value 

    def translate_y(self, value):
        self.rover.position.y = value 

    def start(self):
        return None 

    def stop(self):
        self.rover.state = StopState(self.rover)

    def __str__(self):
        return "Rover engine is started"



class StopState(State):

    def translate_x(self, value):
        return None 

    def translate_y(self, value):
        return None 

    def start(self):
        self.rover.state = WorkingState(self.rover)

    def stop(self):
        return None 

    def __str__(self):
        return "Rover engine stopped"