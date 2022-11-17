from rover import WaterRover
from controller import RemoteController
import commands as cmd 

rover = WaterRover('libanga')
controller = RemoteController()

controller.add_command(cmd.StartCommand(rover))
controller.add_command(cmd.LightUpCommand(rover))
controller.add_command(cmd.TranslateXCommand(rover,12))
controller.add_command(cmd.PrintCoordinateCommand(rover))

rover.print()

controller.run_command()

rover.print()