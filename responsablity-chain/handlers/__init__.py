
class EndHandler:

    def __init__(self):
        pass 
    
    def execute(self, request, response=None):
        return response

class Handler:
    def __init__(self,data):
        self.next: EndHandler = EndHandler()
        self.data = data 

    def execute(self, request, respone=None):
        return None 


class HandlerRegister:

    def __init__(self):
        self.head:Handler = None
        self.current:Handler = self.head 

    def append(self, handler):
        if self.head is None:
            self.head = handler
            self.current = self.head
        else:
            self.current.next = handler
            self.current = self.current.next
            
        return self.current
