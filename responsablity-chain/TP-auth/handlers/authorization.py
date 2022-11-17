from handlers import HandlerWithAuthorizationService


class AuthorizationHandler(HandlerWithAuthorizationService):

    def __init__(self, service):
        super().__init__(service)

    def execute_next(self, request, response={}):
        
        response['granted'] = self.service.authorize(request)

        return self.next.execute_next(request, response)