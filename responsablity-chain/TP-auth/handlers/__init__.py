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




