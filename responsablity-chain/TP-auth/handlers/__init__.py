from abc import ABCMeta, abstractclassmethod
from services import AuthentificationService, AuthorizationService

class EndHandler:

    def __init__(self):
      pass 
    
    def execute_next(self, request, response={}):
        return response


class Handler:

    def __init__(self):
        self.next: EndHandler = EndHandler()

    def execute_next(self, request, response={}):
        return response


class HandlerWithAuthService(Handler):

    def __init__(self, service):
        super().__init__()
        self.service:AuthentificationService = service


class HandlerWithAuthorizationService(Handler):

    def __init__(self, service):
        super().__init__()
        self.service: AuthorizationService = service


class HandlerRegistery:

    def __init__(self):

        self.head: Handler = None  
        self.current = self.head

    def append(self, handler:Handler):
        if self.head is None:
            self.head = handler
            self.current = self.head
           
        else:
            self.current.next = handler
            self.current = handler

        return self.current

    def run(self, request):

        if self.head is None:
            return None 

        return self.head.execute_next(request)

