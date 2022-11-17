from handlers import HandlerWithAuthService


class AuthenficationHandler(HandlerWithAuthService):

    def __init__(self, service):
        super().__init__(service)
       
    def execute_next(self, request,response={}):
        
        response['auth'] = self.service.authenticate(request)
       
        return self.next.execute_next(request, response)