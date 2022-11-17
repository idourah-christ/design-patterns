class CommandQueue:

    def __init__(self):
        self.list = []

    def __len__(self):
        return len(self.list)

    def is_empty(self):
        return len(self) == 0 

    def dequeue(self):
        if self.is_empty():
            return None 

        return self.list.pop(0)

    def queue(self, command):
        self.list.append(command)


class RemoteController:

    def __init__(self):
        self.commands = CommandQueue()

    def add_command(self, command):
        self.commands.queue(command)

    def run_command(self):
        if self.commands.is_empty():
            return None 

        while not self.commands.is_empty():
            command = self.commands.dequeue()
            command.execute()